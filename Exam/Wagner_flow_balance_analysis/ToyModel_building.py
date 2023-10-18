# -*- coding: utf-8 -*-

# Building the toy model from figure 1
##############################################

# Importing the cobra package and the required objects:
import cobra
from cobra import Model, Reaction, Metabolite

# Defining the model:
cobra_model = Model('ToyModel')

# Defining the reactions (16 internal, 5 external):
reaction1 = Reaction('R1')
reaction1.name = 'reaction 1'
reaction1.subsystem = 'internal'
reaction1.lower_bound = 0.
reaction1.upper_bound = 1000.

reaction2 = Reaction('R2')
reaction2.name = 'reaction 2'
reaction2.subsystem = 'internal'
reaction2.lower_bound = 0.
reaction2.upper_bound = 1000.

reaction3 = Reaction('R3')
reaction3.name = 'reaction 3'
reaction3.subsystem = 'internal'
reaction3.lower_bound = 0.
reaction3.upper_bound = 1000.

reaction4 = Reaction('R4')
reaction4.name = 'reaction 4'
reaction4.subsystem = 'internal'
reaction4.lower_bound = -1000.
reaction4.upper_bound = 1000.

reaction5 = Reaction('R5')
reaction5.name = 'reaction 5'
reaction5.subsystem = 'internal'
reaction5.lower_bound = -1000.
reaction5.upper_bound = 1000.

reaction6 = Reaction('R6')
reaction6.name = 'reaction 6'
reaction6.subsystem = 'internal'
reaction6.lower_bound = -1000.
reaction6.upper_bound = 1000.

reaction7 = Reaction('R7')
reaction7.name = 'reaction 7'
reaction7.subsystem = 'internal'
reaction7.lower_bound = 0.
reaction7.upper_bound = 1000.

reaction8 = Reaction('R8')
reaction8.name = 'reaction 8'
reaction8.subsystem = 'internal'
reaction8.lower_bound = 0.
reaction8.upper_bound = 1000.

reaction9 = Reaction('R9')
reaction9.name = 'reaction 9'
reaction9.subsystem = 'internal'
reaction9.lower_bound = 0.
reaction9.upper_bound = 1000.

# Add internal reactions 10 to 16:





reaction17 = Reaction('R17')
reaction17.name = 'reaction 17'
reaction17.subsystem = 'external'
reaction17.lower_bound = -10.
reaction17.upper_bound = 1000.

reaction18 = Reaction('R18')
reaction18.name = 'reaction 18'
reaction18.subsystem = 'external'
reaction18.lower_bound = 0.
reaction18.upper_bound = 1000.

# Add external reactions 19, 20 and 21:




# Defining the metabolites:
A_e = Metabolite(
    'A_e',
    formula='',
    name='A',
    compartment='e')

B_e = Metabolite(
    'B_e',
    formula='',
    name='B',
    compartment='e')

C_e = Metabolite(
    'C_e',
    formula='',
    name='C',
    compartment='e')

M_e = Metabolite(
    'M_e',
    formula='',
    name='M',
    compartment='e')

X_e = Metabolite(
    'X_e',
    formula='',
    name='X',
    compartment='e')

E_c = Metabolite(
    'E_c',
    formula='',
    name='E',
    compartment='c')

F_c = Metabolite(
    'F_c',
    formula='',
    name='F',
    compartment='c')

G_c = Metabolite(
    'G_c',
    formula='',
    name='G',
    compartment='c')

H_c = Metabolite(
    'H_c',
    formula='',
    name='H',
    compartment='c')

I_c = Metabolite(
    'I_c',
    formula='',
    name='I',
    compartment='c')

J_c = Metabolite(
    'J_c',
    formula='',
    name='J',
    compartment='c')

# Introduce the metabolites L_c, M_c, N_c, O_c and X_c:






# Adding the metabolites to the reactions with their respective stoichiometry:
reaction1.add_metabolites({X_c: -1.0,
                           X_e: 1.0})

reaction2.add_metabolites({A_e: -1.0,
                           E_c: 1.0})

reaction3.add_metabolites({E_c: -1.0,
                           F_c: 1.0})

reaction4.add_metabolites({E_c: -1.0,
                           G_c: 1.0})

reaction5.add_metabolites({F_c: -1.0,
                           G_c: 1.0})

reaction6.add_metabolites({F_c: -1.0,
                           I_c: 2.0})

reaction7.add_metabolites({B_e: -1.0,
                           H_c: 1.0})

reaction8.add_metabolites({I_c: -1.0,
                           J_c: 1.0})

reaction9.add_metabolites({J_c: -1.0,
                           O_c: 1.0})

reaction10.add_metabolites({C_e: -1.0,
                            L_c: 1.0})

# Add metabolites to internal reactions 11 to 16:




reaction17.add_metabolites({A_e: -1.0})

reaction18.add_metabolites({M_e: -1.0})

# Add metabolites to external reactions 19, 20 and 21:






# The model is still empty.
print("Model information initially")
print("---------")
print(f"{len(cobra_model.reactions)} reactions initially")
print(f"{len(cobra_model.metabolites)} metabolites initially")
# We are not introducing genes for this example, but it could be done.
print(f"{len(cobra_model.genes)} genes initially")
print("")

# Add the reactions to the model, which will also add all associated metabolites.
for i in range(1, 22):
    cobra_model.add_reactions([eval('reaction'+str(i))])

# Now there are things in the model.
# Check that you get the right amount of reactions and metabolites.
print('Model information')
print("---------")
print(f"{len(cobra_model.reactions)} reactions")
print(f"{len(cobra_model.metabolites)} metabolites")
print(f"{len(cobra_model.genes)} genes")
print("")

# Let's take a further look into the model we have just created.
# Use the information printed to check you have introduced the model the right way.
print("Reactions")
print("---------")
for x in cobra_model.reactions:
    print(f"{x.id} : {x.reaction} / {x.lower_bound} / {x.upper_bound}")

print("")
print("Metabolites")
print("-----------")
for x in cobra_model.metabolites:
    print(f"{x.id} : {x.compartment}")

# Save the model into SBML format:

