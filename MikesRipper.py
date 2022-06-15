# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26, 2019
@author: Mike
"""
filein = open('NACCturnedUpsideDown.csv','r')
fileout = open('NACCRippedToNew.csv','w')
def NotEOF(n):
    newprimeline = next(filein)
    counter = 1
    old_NACC = 'NACC000000'
    while True:
        if old_NACC[0:10] = newprimeline[0:10]:
            newprimeline = next(filein)
        else:
            old_NACC = newprimeline[0:10]
            fileout.write(newprimeline)
            newprimeline = next(filein)
    counter += 1
    if counter > n:
        return
    n =  NotEOF(121682)
    filein.close
    fileout.close
