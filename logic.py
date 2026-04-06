words = ["pink", "unicorns", "crown", "silence"]

# STEP 1
# remove what pretends power
step1 = [w for w in words if w != "crown"]

# STEP 2
# remove what has no color
step2 = [w for w in step1 if w != "silence"]

# STEP 3
# join what remains
step3 = " ".join(step2)

# STEP 4
# numbers still speak
final = "16-9-14-11 / 21-14-9-3-15-18-14-19"

print("Step 1:", step1)
print("Step 2:", step2)
print("Step 3:", step3)
print("Step 4:", final)
