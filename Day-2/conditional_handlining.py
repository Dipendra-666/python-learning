import sys

instance_type = sys.argv[1]
if instance_type == "t2.micro":
    print("this will cost you around 2 dollors")
elif instance_type == "t2.mideum":
    print("this will cost you around 4 dollors")
elif instance_type == "t2.large":
    print("this will cost you around 8 dollors")
else:
    print("this instance type is not supported")
