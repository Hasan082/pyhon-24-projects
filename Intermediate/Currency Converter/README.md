# Exchange Rate Conversion Tool

This project is a simple command-line tool to convert currency values using exchange rates fetched from an API. It is written in Python and utilizes a public API for real-time exchange rate data.

---

## Features

- Fetches real-time exchange rates from the [Exchange Rates API](https://exchangeratesapi.io/).
- Supports mock data for offline testing using a `rates.json` file.
- Converts between different currencies.
- Handles errors gracefully with meaningful log messages.

---

## Requirements

- Python 3.8+
- Internet connection (for real-time exchange rate fetching)

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/exchange-rate-tool.git
   cd exchange-rate-tool
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up the mock data file (optional):

   - If you want to test the tool offline, create a `rates.json` file in the same directory with sample exchange rate data.

---

## Usage

Run the program using the following command:

```bash
python main.py
```

### Arguments

1. **Amount:** Enter the amount you want to convert.
2. **Base Currency:** Specify the currency you are converting from (e.g., `USD`).
3. **Target Currency:** Specify the currency you want to convert to (e.g., `EUR`).

### Example Interaction

```
How much amount you want to convert: 100
Which currency do you want to convert: USD
What currency do you want to convert: EUR
Converted amount: 92.34 EUR
```

---

## Logging

The tool uses Python's built-in logging module to log errors. Logs are printed to the console and can help debug issues such as:

- Missing or invalid data in the mock file.
- Connection issues while fetching data from the API.
- Invalid currency codes.

---

## Configuration

- **API URL:**

  The API URL is set in the `BASE_URL` variable:

  ```python
  BASE_URL: Final[str] = 'https://api.exchangeratesapi.io/v1/latest'
  ```

- **API Key:**

  Replace the `API_KEY` variable with your actual API key:

  ```python
  API_KEY: Final[str] = 'your_api_key_here'
  ```

- **Mock Mode:**

  To use the tool in mock mode, set the `mock` argument to `True` when calling `get_rates`:

  ```python
  data: dict = get_rates(mock=True)
  ```

---

## Error Handling

- **Invalid JSON:** Logs an error if the API returns invalid JSON.
- **Request Failures:** Logs an error if the API request fails.
- **Invalid Currency Codes:** Raises a `ValueError` if the currency code is not valid.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request for improvements or bug fixes.

---

## Acknowledgments

- [Exchange Rates API](https://exchangeratesapi.io/) for providing the currency data.

