def no_chain(str):
    if str != "no":
        return print("no",str)
    elif str[0] == "no":
        return print(str)
chain = str(input("Write a word:"))
noword = no_chain(chain)
result = print(noword)
