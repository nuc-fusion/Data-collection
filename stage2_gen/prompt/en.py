operations = r"""Valid operations:
- #Click# ${id}: Click on the element with the specified id.
- #Scroll up# ${n}: Scroll up n pages.
- #Scroll down# ${n}: Scroll dwon n pages.
- #Goto# ${url}: Go to the specified URL.
- #Go backward#: Go back to the previous page.
- #Go forward#: Go forward to the next page.
- #Hover# ${id}: Hover over the element with the specified id.
- #Type# ${id} ${text}: Type in the specified text at the element with the specified id.
- #Answer# ${text}: Answer the question with the specified text.
- #Login#: Prompt the user to perform the login operation.
- #Verify#: Prompt the user to perform the verification operation.
- #Exit#: Complete the task and exit the program."""

example_operations = r"""Operation format examples:
#Click# AB
#Type# CD 'Apple Mac'
#Scroll down# 0.5
#Goto# https://www.example.com
#Scroll up# 1"""

system = """%s

%s

HTML webpage:
%s

I want you to act as a task generator that can help generate Task-Operation pairs.
Based on the above HTML webpage, I will give you a specified operation. Your goal is to come up with a ONE-STEP task that the specified operation can solve.
Your answer SHOULD be in the following format:
Task: {Generated one-step task}
Operation: {The right operation to solve the task}
NOTICE: 
1. Your generated task should not be too SIMPLE, NAIVE
2. You can only do #type# on <input> and <textarea>
""" % (operations, example_operations, r'%s')

click_example = ('Click on the "Care Global" link.', '#Click# AB')
scroll_up_example = ('Scroll up for half of the page.', '#Scroll up# 0.5')
scroll_down_example = ('Scroll down for half of the page.', '#Scroll down# 0.5')
goto_example = ('Go to the "Apple" link.', '#Goto# https://www.apple.com.cn/')
go_forward_example = ('Go to the next page.', '#Go forward#')
go_back_example = ('Go to the previous page.', '#Go backward#')
hover_example = ('Hover over the "Apple" link.', '#Hover# AB')
type_example = ('Type "Apple Mac" in the "Search" box.', '#Type# CD "Apple Mac"')
login_example = ('The website asks to login my acount', '#Login#')
verify_example = ('The website asks to verify my email', '#Verify#')
exit_example = ('Complete the task and exit', '#Exit#')
answer_example = ('Show me a latest news according to the webpage', '#Anwser# "Apple is going to release a new iPhone"')

one_shot = {
    'Click': [click_example],
    'Scroll down': [scroll_down_example],
    'Scroll up': [scroll_up_example],
    'Goto': [goto_example],
    'Go forward': [go_forward_example],
    'Go backward': [go_back_example],
    'Hover': [hover_example],
    'Type': [type_example],
    'Login': [login_example],
    'Verify': [verify_example],
    'Exit': [exit_example],
    'Answer': [answer_example]
}