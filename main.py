# Function to draw a right-angled triangle
def draw_right_angle(n):
    for i in range(1, n + 1):
        print("*" * i)

# Function to draw an upside-down right-angled triangle
def draw_upside_down_right_angle(n):
    for i in range(n, 0, -1):
        print("*" * i)

# Function to draw a pyramid
def draw_pyramid(n):
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        if i == 1:
            print(spaces + "*")
        else:
            print(spaces + "*" + " " * (2 * i - 3) + "*")

# Main function that interacts with the user
def main():
    while True:  # Add a loop for repeated figures
        # Prompt the user to choose a figure
        choice = input("_______________________________ "
                       "\nPlease Enter: "
                       "\n'a' for right angle,"
                       "\n'b' for upside-down right angle or "
                       "\n'c' for a pyramid: "
                       "\n_______________________________ \n")

        # Check if the choice is valid
        if choice not in ('a', 'b', 'c'):
            print("Invalid choice. Please select 'a', 'b', or 'c.")
            continue

        # Prompt the user for the number of rows
        n = int(input("Enter the number of rows (min 5): "))

        # Check if the number of rows is at least 5
        if n < 5:
            print("Number of rows must be at least 5.")
            continue

        # Draw the selected figure based on the user's choice
        if choice == 'a':
            draw_right_angle(n)
        elif choice == 'b':
            draw_upside_down_right_angle(n)
        elif choice == 'c':
            draw_pyramid(n)

        # Ask the user if they want to draw another figure or exit
        another = input("Do you want to draw another figure? (y/n): ")
        if another.lower() != 'y':  # Use 'y' for yes
            print("_______________________________"
                  "\n Goodbye!"
                  "\n_______________________________")
            break  # Exit the loop if the user does not want to draw another figure

if __name__ == "__main__":
    main()
