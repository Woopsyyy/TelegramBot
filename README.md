# Telegram Bot

An autoresponder bot built with Python and the python-telegram-bot library.

## Setup

1. Create a new bot with [@BotFather](https://t.me/botfather) on Telegram and get your bot token.

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set your bot token in the `.env` file:
   ```
   TELEGRAM_BOT_TOKEN=your_actual_bot_token_here
   ```

4. Run the bot:
   ```
   python main.py
   ```

## Features

- `/start` command: Greets the user
- `/resources` command: Shows available resources with inline buttons
- `/building` command: Shows available buildings with inline buttons
- `/subscription` command: Shows available subscriptions with inline buttons
- `/club` command: Shows available club resources with inline buttons
- Autoresponder: Responds to any text message with resources
- Inline buttons for resources: Simcash, Storage, Simoleons, Land Expansion, Golden Tickets
- Inline buttons for buildings: Omega Buildings, Epic Buildings, Special Building, Deluxe Buildings
- Inline buttons for subscriptions: Unlimited War Items, Unlimited SimCash Refill
- Inline buttons for club resources: War Cards, Booster, War Items
- Transaction handling: "Buy Now" buttons for all deals direct buyers to contact the seller at https://t.me/aintjosh00

## Development

To add more features, modify `main.py` and add new handlers as needed.
