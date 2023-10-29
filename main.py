def draw_right_angle(n):
    for i in range(1, n + 1):
        print("*" * i)

def draw_upside_down_right_angle(n):
    for i in range(n, 0, -1):
        print("*" * i)

def draw_pyramid(n):
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        if i == 1:
            print(spaces + "*")
        else:
            print(spaces + "*" + " " * (2 * i - 3) + "*")

def main():
    choice = input("Enter 'a' for right angle, 'b' for upside-down right angle, or 'c' for a pyramid: ")

    if choice not in ('a', 'b', 'c'):
        print("Invalid choice. Please select 'a', 'b', or 'c.")
        return

    n = int(input("Enter the number of rows (min 5): "))

    if n < 5:
        print("Number of rows must be at least 5.")
        return

    if choice == 'a':
        draw_right_angle(n)
    elif choice == 'b':
        draw_upside_down_right_angle(n)
    elif choice == 'c':
        draw_pyramid(n)

if __name__ == "__main__":
    main()
