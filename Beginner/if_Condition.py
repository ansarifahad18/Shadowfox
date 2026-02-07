def bmi_calculator():
    print("\n--- BMI CATEGORY CALCULATOR ---")
    
    height = float(input("Enter height in meters: "))
    weight = float(input("Enter weight in kilograms: "))

    bmi = weight / (height ** 2)

    if bmi >= 30:
        category = "Obesity"
    elif 25 <= bmi < 30:
        category = "Overweight"
    elif 18.5 <= bmi < 25:
        category = "Normal"
    else:
        category = "Underweight"

    print(f"BMI Category: {category}\n")


def city_to_country():
    print("\n--- CITY TO COUNTRY FINDER ---")

    Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
    UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
    India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

    city = input("Enter a city name: ").strip().title()

    if city in Australia:
        print(f"{city} is in Australia\n")
    elif city in UAE:
        print(f"{city} is in UAE\n")
    elif city in India:
        print(f"{city} is in India\n")
    else:
        print("City not found in the database.\n")


# ===============================
# MAIN PROGRAM (MENU SYSTEM)
# ===============================
while True:
    print("===== MAIN MENU =====")
    print("1. BMI Category Calculator")
    print("2. City to Country Finder")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        bmi_calculator()
    elif choice == "2":
        city_to_country()
    elif choice == "3":
        print("Exiting program... Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.\n")
