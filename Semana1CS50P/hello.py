#some examples from the lecture

print ("hello world")
#storing information into a variable
name = input ("what's your name?").strip().title()

#returning the value stored
print ("Hi,", name, ",nice to meet you")
x = int(input("What is x?"))
y = int(input("What is y?"))
print (x+y)

def hello(to):
    print ("Hello", to)


again = input ("what is yout name?")
hello(again)