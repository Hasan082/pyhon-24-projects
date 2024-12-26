# Weather App

This is a simple Python application that fetches weather data for a city or postal code, and displays the weather
forecast in a structured format. The application retrieves data in 3-hour intervals for the next 5 days from a weather
API and presents it in a readable way, displaying the temperature and weather conditions for each time slot.

## Project Structure

```
WeatherApp/
├── api.py                # Handles API requests to fetch weather data.
├── main.py               # Main script for running the application and displaying weather information.
├── model.py              # Contains the Weather class and model definitions.
├── weather.json          # Example of a dummy weather data file for local testing.
└── weather_api.py        # Functions to interact with the weather API and retrieve data.
```

## Requirements

- Python 3.x
- `requests` library (for making HTTP requests)
- `logging` (for error handling and logging)

You can install the required dependencies using the following:

```bash
pip install -r requirements.txt
```

If the `requirements.txt` file is not available, you can manually install the required libraries:

```bash
pip install requests
```

## How to Use

1. Clone this repository:

   ```bash
   git clone https://github.com/Hasan082/WeatherApp.git
   cd WeatherApp
   ```

2. Open the `main.py` file or run it directly:

   ```bash
   python main.py
   ```

3. When prompted, enter a city name or postal code (e.g., "New York" or "94040" for Mountain View). The program will
   fetch the weather data and display the forecast for the next 5 days in 3-hour intervals.

4. The program will display the weather conditions such as the temperature and weather description at each time
   interval.

### Example Output:

```bash
Enter city name or postal code: London
City from API:  London
Current weather status: 200
2024-12-27
------
00:00 15.52C scattered clouds
03:00 15.73C light rain
06:00 17.43C light rain
09:00 22.45C scattered clouds
12:00 22.59C scattered clouds
15:00 20.29C clear sky
18:00 16.59C scattered clouds
21:00 15.54C overcast clouds
------
```

## How It Works

- The `get_weather` function fetches the current weather data from the weather API, and `get_weather_details` fetches
  detailed weather data for the next 5 days.
- The data is grouped by date, and each day is printed with the corresponding weather conditions in 3-hour intervals.
- The application will keep asking for the correct city name until a valid response is received (status code `200`).

## Error Handling

- If an invalid city name is entered, the program will display an error message asking the user to try again.
- If the API responds with a status code `404`, the program will notify the user that the city was not found.
- For unauthorized access or other errors, the program will handle them gracefully and provide a meaningful message.

### Possible Error Messages:

- **404**: City not found.
- **401**: Unauthorized access (incorrect API key).
- **Other**: General error, something went wrong.

## API Source

The weather data is fetched using a weather API. Make sure to replace the API key in `weather_api.py` with your own API
key if you are using a live service.

## Contributions

Feel free to fork this repository, make changes, and submit pull requests if you'd like to contribute.

## License

This project is licensed under the MIT License.