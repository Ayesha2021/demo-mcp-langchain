from mcp.server.fastmcp import FastMCP
import requests

mcp = FastMCP('WeatherAPI')


@mcp.tool()
def weatherService(latitude: float, longitude: float) -> str:
    """ __Summary__
    You are an Weahter assistent ,takes latitue and longitude as input and Fetches real-time weather  conditions from a live REST API for given GPS coordinates.
    Provides temperature, wind speed.
    """
    try:
        url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
        response = requests.get(url, timeout=6)
        response.raise_for_status()

        payload = response.json().get("current_weather", {})
        temp = payload.get("temperature", "N/A")
        wind = payload.get("windspeed", 0.0)

        return (
            f"--- LIVE CORRIDOR TELEMETRY ---\n"
            f"Target GPS: {latitude}, {longitude}\n"
            f"External Temp: {temp}°C | Wind Speed: {wind} km/h\n"

            f"-------------------------------"
        )
    except Exception as e:
        return f"Corridor API Communication Failure: {str(e)}"


if __name__ == "__main__":
    mcp.run(transport='streamable-http')
