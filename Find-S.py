import pandas as pd

# Step 1: Read the training data
data = pd.read_csv("EnjoySport.csv")

# Step 2: Display the dataset
print("Training Dataset:")
print(data)

# Step 3: Initialize hypothesis
hypothesis = None

# Step 4: Process each training example
for _, row in data.iterrows():

    # Separate input attributes and target
    x = row[:-1].tolist()
    y = row[-1]

    # Consider only positive examples
    if str(y).lower() == "yes":

        # First positive example
        if hypothesis is None:
            hypothesis = x

        # Compare with the current hypothesis
        else:
            for i in range(len(hypothesis)):

                # Generalize if values are different
                if hypothesis[i] != x[i]:
                    hypothesis[i] = "?"

# Step 5: Display final hypothesis
print("\nMost Specific Hypothesis:")
print(hypothesis)