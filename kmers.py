#!/bin/env python 
# this will create the inital call to the kmers value 
class method:
    def kmers(self,value,seq):
        q=len(seq)-value
        for i in range(0,seq):  
            if (value == i):
                print (seq[:])
           print (str(value) + " this is the value and " + seq + "is the sequence." )


def main():
   meth=method()
   sequence="ATGTACGATC"
   print(meth.kmers(5,sequence))
  
main() 
