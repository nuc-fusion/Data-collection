elimination_prompt = '''Here are two Instructions to ChatGPT AI, do you think they are equal to each other, which meet the following requirements:
1. They have same constraints and requirments.
2. They have same depth and breadth of the inquiry.
The First Prompt: %s
The Second Prompt: %s
Your Judgement (Just answer: Equal or Not Equal. No need to explain the reason.): '''

# check if contains prompt tag
def _check_tag(evolvedTask):
    if '#Given' in evolvedTask:
        return True
    if '#Rewritten' in evolvedTask:
        return True
    if '#Website' in evolvedTask:
        return True
    if '#Created' in evolvedTask:
        return True
    
    return False

check_tag = _check_tag

def _better(judgement):
    if 'Not Equal' in judgement:
        return True
    else:
        return False

better = _better