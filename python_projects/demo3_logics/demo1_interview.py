"""Write a function to Return a string which has common letters between
any 2 given strings s1 and s2"""
def find_common_characters(msg1,msg2):
    set1=set(msg1)
    set2=set(msg2)
    remove={" "}
    set3 = (set1&set2)-remove
    msg=''.join(sorted(set3))
    return msg

msg1="I am writing this sample test"
msg2="my python skills"
common_characters = find_common_characters(msg1,msg2)
print(common_characters)

# Find second largest number index from the given number list
a = []
n = int(input("Enter number of elements: "))
for i in range(1,n+1):
    b = int(input("enter elements: "))
    a.append(b)
a.sort()
print("Second largest number is",a[n-2])

# Write a function to return value to summation of all elements

def given_api(num):
    return num

a = []
n = int(input("Enter number of elements: "))
for i in range(1, n+1):
    b = int(input("enter number element: "))
    a.append(b)
e = given_api(a)
print(e)
print(sum(e))

# Write a function to return number of capital letters in a file. Your code should work even if the file is too big to fit in memory
path = "C://Backup Folders//Proposal//Python skills//Text.txt"
with open(path) as file:
    count =0
    text = file.read()
    for i in text:
        if i.isupper():
            count +=1
    print(count)

# UNKNOWN

def main():
    counter = 0
    print(greet("Alice", counter))
    print(f"Counter is {counter}")
    print(greet("Bob", counter))
    print(f"Counter is {counter}")

def greet(name, counter):
    return f"Hi, {name}!", counter + 1

main()
