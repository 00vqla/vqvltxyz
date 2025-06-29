import requests
import json
from flask import Flask, jsonify

# Telegram Bot API configuration
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"  # Get this from @BotFather
CHANNEL_USERNAME = "vqvlt"  # Your supergroup username without @

def get_channel_info():
    """Get channel/supergroup information using Telegram Bot API"""
    try:
        # Method 1: Get channel info
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/getChat"
        params = {"chat_id": f"@{CHANNEL_USERNAME}"}
        
        response = requests.get(url, params=params)
        data = response.json()
        
        if data.get("ok"):
            chat_info = data["result"]
            member_count = chat_info.get("member_count", "Unknown")
            title = chat_info.get("title", "VQVLT")
            description = chat_info.get("description", "")
            
            return {
                "success": True,
                "title": title,
                "member_count": member_count,
                "description": description,
                "username": f"@{CHANNEL_USERNAME}",
                "invite_link": f"https://t.me/{CHANNEL_USERNAME}"
            }
        else:
            return {
                "success": False,
                "error": "Could not fetch channel info",
                "details": data.get("description", "Unknown error")
            }
            
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

def get_chat_member_count():
    """Get member count specifically"""
    try:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/getChatMemberCount"
        params = {"chat_id": f"@{CHANNEL_USERNAME}"}
        
        response = requests.get(url, params=params)
        data = response.json()
        
        if data.get("ok"):
            return {
                "success": True,
                "member_count": data["result"]
            }
        else:
            return {
                "success": False,
                "error": data.get("description", "Unknown error")
            }
            
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

# Flask routes for API endpoints
app = Flask(__name__)

@app.route('/api/channel-info')
def api_channel_info():
    """API endpoint to get channel information"""
    return jsonify(get_channel_info())

@app.route('/api/member-count')
def api_member_count():
    """API endpoint to get member count"""
    return jsonify(get_chat_member_count())

if __name__ == "__main__":
    print("Telegram API Helper")
    print("To use this:")
    print("1. Create a bot with @BotFather")
    print("2. Add the bot to your supergroup as admin")
    print("3. Replace YOUR_BOT_TOKEN_HERE with your actual bot token")
    print("4. Run this file to test the API")
    
    # Test the API (uncomment when you have a bot token)
    # result = get_channel_info()
    # print(json.dumps(result, indent=2)) 