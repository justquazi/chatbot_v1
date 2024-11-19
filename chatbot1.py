from groq import Groq
class Chatbot:
    def __init__(self, key, model="llama3-8b-8192",):
        self.key = key
        self.client = Groq(api_key=key)
        self.model = model
    def createBot(self):
        active = True
        responses = 0
        content = str(input('Enter a prompt: (Type N to end program.)  '))
        while active == True:
            chat_completion = self.client.chat.completions.create(messages=[
            {
            "role": "user",
            "content": content,
            }
            ],
            model= self.model
            #"llama3-8b-8192",
            )
            print(chat_completion.choices[0].message.content)
            responses += 1
            content = str(input('Any more questions? '))
            if content == 'N':
                active = False
            
        print('Program terminated successfully.')
        print(f'Total Responses: {responses}')

bot = Chatbot(key='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')
bot.createBot()
