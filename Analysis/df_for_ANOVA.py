import numpy as np
import pandas as pd

# Load the .npy files
generations_data = np.load('./5-mutation_fitness/generations.npy')
individuals_data = np.load('./5-mutation_fitness/individuals.npy')
times_data = np.load('./5-mutation_fitness/times.npy')

# Convert the data to DataFrames
generations_df = pd.DataFrame(generations_data)
individuals_df = pd.DataFrame(individuals_data)
times_df = pd.DataFrame(times_data)

# Add column headers x1, x2, ..., x100 (adjust based on the number of columns in each DataFrame)
columns_generations = [f'x{i}' for i in range(1, generations_df.shape[1] + 1)]
columns_individuals = [f'x{i}' for i in range(1, individuals_df.shape[1] + 1)]
columns_times = [f'x{i}' for i in range(1, times_df.shape[1] + 1)]

generations_df.columns = columns_generations
individuals_df.columns = columns_individuals
times_df.columns = columns_times

# Transpose the DataFrames
generations_df_transposed = generations_df.transpose()
individuals_df_transposed = individuals_df.transpose()
times_df_transposed = times_df.transpose()

# Save the transposed DataFrames to .csv files
generations_csv_path = './5-mutation_fitness/generations_transposed.csv'
individuals_csv_path = './5-mutation_fitness/individuals_transposed.csv'
times_csv_path = './5-mutation_fitness/times_transposed.csv'

generations_df_transposed.to_csv(generations_csv_path, index=False)
individuals_df_transposed.to_csv(individuals_csv_path, index=False)
times_df_transposed.to_csv(times_csv_path, index=False)

print("Files have been saved successfully.")