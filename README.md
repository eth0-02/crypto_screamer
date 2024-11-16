# Crypto Scream Alert 🚨

This Python script monitors the price of any cryptocurrency, plays a **scream sound** when the price crosses a specified threshold, and tracks your **profit/loss** based on an initial investment. It's customizable for any cryptocurrency available on [CoinGecko](https://www.coingecko.com/), not just "Peanut the Squirrel" 🐿️!

## 🔥 Features

- **Monitor any cryptocurrency** (default is "Peanut the Squirrel").
- Set **price thresholds** to trigger a scream sound when the price goes up or down.
- Track **profit/loss** based on an initial investment 💰.
- **Play a scream sound** from *Silicon Valley* when price crosses thresholds 😱.
- Monitor prices periodically and show live profit 📈.

## 🚀 Prerequisites

Before running the script, make sure you have **Python 3.x** installed on your machine. You'll also need to install the required Python libraries.

Run the following command in your terminal:

```bash
pip install requests httpx pygame termcolor
```

### 🎶 Sound File

The script uses a scream sound from *Silicon Valley* when the price crosses the set thresholds. To use the scream, download the sound file and save it as `gilfoyle_scream.mp3` in the same directory as the script.

## 🛠️ Setup

### Step 1: Customize the Script

1. **Cryptocurrency Selection** 💎

   The script is pre-configured to monitor "Peanut the Squirrel" by default, but you can monitor any cryptocurrency available on CoinGecko by changing the `CRYPTO_ID` variable.

   - Go to [CoinGecko](https://www.coingecko.com/en/) and search for your cryptocurrency.
   - Copy the **ID** from the URL (e.g., for "Peanut the Squirrel" it's `peanut-the-squirrel`, for Bitcoin it's `bitcoin`).

   Change the `CRYPTO_ID` like this:

   ```python
   CRYPTO_ID = 'bitcoin'  # Replace with your chosen cryptocurrency ID
   ```

2. **Set Your Price Thresholds** ⚖️

   You can set your own thresholds to trigger the scream sound:

   ```python
   TARGET_PRICE_LOW = 1.8  # When price drops below this value
   TARGET_PRICE_HIGH = 2.0  # When price rises above this value
   ```

3. **Set Your Investment and Profit Goal** 🎯

   The script will track your profit based on an initial investment. By default, the script assumes you are investing $100 with a $20 daily profit goal.

   ```python
   AMOUNT_TO_INVEST = 100  # Amount in USD to start with
   DAILY_PROFIT_GOAL = 20  # Daily profit goal in USD
   ```

### Step 2: Run the Script

1. **Save the Script** 💾

   Save the provided Python script as `crypto_screamer.py` (or any name you prefer).

2. **Run the Script** 🚀

   Open your terminal, navigate to the directory where the script is saved, and run the following command:

   ```bash
   python crypto_screamer.py
   ```

   The script will start monitoring the cryptocurrency, print updates on the price, and trigger the scream sound if the price crosses your specified thresholds.

## 💡 Example Output

```bash
Current Price: $1.85
Amount of peanut-the-squirrel bought: 54.05
Price dropped below 1.80 USD: 1.79 USD
(Plays scream sound)
Current Price: 1.81 USD
Price went above 2.00 USD: 2.05 USD
(Plays scream sound)
Profit goal reached: $20.12!
```

## ⚙️ Customizing for Your Needs

- **Monitor multiple cryptocurrencies**: You can modify the script to track several coins by calling `get_crypto_price()` with different `crypto_id` values and managing alerts for each one.
- **Adjust the price-check interval**: The script checks prices every 60 seconds. You can modify the `time.sleep(60)` to check at different intervals.

## 🛠️ Troubleshooting

- **Error fetching price**: If the script fails to load the price, there may be an issue with the CoinGecko API or your internet connection. Please try again later.
- **SSL/TLS issues**: If you encounter SSL/TLS errors, switching from `requests` to `httpx` should resolve most of these issues.

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

### 💬 Feedback or Contributions?

Feel free to open an issue or create a pull request if you'd like to contribute. I'm open to suggestions for improvements or new features!

```
