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
def xot() -> OBBject[dict]:
    return OBBject(results = {'foo' : 'bar'})

@router.command(model="CommitmentOfTraders")
async def cot2(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Example Data."""
    return await OBBject.from_query(Query(**locals()))
