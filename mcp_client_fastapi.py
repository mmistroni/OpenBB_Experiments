import asyncio
from fastmcp import Client, FastMCP

# In-memory server (ideal for testing)
#server = FastMCP("TestServer")
#client = Client(server)

# HTTP server
client = Client("http://127.0.0.1:8001/mcp")

# Local Python script
#client = Client("my_mcp_server.py")


async def main():
    async with client:
        # Basic server interaction
        await client.ping()

        # List available operations
        tools = await client.list_tools()
        resources = await client.list_resources()
        prompts = await client.list_prompts()

        # Execute operations
        #result = await client.call_tool("example_tool", {"param": "value"})
        from pprint import pprint
        pprint(tools)


asyncio.run(main())