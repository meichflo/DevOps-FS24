import time

print("hello world")
letters = ["F","L","O","R","I","A","N",]
word= ""

for i in letters:
    print(i)
    word = word + str(i)
    time.sleep(0.2)

print(f"-------\nThe entire word is: {word.capitalize()}")