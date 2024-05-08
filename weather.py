import requests

# API key for OpenWeatherMap
api_key = "a07f5a47c9198a51e2e3c908470cfadf"  # Replace "YOUR_API_KEY" with your actual API key

# Base URL for the OpenWeatherMap API
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Input city name from the user
city_name = input("Enter city name: ")

# Construct the complete URL
complete_url = f"{base_url}q={city_name}&appid={api_key}&units=metric"

# Send an HTTP GET request to the API
response = requests.get(complete_url)

#r="http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={"+api_key+"}"
#print(r)
print("Not")

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Extract weather data from the response
    weather_data = response.json()

    # Extract relevant information from the weather data
    temperature = weather_data["main"]["temp"]
    humidity = weather_data["main"]["humidity"]
    description = weather_data["weather"][0]["description"]

    # Print the weather information
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Description: {description}")
else:
    # Print an error message if the request was not successful
    print("Error:", response.status_code)
