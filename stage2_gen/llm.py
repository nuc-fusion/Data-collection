from prompt.click import browser
from chatgpt import chatgpt_call
import re
debug = False

class Agent:
    def __init__(self):
        self.history = []
        self.intention_history = []
        self.operation = [
            r"(Click)\s*([A-Z]{2})",
            r"(Type)\s*([A-Z]{2})\s*([\w\s]+)",
            r"(Scroll up)\s*(\d+\.?\d*)",
            r"(Scroll down)\s*(\d+\.?\d*)",
            r"(Goto)\s*(/https?\/\/:[-a-z0-9]+(\.[-a-z0-9])*\.(com|cn|edu|uk)\/[-a-z0-9_:@&?=+,.!/~*'%$]*/ig)",
            r"(Go backward)",
            r"(Go forward)",
            r"(Hover)\s*([A-Z]{2})",
            r"(Answer)\s*([\w\s]+)",
            r"(Login)",
            r"(Verify)",
            r"(Exit)"
        ]
    
    def extract_action(self, answer):
        print(answer)
        for regex in self.operation:
            matches = re.findall(regex, answer)

            if matches:
                m = matches[-1]
                if isinstance(m, tuple):
                    operation = m[0]
                    param = m[1:]
                else:
                    operation = m
                    param = None
                    
                return operation, param
            
        return None, None

    def extract_intention(self, answer):
        matches = re.findall(r"\# Intention: ([\w\s]+)", answer)

        if matches:
            return matches[-1]
        else:
            return 'None'
        
    async def get_model_output(self, page_html, opertation):
        prompt = browser % (page_html)
        answer = await chatgpt_call(self.history, prompt, opertation)
            
        print('==== Prompt ====\n' + prompt + '\n==== Prompt ====')
        print('==== Answer ====\n' + answer + '\n==== Answer ====')
        
        
        regex = r'(?i)Mission: (.*)'
        matches = re.findall(regex, answer)
        question = matches[-1]

        regex = r'(?i)Operation: (.*)'
        matches = re.findall(regex, answer)
        answer_ = matches[-1]
        
        op, param = self.extract_action(answer_)
        
        return question, answer_, op, param
            
        

    