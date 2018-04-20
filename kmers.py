#!/bin/env python 
import pdb

# this will create the inital call to the kmers value 
class method:
    def kmers(self,value,seq):
        ls="" 
        rs=""
        i=0
        j=0
        while (i <= len(seq)):
            if (value == i):
                ls= seq[value-i:i]
            if (value == i):
                rs = (seq[2*value-i:2*i])
            i= i + 1
        side = [ ls , rs ]
        j=i
        if (j== len(seq)):
            self.kmers(value,seq)
        return side 
    def slideingwindow(self,value, side):
        pdb.set_trace()
        print ("The new value" + str(value-1))   

def main():
   meth=method()
   #sequence="ATGTACGATCATTTA"
   #subproblem=input("random graphing frame")
   #subproblem=int(subproblem)
   #side=meth.kmers(subproblem,sequence)
   #meth.slideingwindow(subproblem,side)
   sub=input("random graphing frame")
   sub=int(sub)
   neon =input("please input a short genome ")
   type(neon)
   nearestkmers=meth.kmers(sub,neon)
   print(nearestkmers)
  
main() 



#Hamming distance 
#
