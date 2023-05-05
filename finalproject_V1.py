import json, requests

def get_weather_data(location):
    """
    Request weather data from openweathermap.org API for the given location
    and return the weather information in a dictionary format.
    """
    # replace with your own API key
    api_key = "501d216374eb757725c762530c534ec9"

    # API endpoint for weather forecast
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"

    try:
        # request weather data from API
        response = requests.get(url)
        response.raise_for_status()  # raise an exception if not successful
    except requests.exceptions.RequestException as e:
        # if there was an error connecting to the API, print an error message and return None
        print(f"Error: {e}")
        return None

    # extract weather information from JSON response
    weather_data = response.json()
    city = weather_data["name"]
    weather = weather_data["weather"][0]["description"]
    temperature = weather_data["main"]["temp"] - 273.15  # convert from Kelvin to Celsius

    # return weather information as dictionary
    return {"city": city, "weather": weather, "temperature": temperature}


def get_user_input():
    """
    Prompt user for zip code or city name and return the input as a string.
    """
    while True:
        user_input = input("Enter a zip code or city name: ")
        if user_input.strip():
            return user_input


def display_weather_info(weather_info):
    """
    Display the weather information to the user in a readable format.
    """
    print(f"Weather for {weather_info['city']}:")
    print(f"Description: {weather_info['weather'].title()}")
    print(f"Temperature: {weather_info['temperature']:.1f}°C")


def main():
    """
    Main function that runs the program.
    """
    while True:
        # get location input from user
        location = get_user_input()

        # get weather data for the location
        weather_info = get_weather_data(location)

        if weather_info is not None:
            # display weather information to user
            display_weather_info(weather_info)
        else:
            print("Failed to get weather data.")

        # ask if user wants to check the weather for another location
        choice = input("Check the weather for another location? (y/n) ")
        if choice.lower() not in ["yes", "y", "Y"]:
            break


if __name__ == "__main__":
    main()
