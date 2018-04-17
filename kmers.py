#!/bin/env python 
import pdb

# this will create the inital call to the kmers value 
class method:
    def kmers(self,value,seq):
        ls="" 
        rs=""
        i=0
	while i <= value :  
            if (value == i):
                ls= seq[value-i:i]
            if (value == i):
                rs = (seq[2*value-i:2*i])
            i= i + 1
        side= [ls, rs] 
        return side
    def slideingwindow(self,value, side):
        pdb.set_trace()
        print ("The new value" + str(value-1) + "I want to see what the two sides look like like" + side + side[2])   

def main():
   meth=method()
   sequence="ATGTACGATC"
   side=meth.kmers(5,sequence)
   meth.slideingwindow(5,side)
  
main() 
