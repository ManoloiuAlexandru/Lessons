user_input = int(input("On what number do you want to make a factorial ?"))

res = 1
for i in range(1, user_input+1):
    res = res * i

print(res)
