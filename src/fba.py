import cobra.test
import os
from os.path import join

import pandas as pd
import numpy as np
from cobra.flux_analysis import single_gene_deletion


def load_model():
    data_dir = cobra.test.data_dir

    print("mini test files: ")
    print(", ".join(i for i in os.listdir(data_dir) if i.startswith("mini")))

    model = cobra.io.read_sbml_model("/Users/willfuchs/Documents/Cal Poly 20-21/csc 448/cvmax/data/photoautotrophy.xml")
    print(model)
    solution = model.optimize()
    print("solution objective value: ", solution.objective_value)

    solutions = {}
    for i, gene in enumerate(model.genes):
        with model:
            gene.knock_out()
            sol = model.optimize()

        if sol.status is not 'infeasible':
            solutions[gene.id] = sol.objective_value
        else:
            solutions[gene.id] = np.nan

    # Optional, but probably useful
    solution_df = pd.DataFrame(solutions, index=["objective value"])
    solution_df = solution_df.transpose()
    index_max = solution_df.idxmax()
    print(f"Knockout objective value: {solution_df[index_max]} on gene {index_max}")
    solution_df.to_csv('/Users/willfuchs/Documents/Cal Poly 20-21/csc 448/cvmax/out/photoautotrophy.csv')


if __name__ == '__main__':
    load_model()
