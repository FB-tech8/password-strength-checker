import re

password = input("Enter your password: ")

score = 0
suggestions = []

# Check length
if len(password) >= 8:
    score += 1
else:
    suggestions.append("Password should be at least 8 characters")

# Check uppercase letters
if re.search("[A-Z]", password):
    score += 1
else:
    suggestions.append("Add at least one uppercase letter")

# Check numbers
if re.search("[0-9]", password):
    score += 1
else:
    suggestions.append("Add at least one number")

# Check special characters
if re.search("[!@#$%^&*(),.?\":{}|<>]", password):
    score += 1
else:
    suggestions.append("Add a special character")

# Determine strength
if score == 4:
    strength = "Strong"
elif score == 3:
    strength = "Medium"
else:
    strength = "Weak"

print("\nPassword Strength:", strength)

if suggestions:
    print("\nSuggestions to improve:")
    for s in suggestions:
        print("-", s)
