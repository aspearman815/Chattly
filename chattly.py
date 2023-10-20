import random
print ("Chattly🥰")
print  ("*******************************")
print ("Question\'s you can ask Chattly")
print ("*******************************")
print ("what is your name?")
print ("what is your favorite color?")
print ("what is your favorite instrument?")
print ("what is your favorite holiday?")



request = ''
#          0       1       2       3
colors =['red', 'pink', 'green', 'blue']
while request != "bye":
    request = input("Ask Me A Question please? 😜:  ")
    request = request.lower()
    if request == "what is your name?":
        print ("chattly🫡")
    elif request == "what is your favorite color?":
        pick = random.randint(0,len(colors)-1)
        print(colors[pick]+ "🎨")
    elif request == "what is your favorite instrument?":
        print ("guitar🎸")
    elif request == "what is your favorite holiday?":
        print ("halloween🎃")

    elif request == "bye":
        print ("thank you for chatting🤭")
    else:
        print("honey what? 🙃")