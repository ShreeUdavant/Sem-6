
with open("input.txt") as inp:
   code = inp.read().splitlines()
   print(code)

   temp=[]
   checklist=[]
   samelist=[]
   indexnum=1
   for line in code:
      cpt = line.split()
      print(cpt)
      temp.append(cpt)
   
   checklist.append(temp[0])
   # print(checklist[0][0])
   
   for line in code:
      cpt = line.split()
      if cpt[0] == checklist[0][0]:
         samelist.append(cpt)
         
   print("\n\n")
   print(samelist[1][3])
   
   # print(temp[0])
      
      
      
      
