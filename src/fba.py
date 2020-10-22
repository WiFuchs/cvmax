import cobra.test
import os
from os.path import join

import pandas as pd
import numpy as np
from cobra.flux_analysis import single_gene_deletion
from cobra.medium import minimal_medium


def load_model():

    model = cobra.io.read_sbml_model("/Users/willfuchs/Documents/Cal Poly 20-21/csc 448/cvmax/data/msb201152-sup-0015.xml")
    biomass_heterotrophic = model.reactions.get_by_id('Biomass_Chlamy_hetero')
    model.objective = biomass_heterotrophic
    soln = model.optimize()
    print(soln)
    print(model)

    deletion_results = single_gene_deletion(model)
    print(deletion_results)
    filtered = deletion_results.loc[deletion_results['growth'] < 6.373328]
    print("Worse Growth", filtered)
    # solution = model.optimize()
    # print(solution)
    # cobra.io.write_sbml_model(
    #     model, "updated_reinhardtii_2.xml")
    # print("solution objective value: ", solution.objective_value)
    # print(model.medium)
    #
    # max_growth = model.slim_optimize()
    # print(minimal_medium(model, max_growth))
    #
    # # remove all oxygen
    # # medium = model.medium
    # # medium['EX_o2_LPAREN_e_RPAREN_'] = 0.0
    # # model.medium = medium
    # # solution = model.optimize()
    # # print("solution objective value (no o2): ", solution.objective_value)
    #
    # solutions = {}
    # for i, gene in enumerate(model.genes):
    #     with model:
    #         gene.knock_out()
    #         sol = model.optimize()
    #
    #     if sol.status is not 'infeasible':
    #         solutions[gene.id] = sol.objective_value
    #     else:
    #         solutions[gene.id] = np.nan
    #
    # # Optional, but probably useful
    # solution_df = pd.DataFrame(solutions, index=["objective value"])
    # solution_df = solution_df.transpose()
    # index_max = solution_df.idxmax()
    # print(f"Knockout objective value: {solution_df[index_max]} on gene {index_max}")
    # solution_df.to_csv('/Users/willfuchs/Documents/Cal Poly 20-21/csc 448/cvmax/out/photoautotrophy.csv')


if __name__ == '__main__':
    load_model()
