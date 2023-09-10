from prompt.usage import browser
from chatgpt import chatgpt_call
import re
debug = False

class Agent:
    def __init__(self):
        self.history = []
        pass

    async def get_model_output(self, page_html):
        prompt = browser % (page_html)
        answer = await chatgpt_call(self.history, prompt)
            
        print('==== Prompt ====\n' + prompt + '\n==== Prompt ====')
        print('==== Answer ====\n' + answer + '\n==== Answer ====')
        
        regex = r'(?i)Question: (.*)'
        matches = re.findall(regex, answer)
        question = matches[-1]

        regex = r'(?i)Answer: (.*)'
        matches = re.findall(regex, answer)
        answer = matches[-1]
        
        return question, answer
            
        

    