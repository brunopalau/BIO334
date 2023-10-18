# -*- coding: utf-8 -*-

# Building example
##############################################

# Import the cobra package and the required objects:
import cobra
from cobra import Model, Reaction, Metabolite

# Define the model:
cobra_model = Model('ExampleModel_building')

# Define the reactions:
reaction1 = Reaction('R1')
reaction1.lower_bound = 0.
reaction1.upper_bound = 1000.

reaction2 = Reaction('R2')
reaction2.lower_bound = 0.
reaction2.upper_bound = 1000.

reaction3 = Reaction('R3')
reaction3.lower_bound = -1000.
reaction3.upper_bound = 1000.

# Define the metabolites:
A = Metabolite('A', compartment='c')
B = Metabolite('B', compartment='c')
C = Metabolite('C', compartment='c')
D = Metabolite('D', compartment='c')
E = Metabolite('E', compartment='c')

# Link (‘add’) the metabolites to reactions with their respective stoichiometric coefficients:
reaction1.add_metabolites({A: -1.0,
                           B: -2,
                           C: 1.0})
reaction2.add_metabolites({B: -1.0,
                           C: -1.0,
                           D: 1.0})
reaction3.add_metabolites({A: -1.0,
                           D: -1.0,
                           E: 2.0})

# Add the reactions to the model, which will automatically add all associated metabolites:
cobra_model.add_reactions([reaction1,
                           reaction2,
                           reaction3])

# Set the objective function.


# Now your model has been populated with reactions and metabolites. Check that you have the
# right reactions and metabolites.
print("Model information")
print("---------")
print(f"{len(cobra_model.reactions)} reactions")
print(f"{len(cobra_model.metabolites)} metabolites")
print("")

# Let's take a further look at the model we have just created. Use the information printed to
# check you have introduced the model the right way.
print("Reactions")
print("---------")
for x in cobra_model.reactions:
    print(f"{x.id} : {x.reaction} / lb: {x.lower_bound} / ub: {x.upper_bound}")

#Save model in SBML format
cobra.io.write_sbml_model(cobra_model, 'ExampleModel_building.xml')
