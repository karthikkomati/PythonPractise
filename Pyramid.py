def pyramid(n):
    k = ""
 
    for i in range(2*n+1):
         k += " "
         
    for x in range(n):

        j = list(k)
        j[n-x] = "*"
        j[n+x] = "*"
        k = "".join(j)
        print(k)
        
    
pyramid(7)
