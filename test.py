import numpy as np

max_iter=10
taille=3
longueur=12
affluence=0.4

def creation_route(taille):
    route=np.zeros((longueur,taille),dtype=int)
    return route


def trafic_routier(route):
    for i in range(0,max_iter):
        
            for j in range(0,taille):
                if route[longueur-1,j]==0:
                    route[longueur-1,j]=np.random.choice([0,1],p=[1-affluence,affluence]) 
                    
            for k in range(0,longueur):
                for l in range(0,taille):
                    if route[k-1,l]==0 and route[k,l]==1:
                        route[k-1,l]=1
                        route[k,l]=0
                    if route[k-1,l]==1 and route[k,l]==1:
                        if route[k,l-1]==0 and route[k-1,l-1]==0:
                            route[k,l-1]=1
                            route[k,l]=0
                        if route[k,l+1]==0 and route[k+1,l+1]==0:
                            route[k,l+1]=1
                            route[k,l]=0
                            
            for m in range(0,taille):
                if route[0,m]==1:
                    route[0,m]=0
            
            print(route)
            