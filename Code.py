# Get input values from the user
fresh_weight = float(input("Enter the fresh weight (in grams): "))
dry_weight = float(input("Enter the dry weight (in grams): "))
turgid_weight = float(input("Enter the turgid weight (in grams): "))

# Calculate the RWC
rwc = ((fresh_weight - dry_weight) / (turgid_weight - dry_weight)) * 100

# Print the RWC
print("The RWC is: {:.2f}%".format(rwc))
