import openai

openai.api_key = "sk-6T09FQHoprIOt1uvsHx2su80kKMxrbs4N2j64MKtPLT3BlbkFJ2cTqUjcrSdPROMiYkhsUt8n7F1XitvEvNga7sPyssA"

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
    )
    
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "exit":
            break
        
        response = chat_with_gpt(user_input)
        print(f"GPT: {response}")