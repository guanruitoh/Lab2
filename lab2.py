# This is a sample Python script.
import statistics


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.





# Press the green button in the gutter to run the script.
def main():
    display_main_menu()
    num_list = get_user_input()
    avg = calc_average(num_list)
    print(avg)
    find_min_max(num_list)
    calc_median_temperature(num_list)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")


def display_main_menu():
    print("display_main_menu")
    print("Enter some numbers separated by commas (e.g. 5, 67,32)")
def calc_average(z):
    print("calc_average")
    return sum(z)/len(z)


def get_user_input():
    print("get_user_input")
    x = input()
    y = x.split(",")
    z = list(map(float, y))
    print(z)
    return z
def find_min_max(z):
    print("find_min_max")
    minn = min(z)
    maxx = max(z)
    print("Minimum = " + str(minn))
    print("Maximum = " + str(maxx))
def sort_temperature():
    print("sort_temperature")
def calc_median_temperature(z):
    print("calc_median_temperature")
    print("Median = " + str(statistics.median(z)))

if __name__ == '__main__':
    main()