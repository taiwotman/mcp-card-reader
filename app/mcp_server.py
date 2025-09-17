from mcp_utils.core import MCPServer

mcp = MCPServer("card-reader", "1.0")

@mcp.tool()
def extract_first_name(track_data: str) -> str:
    if track_data.startswith('%B'):
        try:
            name_field = track_data.split('^')[1]
            return name_field.split('/')[1]  # firstname
        except:
            return "Parse error"
    return "Invalid data"
