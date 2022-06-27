#print("hello python....");
#print("hello again");

num=str(5);
num2=int(9);
print(type(num2));
print(type(num));

#multple assignment to variables in asingle line
x,y,z="banana","orange","cherry"
print(x);
print(y);
print(z);

#multiple variables to one value
x1=y1=z1="orange"
print(x1,y1,z1)

#unpacking a collection and assining to avariable
fruits=["apple","banana","cherry"]
x2,y2,z2=fruits
print(x2)
print(y2)
print(z2)

#the global key word

def myfunction():
    global x
    x="fantastic"
myfunction()
print("python is " + x)    

# x=1j this is type complex
# x=["a","b","c"] this is list
# x=("a","b,"c)   this is tuple
# x=range(6)      this is range
# x={"a":"b","c":"d"} this is dictionary
# x={"apple","cherry"} this is set
# x=frozenset({"apple","banan","cherry"}) this is frozenset


#multiine strings

paragraph="""Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

print(paragraph)

a="hello,world"
print(len(a))

#checking a string presence
txt="the best thing in life are free!"
print("free" in txt)

#checking if a string is not present
txt="the best thing in life are free!"
print("free" not in txt)

#creating random numbers
import random
print(random.randrange(1,10))

#slicing a string
b="hello,world"
print(b[2:5])

#slicing from start
print(b[:6])

#slicing to the end
print(b[2:])

#negative slice to start from the end
print(b[-5:-2])

#upper method
a=" hello, python "
print(a.upper())

#lower method
print(a.lower())

#remove whitespace
print(a.strip())

#replacing string
a="hello, world"
print(a.replace("h","j"))

#split string returns a set
print(a.split(","))
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
