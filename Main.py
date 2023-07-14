print("HELLO")


print("      /\\")
print("     /  \\")
print("     /  \\")
print("     ----")

character_name = "John"
character_age= "35"

print("There once was a man named", character_name, "John, ")
print("he was" ,character_age,  "years old.")
print("He really liked the name", character_name + ",")
print("but didn't like being" ,character_age)

isMale = True


print("---------------------------------------------------------------------------")

print("Giraffe\nAcademy")
print("Giraffe \"Academy")
print("Giraffe \\ Academy")

phrase = "Graffe Acdemy"

print(phrase + "is cool")
print(phrase.upper())
print(phrase.lower())
print(len(phrase))
print(phrase.index("G"))
print(phrase.replace("Graffe", "Elephant"))

print("---------------------------------------------------------------------------")


print(2)
print(2.8097)
print(-2.3423)
print(2+2)
print(2*2)
print(2/2)
print(10 %3)
print(2*(10%3))
my_num = 5
print(my_num)
print(str(my_num) + " My Number")
my_num = -5
print(my_num)
print(abs(my_num))
print(pow(3,2))
print(max(6,3))
print(min(2,4,7))
print(round(3.7))

from math import *
print(floor(3.7))
print(ceil(3.7))
print(sqrt(36))


print("---------------------------------------------------------------------------")

# name = input("Enter your name: ")
# age = input("Enter your age:")
# print(name)
# print("hello" + name + "your age is" + age+".")
print("---------------------------------------------------------------------------")

# num1 = input(" Enter a number to add: ")
# num2 = input(" Enter a second number to add: ")
# result = float(num1) + float(num2)
# print(num1+"+"+num2 + "=" + str(result))
print("---------------------------------------------------------------------------")


# color = input("Enter a color: ")
# plural_noun = input("Enter a plural noun: ")
# celebrity = input("Enter a celebrity: ")
# print("Roses are " + color)
# print(plural_noun + " are blue")
# print("I love " + celebrity)

print("---------------------------------------------------------------------------")


color=[ "blue", "Yellow", "Green" ]
print(color[1])
print(color[-1])
print(color[1:3])
print(color[1:])
print(color[:2])
color[1]="Purple"
print(color)


print("---------------------------------------------------------------------------")

number= [2,5,8,12,16,20]
color=[ "blue", "Yellow", "Green" ]
print(number)
number.extend(color)
print(number)
number= [2,5,8,12,16,20]
color=[ "blue", "Yellow", "Green" ]
color.append("Pruple")
print(color)
color.insert(1,"White")
print(color)
color.remove("Green")
print(color)
color.pop()
print(color)
print(color.index("blue"))
color.append("blue")
print(color.count("blue"))
color.sort()
print(color)
color.reverse()
print(color)
color1 = color.copy()
print(color1)


print("---------------------------------------------------------------------------")

color = ( "blue" , "red")
print(color[0])

color= [("blue,red"), ("Green, Purple")]


print("---------------------------------------------------------------------------")

def function1():
    print("Hello")
print("top")
function1()
print("Bottom")
def function2(name, age):
    print("Hello " + name + ", you are " + str(age))
function2("Joe",25)


print("---------------------------------------------------------------------------")

def function1(num1):
    return(num1*num1*num1)
print(function1(3))

print("---------------------------------------------------------------------------")

if( 4>2):
    print("4>2")


if(2>3):
    print("2>3")
else:
    print("2<3")


if(4<2):
    print(4>2)
elif(5>2):
    print("5>2")
else:
    print(False)

if (2>3) or (2<3):
    print("Something is true")

if(2>3) and (2<3):
    print("everything is true")

if not(2>3):
    print("oppsite of (2>3)")

print("---------------------------------------------------------------------------")

# def adding(num1, num2):
#     return( num1 + num2)
# def subtracting(num1, num2):
#     return( num1 - num2)
# def multipling(num1, num2):
#     return( num1 * num2)
# def dviding(num1, num2):
#     return( num1 / num2)

# num1 = float(input("Enter a number: "))
# num2 = float(input("Enter another number: "))
# opparater = input("Enter a opprater: ")

# if opparater == "+":
#     print(adding(num1,num2))
# elif opparater == "-":
#     print(subtracting(num1,num2))
# elif opparater == "*":
#     print(multipling(num1,num2))
# elif opparater == "/":
#     print(dviding(num1,num2))
# else:
#     print("invalade opparater")

print("---------------------------------------------------------------------------")

people= {
    "joe":"29",
    "jenny":"25",
    "jb":"25"
}

print(people.get("joe","Not a Valid Key"))
print(people)
print(people["joe"])

print("---------------------------------------------------------------------------")
i=0
while i < 5:
    i +=1
    print("Hello")

print("---------------------------------------------------------------------------")

# word = "Giraffe"
# guess = ""
# tries = 0
# tries_limte = 3
# while guess != word and tries != tries_limte:
#     guess= input("Guess a word: ")
#     tries += 1
# if tries == tries_limte:
#     print("You Lose")
# else:
#     print("You win")
print("---------------------------------------------------------------------------")

for x in "Joe":
    print(x)


friends= ["Joe", "Jenny", "Jacob"]

for friend in friends:
    print(friend)


range(1,3)

print("---------------------------------------------------------------------------")

print(2**3)

def raise_to_power(x,exponent):
    result = 1
    while exponent != 0:
        result = result * x
        exponent -= 1
    return(result)

print(raise_to_power(2,2))

print("---------------------------------------------------------------------------")

number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# print(number_grid[1][1])

for row in number_grid:
    for colium in row:
        print(colium)

print("---------------------------------------------------------------------------")

def tranlate(word):
    vowel = ["a","e","i","o","u","A","E","I","O","U"]
    x=0
    for letters in vowel:
        word=word.replace(letters,"g")
    return(word)
print(tranlate("dog"))
print("---------------------------------------------------------------------------")


# try:
#     10/0
#     number = int(input("Enter a Number"))
#     print(number)
# except ZeroDivisionError as err:
#     print(err)
# except ValueError as err:
#     print(err)

print("---------------------------------------------------------------------------")
employess_file = open("employees.txt","r")
# print(employess_file.read())
# print(employess_file.readline())
# print(employess_file.readlines())
# print(employess_file.readable())

# for employee in employess_file.readlines():
#     print(employee)
# employess_file.close()

print("---------------------------------------------------------------------------")


employee_file = open("employees.txt","w")
employee_file.write("John\n")
employess_file.close()

print("---------------------------------------------------------------------------")


class student:
    def __init__(self,name, major, gpa,is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

student1 = student("joe","compsi",2.0,False)

print(student1.gpa)


print("---------------------------------------------------------------------------")

# object funcation