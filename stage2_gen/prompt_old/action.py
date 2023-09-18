browser = """You are a helpful assistant that can assist with web browsing tasks.
You are given a simplified HTML code. 
Your task is to come up with a one-step operation on the webpage and perform the specified operation using the provided simplified HTML.

HTML code: %s

Please write out the mission you come up with and the ONE of valid operation you would like ChatGPT to act on the webpage.

Valid operations:
- Click ${id}: Click on the element with the specified id.
- Scroll ${pos}: Scroll to the specified position.
- Goto ${url}: Navigate to the specified URL.
- Go backward: Navigate back to the previous page.
- Go forward: Go forward to the next page.
- Hover ${id}: Hover over the element with the specified id.
- Type ${text}: Type the specified text at the corresponding cursor position.
- Login: Prompt the user to perform a login.
- Verify: Prompt the user to perform a verification.
- Exit: Exit the webpage.

Example answer format:
Mission: Click the 'Login' button.
Operation: Click 111

Please provide the one-step mission and the operation to be executed."""