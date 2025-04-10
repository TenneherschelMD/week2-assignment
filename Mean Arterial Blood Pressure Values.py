my_mean_arterial_pressure_list = []

my_mean_arterial_pressure_list.append(67)
my_mean_arterial_pressure_list.append(50)
my_mean_arterial_pressure_list.append(29)
my_mean_arterial_pressure_list.append(96)
my_mean_arterial_pressure_list.append(45)
my_mean_arterial_pressure_list.append(100)
my_mean_arterial_pressure_list.append(101)
my_mean_arterial_pressure_list.append(10)
my_mean_arterial_pressure_list.append(160)
my_mean_arterial_pressure_list.append(70)
my_mean_arterial_pressure_list.append(77)
my_mean_arterial_pressure_list.append(99)
my_mean_arterial_pressure_list.append(30)
my_mean_arterial_pressure_list.append(41)
my_mean_arterial_pressure_list.append(59)

my_mean_arterial_pressure_list.insert(2,67)
my_mean_arterial_pressure_list.insert(9,67)
my_mean_arterial_pressure_list.insert(7,91)
my_mean_arterial_pressure_list.insert(5,66)
my_mean_arterial_pressure_list.insert(0,7)

my_mean_arterial_pressure_list.extend([36, 49, 72, 90, 38, 24, 10, 29, 100])

my_mean_arterial_pressure_list.pop()

my_mean_arterial_pressure_list.sort()

index_70 = my_mean_arterial_pressure_list.index(70)
print("index of 70:", index_70)

index_45 = my_mean_arterial_pressure_list.index(45)
print("index of 45:", index_45)

index_160 = my_mean_arterial_pressure_list.index(160)
print("index of 160:", index_160)

print(my_mean_arterial_pressure_list)