import requests
import json
import time

# --- Configuration ---
# The URL of the Model Communication Protocol (MCP) endpoint.
# We use HTTP protocol and the port specified by the user.
MCP_URL = "http://localhost:8001/mcp"


# --- Configuration ---


def get_available_tools(url: str):
    """
    Connects to the specified MCP server endpoint, retrieves the tool list,
    and prints the response.

    This function assumes the server responds with a JSON object.
    For simplicity, it uses a GET request, as this is standard for discovery
    or fetching a manifest/resource list.
    """
    print(f"Attempting to connect to MCP server at: {url}")
    print("-" * 40)

    # Define headers required by the server for acceptable response type.
    # The server error indicated that the client must accept 'text/event-stream'.
    headers = {
        'Accept': 'text/event-stream'
    }

    # Simple retry logic for transient connection errors
    MAX_RETRIES = 3
    for attempt in range(MAX_RETRIES):
        try:
            # 1. Make the GET request to the discovery endpoint with required headers
            response = requests.get(url, headers=headers, timeout=5)

            # 2. Check for successful HTTP status code (200 OK)
            response.raise_for_status()

            # 3. Server responded successfully, attempt to parse JSON
            response_data = response.json()

            print("✅ Successfully received response from MCP Server!")
            print(f"Status Code: {response.status_code}")
            print("\n--- Available Tools Manifest ---")

            # Use json.dumps for pretty printing the entire JSON response
            # This allows the user to see the exact structure (e.g., if tools
            # are under a key like 'tools', 'manifest', or 'data').
            print(json.dumps(response_data, indent=4))

            print("--------------------------------")
            # If the server has a specific key for tools, you could refine this:
            # if 'tools' in response_data:
            #     print(f"Found {len(response_data['tools'])} tools.")
            # else:
            #     print("The response did not contain a 'tools' key.")

            return response_data

        except requests.exceptions.ConnectionError:
            print(f"Attempt {attempt + 1}/{MAX_RETRIES}: Connection failed. Is the server running at {url}?")
            if attempt < MAX_RETRIES - 1:
                time.sleep(2)  # Wait 2 seconds before retrying
        except requests.exceptions.Timeout:
            print(f"Attempt {attempt + 1}/{MAX_RETRIES}: Request timed out.")
        except requests.exceptions.HTTPError as e:
            # Handle 4xx or 5xx client/server errors
            print(f"HTTP Error: {e}")
            print(f"Server response content: {response.text[:200]}...")
            return
        except requests.exceptions.JSONDecodeError:
            print("Error: Could not decode JSON response.")
            # If the server responds with text/event-stream but the content
            # isn't valid JSON, this error will catch it.
            print(f"Raw response received: {response.text[:200]}...")
            return
        except requests.exceptions.RequestException as e:
            print(f"An unexpected error occurred: {e}")
            return

    print(f"\n❌ Failed to connect to the MCP server after {MAX_RETRIES} attempts.")
    print("Please ensure your server is running and accessible at the specified address.")


if __name__ == "__main__":
    get_available_tools(MCP_URL)
