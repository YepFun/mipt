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
print_histogram_data(data_10, data_20, data_40, data_80)
