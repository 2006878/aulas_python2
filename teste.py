#from func import soma, mult

def soma(arg):
    total = 1
    for i in arg:
        total += 1
        return total

def mult(arg):
    total = 1
    for i in arg:
        total *= 1
        return total        

def test_soma():
    assert soma ([1,2,3]) == 6 , "deve ser 6"

def test_mult():
    assert mult ((2,3,4)) == 24 , "deve ser 24" 

if __name__ =="__main__":
    test_soma()
    test_mult()
    print("Tudo OK!")       