task_system = '''I want you to act as a Task Generator. Your objective is to generate as many REAL and DIVERSE tasks based on the website's HTML text and explanation as possible. Each task requires the model to interact with the website to complete the daily tasks that humans REALLY do on the website. You SHOULD generate tasks using the following method:
Please list the tasks in the following form: 1. xxx
2. xxx
3. xxx
...
Content other than tasks is not allowed to appear in #Tasks#'''

task_query = '''#Website Text#:\n%s\n\n#Explain#:\n%s\n\n#Tasks#:\n'''