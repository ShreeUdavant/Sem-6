

def isEqual(a,b,c):
   pass
   



with open("input.txt", "r") as inp:
   code = inp.read().splitlines()
   print(code)

   temp=[]
   indexnum=1
   for line in code:
      cpt = line.split()
      print(cpt[0])
      if cpt[0]=="+" or "-" or "*" or "/":
         temp.append(indexnum)
         temp.append(cpt)
         indexnum+=1
   print(temp)
      
      
      
