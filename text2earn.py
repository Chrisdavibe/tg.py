https://github.com/Chrisdavibe/T2E-for-Sulaimon-.git

from telegram.ext import Updater, MessageHandler, Filters

# Function to track and assign points
def track_message(update, context):
    user_id = update.message.from_user.id
    user_name = update.message.from_user.username
    # Assign points (e.g., 5 points per message)
    add_points(user_id, user_name, 5)

updater = Updater('YOUR_BOT_TOKEN', use_context=True)
dp = updater.dispatcher
dp.add_handler(MessageHandler(Filters.text, track_message))

updater.start_polling()
updater.idle()


Store User point. 

import sqlite3

# Initialize or connect to the database
conn = sqlite3.connect('points.db')
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS user_points 
                  (user_id INTEGER PRIMARY KEY, username TEXT, points INTEGER DEFAULT 0)''')

# Add points function
def add_points(user_id, user_name, points):
    cursor.execute('SELECT points FROM user_points WHERE user_id=?', (user_id,))
    result = cursor.fetchone()
    if result:
        new_points = result[0] + points
        cursor.execute('UPDATE user_points SET points=? WHERE user_id=?', (new_points, user_id))
    else:
        cursor.execute('INSERT INTO user_points (user_id, username, points) VALUES (?, ?, ?)', (user_id, user_name, points))
    conn.commit()


Handle Point Redemption 
def get_points(update, context):
    user_id = update.message.from_user.id
    cursor.execute('SELECT points FROM user_points WHERE user_id=?', (user_id,))
    result = cursor.fetchone()
    if result:
        update.message.reply_text(f"You have {result[0]} points.")
    else:
        update.message.reply_text("You don't have any points yet.")

dp.add_handler(CommandHandler('points', get_points))
