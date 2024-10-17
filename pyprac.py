a = 6
print(a)

a = 1
b = "Hello"
c = True
d = 10.01
print(a)
print(b)
print(c)
print(d)

a , b = 1 , "Hello"
print(a)
print(b)

a = b = c = "orange"
print(a)
print(b)
print(c)

fruit = ["apple", "mango", "grape"]
a , b , c = fruit
print(a)
print(b)
print(c)

a = "Hello"
b = "world"
print(a + b)

a = 6
b = "Hello"
c = True
d = 12.43
print(type(a))
print(type(b))
print(type(c))
print(type(d))

a = int(20.5)
print(a)

a = "Rushikesh"
print(a[2])

a = "Rushikesh"
for i  in a:
    print(i)

a = "Rushikesh"
print(len(a))

a = "Hello user enter password"
print("user" in a)

a = "Hello user enter password"
if "user" not in a:
    print("not exist")
else:
    print("yes exist")

a = "Hello world"
print (a[2:9])

a = "hello"
print(a.upper())
b = "RUSHIKESH"
print(b.lower())

a = "Hello,user,enter,password"
print(a.strip())

a = "Hello user"
print(a.replace("H", "J"))

a = "Hello , User"
print(a.split(","))
`
a = "Hello"
b = "World"
c = a + " " + b
print(c)

a = "18"
b= f"I am {a}"
print(b)

a = []"pen", "book", "pencil"]
print(len(a))

a = ["pen", "book", "pencil"]
print(a[1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

mylist = ['apple', 'banana', 'cherry']
mylist.insert(0, 'orange')
print(mylist[1])

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
