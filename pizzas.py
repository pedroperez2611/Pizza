@author: Pedro
"""
import itertools


def pizzas (M,N,S):
   
   
    for m in range(M):
    #bucle de permutaciones
        for i in range(N):
            permutaciones=[]
            K=0
            permutaciones=list(itertools.permutations(S,N-i))
            n=len(permutaciones)
            for j in range (n):
                if sum(permutaciones[j])==M:
                    sol=permutaciones[j]
                    K=N-i
                    break
                
            if K !=0:
                break
        if K !=0:
            break
        M=M-1
        
        S_pos=[]
        
    for l in range(K):
        
        S_pos.append(S.index(sol[l]))
        L=S_pos
            
    return(L,K)
    
   
print(pizzas(17,4,[2,5,6,8]))
