import random

# -----------------------------------------
# Option 1: Dice Roll Simulation
# -----------------------------------------
def dice_roll_simulation():
    print("\n=== DICE ROLL SIMULATION ===")

    rolls = 20  # you can change this to any number >= 20

    count_6 = 0
    count_1 = 0
    two_6s_in_a_row = 0

    previous_roll = None

    for i in range(rolls):
        roll = random.randint(1, 6)
        print(f"Roll {i+1}: {roll}")

        # Count 6s and 1s
        if roll == 6:
            count_6 += 1
        if roll == 1:
            count_1 += 1

        # Count two 6s in a row
        if roll == 6 and previous_roll == 6:
            two_6s_in_a_row += 1

        previous_roll = roll

    print("\n=== Dice Roll Statistics ===")
    print("Total rolls:", rolls)
    print("Number of times you rolled a 6:", count_6)
    print("Number of times you rolled a 1:", count_1)
    print("Number of times you rolled two 6s in a row:", two_6s_in_a_row)
    print()


# -----------------------------------------
# Option 2: Jumping Jacks Workout
# -----------------------------------------
def jumping_jacks_workout():
    print("\n=== JUMPING JACKS WORKOUT ===")

    total_jumping_jacks = 100
    done = 0

    print("Workout Start: You need to complete 100 jumping jacks!")

    while done < total_jumping_jacks:
        done += 10
        print(f"\nYou completed {done} jumping jacks.")

        # If completed, stop
        if done == total_jumping_jacks:
            print("\n🎉 Congratulations! You completed the workout!")
            break

        tired = input("Are you tired? (yes/no): ").strip().lower()

        if tired in ["yes", "y"]:
            stop = input("Do you want to skip the remaining sets? (yes/no): ").strip().lower()

            if stop in ["yes", "y"]:
                print(f"\nYou completed a total of {done} jumping jacks.")
                break
            else:
                remaining = total_jumping_jacks - done
                print(f"{remaining} jumping jacks remaining. Keep going!")
        else:
            remaining = total_jumping_jacks - done
            print(f"{remaining} jumping jacks remaining. Let's continue!")


# -----------------------------------------
# MAIN MENU
# -----------------------------------------
while True:
    print("===== MAIN MENU =====")
    print("1. Dice Roll Simulation")
    print("2. Jumping Jacks Workout")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ").strip()

    if choice == "1":
        dice_roll_simulation()
    elif choice == "2":
        jumping_jacks_workout()
    elif choice == "3":
        print("Exiting program... Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.\n")
