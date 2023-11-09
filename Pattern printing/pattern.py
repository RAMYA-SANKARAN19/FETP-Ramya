l=['F','O','R','M','U','L','A','Q','S','O','L','U','T','I','O','N','S','F','O','R','M','U','L','A','Q','S','O','L','U','T','I','O','N','S']
N=int(input("Input: Enter the number of lines for the design: "))
k=N//2
print("Output:")
for i in range(k+1):
    spaces = " " * (N - i - 1)
    char="".join(l[i:(i*3)+1])
    print(spaces+char)
cha=list(char)

li=[]

for i in range(k,-1,-1): 
    if cha!=[]:
      spaces =  " " * (N - i - 1)
      
      if len(cha)!=0:
          cha.pop(0)
          cha.pop(-1)
    
      char="".join(cha)
      print(f"",spaces+(char))
      
    
    
    