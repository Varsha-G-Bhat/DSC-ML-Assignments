# -*- coding: utf-8 -*-
"""DSC ML Assignment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FvsW8Btk_wBBLIOjWNcoLrXENCcO8MUf
"""

def ConvertListToLowerCase(Movies):
  """ Function to convert the list items into lowercase """
  MoviesList =[]
  for movie in Movies:
    MoviesList.append(movie.lower())
  return MoviesList



if __name__ == "__main__":

  thriller=["Dark","Mindhunter","Parasite","Inception","Insidious","Interstellar","Prison Break","Money Heist","War","Jack Ryan"]
  comedy=["Friends","3 Idiots","Brooklyn 99","How I Met Your Mother","Rick And Morty","The Big Bang Theory","The Office","Space Force"]

  Thriller = ConvertListToLowerCase(thriller)   #Convert thriller list to lowercase
  Comedy = ConvertListToLowerCase(comedy)   #Convert conedy list to lowercase

  Movie = input()   #Take the input Movie/Series

  if Movie.lower() in Thriller:   #Check if the Movie/Series is Thriller
    print("It is a thriller ")
  elif Movie.lower() in Comedy:   #Check if the Movie/Series is Comedy
    print("It is a comedy ")
  else:                          
    print("It's neither comedy nor thriller ")



x = int(input())
box = input().split
i=0
count = 0
while i != x:
  for gloves in range((i+1),len(box)):
    count = count + 1
    if box[i] == box[gloves]:
      box.pop(gloves)
      box.pop(i)
    i = i + 1
    x = int(len(box))
print(count)

a = input().split()
len(a)

x = int(input())
box = input().split()
i=0
count = 0
while i != x:
    gloves = i + 1
    while gloves< len(box):
    #for gloves in range((i+1),int(len(list(box)))):
        count = count + 1
        if box[i] == box[gloves]:
            box.pop(gloves)
            box.pop(i)
    i = i + 1
    x = int(len(box))
print(count)

n = int(input())
box = input().split()
number = 0
count = 0
for i in range(n):
  for j in range(i+1,n):
    if box[i]==box[j]:
      count = count + 1
  if count % 2 == 0:
    number = number + 1
print(number )

x = int(input())
box = input().split()
j = 0
count = 0
box = sorted(box, reverse=False)
while  j < x-1 :
  i = j
  j = i + 1
  if box[i] == box[j]:
    j = j + 1
    count = count + 1
print(count)

x = int(input())
box = input().split()
j = 0
count = 0
print(sorted(box, reverse=False))
#j < int(len(box))
