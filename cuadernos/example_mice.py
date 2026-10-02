from sklearn.experimental import enable_iterative_imputer  
from sklearn.impute import IterativeImputer
import pandas as pd
import numpy as np

random_seeds = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# merged_fh corresponde al dataframe de factores habilitantes con los elementos ausentes, unido # a las columnas auxiliares

columns = list(merged_fh.columns)

original_nans = merged_fh.isnull()

imputed_values_comparison = {}

print("Running IterativeImputer with different random seeds to observe imputation variability:\n")

for seed in random_seeds:
    print(f"Processing with random_state = {seed}...")

    imputer = IterativeImputer(
        max_iter=100,
        sample_posterior=True, # ←- sample_posterior True activa la aleatoriedad para cada iteracion
        random_state=seed, # ←- semilla
        min_value=0, # ←– se fija el valor mínimo posible, que sería un puntaje igual a 0
        max_value=100 # ←– se fija el valor máximo posible, que sería un puntaje igual a 100
    )

    imputed_data_array = imputer.fit_transform(merged_fh[columns])
    imputed_df_current = pd.DataFrame(imputed_data_array, columns=columns, index=merged_fh.index)

    imputed_nans_for_seed = imputed_df_current[original_nans].stack()

    imputed_values_comparison[f'Imputed_Seed_{seed}'] = imputed_nans_for_seed

    print(f"\tNumber of imputed values for original NaNs: {len(imputed_nans_for_seed)}")

comparison_df = pd.DataFrame(imputed_values_comparison)

comparison_df["std_of_all_seeds"] = comparison_df.std(axis=1)
comparison_df["avg_of_all_seeds"] = comparison_df.mean(axis=1)

comparison_df = comparison_df.sort_values(by="std_of_all_seeds", ascending=False)

print("\nComparison of imputed values for originally missing data across different seeds:")
display(comparison_df[["std_of_all_seeds", "avg_of_all_seeds"]])
