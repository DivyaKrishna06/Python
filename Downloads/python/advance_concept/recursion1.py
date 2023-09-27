def rp1( L, i ):
    if i < len(L):
        print (L[i])
        rp1( L, i+1 )
    else:
        print

def rp2( L, i ):
    if i < len(L):
        rp2( L, i+1 )
        print (L[i])
    else:
        print

L = [ 2, 3, 5, 7, 11 ]
rp1(L,0)
rp2(L,0)