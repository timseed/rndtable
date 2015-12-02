import pprint
import random

class tab(object):

    def __init__(self):
       print("tab init")
       self.rows=6
       self.cols=4
       self.data= [[str.format("r{}c{}",j,i) for i in range(self.cols)] for j in range(self.rows)]

    def dump(self):
        pprint.pprint(self.data)

    def setdata(self,d):
        self.data=d
        self.rows=len(d)
        self.cols=len(d[0])

class rndtab(tab):

      def __init__(self):
          print("rndtab init")
          super(self.__class__,self).__init__()
          self.rnddata=[]

      def fullrandom(self):
         self.rnddata=[[ self.data[random.randint(0,self.rows-1)][random.randint(0,self.cols-1)] for c in range(self.cols)] for r in range(self.rows)]
      
      def random_row(self):
         self.rnddata=[[ self.data[random.randint(0,self.rows-1)][c] for c in range(self.cols)] for r in range(self.rows)]

      def random_col(self):
         self.rnddata=[[ self.data[r][random.randint(0,self.cols-1)] for c in range(self.cols)] for r in range(self.rows)]
                         
      def dump(self):
        print("======== Original Data ===========")
        pprint.pprint(self.data)
        print("======== Randomized Data ===========")
        pprint.pprint(self.rnddata)

if __name__ == "__main__":
     t=tab()
     t.dump()
     rt=rndtab()
     print("Full Random")
     rt.fullrandom()
     rt.dump()
     print("Random Row")
     rt.random_row()
     rt.dump()
     print("Random Col")
     rt.random_col()
     rt.dump()
