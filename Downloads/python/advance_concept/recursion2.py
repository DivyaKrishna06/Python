def blast(n):
    if n > 0:
        print (n)
        blast(n-1)
    else:
        print ("Blast off!")

blast(5)