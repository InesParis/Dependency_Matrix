import matplotlib.pyplot as plt 
import numpy as np
components = ['A', 'B', 'C', 'D']

matrix = np.zeros((len(components), len(components)))

for i in range(len(components)):
    matrix[i,i]=1

modifications=[('A', 'B'), ('B', 'C'), ('C', 'D')]

for mod in modifications:
    mod_index=(components.index(mod[0]), components.index(mod[1]))
    matrix[mod_index[0], mod_index[1]]=1
    
plt.figure(figsize=(6,6))
plt.imshow(matrix, cmap="Blues", interpolation='nearest')

plt.xticks(np.arange(len(components)), components)
plt.yticks(np.arange(len(components)), components)


plt.grid(False)

plt.colorbar(label="Dependency (1:Yes, 0:No)")

plt.title("Dependency Matrix Heatmap")
plt.xlabel("Dependent Component")
plt.ylabel("Modifying Component")

plt.show()



#creation of the matrix without matplot
#components = ['A', 'B', 'C', 'D']
#matrix = [[0] * len(components) for _ in range(len(components))]

#for i in range (len(components)):
    #matrix[i][i]=1
    
#modifications= [('A','B'), ('B', 'C'),('C','D')]
#for mod in modifications:
    #mod_index=(components.index(mod[0]), components.index(mod[1]))
    #matrix[mod_index[0]][mod_index[1]]=1
    
#print("Dependency matrix:")
#print(" ", end="")
#for component in components:
    #print(f"{component}", end="|")
#print()

#print("   "+ "---" * len(components))

#for i in range(len(components)):
    #print(f"{components[i]}", end="|")
    #for j in range(len(components)):
        #print(f"{matrix[i][j]} ", end="|")
    #print()
    #print("   "+ "---" *len(components))
    