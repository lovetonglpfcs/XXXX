n = int(input("n="))
x = 1
if n < 10:
    i=0
    while i<(n*2-1):
        st=""
        j=0
        while j<(n*2-1):
            if ((i==0 or n*2-2==i or n-1==i)and j==n-1) or (n-1==i and (j==0 or j==n*2-2)):
                st=st+"X"
            elif (n==i or n-2==i) and (j==1 or j==n*2-3):
                st=st+"X"
            elif (n+1==i or n-3==i) and (j==2 or j==n*2-4):
                st=st+"X"
            elif (n+2==i or n-4==i) and (j==3 or j==n*2-5):
                st=st+"X"
            elif (n+3==i or n-5==i) and (j==4 or j==n*2-6):
                st=st+"X"
            elif (n+4==i or n-6==i) and (j==5 or j==n*2-7):
                st=st+"X"
            elif (n+5==i or n-7==i) and (j==6 or j==n*2-8):
                st=st+"X"
            elif (n+6==i or n-8==i) and (j==7 or j==n*2-9):
                st=st+"X"
            else:
                st=st+"-"

            j+=1
        i+=1
        print(st)
        x+=1

