import numpy as np
import networkx as nx
# Here you may include additional libraries and define more auxiliary functions:


# This function should return the EMD distances between file1 and file2.
# EMD distance depends on your choice of distance between pixels and
# this will be taken into account during grading.
def comp_dist(file1, file2):
    # Write your code here:
  
    data_0 = []
    with open(file1, "r") as file:
        data_0.append(file.read().replace("\n", ""))
    

    data_1 = []
    with open(file2, "r") as file:
        data_1.append(file.read().replace("\n", ""))
    
    
    x_0 = np.zeros(80*10)
    for i in range(len(data_0[0])):
        x_0[i] = int(data_0[0][i])

    j_0 = np.reshape(x_0, (10,80))    
    k_0 = []
    for i in range(len(j_0)):
        for b in range(j_0.shape[1]):
            if j_0[(i,b)] != 0:
                node_name = "n0_" + str(i+1) + "_" + str(b+1)
                k_0.append((node_name, j_0[i,b],(i+1,b+1)))
                
    x_1 = np.zeros(80*10)
    for i in range(len(data_1[0])):
        x_1[i] = int(data_1[0][i])

    j_1 = np.reshape(x_1, (10,80))    
    k_1 = []
    for i in range(len(j_1)):
        for b in range(j_1.shape[1]):
            if j_1[(i,b)] != 0:
                node_name = "n1_" + str(i+1) + "_" + str(b+1)
                k_1.append((node_name, j_1[i,b],(i+1,b+1)))          
    
             
    G = nx.DiGraph()

    somma_0 = sum(j[1] for j in k_0)
    somma_1 = sum(k[1] for k in k_1)

    
    
    if somma_1 != somma_0:
        res_k_1 = []
        for i in range(len(k_1)):
            res_k_1.append((k_1[i][0],(k_1[i][1]/somma_1)*somma_0, k_1[i][2]))
        somma_1 = round(sum(k[1] for k in res_k_1))
        k_1 = res_k_1
 
    G.add_node("s", demand = -somma_0)
    G.add_node("t", demand = somma_1)
    

    for u in k_0:
        for v in k_1:
            if u != v:
                
                dist = (v[2][1] - u[2][1] + 80) % 80
                
                G.add_edge("s", u[0], weight = 0, capacity = u[1])
                G.add_edge(u[0],v[0], weight = dist, capacity =min(u[1], v[1]))
                G.add_edge(v[0], "t", weight = 0, capacity = v[1])
    
                   
    flow = nx.min_cost_flow(G)

    tot_cost = sum(flow[node1][node2] * G[node1][node2]["weight"] for (node1, node2) in G.edges)
    tot_mass = sum(flow[node1][node2] for (node1, node2) in G.edges)
    distance = tot_cost/tot_mass

    # And return the EMD distance, it should be float.
    return float(distance)


# This function should sort the files as described on blackboard.
# P1.txt should be the first one.
def sort_files():
    # If your code cannot handle all files, remove the problematic ones
    # from the following list and sort only those which you can handle.
    # Your code should never fail!
    # Write your code here:
    
    files = ['P1.txt', 'P2.txt', 'P3.txt', 'P4.txt', 'P5.txt', 'P6.txt', 'P7.txt', 'P8.txt', 'P9.txt', 'P10.txt', 'P11.txt',           'P12.txt', 'P13.txt', 'P14.txt', 'P15.txt']
    
    x = []
    
    for file in files:
        j = comp_dist(file1 = "P1.txt", file2 = file)
        x.append((j,file))
    x.sort()
    

    sorted_files = []
    for i in range(len(x)):
        sorted_files.append(x[i][1])

    
    



    # should return sorted list of file names
    return sorted_files
