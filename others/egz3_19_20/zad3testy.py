# zad3testy -- testy dla zadania 3 z egzaminu ASD (15. IX 2020)

class Node:
  def __init__( self, val ):
    self.next = None
    self.val = val

def tab2list(T):
    if len(T) == 0:
        return None
    frst = Node(T[0])
    tmp = frst
    for i in range(1,len(T)):
        e2 = Node(T[i])
        tmp.next = e2
        tmp = tmp.next
    return frst

def list2tab(L):
    T = []
    el = L
    while el != None:
        T.append(el.val)
        el = el.next
    return T


Test1 = [[1,4,8,10], [2,3,4,5], [7,16,18,20]]

R1 = [1,2,3,4,4,5,7,8,10,16,18,20]

Test2 = [[0,1], [10,20,30,40], [25,27], [35,45]]

R2 = [0,1,10,20,25,27,30,35,40,45]

Test3 = [[1,2,2,3,4], [2,3,4,5,5]]

R3 = [1,2,2,2,3,3,4,4,5,5]

Test4 = [[0,1,2], [10,15,20], [2,7], [3,9], [1], [123], [16]]

R4 = [0,1,1,2,2,3,7,9,10,15,16,20,123]

Test5 = [[1], [7], [2], [6], [5], [4], [3], [8], [10], [9], [11], [12], [14], [13], [0]]

R5 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]

TESTS = [Test1,Test2,Test3,Test4,Test5]

Res = [R1,R2,R3,R4,R5]


def runtests( f ):

    OK = True
    for i in range(len(TESTS)):
        X = []
        for li in TESTS[i]:
            X.append(tab2list(li))
        
        y = f(X)
        z = list2tab(y)
        print("----------------------")
        print( "Test:", TESTS[i] )
        print( "oczekiwany wynik =", Res[i] )
        print( "otrzymany wynik  =", z )
        
        if z != Res[i]:
            print( "Blad!" )
            OK = False
    print("----------------------")

    if OK:
        print( "OK!" )
    else:
        print( "Bledy!" )
            
 

