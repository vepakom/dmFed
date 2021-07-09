from mpi4py import MPI
import numpy as np
import matplotlib.pyplot as plt
import random
#Open communication()
comm = MPI.COMM_WORLD 
rank = comm.Get_rank()
print(str(rank) + ": online")    

if(rank == 0):
    #initialize server variables
else:
    #initialize client variables

if(rank == 0):
        #prints the number of nodes (#clients + 1 server) 
    size = comm.Get_size()
    print(size)
    avgWeights = []
      for i in range(1,size):
           array = np.empty(avgWeights.shape, dtype=np.float32)
           comm.Recv(array,source=i) #server rcvs local weight via MPI
           avgWeights.append(array) # make this streaming average instead or change to use mpi.gather
else:
    #train local model code and create localWeight
    comm.Send(localWeight,dest=0) #clients send their local weight via MPI

avgWeights = comm.bcast(avgWeights, root=0) # server broadcasts the averaged weight
#note any computation/eqn now done on avgWeights gets computed by all clients automatically
