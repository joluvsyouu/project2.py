F=input("Please input a file: ")
file=open(F,'r')
old=file.read()

#overwrite as a new file without punctuation
file=open(F,'r')
remove="!(),:;.?"
overwrite=""
for line in file:
  for char in line:
    if char not in remove:
      overwrite=overwrite+char
file=open(F,'w')
file.write(overwrite.lower())
file.close()

# function one:
def LineList(F):
  accepted='mr. ms. mrs. dr.'
  L = []
  with open(F, 'r') as f:
    for line in f:
      words = line.lower().split()
      L.append([word for word in words if word.isalpha() or word in accepted])
  return L
print(LineList(F))

# function two - SentenceCount 

def SentenceCount(F):
  file = open(F,'w')
  file.write(old)
  file.close()
  file=open(F,'r')
  lines=file.readlines()
  counter=0
  for line in lines:
    count=line.count('.')+line.count("!")+line.count("?")
    delete=line.count('Mr.')+line.count("Dr.")+line.count("Mrs.")+line.count("Ms.")
    total=count-delete
    counter +=total
  return counter
print("The output for the SentenceCount function is:",SentenceCount(F))


# function three - WordDict

def WordDict(F):
  file=open(F,'w')
  file.write(overwrite.lower())
  file.close()
  file=open(F,'r')
  lines=file.read()
  words=lines.lower().split()
  word_dict={}
  for word in words:
    if word.isalpha():
      if word not in word_dict:
       word_dict[word]=1
      else:
       word_dict[word]+=1
  return word_dict

print(WordDict(F))

# 4th fynction
def Sentiment(F):
  pos=open("positivesentimentwords.txt").read().split()
  neg=open("negativesentimentwords.txt").read().split()
  ign=open("ignorewords.txt").read().split()
  positive=0
  negative=0
  ignore=0
  neutral=0
  file=open(F,'r')
  for line in file:
    words=line.split()
    for word in words:
      if word.isalpha():
        if word in pos:
          positive+=1
        elif word in neg:
          negative+=1
        elif word in ign:
          ignore+=1
        else:
          neutral+=1
  total=positive+negative+neutral
  pp=positive/total
  np=negative/total
  nep=neutral/total
  
  print("Positive Sentiment Word Count:{} ({:.0%})".format(positive,pp))
  print("Negative Sentiment Word Count:{} ({:.0%})".format(negative,np))
  print("Neutral Sentiment Word Count:{} ({:.0%})".format(neutral,nep))
  if positive>negative:
    return("This document has a positive sentiment.")
  elif negative>positivetive:
    return("This document has a negative sentiment.")
  elif negative==positive:
    return("This document has a neutral sentiment.")
print(Sentiment(F))

file = open(F,'w')
file.write(old)
file.close()
#print(old)