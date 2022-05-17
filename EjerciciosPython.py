#Counting Cells in a Blob 
def CountingCells(lista):
   listGroups = [[0 for ejex in range(len(lista))] for ejey in range(len(lista))]    
   movX = [0,-1,0,1]
   movY = [-1,0,1,0]  
   puntoActX = len(lista) / 2         
   puntoActY = len(lista) / 2         
   cont = 1
   thereIsCell = True
   while(thereIsCell):
      thereIsCell = False
      for i in range(4):
         if ((i != 3 or puntoActX != len(lista) - 1) and (i != 2 or puntoActY != len(lista[0]) - 1) and (i != 1 or puntoActX != 0) and (i != 0 or puntoActY != 0)):
            if (listBi[puntoActX + movX[i]][puntoActY + movY[i]] == 1):
               listGroups[puntoActX + movX[i]][puntoActY + movY[i]] = cont
               

cases = int(input())
for i in range(cases):
   input()
   fila = input()
   listBi = [[0 for ejex in range(len(fila))] for ejey in range(len(fila))]    
   for j in range(int(listaBi)):
      line = input()
      for k in range(int(listaBi[j])):
          listBi[j][k] = int(fila[k])
      fila = input()
   res = CountingCells(listBi) 
   print("Case " + str(i + 1) + ': ' + str(res))


#search Binary
def BusquedaBinaria(lista, x, valueSide):
    izq = 0
    der = len(lista) -1
    while izq <= der:
        medio = int((izq+der)/2)
        if lista[medio][0] == int(x):
            return medio
        elif lista[medio][0] > int(x):
            der = medio-1
        else:
            izq = medio+1
    if valueSide: 
       return medio
    else: return -1
#Back to Underworld
cases = int(input())
for i in range(cases):
    lenTeam0 = 0 
    res = 0
    contGrafos = 0;
    fights = int(input())
    listFights = [[0 for x in range(3)] for y in range(1)]
    for j in range(fights):
       x, y = input().split()
       existX = False; existY = False; teamX = -1; teamY = -1; grafoX = -1; grafoY = -1 
       k = BusquedaBinaria(listFights, int(x), False)
       if k >= 0:
          existX = True; grafoX = listFights[k][1]; teamX = listFights[k][2] 
       k = BusquedaBinaria(listFights, int(y), False)
       if k >= 0:
          existY = True; grafoY = listFights[k][1]; teamY = listFights[k][2]

       if existX and existY and grafoX != grafoY:
           for k in listFights:
               if k[1] == grafoY: 
                  if teamX == teamY:
                      if k[2] == 0: k[2] = 1; lenTeam0 -= 1                      
                      else: k[2] = 0; lenTeam0 += 1                    
                  k[1] == grafoX               
       if existX and existY == False: 
           if teamX == 0: teamY = 1
           if teamX == 1: teamY = 0; lenTeam0 += 1
           index = BusquedaBinaria(listFights, int(y), True)
           listFights.insert(index + 1, [int(y), grafoX, teamY])
       if existY and existX == False: 
           if teamY == 0: teamX = 1
           if teamY == 1: teamX = 0; lenTeam0 += 1
           index = BusquedaBinaria(listFights, int(x), True)
           listFights.insert(index + 1, [int(x), grafoY, teamX])
       if existX == False and existY == False: 
           if len(listFights) == 1: 
               listFights.clear(); lenTeam0 += 1; contGrafos += 1;
               listFights.append([int(x), contGrafos, 0])
               listFights.append([int(y), contGrafos, 1])
           else:
              contGrafos += 1; lenTeam0 += 1
              index = BusquedaBinaria(listFights, int(x), True)
              listFights.insert(index + 1, [int(x), contGrafos, 0])
              index = BusquedaBinaria(listFights, int(y), True)
              listFights.insert(index + 1, [int(y), contGrafos, 1])      
    lenTeam1 = len(listFights) - lenTeam0
    if lenTeam0 >= lenTeam1: res = lenTeam0
    else: res = lenTeam1    
    print("Case " + str(i + 1) + ': ' + str(res))

#Back to Underworld 2
def addEdge(adj, v, w):     
    adj[v].append(w)
    adj[w].append(v) 
    return adj
def greedyColoring(list, largo):
     
    result = [-1] * largo
    result[0] = 0;
    available = [False] * largo
    for i in range(1, largo):
        for j in list[i]:
            if (result[j] != -1):
                available[result[j]] = True
        color = 0
        while color < largo:
            if (available[color] == False):
                break            
            color += 1
        result[i] = color
        for j in list[i]:
            if (result[j] != -1):
                available[result[j]] = False
    res = 0
    for i in result:
        if i == 0: res += 1
    if largo - res > res: res = largo - res
    return res
def ConverValid(listFights):
    listWork = []
    for i in range(len(listFights)):
        for j in range(len(listFights[i])):
            thereIs = False
            for k in range(len(listWork)):
                if listFights[i][j] == listWork[k]: thereIs = True; listFights[i][j] = int(k); 
            if thereIs == False: listWork.append(listFights[i][j]); listFights[i][j] = int(len(listWork) - 1)
    return listFights
cases = int(input())                   
for i in range(cases):
    fights = int(input())
    listFights = [[] for i in range(1)]
    for j in range(fights):
       x, y = input().split()    
       listFights.append([x, y])
    listFights.pop(0)
    listNum = ConverValid(listFights)
    largo = 0
    for j in range(len(listNum)):
        if listNum[j][0] > largo: largo = listNum[j][0]
        if listNum[j][1] > largo: largo = listNum[j][1]
    largo += 1
    listNodo = [[] for i in range(largo)]
    for j in range(len(listNum)):
        listNodo = addEdge(listNodo, listNum[j][0], listNum[j][1])
    res = greedyColoring(listNodo, largo)
    print("Case " + str(i + 1) + ': ' + str(res))


#Escape from Jail 
def EscapeFromJail(N, listK, listM):
    wayTraveled = ["new" for t in range(int(N))]
    wayTraveled[0] = "traveled"
    endWay = False
    while (endWay == False):
        endWay = True
        posiciones = [i for i, x in enumerate(wayTraveled) if x == "traveled"]
        for i in posiciones:
                cont = 0
                for j in range(len(listM)):
                    direccion = 2
                    seguir = False
                    if (listM[j][0] == i + 1): direccion = 1; seguir = True
                    if (listM[j][1] == i + 1): direccion = 0; seguir = True
                    if (seguir):
                        if (wayTraveled[listM[j][direccion] - 1] == "new"):
                            for k in range(len(listK)):
                                go = True 
                                if (listK[k][1] == listM[j][direccion]):
                                    go = False
                                if(go):
                                    if (listK[k][0] == listM[j][direccion]):
                                        for l in range(len(listK)):
                                            if (listK[l][1] == listK[k][0]): listK[l][1] = 0
                                    wayTraveled[listM[j][direccion] - 1] = "traveled"
                                    cont += 1
                                    if (wayTraveled[len(wayTraveled) - 1] == "traveled"): return 'Y' 
                                    if (direccion == 0): wayTraveled[listM[j][1] - 1] = "last"
                                    else: wayTraveled[listM[j][0] - 1] = "last"
                                    endWay = False      
                                    if (cont == 2): break 
                    if (cont == 2): break 
    return 'N'

N, K, M = input().split()
listaRes = []
while(int(N) != -1 and int(K) != -1 and int(M) != -1):
    listK = [[0 for y in range(2)] for x in range(int(K))] 
    for i in range(int(K)):
        a, b = input().split()
        listK[i][0] = int(a) 
        listK[i][1] = int(b) 
    listM = [[0 for y in range(2)] for x in range(int(M))]  
    for i in range(int(M)):
        a, b = input().split()
        listM[i][0] = int(a) 
        listM[i][1] = int(b) 
    listaRes.append(EscapeFromJail(int(N), listK, listM))
    N, K, M = input().split()
for i in listaRes:
    print(i)

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




 


