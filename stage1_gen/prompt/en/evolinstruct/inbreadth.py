in_breadth_prompt = [
'''I want you act as a Prompt Creator. I will give you a website description and a task prompt which is to be completed on the website. Your goal is to draw inspiration from the #Given Prompt# to create a brand new prompt. This new prompt should belong to the same domain as the #Given Prompt# but be even more rare.
The LENGTH and difficulty level of the #Created Prompt# should be similar to that of the #Given Prompt#.
The #Created Prompt# must be reasonable and must be understood and responded by humans.
‘#Given Prompt#’, ‘#Created Prompt#’, ‘given prompt’ and ‘created prompt’ are not allowed to appear in #Created Prompt#.
#Website Description#:
%s
#Given Prompt#:
%s
#Created Prompt#:
'''
]