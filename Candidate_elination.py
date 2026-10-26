import pandas as pd

# Step 1: Read the CSV file
data = pd.read_csv("EnjoySport_Candidate_Elimination.csv")

# Step 2: Display the dataset
print("Training Dataset:")
print(data)

# Step 3: Separate concepts and target
concepts = data.iloc[:, :-1].values
target = data.iloc[:, -1].values

# Step 4: Initialize specific boundary
specific = concepts[0].copy()

# Step 5: Initialize general boundary
general = [
    ["?" for _ in range(len(specific))]
    for _ in range(len(specific))
]

# Step 6: Process training examples
for i, h in enumerate(concepts):

    # Positive example
    if target[i].lower() == "yes":

        for x in range(len(specific)):

            if h[x] != specific[x]:
                specific[x] = "?"
                general[x][x] = "?"

    # Negative example
    else:

        for x in range(len(specific)):

            if h[x] != specific[x]:
                general[x][x] = specific[x]
            else:
                general[x][x] = "?"

# Step 7: Remove completely general hypotheses
general = [
    g for g in general
    if g != ["?"] * len(specific)
]

# Step 8: Display the boundaries
print("\nSpecific Boundary:")
print(specific)

print("\nGeneral Boundary:")
for g in general:
    print(g)