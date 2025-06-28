#Step 1: Define the Bot’s Personality
print("👋 Hey there! I'm CryptoBuddy – your AI-powered financial sidekick! 🚀")
print("Ask me anything about trending or sustainable cryptos, and I’ll do my best to guide you!")

#Step 2: Predefined Crypto Dataset
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10
    }
}

#Step 3: Chatbot Logic with If-Else Rules
def chatbot_response(user_query):
    user_query = user_query.lower()
    
    if "sustainable" in user_query or "eco" in user_query:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        print(f"🌱 Try {recommend}! It's eco-friendly and built for the long run!")

    elif "trending" in user_query or "rising" in user_query:
        trending = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising"]
        print("📈 These coins are on the rise:", ", ".join(trending))

    elif "most profitable" in user_query or "long-term growth" in user_query:
        for coin, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["market_cap"] == "high":
                print(f"🚀 Consider {coin}! It's trending and has strong market value!")
                break
        else:
            print("Hmm, I couldn’t find a coin with both high growth and high market cap right now.")

    else:
        print("🤔 I’m not sure about that. Try asking about 'sustainability' or 'trending coins'.")

#Step 4: Sample Conversation
# Example run
chatbot_response("Which crypto should I buy for long-term growth?")
chatbot_response("What’s the most sustainable coin?")
chatbot_response("Which crypto is trending up?")
chatbot_response("Tell me something new")

#Disclaimer
print("⚠️ Reminder: Crypto is risky—always do your own research before investing.")

