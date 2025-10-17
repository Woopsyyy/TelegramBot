import os
import logging
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters, CallbackQueryHandler

# Load environment variables from .env file
load_dotenv()

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Get bot token from environment variable
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
if not TOKEN:
    raise ValueError("Please set the TELEGRAM_BOT_TOKEN environment variable")



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! I am your autoresponder bot. Use /resources for resources, /building for buildings, /subscription for subscriptions, or /club for club resources.')

async def resources(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Simcash", callback_data='simcash')],
        [InlineKeyboardButton("Storage", callback_data='storage')],
        [InlineKeyboardButton("Simoleons", callback_data='simoleons')],
        [InlineKeyboardButton("Land Expansion", callback_data='land')],
        [InlineKeyboardButton("Golden Tickets", callback_data='golden')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Available services:', reply_markup=reply_markup)

async def building(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Omega Buildings", callback_data='omega')],
        [InlineKeyboardButton("Epic Buildings", callback_data='epic')],
        [InlineKeyboardButton("Special Building", callback_data='special')],
        [InlineKeyboardButton("Deluxe Buildings", callback_data='deluxe')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Available buildings:', reply_markup=reply_markup)

async def subscription(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Unlimited War Items", callback_data='war')],
        [InlineKeyboardButton("Unlimited SimCash Refill", callback_data='simcash_refill')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Available subscriptions:', reply_markup=reply_markup)

async def club(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("War Cards", callback_data='war_cards')],
        [InlineKeyboardButton("Booster", callback_data='booster')],
        [InlineKeyboardButton("War Items", callback_data='war_items')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Available club resources:', reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == 'simcash':
        deal_text = """
💵 SIMCASH DEAL 💵
💰 40,000 – $4
💰 30,000 – $3
💰 20,000 – $2
💰 10,000 – $1

⚠ 45,000 Simcash is the limit. Exceeding this will result in a ban.
        """
        keyboard = [[InlineKeyboardButton("Buy Now", callback_data='buy_simcash')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text=deal_text, reply_markup=reply_markup)
    elif query.data == 'storage':
        deal_text = """
📦STORAGE UPGRADE DEAL📦

🛒 1000 Storage Space – $10
🛒 1800 Storage Space – $15 (Must empty storage first)
        """
        keyboard = [[InlineKeyboardButton("Buy Now", callback_data='buy_storage')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text=deal_text, reply_markup=reply_markup)
    elif query.data == 'simoleons':
        deal_text = """
SIMOLEONS DEAL
💰 25,000,000 – $4
💰 50,000,000 – $8
💰 75,000,000 – $10
        """
        keyboard = [[InlineKeyboardButton("Buy Now", callback_data='buy_simoleons')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text=deal_text, reply_markup=reply_markup)
    elif query.data == 'land':
        deal_text = """
━━ ✦ LAND EXPANSION DEALS ✦ ━━

🏝 Land Expansion Package – $35 🏝
✔ 75 Land Items
✔ 20 Beach & Mountain Items

📌 Separate Deal:
💰 $0.75 per Land Ticket
💰 $0.50 per Beach & Mountain Ticket
        """
        keyboard = [[InlineKeyboardButton("Buy Now", callback_data='buy_land')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text=deal_text, reply_markup=reply_markup)
    elif query.data == 'golden':
        deal_text = """
✨ Golden Tickets – $10 ✨
🎟 100 Golden Ticket
        """
        keyboard = [[InlineKeyboardButton("Buy Now", callback_data='buy_golden')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text=deal_text, reply_markup=reply_markup)
    elif query.data == 'omega':
        deal_text = """
🏢 BUILDINGS DEAL 🏢
💰 Each Building – $3 (100 per purchase)

🟣 Omega Buildings 🟣
- Omega Recycling Center
- Omega Power Plant
- Omega Water Tower
- Omega Sewage Treatment Plant
        """
        keyboard = [[InlineKeyboardButton("Buy Now", callback_data='buy_omega')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text=deal_text, reply_markup=reply_markup)
    elif query.data == 'epic':
        deal_text = """
🛒 SimCity BuildIt Shop
Affordable & Instant Delivery!

🏛 Epic Buildings
💰 $10 per 4 Houses

Landmark
Beach
Mountain
Space Gambling
Entertainment
Transportation
Education
🏡 Normal

Residential Houses
💰 $5 per 4 Houses

Residential
Paris
Tokyo
London
Green Valley
Cactus Canyon
Sunny Island
Frozen Fjord
Limestone
Latin
Old Town
Art Nouveau
Florentine Zone
Omega
        """
        keyboard = [[InlineKeyboardButton("Buy Now", callback_data='buy_epic')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text=deal_text, reply_markup=reply_markup)
    elif query.data == 'special':
        deal_text = """
🏢 BUILDINGS DEAL 🏢
💰 Each Building – $3 (100 per purchase)

🏛 Special Building
- Maxis Manor
        """
        keyboard = [[InlineKeyboardButton("Buy Now", callback_data='buy_special')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text=deal_text, reply_markup=reply_markup)
    elif query.data == 'deluxe':
        deal_text = """
🏢 BUILDINGS DEAL 🏢
💰 Each Building – $3 (100 per purchase)

🚀 Deluxe Buildings
- Deluxe Drone Base
- Deluxe ControlNet Tower
        """
        keyboard = [[InlineKeyboardButton("Buy Now", callback_data='buy_deluxe')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text=deal_text, reply_markup=reply_markup)
    elif query.data == 'war':
        deal_text = """
Unlimited War Items (1 month)
🔥 $30 → Any War Item 🔥

Get unlimited refills of any war item for a whole week! ⚔💥
        """
        keyboard = [[InlineKeyboardButton("Buy Now", callback_data='buy_war')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text=deal_text, reply_markup=reply_markup)
    elif query.data == 'simcash_refill':
        deal_text = """
Unlimited SimCash Refill (1 month)
✨ $60 → 45,000 SimCash ✨

Enjoy unlimited refills anytime for a whole week! 🚀
        """
        keyboard = [[InlineKeyboardButton("Buy Now", callback_data='buy_simcash_refill')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text=deal_text, reply_markup=reply_markup)
    elif query.data == 'war_cards':
        deal_text = """
*⚔ WAR CARDS DEAL ⚔*

📌 *Buy at your own risk*

 *📜 New Account* – *$10*
🔹 Level 7

*📜 3 Months or More* – *$20*
🔹 Max Level / Level 20

*🔥 Available War Cards*
- Magnetism
- Shield Buster
- Mellow Bellow
- Doomsday Quack

⚠ *Reminder:* Before buying disaster cards, make sure your club is not in war.
        """
        keyboard = [[InlineKeyboardButton("Buy Now", callback_data='buy_war_cards')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text=deal_text, reply_markup=reply_markup, parse_mode='Markdown')
    elif query.data == 'booster':
        deal_text = """
🚀 BOOSTER DEAL 🚀

🎟 $5 per 100 Boosters

📌 Example:
✅ 100 JP III + 100 Freeze III = $10
        """
        keyboard = [[InlineKeyboardButton("Buy Now", callback_data='buy_booster')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text=deal_text, reply_markup=reply_markup)
    elif query.data == 'war_items':
        deal_text = """
⚔ WAR ITEMS DEAL ⚔

💥 $3 per 100 War Items 💥

📌 Example:
✅ 100 Anvils + 100 Binoculars = $6(200 storage space)
        """
        keyboard = [[InlineKeyboardButton("Buy Now", callback_data='buy_war_items')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text=deal_text, reply_markup=reply_markup)
    elif query.data == 'buy_simcash':
        await query.edit_message_text(text="Contact the seller to discuss the transaction: https://t.me/aintjosh00")
    elif query.data == 'buy_storage':
        await query.edit_message_text(text="Contact the seller to discuss the transaction: https://t.me/aintjosh00")
    elif query.data == 'buy_simoleons':
        await query.edit_message_text(text="Contact the seller to discuss the transaction: https://t.me/aintjosh00")
    elif query.data == 'buy_land':
        await query.edit_message_text(text="Contact the seller to discuss the transaction: https://t.me/aintjosh00")
    elif query.data == 'buy_golden':
        await query.edit_message_text(text="Contact the seller to discuss the transaction: https://t.me/aintjosh00")
    elif query.data == 'buy_omega':
        await query.edit_message_text(text="Contact the seller to discuss the transaction: https://t.me/aintjosh00")
    elif query.data == 'buy_epic':
        await query.edit_message_text(text="Contact the seller to discuss the transaction: https://t.me/aintjosh00")
    elif query.data == 'buy_special':
        await query.edit_message_text(text="Contact the seller to discuss the transaction: https://t.me/aintjosh00")
    elif query.data == 'buy_deluxe':
        await query.edit_message_text(text="Contact the seller to discuss the transaction: https://t.me/aintjosh00")
    elif query.data == 'buy_war':
        await query.edit_message_text(text="Contact the seller to discuss the transaction: https://t.me/aintjosh00")
    elif query.data == 'buy_simcash_refill':
        await query.edit_message_text(text="Contact the seller to discuss the transaction: https://t.me/aintjosh00")
    elif query.data == 'buy_war_cards':
        await query.edit_message_text(text="Contact the seller to discuss the transaction: https://t.me/aintjosh00")
    elif query.data == 'buy_booster':
        await query.edit_message_text(text="Contact the seller to discuss the transaction: https://t.me/aintjosh00")
    elif query.data == 'buy_war_items':
        await query.edit_message_text(text="Contact the seller to discuss the transaction: https://t.me/aintjosh00")

async def autorespond(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Simcash", callback_data='simcash')],
        [InlineKeyboardButton("Storage", callback_data='storage')],
        [InlineKeyboardButton("Simoleons", callback_data='simoleons')],
        [InlineKeyboardButton("Land Expansion", callback_data='land')],
        [InlineKeyboardButton("Golden Tickets", callback_data='golden')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Available services:', reply_markup=reply_markup)

def main():
    application = ApplicationBuilder().token(TOKEN).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("resources", resources))
    application.add_handler(CommandHandler("building", building))
    application.add_handler(CommandHandler("subscription", subscription))
    application.add_handler(CommandHandler("club", club))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, autorespond))

    # Start the bot
    application.run_polling()

if __name__ == '__main__':
    main()
