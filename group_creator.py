import random

def get_names():
    names_input = input("Enter names separated by commas: ")
    names = [name.strip() for name in names_input.split(',') if name.strip()]
    return names

def create_groups(names, num_groups):
    random.shuffle(names)
    groups = [[] for _ in range(num_groups)]
    for i, name in enumerate(names):
        groups[i % num_groups].append(name)
    return groups

def main():
    names = get_names()
    if not names:
        print("No names were entered.")
        return
    
    while True:
        try:
            num_groups = int(input("How many groups do you want to create? "))
            if num_groups <= 0:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    
    groups = create_groups(names, num_groups)
    
    for i, group in enumerate(groups, 1):
        print(f"Group {i}: {', '.join(group)}")

if __name__ == "__main__":
    main()
