"""mm_obb_extensions OpenBB Platform Provider."""

from openbb_core.provider.abstract.provider import Provider
from mm_obb_extensions.models.example import ExampleFetcher

# mypy: disable-error-code="list-item"

provider = Provider(
    name="mm_obb_extensions",
    description="Data provider for MM_OBB_Extensions.",
    # Only add 'credentials' if they are needed.
    # For multiple login details, list them all here.
    credentials=["api_key"],
    website="https://mm_obb_extensions.com",
    # Here, we list out the fetchers showing what our provider can get.
    # The dictionary key is the fetcher's name, used in the `router.py`.
    fetcher_dict={
        "Example": ExampleFetcher,
    }
)
