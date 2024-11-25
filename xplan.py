import matplotlib.pyplot as plt 
import numpy as np
import random


#random components
# Define a list of components
components = ['A', 'B', 'C', 'D','E', 'F', 'G', 'H', 'I', 'J']

# Function to generate random dependencies
def generate_random_dependencies(components):
    dependencies = []
    for i in range(len(components)):
        for j in range(i+1, len(components)):  
            if random.choice([True, False]):  
                dependencies.append((components[i], components[j]))
    return dependencies

# Initialize a square matrix with zeros. 
matrix = np.zeros((len(components), len(components)))

# Generate random dependencies
modifications = generate_random_dependencies(components)

# Mark the diagonal elements (self-dependencies)
for i in range(len(components)):
    matrix[i, i] = 1

# Update the matrix based on the generated dependencies
for mod in modifications:
    mod_index = (components.index(mod[0]), components.index(mod[1]))
    matrix[mod_index[0], mod_index[1]] = 1
    
outgoing_dependencies = np.sum(matrix, axis=1)

# Create the heatmap plot
plt.figure(figsize=(6, 6))
plt.imshow(matrix, cmap='Blues', interpolation='nearest')

# Add labels for the rows and columns (the components)
plt.xticks(np.arange(len(components)), components)
plt.yticks(np.arange(len(components)), components)

# Add gridlines for clarity
plt.grid(False)

# Show colorbar to represent the values
plt.colorbar(label="Dependency (1: Yes, 0: No)")

# Set title and labels
plt.title('Dependency Matrix Heatmap')
plt.xlabel('Dependent Component')
plt.ylabel('Modifying Component')

# Display the matrix description
print("This is a randomly generated dependency matrix.")
if modifications:
    print("The following dependencies were randomly chosen:")
    for dep in modifications:
        print(f"  Changing {dep[0]} requires changing {dep[1]}.")
else:
    print("No dependencies were randomly generated.")

print("\nThe next simplest case involves a single dependency, where:")
print("Changing component C requires changing component A as well.")
print("Note that the dependencies are one-way: Changing component A does not require changing component C.")



#line chart showing outgoing dependencies
plt.figure(figsize=(8, 5))

# Plot the number of outgoing dependencies for each component
plt.plot(components, outgoing_dependencies, marker='o', color='tab:blue')


plt.title('Outgoing Dependencies per Component')
plt.xlabel('Components')
plt.ylabel('Number of Outgoing Dependencies')


plt.grid(True)
plt.show()
plt.show()

#----------------------------------------------------------------------------------------------------------

#basic selected components
#components = ['A', 'B', 'C', 'D']

#matrix = np.zeros((len(components), len(components)))

#for i in range(len(components)):
    #matrix[i,i]=1

#modifications=[('A', 'B'), ('B', 'C'), ('C', 'D')]

#for mod in modifications:
    #mod_index=(components.index(mod[0]), components.index(mod[1]))
    #matrix[mod_index[0], mod_index[1]]=1
    
#plt.figure(figsize=(6,6))
#plt.imshow(matrix, cmap="Blues", interpolation='nearest')

#plt.xticks(np.arange(len(components)), components)
#plt.yticks(np.arange(len(components)), components)


#plt.grid(False)

#plt.colorbar(label="Dependency (1:Yes, 0:No)")

#plt.title("Dependency Matrix Heatmap")
#plt.xlabel("Dependent Component")
#plt.ylabel("Modifying Component")

#plt.show()


#-----------------------------------------------------------------------------------


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
    