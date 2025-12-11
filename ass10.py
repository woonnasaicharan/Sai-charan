# import requests


# print("words related to something that start with the letter something	")
# word=input("enter word: ")
# letter=input("enter letter: ")

# request=requests.get(f"https://api.datamuse.com/words?ml={word}&sp={letter}*&max=10")
# content=request.json()
# # print(content)
# print(request.status_code)
# for i in range(5):
#     print(content[i]["word"])



import requests
b = input("Enter a letter to display words that sound like:")
a = requests.get(f"https://api.datamuse.com/words?ml=duck&sp={b}*&max=10")
content = a.json()
item = 0

for item in range(5):
    print(content[item]["word"])
    item+=1
    