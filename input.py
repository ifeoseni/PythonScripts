# use input() to get user prompt

prompt = "How are you?"
user_input = input(prompt)
print("You said" , user_input)

response = input("What should I do?")
response = response.upper()
print("Well, if you insist...",response)
response_length = len(response)
print(response_length)