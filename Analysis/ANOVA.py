import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from scipy.stats import ttest_ind
from statsmodels.stats.multitest import multipletests

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

# Melt the DataFrames to long format
generations_df_melted = generations_df.melt(var_name='variable', value_name='value')
individuals_df_melted = individuals_df.melt(var_name='variable', value_name='value')
times_df_melted = times_df.melt(var_name='variable', value_name='value')

# Add a column to identify the source DataFrame
generations_df_melted['group'] = 'generations'
individuals_df_melted['group'] = 'individuals'
times_df_melted['group'] = 'times'

# Combine all DataFrames
combined_df = pd.concat([generations_df_melted, individuals_df_melted, times_df_melted], ignore_index=True)

# Perform ANOVA
model = ols('value ~ group', data=combined_df).fit()
anova_table = sm.stats.anova_lm(model, typ=2)

print(anova_table)

# Perform Tukey's HSD test
tukey = pairwise_tukeyhsd(endog=combined_df['value'], groups=combined_df['group'], alpha=0.05)
print(tukey)

# Extract groups
groups = combined_df['group'].unique()
p_values = []

# Perform pairwise t-tests
for i, group1 in enumerate(groups):
    for group2 in groups[i+1:]:
        group1_data = combined_df[combined_df['group'] == group1]['value']
        group2_data = combined_df[combined_df['group'] == group2]['value']
        _, p_value = ttest_ind(group1_data, group2_data)
        p_values.append(p_value)

# Apply Bonferroni correction
reject, pvals_corrected, _, _ = multipletests(p_values, alpha=0.05, method='bonferroni')

# Output results
for i, (group1, group2) in enumerate([(group1, group2) for i, group1 in enumerate(groups) for group2 in groups[i+1:]]):
    print(f"Comparison: {group1} vs {group2}")
    print(f"P-value (corrected): {pvals_corrected[i]}")
    print(f"Reject null hypothesis: {reject[i]}\n")