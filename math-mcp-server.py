from mcp.server.fastmcp import FastMCP

mcp = FastMCP('MCP-Calculator')


@mcp.tool()
def add(a: int, b: int) -> int:
    """ _Summary_
    You are helpful math Assitent takes two numbers as input and returns the result of addition of two numbers
    """
    return a+b


@mcp.tool()
def multiply(a: int, b: int) -> int:
    """ _Summary_
    You are helpful math Assitent takes two numbers as input and returns the result of multiplication of two numbers
    """
    return a*b


if __name__ == "__main__":
    mcp.run(transport='stdio')
