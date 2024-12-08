### Fetching senate disclosures
import io
import requests
import re
import pandas as pd

from PyPDF2 import PdfReader
import requests
import zipfile
import xml.etree.ElementTree as ET
import os
# Parallelize.
import io
import xml.etree.ElementTree as ET
import aiohttp
import asyncio

import pandas as pd
from bs4 import BeautifulSoup
from typing import Any, List, Optional


BASE_URL = "https://disclosures-clerk.house.gov/public_disc/financial-pdfs/"
FINANCIAL_DOC_URL= "https://disclosures-clerk.house.gov/public_disc/ptr-pdfs"

def extract_docids_from_year_disclosures(res):
  xml_data = res
  # Parse the XML data from the BytesIO object
  tree = ET.parse(xml_data)
  root = tree.getroot()

  # Find all members with FilingType == "P" and extract their DocID
  doc_ids = []
  for member in root.findall('Member'):
      filing_type = member.find('FilingType').text
      if filing_type == "P":
          doc_id = member.find('DocID').text
          membername = f"{member.find('Last').text} {member.find('First').text}"
          state = member.find('StateDst').text
          filing_date = member.find('FilingDate').text
          doc_ids.append(dict(doc_id=doc_id, member=membername, state=state, filing_date=filing_date))
      else:
        pass#print(f'Found filing type :{filing_type}') # Need to find all filing types # and place by filing_date. perhaps in a df
  return doc_ids


async def aextract_xml_from_zip_url(client, url, output_file):
    """Extracts an XML file from a ZIP archive available at a given URL and saves it to a specified file.

    Args:
        url: The URL of the ZIP archive.
        output_file: The path to save the extracted XML file.
    """
    async with client.get(url) as response:
        # Download the ZIP file
        if response.status == 200:
          content = b""
          while True:
              data = await response.content.read(1024)  # Read up to 1024 bytes
              if not data:
                  break
              content += data
    zip_file = io.BytesIO(content)
    with zipfile.ZipFile(zip_file, "r") as zip_ref:
      for member in zip_ref.infolist():
          if member.filename.endswith(".xml"):
              xml_stream = io.BytesIO(zip_ref.read(member))
              break
    return extract_docids_from_year_disclosures(xml_stream)

async def get_report_for_year(year:str) -> list[str]:
    zip_name = f'{year}FD.zip'
    url = f"{BASE_URL}/{zip_name}"
    output_file = f"{year}.xml"
    session = aiohttp.ClientSession()
    return await aextract_xml_from_zip_url(session, url, output_file)

async def fetch_data(year:str) -> list[str]:
    return await get_report_for_year(year) 