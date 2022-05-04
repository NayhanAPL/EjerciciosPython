#Guilty Prince
def GuiltyPrince (listBi):
   movX = [0,-1,0,1]
   movY = [-1,0,1,0]  
   puntoActX = 0          
   puntoActY = 0          
   for i in range(len(listBi)):
      for j in range(len(listBi[i])):
         if listBi[i][j] == '@':
            puntoActX = i
            puntoActY = j
   cont = 1
   thereIsWay = True
   while(thereIsWay):
      thereIsWay = False
      for i in range(4):
         if ((i != 3 or puntoActX != len(listBi) - 1) and (i != 2 or puntoActY != len(listBi[0]) - 1) and (i != 1 or puntoActX != 0) and (i != 0 or puntoActY != 0)):
            if (listBi[puntoActX + movX[i]][puntoActY + movY[i]] == '.'):
               listBi[puntoActX + movX[i]][puntoActY + movY[i]] = ','
               cont += 1
            
      for i in range(len(listBi)):
          for j in range(len(listBi[i])):
              if listBi[i][j] == ',':
                  puntoActX = i
                  puntoActY = j
                  listBi[i][j] = '@'
                  thereIsWay = True  
                  break
          if (thereIsWay):
              break
   return cont
       
cases = int(input())
for i in range(cases):
   x, y = input().split()
   listBi = [[0 for ejex in range(int(x))] for ejey in range(int(y))] 
   for j in range(int(y)):
      line = input()
      for l in range(len(line)):
          listBi[j][l] = line[l]
   res = GuiltyPrince(listBi) 
   print("Case " + str(i + 1) + ': ' + str(res))

#problema E

def HiddenSecret (textIn, textOut):
   res = "no"
   totalCaracter = 0
   caracterCompare = 0
   for i in textIn:
       if i != " ":
          totalCaracter += 1 
          index = textOut.find(i)
          if index != -1:
              caracterCompare += 1
              textOut.replace('a',  '', 1)
   if totalCaracter == caracterCompare:
       res = "Yes"
   return res

cases = int(input())
for i in range(cases):
   textIn = input()
   textIn = textIn.lower()
   textOut = input()
   textOut = textOut.lower()
   res = HiddenSecret(textIn, textOut)
   print("Case " + str(i + 1) + ': ' + res)


#problema D

cases = int(input())
for i in range(cases):
   x1, y1, x2, y2 = input().split()
   cows = int(input())
   print("Case " + str(i + 1) + ':')
   for cow in range(cows):
       cowX, cowY = input().split()
       inside = "No"
       if int(cowX) > int(x1) and int(cowX) < int(x2) and int(cowY) > int(y1) and int(cowY) < int(y2):
           inside = "Yes"
       print(inside)

#problema C

cases = int(input())
for i in range(cases):
   input()
   students = int(input())
   listDustStr = input().split()
   listDust = []
   for nums in listDustStr:
       num = int(nums)
       if num < 0:
          num = 0
       listDust.append(num)
   
   sumDust = sum(listDust) 
   print("Case " + str(i + 1) + ': ' + str(sumDust))

#problema B

def ShadedArea (radius):
   acos = 2 * 1.57079633
   areaCircle = (radius ** 2) * acos
   areaSquare = (radius * 2) ** 2
   res = round((areaSquare - areaCircle), 2)
   return res

cases = int(input())
if cases <= 1000:
   for i in range(cases):
      radius = float(input())
      if radius <= 1000 and radius > 0 and radius == round(radius, 4):
         strOutput = str(ShadedArea(radius))
         print("Case " + str(i + 1) + ': ' + strOutput)

#problema A

def Suma (num1, num2):
   res = num1 + num2
   return res

r = int(input())
for i in range(r):
   a, b = input().split()
   print("Case " + str(i + 1) + ': ' + str(Suma(int(a), int(b))))


