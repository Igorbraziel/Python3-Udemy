class A:
    def quem_sou(self):
        print('A')
        
class B(A):
    def quem_sou(self):
        print('B')
        
class C(A):
    def quem_sou(self):
        print('C')
        
class D(C, B):
    def quem_sou(self):
        print('D')
        B.quem_sou(self)    
        
        
d = D()
d.quem_sou()
print(D.mro())