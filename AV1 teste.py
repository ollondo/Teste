
Av1 = float(input("Digite Sua Nota da Av1: "))
Av2 = float(input("Digite Sua nota da Av2: "))
Av3 = 0
AvC = 0 
AvC2 = 0

Média = (Av1 + Av2) / 3



print("Sua média é: %.0f" % Média)

if (Av1 <= 4) or (Av2 <= 4):
  print("Uma de suas notas está abaixo da média, faça uma nova chance")
  if (Av1 <4):AvC = float(input("Digite a nota da chance da Av1: "))
  if (Av2 <4):AvC2 = float(input("Digite a nota da chance da Av2: "))
 
  Média2 = (AvC + Av2) / 3
  Média3 = (AvC2 + Av1) / 3
  
  print("Sua nova média é: %.0f" % Média2) 
  print("Sua nova média é: %.0f" % Média3) 


  if (Média2 < 6) or (AvC < 4) or (AvC2 < 4) or (Média3 < 6):
     print ("Você tirou menos que 4 em uma das provas, faça a Av3")
     Av3 = float(input("Digite sua nota da Av3: "))
     Av2 = float(input("Digite sua nota que não foi substituida: "))
     Média4 = (Av3 + Av2) / 2
     print("Sua média é: %.0f" % Média4)

     if (Média4 < 6) or (Av3 < 4) or (Av2 < 4):
        print ("Você foi reprovado")
     else:
        print ("Parabéns você foi Aprovado")
  else: print("Você foi aprovado")
         
else: 
   print("Você foi aprovado")

    
    
        
    
    


 
    

    
    
 


    
    

 

  





   
   



