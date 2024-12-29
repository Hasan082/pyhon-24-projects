# Cryptocurrency Price Alert System

This Python script monitors the prices of selected cryptocurrencies and triggers an alert if the price exceeds the predefined upper or lower limits. It uses the `crypto_data` module to retrieve real-time coin data and check for price thresholds. Alerts are printed in the console for high or low price conditions and if the current price exceeds the 24-hour high or low for the coin.

## Features

- Monitors cryptocurrency prices in real-time.
- Alerts when the price crosses a specified upper or lower limit.
- Alerts if the current price exceeds the highest or lowest price in the past 24 hours.
- Adjustable coin selection and price range.

## Requirements

Before running the script, ensure that you have the following dependencies installed:

- Python 3.7 or higher
- `crypto_data` module (assumed to be custom or pre-installed)

### Installation

1. **Install required dependencies** (if applicable). Assuming `crypto_data` is a custom module, ensure that it is available in your environment.

2. **Logging setup**: The script uses the `logging` module for error logging. You may want to configure it further if needed.

## Setup

1. **Run the script**:

   Once the setup is complete, you can run the script as follows:

   ```bash
   python price_alert.py
   ```

   The script will start monitoring the prices of `BTC` and `ETH` (Bitcoin and Ethereum) and alert you if their prices cross the set limits.

2. **Modify the Coin Selection**:

   To change the coins being monitored, modify the symbols and limits in the script. For example, to add a new coin or change the existing ones, update the `alerter()` function calls in the `while` loop:

   ```python
   alerter('btc', lower_limit=90000, upper_limit=97100, coin_list=coins)
   alerter('eth', lower_limit=1800, upper_limit=3400, coin_list=coins)
   ```

   Replace `'btc'` and `'eth'` with the desired cryptocurrency symbols, and adjust the `lower_limit` and `upper_limit` as needed.

3. **Error Handling**:

   If any error occurs, the script will log the error message. You can view the log by checking the output of the script or configuring a logging file to store logs.

## Code Overview

- **alerter**: This function checks the current price of the cryptocurrency and compares it with the specified upper and lower limits. It also checks if the price exceeds the 24-hour high or low.
- **Logging**: Errors are caught and logged using the `logging` module.
- **Main Loop**: The script runs continuously, checking prices every 30 seconds for the specified coins.

## Example Output

If the price of Bitcoin (BTC) crosses the defined range, you might see an output like:

```
Bitcoin | High Price | TRIGGER ALERT!!
Bitcoin | Today's Highest Alert!! Current Price: $95,000.00 | Highest 24h: $94,000.00
```

## License

This project is licensed under the MIT License
