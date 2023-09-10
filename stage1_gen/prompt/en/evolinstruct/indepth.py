add_constraints_prompt = '''I want you to act as a Prompt Rewriter. I will give you a website description and a task prompt which is to be completed on the website. Your objective is to rewrite the given prompt into a more complex version to make those famous AI systems (e.g., ChatGPT and GPT4) a bit harder to handle. But the rewritten prompt must be reasonable, understood, and responded to by humans. Your rewriting cannot omit the non-text parts, such as the table and code in #Given Prompt#. Also, please do not omit the input in #Given Prompt#. You SHOULD complicate the given prompt using the following method:
Please add one more constraint/requirement into #Given Prompt#
You should try your best to avoid making the #Rewritten Prompt# verbose. # Rewritten Prompt# can only add 10 to 20 words into #Given Prompt#. 
‘#Given Prompt#’, ‘#Rewritten Prompt#’, ‘given prompt’ and ‘rewritten prompt’ are not allowed to appear in #Rewritten Prompt#
#Website Description#:
%s
#Given Prompt#:
%s
#Rewritten Prompt#:
'''

deepening_prompt = '''I want you to act as a Prompt Rewriter. I will give you a website description and a task prompt which is to be completed on the website. Your objective is to rewrite the given prompt into a more complex version to make those famous AI systems (e.g., ChatGPT and GPT4) a bit harder to handle. But the rewritten prompt must be reasonable, understood, and responded to by humans. Your rewriting cannot omit the non-text parts, such as the table and code in #Given Prompt#. Also, please do not omit the input in #Given Prompt#. You SHOULD complicate the given prompt using the following method:
If #Given Prompt# contains inquiries about certain issues, the depth and breadth of the inquiry can be increased.
You should try your best to avoid making the #Rewritten Prompt# verbose. # Rewritten Prompt# can only add 10 to 20 words into #Given Prompt#. 
‘#Given Prompt#’, ‘#Rewritten Prompt#’, ‘given prompt’ and ‘rewritten prompt’ are not allowed to appear in #Rewritten Prompt#
#Website Description#:
%s
#Given Prompt#:
%s
#Rewritten Prompt#:
'''

concretizing_prompt = '''I want you to act as a Prompt Rewriter. I will give you a website description and a task prompt which is to be completed on the website. Your objective is to rewrite the given prompt into a more complex version to make those famous AI systems (e.g., ChatGPT and GPT4) a bit harder to handle. But the rewritten prompt must be reasonable, understood, and responded to by humans. Your rewriting cannot omit the non-text parts, such as the table and code in #Given Prompt#. Also, please do not omit the input in #Given Prompt#. You SHOULD complicate the given prompt using the following method:
Please replace general concepts with more specific concepts.
You should try your best to avoid making the #Rewritten Prompt# verbose. # Rewritten Prompt# can only add 10 to 20 words into #Given Prompt#. 
‘#Given Prompt#’, ‘#Rewritten Prompt#’, ‘given prompt’ and ‘rewritten prompt’ are not allowed to appear in #Rewritten Prompt#
#Website Description#:
%s
#Given Prompt#:
%s
#Rewritten Prompt#:
'''

increase_reasoning_steps_prompt = '''I want you to act as a Prompt Rewriter. I will give you a website description and a task prompt which is to be completed on the website. Your objective is to rewrite the given prompt into a more complex version to make those famous AI systems (e.g., ChatGPT and GPT4) a bit harder to handle. But the rewritten prompt must be reasonable, understood, and responded to by humans. Your rewriting cannot omit the non-text parts, such as the table and code in #Given Prompt#. Also, please do not omit the input in #Given Prompt#. You SHOULD complicate the given prompt using the following method:
If #Given Prompt# can be solved with just a few simple thinking processes, you can rewrite it to explicitly request multiple-step reasoning.
You should try your best to avoid making the #Rewritten Prompt# verbose. # Rewritten Prompt# can only add 10 to 20 words into #Given Prompt#. 
‘#Given Prompt#’, ‘#Rewritten Prompt#’, ‘given prompt’ and ‘rewritten prompt’ are not allowed to appear in #Rewritten Prompt#
#Website Description#:
%s
#Given Prompt#:
%s
#Rewritten Prompt#:
'''

replace_input_prompt = '''I want you to act as a Prompt Rewriter. I will give you a website description and a task prompt which is to be completed on the website. If #Given Prompt# contains information like location, destination, date, time, name, etc., your objective is to replace the information with another REAL, ACTUAL one. You should rewrite the task prompt to make it as close to the real website user queries as possible.
#Website Description#:
%s
#Given Prompt#:
%s
#Rewritten Prompt#:
'''

in_depth_prompt = [
    add_constraints_prompt,
    deepening_prompt,
    concretizing_prompt,
    increase_reasoning_steps_prompt,
    replace_input_prompt
]