#
# Jake Shankman, September 8 2011
#
# Word Ladders Lab02: Random Ladders
#
#   Input: A 6 six letter word and a dictionary of 6 letter words
# Process: Finds all neighbors of word, selects one, finds neighbors and repeats
#  Output: A word that, using a word ladder, has all 6 letters different from the starting word
#
import random
wlist=open('words.txt','r').read().split()
ustr=raw_input('Statring Word: ')
#
def findnbrs(ustr,wlist):
  neighbors=[]
  k=0
  while k<len(wlist):
	  #
      diff=0
      index=0
      while index<len(ustr):
	      #
	  uletter=ustr[index]
	  word=wlist[k]
	  wletter=word[index]
	  if uletter != wletter:
	      diff=diff+1
	      #
	  index=index+1
      if diff == 1:
	   neighbors.append(wlist[k])
	  #
	  #
      k=k+1
  return neighbors
#    
#
print ustr
word=ustr
diff = 0
while diff !=6:
  neighbors=findnbrs(word, wlist)
  random.shuffle(neighbors)
  #print neighbors
  word=random.choice(neighbors)
  diff=0
  index=0
  while index<len(ustr):
	    #
	uletter=ustr[index]
	wletter=word[index]
	if uletter != wletter:
	    diff=diff+1
	    #
	index=index+1
  print word
  if diff == 6:
      writer = open('startend.txt','w')
      writer.write(ustr)
      writer.write('\n')
      writer.write(word)
      writer.close()
#
# end of file
#

  
