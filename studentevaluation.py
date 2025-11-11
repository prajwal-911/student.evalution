import sys;
if len(sys.argv) == 5:
   script_name = sys.argv[0]
   name = sys.argv[1]
   marks1 = sys.argv[2]
   marks2 = sys.argv[3]
   marks3= sys.argv[4]
else  :
   script_name = sys.argv[0]
   name = "nikhil"
   marks1 = 20
   marks2 = 30
   marks3= 40

sum = marks1+marks2+marks3
avg = sum/3
print(f"Sum {sum}\n")
print(f"Average: {avg}")