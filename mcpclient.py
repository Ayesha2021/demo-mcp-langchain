from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent
# from langchain.agents import create_tool_calling_agent
from dotenv import load_dotenv
import os
import asyncio

load_dotenv('.env')
api_key = os.getenv('GROQ_API_KEY')


async def main():

    client = MultiServerMCPClient(
        {"MCP-Calculator": {
            "command": "python",
            "args": ["math-mcp-server.py"],
            "transport": "stdio",
        },
            "WeatherAPI": {
            "url": "http://localhost:8000/mcp",
            "transport": "streamable_http",

        }
        }


    )
    # setting environmental variable
    os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')

    tools = await client.get_tools()

    model = ChatGroq(model="qwen/qwen3.8-27b")

    agent = create_react_agent(model, tools)

    # mathResponse = await agent.ainvoke(
    #   {
    #   "messages": [{"role": "user", "content": "what is the value of (9897+9654)*6"}]
    #  })
    liveWeatherResponse = await agent.ainvoke(

        {
            "messages": [{"role": "user", "content": "how is the weather in city edison ,NJ with Latitude : 40.5187 N and Longitude : -74.4121 W"}]
        }
    )
    # print('Printing Math Response')
    # print(mathResponse['messages'][-1].content)
    # print('End of Math server response')
    print('--'*50)
    print(liveWeatherResponse)
    print('--'*50)

asyncio.run(main())
