polish_prompt = '''I want you to act as a Task Prompt Rewriter. I will give you a website description and a task prompt which is to be completed on the website. Your objective is to rewrite the task prompt into a more realistic, specific one. You SHOULD rewrite the task using the following method:
If #Given Prompt# contains information like location, destination, date, time, name, etc., replace this information with a REAL, ACTUAL one.
You should rewrite the task prompt to make it as close to the real website user queries as possible.
#Website Description#:
%s
#Given Task Prompt#:
%s
#Rewritten Task Prompt#:
'''