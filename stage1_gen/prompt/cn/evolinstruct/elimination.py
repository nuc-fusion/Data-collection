elimination_prompt = '''以下是两条针对ChatGPT AI的指令，你认为它们彼此相等吗，如果相等需满足以下要求：
1.指令有相同的约束和要求。
2.指令的深度和广度相同。

第一个提示：%s
第二个提示：%s

你的判断（只需回答：相等或不相等。无需解释原因。）： '''

# from rouge_chinese import Rouge
# import jieba
# scorer = Rouge()

# def _check_repetition(originalTask, evolvedTask):
#     global scorer
#     _originalTask = ' '.join(jieba.cut(originalTask))
#     _evolvedTask = ' '.join(jieba.cut(evolvedTask))

#     score = scorer.get_scores(_originalTask, _evolvedTask)[0]

#     recall = score['rouge-l']['r']
#     precision = score['rouge-l']['p']
    
#     return recall > 0.8 or precision > 0.8


# check if contains prompt tag
def _check_tag(evolvedTask):
    if '#给定' in evolvedTask:
        return True
    if '#重写' in evolvedTask:
        return True
    if '#网站' in evolvedTask:
        return True
    if '#创建' in evolvedTask:
        return True
    
    return False

check_tag = _check_tag
check_repetition = _check_repetition

def _better(judgement):
    if '不相等' in judgement:
        return True
    else:
        return False

better = _better