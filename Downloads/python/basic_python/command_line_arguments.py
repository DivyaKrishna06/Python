import sys
# Check the number of arguments passed
if len(sys.argv) < 2:
    print("Sample Usage: python myprogram.py arg1 arg2 ...")
else:
    # The first argument (sys.argv[0]) is the script name itself
    # The rest of the arguments are stored in sys.argv[1:], so you can access them using indexing
    print("Number of arguments:", len(sys.argv) - 1)
    print("Arguments:", sys.argv[1:])