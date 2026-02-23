import os
from bitarray import bitarray

cut = input("cut:")
datasetname = input("insert dataset name:")
format = int(input("Format: 1-DIMACS 2-simple adjacency list "))
if format != 1 and format != 2:
    print("invalid format.")
    exit()

dir_path = os.path.dirname(os.path.realpath(__file__))
datasetpath = dir_path+'\\'+datasetname+'\\cut_'+str(cut)+'\\'
if not os.path.exists(datasetpath):
    print("dataset do not exist.")
    exit()

metadata = datasetpath + "metadata.csv"
number_edges = 0
number_nodes = 0
print("reding metadata..")
with open(metadata,'r') as file:
    for line in file:
        line = line.strip()
        line = line.split('\t')
        if line[0] == "Number of Nodes:":
            number_nodes = int(line[1])
        if line[0] == "Number of Edges:":
            number_edges = int(line[1])
print("number of nodes:",number_nodes,"number of edges:",number_edges)
adj_list =[]
adj_list.append([])
for i in range(1,number_nodes):
    bit_array = bitarray(i)
    bit_array.setall(0)
    adj_list.append(bit_array)

print("reading and generating adjacent matrix..")
with open(datasetpath+'edgecover.txt') as file:
    for line in file:
        line = line.strip()
        line = line.split()
        for i in range(0,len(line)-1):
            for j in range(i+1,len(line)):
                adj_list[int(line[j])][int(line[i])] = 1

edges = 0
for row in range(1,len(adj_list)):
    for column in range(len(adj_list[row])):
        if adj_list[row][column]:
            edges +=1
            #print(row," ",column)
print("total edges ",edges)

if format == 1:
    outputfile = datasetpath+'edgelistDIMACS.txt'
    print("writing into file...")
    with open(outputfile,'w') as outputfile:
        outputfile.write("p edge "+str(number_nodes)+' '+ str(number_edges)+'\n')
        
        for row in range(1,len(adj_list)):
            for column in range(len(adj_list[row])):
                if adj_list[row][column]:
                    outputfile.write("e "+str(row+1)+' '+str(column+1)+'\n')
elif format == 2:
    outputfile = datasetpath+'edgelist.txt'
    print("note:the index starts with 0.")
    
    outputfile = datasetpath+'edgelist.txt'
    print("writing into file...")
    with open(outputfile,'w') as outputfile:
        for row in range(1,len(adj_list)):
            for column in range(len(adj_list[row])):
                if adj_list[row][column]:
                        outputfile.write(str(row)+' '+str(column)+'\n')
else:
    print("format error")

print("operation complete.")