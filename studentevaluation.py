import sys

if len(sys.argv) == 5:
    script_name = sys.argv[0]
    name = sys.argv[1]
    mark1 = sys.argv[2]
    mark2 = sys.argv[3]
    mark3= sys.argv[4]
    
    print("User provided input values:")
else:
    name = "prajwal"
    rollno = "052"
    mark1 = "35"
    mark2 = "35"
    mark3= "35"
    print("No input given, using default values:")

total = int(mark1) + int(mark2) + int(mark3) 
average = total / 5 
print(" Name:", name)
print("Student Name:", name)
print("Subject 1 marks :", mark1)
print("Subject 2 marks :", mark2)
print("Subject 3 marks :", mark3)
print("Total Marks:", total)
print("Average Marks:", average)
