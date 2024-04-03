"""OpenBB mmext router command example."""

import requests
from openbb_core.app.model.command_context import CommandContext
from openbb_core.app.model.obbject import OBBject
from openbb_core.app.provider_interface import (ExtraParams, ProviderChoices,
                                                StandardParams)
from openbb_core.app.query import Query
from openbb_core.app.router import Router
from pydantic import BaseModel
from openbb_mmext.utils.helpers import get_nymo, get_nysi

router = Router(prefix="")


@router.command(methods=["GET"])
async def nymo() -> OBBject[dict]:
    """Get NYMO ."""
    data = get_nymo()
    return OBBject(results=data)

@router.command(methods=["GET"])
async def nysi() -> OBBject[dict]:
    """Get NYSI."""
    data = get_nysi()
    return OBBject(results=data)

