# Initial Justice League list
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
print("Initial Justice League:", justice_league)


# -----------------------------------------
# 1. Calculate the number of members
# -----------------------------------------
num_members = len(justice_league)
print("\n1. Number of members:", num_members)


# -----------------------------------------
# 2. Batman recruited Batgirl and Nightwing
# -----------------------------------------
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("\n2. After adding Batgirl and Nightwing:", justice_league)


# -----------------------------------------
# 3. Wonder Woman becomes the leader
# -----------------------------------------
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("\n3. After making Wonder Woman the leader:", justice_league)


# -----------------------------------------
# 4. Separate Aquaman and Flash by placing Superman in between
# -----------------------------------------
justice_league.remove("Superman")  # temporarily remove him
flash_index = justice_league.index("Flash")
justice_league.insert(flash_index, "Superman")
print("\n4. After separating Flash and Aquaman using Superman:", justice_league)


# -----------------------------------------
# 5. Replace entire list with new team
# -----------------------------------------
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("\n5. New Justice League team:", justice_league)


# -----------------------------------------
# 6. Sort alphabetically
# -----------------------------------------
justice_league.sort()
print("\n6. Sorted Justice League:", justice_league)
print("New Leader (index 0):", justice_league[0])
