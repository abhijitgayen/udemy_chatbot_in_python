from chat import BasicChatBot

chatbot = BasicChatBot('intent.json','model/intent_model.pth')

while True:
    user_input = input("User Message: ")
    bot_response, _ = chatbot.get_bot_response(user_input)
    
    if (bot_response.get("answers")):
        bot_answer = bot_response.get("answers")[0]
    else:
        bot_answer = "I am not able to give answers"
        
    print("Bot Response: ",bot_answer)