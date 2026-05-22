#   File Handling

# file = open('question.py')
# print(file.read())
# file.close()

""" w -- write mode (1. agar file created nahi hai toh create ho jayegi , 2. agar purana data hai to overwrite ho jayegi.)
    a -- append mode
    r -- read mode
    x create mode
    """

# create file

# file = open("gangadhar.txt","w") # yedi file exist nhi karega to create kar dega
# file.write("this is gangadhar file") # gangadhar file ke andar ye likh dega 

# file = open("gangadhar.txt","w") 
# file.write("the content is now overwritten")
# file.close()


# #append mode
# file = open("gangadhar.txt","a") 
# file.write("the content is added using a (append) mode")
# file.close()

# file = open("gangadhar.txt","r")
# for i in file:
#     print(i)
# file.close()

# with statement (auto close)

# with open("gangadhar.txt","r") as file:
#     print(file.read())

# with open("gangadhar.txt" ,"w") as file:
#     file.write("content overwritten")
#     print("done")


    # paths 
# /Users/raviprakash/Desktop/p 23 batch/gangadhar.txt

# from pathlib import Path
# p = Path("shaktima.txt")
# if p.exists():
#     print("file exists")
# else:
#     print("file does not exist")