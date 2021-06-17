# Quiz game 
score = 0

print("How old am I? ")
Person_user = input().lower()

if Person_user == "15":
  print("Woah you know how old i am, WEIRD!!")
  score = score + 1
elif Person_user == "16":
  print("Your sooo dumb!")
else:
  print("woow thats sad :")

print("What is my favourite colour?")
Person_user = input().lower()

if Person_user ==("black"):
  print("damn you know me pretty well")
  score = score + 1
else:
    ("damn wrong, totally wrong ")
    
print("you scored "+str(score))
