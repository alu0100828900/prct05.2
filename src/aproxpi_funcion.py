#!/usr/bin/python
PI = 3.14159265358979323846264338327950288
import sys
def aproximacion (n):
   sumatorio=0
   for i in range (1,n+1):
       x_i=(i-0.5)/float(n)  
       fx_i=4/(1+x_i**2)
       sumatorio+=fx_i
   pi=sumatorio/n
   return pi

print '\nEl valor de pi con 35 decimales es %.35f\n' %PI
veces = int(sys.argv[2])
n=int(sys.argv[1])
l=[]
print 'i   PI35DT                               listai                                PI35DT-listai\n'
for vez in range (1, veces+1):
    pi = aproximacion( n*vez) 
    l= l +[pi]
    diferencia= abs(PI-pi)
    print '%d  %.35f %.35f %.35f' %(vez, PI, pi, diferencia)
print l

    