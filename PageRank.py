#!/usr/bin/env python
from math import log
import operator
from collections import defaultdict
#Code for WT2g_inlinks file

f = open('wt2g_inlinks.txt', 'r') 
l = f.readlines()

#data structures: 
#M is a dictionary where the document id is the key and the values are all the pages pointing to it(inlinks).
#L is a dictionary where the document id is the key and the value is the number of outlinks from that page.
#PR is a dictionary where the document id is the key and the value is the PageRank value for that page.
#newPR is a dictionary which is used as a temporary variable to update the PageRank value in PR.
#S is the list of sink nodes.
#P is the list of all the pages(document ID's).
#preplexity is a list of all the preplexity values used to calculate the convergence.
#SortedPR is a list of the PR items in sorted in descending fashion on basis of their PageRank values.
M = {}
L = {}
PR = {}
newPR = {}
S = []
P = []
preplexity = []
SortedPR = []

#Function to calculate preplexity value.
def calcprep():
    entropy = 0
    for page in PR.keys():
        entropy += PR[page]*log(1/PR[page],2)
    return 2**entropy

#Function to find out if the preplexity values have converged upto units place or not.
def calcconvergence(j):
    preplexvalue = calcprep()           
    preplexity.append(preplexvalue)     
    if (len(preplexity)>4):             
        if((int(preplexity[j]))==(int(preplexity[j-1]))==(int(preplexity[j-2]))==(int(preplexity[j-3]))): 
            print j+1,calcprep()
            return False
        else:
            return True
    else:
        return True

#Populating M and P from input representation file.
#For read lines, we break it into individual elements, make the first element as the key and the rest as the value for M.
#we append the first element to the P list.
for line in l:
    line = line.split()
    M[line[0]] = line[1:]
    P.append(line[0])

#Initialize all elements in L with key as element in P, and value as 0.
for i in P:
    L[i] = 0

#Populating L.
#for every page in the inlinks dictionary M, we increment the counter in the outlinks counter dictionary L
for values in M.values():
    for value in values:
            L[value] += 1

#Populating the Sink node list S.
#If the number of outlinks is 0, then its a sink node.
for page in L.keys():
    if L[page] == 0:
        S.append(page)

#N is the total number of pages.
N = float(len(P))

#d is the damping factor as usual taken as 0.85
d = 0.85

#PageRank Algorithm implementation.
for p in P:
    PR[p] = 1.0/N

j = 0
while calcconvergence(j):
    print j+1, calcprep()              
    sinkPR = 0
    for p in S:
        sinkPR += PR[p]
    for p in P:
        newPR[p] = (1.0 - d)/N
        newPR[p] += d*sinkPR/N
        for q in M[p]:
            newPR[p] += d*PR[q]/L[q] 
    for p in P:
        PR[p] = newPR[p]
    j += 1

#Sorting the PR dictionary and storing it in a list SortedPR.
SortedPR = sorted(PR.iteritems(), key=operator.itemgetter(1), reverse=True)

#printing the top 10 results.
for i in range(10):   
    print SortedPR[i] 


#TEST/ANALYSIS PURPOSE CODE: 
    
#resultlist = ['WT21-B37-76','WT21-B37-75','WT25-B39-116','WT23-B21-53','WT24-B40-171','WT23-B39-340','WT23-B37-134','WT08-B18-400','WT13-B06-284','WT24-B26-46']

#for i in resultlist:
#    print "number of inlinks to %s is %s " %(i,len(M[i]))
#    print "number of outlinks from %s is %s " %(i,L[i])
#    if i in S:
#        print i + " is a sink"
   
#print "pages linking to %s are %s \n" %(resultlist[7],M['WT08-B18-400'])
#count = defaultdict(int)
#for values in M['WT21-B37-76']:
#    count[values] += 1
#print sorted(count.iteritems(), key=operator.itemgetter(1), reverse=True)

#for i in resultlist:
#    print "original %s" %i
#    for value in M[i]:
#        print value ,L[value]
