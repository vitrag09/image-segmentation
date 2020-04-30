import numpy as np
image=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0],[0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0],[0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0],[0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0],[0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0],[0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1],[0,0,1,0,0,0,0,0,0,0,0,0,0,1,1,1],[0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0],[0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0]]
#label=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
label_arr=np.zeros(shape=(16,16),dtype=int)

def generate_neighbours(i,j,image):
    length=len(image)
    neighbours=[[i-1,j-1],[i-1,j],[i-1,j+1],[i,j-1],[i,j+1],[i+1,j-1],[i+1,j],[i+1,j+1]]
    true_neigbour=[]
    for [a,b] in neighbours:
        if a>=0 and b>=0 and a<length and b<length and image[a][b]==1:
            true_neigbour.append([a,b])
    return true_neigbour

def labeled_neighbour(neighbours,label_arr):
    for [a,b] in neighbours:
        if label_arr[a,b]!=0:
            return label_arr[a,b]
    return 0
def do_labeling(pairs,label_arr,label):
    for [i,j] in pairs:
        label_arr[i,j]=label
    return label_arr
def segmentation(image,label_arr):
    explored_node_list=[]
    regions=0

    for i in range(len(image)):
        for j in range(len(image)):
            if image[i][j]==1 and [i,j] not in explored_node_list:
                neighbours=generate_neighbours(i,j,image)
                label=labeled_neighbour(neighbours,label_arr)
                explored_node_list.append(list([i,j]))
                if label!=0:
                    label_arr[i,j]=label
                    label_arr=do_labeling(neighbours,label_arr,label)
                else:
                    regions+=1
                    label=regions
                    label_arr[i,j]=label
                    label_arr=do_labeling(neighbours,label_arr,label)
    return regions,label_arr

regions,label_arr=segmentation(image,label_arr)
print("number of regions are :"+str(regions))
for i in label_arr:
    print(i)
