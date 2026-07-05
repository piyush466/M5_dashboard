name = "my name is piyush"

new_name = name.split()

# print(new_name)
c = ""
for i in new_name:
    # print(i[::-1])
    c = c + i[::-1] + " "

print(c)

