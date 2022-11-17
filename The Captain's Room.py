class Farhad:
    def __init__(self,i,a):
        self.i=i
        self.a=a
    def Faru(self):
        self.c=set(self.a)
        #print(self.c)
        #print(sum(self.c)*self.i)
        print(sum(self.c)*self.i-sum(self.a))
        self.d=sum(self.c)*self.i-sum(self.a)
        print(round(self.d/(self.i-1)))
        #self.b=(sum(self.c)*self.i)-sum(self.a)
        #print(round(self.b/(self.k-1)))
farhad=Farhad(i=int(input()),a=list(map(int,input().split())))
farhad.Faru()