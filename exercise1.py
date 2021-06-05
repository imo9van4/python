mystring = "hello"
myfloat = 10.0
myint = 20

if mystring == "hello":
    print("String: %s" % mystring)
    # %s means you want to add a string inside a string
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
    # %f adding a float inside of a float
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)
    # %d adding an int inside an int (decimal)