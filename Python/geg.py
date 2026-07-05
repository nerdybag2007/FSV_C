import sys
sys.argv
if len(sys.argv)>2:
    print("name too long")
elif len(sys.argv)<2:
    print("name too short")
else:
    print("my name is: ",sys.argv[1])