# first_file = open("/home/ilia/Documents/Python/files/movies.txt", "r")
# # read the whole thing
# print(first_file.read())

# # read line by line
# print(first_file.read()) #first line
# print(first_file.read()) #second line

# # read all lines splitted to a list
# print(first_file.readlines())

# # always remember to close it
# first_file.close()


# if you feel that you might forget to close it , use this approach
# with open("/home/ilia/Documents/Python/files/greeting.txt", "r") as f:
#     #print(f.readlines())
    
with open("/home/ilia/Documents/Python/files/greeting.txt" , "r") as f:
        for line in f :
                print(line.strip())