import numpy as np

max_iter=100
taille=3
longueur=25
nvoit=50


"""creation route aléatoire"""
def creation_route(taille):
    route=np.zeros((longueur,taille),dtype=int)
    a=True
    for i in range(0,nvoit):
        while a:
            x=np.random.choice(range(longueur))
            y=np.random.choice(range(taille))
            if route[x][y]==0:
                route[x][y]=1
                a=False
        a=True
    return route

"""affichage de la route"""
def affiche(route):
    r=np.zeros((longueur,taille),dtype=str)
    for i in range(0,taille):
        for j in range(0,longueur):
            if route[j][i]==0:
                r[j][i]="_"
            elif route[j][i]==2:
                r[j][i]="X"
            elif route[j][i]==1: 
                r[j][i]="🚗"
    print(r)



    
    
"""simulation du traffic routier"""
def trafic_routier(route) :
    x=0
    for i in range(0,max_iter):
        for k in range(0,longueur):
            for l in range(0,taille):
                
                if k==0 and route[k,l]==1 and route[longueur-1,l]==0:
                    route[k,l]=0
                    route[longueur-1,l]=1
                    
                elif route[k-1,l]==0 and route[k,l]==1:
                    route[k-1,l]=1
                    route[k,l]=0
            
                    
                elif l!=0 and l!=taille-1:        
                    if route[k-1,l]==1 and route[k,l]==1:
                    
                        if route[k,l-1]==0 and route[k-1,l-1]==0:
                            route[k,l-1]=1
                            route[k,l]=0
                    
                        if route[k,l+1]==0 and route[k-1,l+1]==0:
                            route[k-1,l+1]=1
                            route[k,l]=0
                elif l==0:
                    if route[k,l+1]==0 and route[k-1,l+1]==0:
                            route[k-1,l+1]=1
                            route[k,l]=0
                            
                elif l==taille:
                    if route[k,l-1]==0 and route[k-1,l-1]==0:
                            route[k-1,l-1]=1
                            route[k,l]=0
                    
                    
        """"bouchon aléatoire"""  
        if x==10:
            a=True
            while a:
                x=np.random.choice(range(longueur))
                y=np.random.choice(range(taille))
                if route[x][y]==1:
                    route[x][y]=2
                    a=False
            
        x=x+1
        affiche(route)
        input(f"\nACTUALISATION {i} : \n")
    return x


route=creation_route(taille)
trafic_routier(route)
