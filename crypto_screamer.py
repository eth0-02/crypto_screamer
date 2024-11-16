import time
import requests
from termcolor import colored
import pygame
import httpx  # Using httpx to avoid SSL/TLS issues

# Configuration
CRYPTO_ID = 'peanut-the-squirrel'  # Crypto identifier for CoinGecko
TARGET_PRICE_LOW = 1.8  # Price at which to scream if price drops below this
TARGET_PRICE_HIGH = 2.0  # Price at which to scream if price goes above this
AMOUNT_TO_INVEST = 100  # Amount in USD to start with
DAILY_PROFIT_GOAL = 20  # Daily profit goal in USD
GILFOYLE_SCREAM_SOUND_PATH = "gilfoyle_scream.mp3"  # Path to the scream sound

# Initialize Pygame mixer for playing sound
pygame.mixer.init()

# Fetch current price of the crypto from CoinGecko
def get_crypto_price(crypto_id=CRYPTO_ID):
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies=usd'
    try:
        with httpx.Client() as client:
            response = client.get(url)
        data = response.json()
        if crypto_id in data:
            return data[crypto_id]['usd']
        else:
            print("Error: Crypto data not found.")
            return None
    except Exception as e:
        print(f"Error fetching data from CoinGecko: {e}")
        return None

# Function to play scream sound
def play_scream():
    pygame.mixer.music.load(GILFOYLE_SCREAM_SOUND_PATH)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():  # Wait until sound finishes playing
        time.sleep(1)

# Monitor the crypto price and check when to buy, sell, and scream
def monitor_price():
    current_balance = AMOUNT_TO_INVEST
    current_price = get_crypto_price()

    if current_price is None:
        print("Could not fetch price.")
        return

    print(colored(f"Current Price: ${current_price:.2f}", 'green'))

    # Buying logic
    coins_bought = current_balance / current_price
    print(f"Amount of {CRYPTO_ID} bought: {coins_bought:.2f}")

    # Simulate price tracking for a day to check if we meet profit goal
    profit_made = 0
    while profit_made < DAILY_PROFIT_GOAL:
        current_price = get_crypto_price()
        if current_price is None:
            print("Error fetching price. Exiting monitoring.")
            break
        
        # Calculate potential profit
        new_balance = coins_bought * current_price
        profit_made = new_balance - current_balance

        if profit_made >= DAILY_PROFIT_GOAL:
            print(f"Profit goal reached: ${profit_made:.2f}!")
            break
        
        # Output price in red/green depending on whether the price goes up or down
        if current_price < TARGET_PRICE_LOW:
            print(colored(f"Price dropped below {TARGET_PRICE_LOW} USD: {current_price:.2f} USD", 'red'))
            play_scream()
        elif current_price > TARGET_PRICE_HIGH:
            print(colored(f"Price went above {TARGET_PRICE_HIGH} USD: {current_price:.2f} USD", 'green'))
            play_scream()
        else:
            print(colored(f"Current Price: {current_price:.2f} USD", 'yellow'))
        
        # Sleep before checking again
        time.sleep(60)  # Check every minute (adjust as needed)

if __name__ == "__main__":
    monitor_price()
