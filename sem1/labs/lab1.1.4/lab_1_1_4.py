import math

def group_data(data):
    data_10 = [0] * 400
    i = 0
    while i < 400:
        for j in range(10):
            data_10[i] += int(data[i * 10 + j])
        i += 1

    data_20 = [0] * 200
    i = 0
    while i < 200:
        for j in range(20):
            data_20[i] += int(data[i * 20 + j])
        i += 1

    data_40 = [0] * 100
    i = 0
    while i < 100:
        for j in range(40):
            data_40[i] += int(data[i * 40 + j])
        i += 1

    data_80 = [0] * 50
    i = 0
    while i < 50:
        for j in range(80):
            data_80[i] += int(data[i * 80 + j])
        i += 1

    return data_10, data_20, data_40, data_80

def print_tables(data_10, data_20, data_40, data_80):
    print("\ndata_10:")
    i, j = 0, 0
    while i < 400:
        while j < 20:
            for k in range(20):
                print(data_10[i], end=" ")
                i += 1
            print("")
            j += 1

    print("\ndata_20:")
    i, j = 0, 0
    while i < 200:
        while j < 20:
            for k in range(10):
                print(data_20[i], end=" ")
                i += 1
            print("")
            j += 1

    print("\ndata_40:")
    i, j = 0, 0
    while i < 100:
        while j < 10:
            for k in range(10):
                print(data_40[i], end=" ")
                i += 1
            print("")
            j += 1

    print("\ndata_80:")
    i, j = 0, 0
    while i < 5:
        while j < 10:
            for k in range(5):
                print(data_80[i], end=" ")
                i += 1
            print("")
            j += 1

def print_histogram_data(data_10, data_20, data_40, data_80):
    print("\nHistogram Data")
    print("\ndata_10:")
    for i in range(18):
        print(i, data_10.count(i), data_10.count(i) / 400)

    print("\ndata_20:")
    for i in range(7, 34):
        print(i, data_20.count(i), data_20.count(i) / 200)

    print("\ndata_40:")
    for i in range(20, 52):
        print(i, data_40.count(i), data_40.count(i) / 100)

    print("\ndata_80:")
    for i in range(55, 96):
        print(i, data_80.count(i), data_80.count(i) / 50)


with open('lab_data_bare.txt') as f:
    data = f.readlines()

data_10, data_20, data_40, data_80 = group_data(data)

#print_tables(data_10, data_20, data_40, data_80)
#print_histogram_data(data_10, data_20, data_40, data_80)

sum_10, sum_20, sum_40, sum_80 = 0, 0, 0, 0
sq_sum_10, sq_sum_20, sq_sum_40, sq_sum_80 = 0, 0, 0, 0
for i in range(len(data_10)):
    sum_10 += data_10[i]
for i in range(len(data_20)):
    sum_20 += data_20[i]
for i in range(len(data_40)):
    sum_40 += data_40[i]
for i in range(len(data_80)):
    sum_80 += data_80[i]
print("sum:", sum_10, sum_20, sum_40, sum_80)
average_10, average_20, average_40, average_80 = sum_10/400, sum_20/200, sum_40/100, sum_80/50
print("average:", average_10, average_20, average_40, average_80)

for i in range(len(data_10)):
    sq_sum_10 += (data_10[i] - average_10) ** 2
for i in range(len(data_20)):
    sq_sum_20 += (data_20[i] - average_20) ** 2
for i in range(len(data_40)):
    sq_sum_40 += (data_40[i] - average_40) ** 2
for i in range(len(data_80)):
    sq_sum_80 += (data_80[i] - average_80) ** 2

sq_sigma_10, sq_sigma_20, sq_sigma_40, sq_sigma_80 = sq_sum_10/400, sq_sum_20/200, sq_sum_40/100, sq_sum_80/50
sigma_10, sigma_20, sigma_40, sigma_80 = math.sqrt(sq_sigma_10), math.sqrt(sq_sigma_20), math.sqrt(sq_sigma_40), math.sqrt(sq_sigma_80)
print("sq_sum:", sq_sum_10, sq_sum_20, sq_sum_40, sq_sum_80)
print("sq_sigma:", sq_sigma_10, sq_sigma_20, sq_sigma_40, sq_sigma_80)
print("sigma:", sigma_10, sigma_20, sigma_40, sigma_80)
print("2 * sigma:", 2 * sigma_10, 2 * sigma_20, 2 * sigma_40, 2 * sigma_80)

print("sqrt_average:", math.sqrt(average_10), math.sqrt(average_20), math.sqrt(average_40), math.sqrt(average_80))
print("")

count_s_10, count_s_20, count_s_40, count_s_80 = 0, 0, 0, 0
count_2s_10, count_2s_20, count_2s_40, count_2s_80 = 0, 0, 0, 0
for i in range(len(data_10)):
    if abs(data_10[i] - average_10) <= sigma_10:
        count_s_10 += 1
    if abs(data_10[i] - average_10) <= 2 * sigma_10:
        count_2s_10 += 1
for i in range(len(data_20)):
    if abs(data_20[i] - average_20) <= sigma_20:
        count_s_20 += 1
    if abs(data_20[i] - average_20) <= 2 * sigma_20:
        count_2s_20 += 1
for i in range(len(data_40)):
    if abs(data_40[i] - average_40) <= sigma_40:
        count_s_40 += 1
    if abs(data_40[i] - average_40) <= 2 * sigma_40:
        count_2s_40 += 1
for i in range(len(data_80)):
    if abs(data_80[i] - average_80) <= sigma_80:
        count_s_80 += 1
    if abs(data_80[i] - average_80) <= 2 * sigma_80:
        count_2s_80 += 1

print("count_s:", count_s_10, count_s_20, count_s_40, count_s_80)
print(count_s_10/400, count_s_20/200, count_s_40/100, count_s_80/50)
print("count_2s:", count_2s_10, count_2s_20, count_2s_40, count_2s_80)
print(count_2s_10/400, count_2s_20/200, count_2s_40/100, count_2s_80/50)

sigma_st_10, sigma_st_20, sigma_st_40, sigma_st_80 = sigma_10/math.sqrt(400), sigma_20/math.sqrt(200), sigma_40/math.sqrt(100), sigma_80/math.sqrt(50)
print("sigma_st:", sigma_st_10, sigma_st_20, sigma_st_40, sigma_st_80)

print("e:", sigma_st_10/average_10, sigma_st_20/average_20, sigma_st_40/average_40, sigma_st_80/average_80)