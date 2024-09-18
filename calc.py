def calculate_love_score(name1, name2):
    name1 = name1.lower()
    name2 = name2.lower()

    combined_names = name1 + name2

    true_count = 0
    true_count += combined_names.count('t')
    true_count += combined_names.count('r')
    true_count += combined_names.count('u')
    true_count += combined_names.count('e')

    love_count = 0
    love_count += combined_names.count('l')
    love_count += combined_names.count('o')
    love_count += combined_names.count('v')
    love_count += combined_names.count('e')

    love_score = int(str(true_count) + str(love_count))
 
    print(f"Your love score is: {love_score}")



calculate_love_score("Alice", "Bob")
