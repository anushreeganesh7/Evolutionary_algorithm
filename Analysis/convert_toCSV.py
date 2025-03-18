import pandas as pd 
import numpy as np 

generations = np.load("/Users/anushree/Desktop/5-mutation_fitness/generations.npy")
individuals = np.load("/Users/anushree/Desktop/5-mutation_fitness/individuals.npy")
times = np.load("/Users/anushree/Desktop/5-mutation_fitness/times.npy")
np.savetxt("generations_fitness.csv", generations, delimiter=",")
np.savetxt("individuals_fitness.csv", individuals, delimiter=",")
np.savetxt("times_fitness.csv", times, delimiter=",")
