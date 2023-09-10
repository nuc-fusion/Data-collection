add_constraints_prompt = '''请扮演一个提示工程师。我会给你一个网站描述和一个在该网站上执行的任务提示。你的目标是将给定的提示重写为更复杂的版本，使那些著名的人工智能系统（例如，ChatGPT和GPT4）更难处理。但是重写后的提示必须是合理的、能被人类理解和回复的。你的重写不能省略非文本部分，例如#给定提示#中的表和代码。此外，请不要省略#给定提示#中的输入。请使用以下方法使给定的提示复杂化：
请在#给定提示#中再添加一个约束/要求
尽量避免让“重写提示”变得冗长。#重写提示#字数只能增加20到30个字。
在#重写提示#中不允许出现“#给定提示#”和“#重写提示#”。
#网站描述#：
%s
#给定提示#：
%s
#重写提示#：
'''

deepening_prompt = '''请扮演一个提示工程师。我会给你一个网站描述和一个在该网站上执行的任务提示。你的目标是将给定的提示重写为更复杂的版本，使那些著名的人工智能系统（例如，ChatGPT和GPT4）更难处理。但是重写后的提示必须是合理的、能被人类理解和回复的。你的重写不能省略非文本部分，例如#给定提示#中的表和代码。此外，请不要省略#给定提示#中的输入。请使用以下方法使给定的提示复杂化：
如果#给定提示#包含有关某些事件的问题，则可以增加问题的深度和广度。
尽量避免让“重写提示”变得冗长。#重写提示#字数只能增加20到30个字。
在#重写提示#中不允许出现“#给定提示#”和“#重写提示#”。
#网站描述#：
%s
#给定提示#：
%s
#重写提示#：
'''

concretizing_prompt = '''请扮演一个提示工程师。我会给你一个网站描述和一个在该网站上执行的任务提示。你的目标是将给定的提示重写为更复杂的版本，使那些著名的人工智能系统（例如，ChatGPT和GPT4）更难处理。但是重写后的提示必须是合理的、能被人类理解和回复的。你的重写不能省略非文本部分，例如#给定提示#中的表和代码。此外，请不要省略#给定提示#中的输入。请使用以下方法使给定的提示复杂化：
请用更具体的概念取代一般概念。
尽量避免让“重写提示”变得冗长。#重写提示#字数只能增加20到30个字。
在#重写提示#中不允许出现“#给定提示#”和“#重写提示#”。
#网站描述#：
%s
#给定提示#：
%s
#重写提示#：
'''

increase_reasoning_steps_prompt = '''请扮演一个提示工程师。我会给你一个网站描述和一个在该网站上执行的任务提示。你的目标是将给定的提示重写为更复杂的版本，使那些著名的人工智能系统（例如，ChatGPT和GPT4）更难处理。但是重写后的提示必须是合理的、能被人类理解和回复的。你的重写不能省略非文本部分，例如#给定提示#中的表和代码。此外，请不要省略#给定提示#中的输入。请使用以下方法使给定的提示复杂化：
如果#给定提示#只需要几个简单的思考过程就可以解决，请重写它来明确请求多步骤推理。
尽量避免让“重写提示”变得冗长。#重写提示#字数只能增加20到30个字。
在#重写提示#中不允许出现“#给定提示#”和“#重写提示#”。
#网站描述#：
%s
#给定提示#：
%s
#重写提示#：
'''

replace_input_prompt = '''请扮演一个提示工程师。我会给你一个网站描述和一个在该网站上执行的任务提示。如果#给定提示#包含位置、目的地、日期、时间、姓名等信息，你的目标是用另一个“真实”、“实际”的信息替换这些信息。请重写任务提示，使其尽可能接近真实的网站用户查询。
#网站描述#：
%s
#给定提示#：
%s
#重写提示#：'''

in_depth_prompt = [
    add_constraints_prompt,
    deepening_prompt,
    concretizing_prompt,
    increase_reasoning_steps_prompt,
    replace_input_prompt
]