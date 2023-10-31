import lab2
import statistics

def test_find_min_max():
    z =5,4,3,2,3
    print("find_min_max")
    minn = min(z)
    maxx = max(z)
    print("Minimum = " + str(minn))
    print("Maximum = " + str(maxx))
def test_calc_average():
    z = 5, 4, 3, 2, 3
    print("calc_average")
    print(sum(z)/len(z))
def test_calc_mediantemperature():
    z = 5, 4, 3, 2, 3
    print("calc_median_temperature")
    print("Median = " + str(statistics.median(z)))