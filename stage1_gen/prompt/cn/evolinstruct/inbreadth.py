in_breadth_prompt = [
'''请扮演一个提示工程师。我会给你一个网站描述和一个在该网站上执行的任务提示。你的目标是从#给定提示#中汲取灵感，创建一个全新的提示。这个新提示应该与#给定提示#属于同一个领域，但更为罕见。
#创建提示#的“长度”和难度级别应与#给定提示#相近。
#创建提示#必须是合理的，并且必须能被人类理解和回复。
在#创建提示#中不允许出现“#给定提示#”和“#创建提示#”。
#网站描述#：
%s
#给定提示#：
%s
#创建提示#：
'''
]