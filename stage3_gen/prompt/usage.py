browser = """You are a helpful assistant that can assist with web understanding.
You are given a simplified HTML code. 
Your task is to come up with a qustion to ask the usage of one element on the html and answer the question based the provided simplified HTML. If you are not sure about the usage of the element, you should answer "None".

HTML code: %s

Please write out the question you come up with and the answer to the question, which is the usage of the chosen element.

Example HTML code:
<< FasterXML is the business<a[AA] Woodstox streaming XML pa><a[AB] Jackson streaming JSON pa><a[AC] Aalto><a[AD] family>> FasterXML offers consulti<a[AE] services> Nobody does bits, bytes, <a[AF] Contact us><<a[AG] Projects><a[AH] Services><a[AI] People><a[AJ] Contact>>>

Example answer format:
Question: What is the usage of the elemnet <a[AJ] Contact>?
Answer: To redirect the user to the contact page.

Please provide the Qustion and Answer.
"""