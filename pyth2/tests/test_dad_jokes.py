import pytest
import requests
from bs4 import BeautifulSoup
import re


def response_filter(response):
    if "Location" in response["headers"]:
        response["headers"]["Location"] = [
            re.sub(r"apikey=[^&]+", "apikey=MOCK_API_KEY", x)
            for x in response["headers"]["Location"]
        ]
    return response


@pytest.fixture(scope="module")
def vcr_config():
    return {
        "filter_headers": [("User-Agent", None)],
        "filter_query_parameters": [
            ("apikey", "MOCK_API_KEY"),
        ],
        "before_record_response": response_filter,
    }



@pytest.mark.vcr()
def test_dad_jokes() -> None:
    response = requests.get('https://icanhazdadjoke.com/')
    assert "dad joke about momentum" in response.text
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the element that contains the joke content
    joke_element = soup.find("p", class_="subtitle")

    # Extract the joke text
    joke = joke_element.text.strip()
    assert joke
    print(joke)

@pytest.mark.vcr()
def test_fetch_http_data() -> None:
    response = requests.get('https://financialmodelingprep.com/api/v3/historical-market-capitalization/AAPL?limit=5&&apikey=MOCK_API_KEY')
    print(response.json())