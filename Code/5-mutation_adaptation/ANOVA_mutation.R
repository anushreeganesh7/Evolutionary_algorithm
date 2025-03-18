#loading reticulate and use it to load numpy
#library(reticulate)
#np <- import("numpy")

#getwd()
#data reading
#generations <- np$load("Desktop/5-mutation_adaptation/generations.npy")
#individuals <- np$load("Desktop/5-mutation_adaptation/individuals.npy")
#times <- np$load("Desktop/5-mutation_adaptation/times.npy")
 #reading the data
generations <- read.csv("Desktop/5-mutation_adaptation/generations.csv")
individuals <- read.csv("Desktop/5-mutation_adaptation/individuals.csv")
times <- read.csv("Desktop/5-mutation_adaptation/times.csv")

#ANOVA
