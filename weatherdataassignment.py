#DAA Assignment By Vasu Sehgal 46
# WeatherData = [[Serial no. , Name, TimeStamp, Temp, Rainfall, Humidity]]
WeatherData = [[40, 'Bengalore', '00:00', 18, 20, 31],
               [39, 'Mumbai', '00:10', 20, 50, 65],
               [35, 'Bengalore', '00:20', 19, 20, 21],
               [24, 'Pune', '01:41', 22, 23, 30],
               [32, 'Pune', '01:41', 22, 23, 30],
               [38, 'Pune', '02:00', 21, 30, 45],
               [2, 'Delhi', '02:30', 27, 56, 20],
               [20, 'Mumbai', '03:00', 19, 32, 40],
               [28, 'Bengalore', '03:10', 19, 20, 21],
               [16, 'Bengalore', '03:32', 26, 22, 15],
               [23, 'Kolkata', '08:09', 27, 55, 25],
               [10, 'Mumbai', '09:00', 21, 29, 35],
               [14, 'Delhi', '09:09', 32, 21, 30],
               [5, 'Mumbai', '10:05', 23, 30, 35],
               [4, 'Bengalore', '10:10', 21, 36, 30],
               [31, 'Kolkata', '10:10', 26, 50, 70],
               [19, 'Kolkata', '10:39', 28, 25, 30],
               [27, 'Kolkata', '11:00', 28, 27, 36],
               [18, 'Delhi', '11:11', 29, 24, 25],
               [9, 'Delhi', '11:16', 31, 44, 30],
               [1, 'Kolkata', '12:10', 27, 87, 15],
               [37, 'Kolkata', '12:10', 32, 40, 60],
               [26, 'Delhi', '12:11', 30, 23, 20],
               [33, 'Delhi', '12:11', 30, 23, 20],
               [17, 'Pune', '12:19', 25, 23, 20],
               [15, 'Mumbai', '12:30', 26, 22, 30],
               [45, 'Pune', '12:45', 21, 45, 55],
               [34, 'Mumbai', '13:00', 25, 31, 31],
               [29, 'Pune', '13:30', 31, 55, 44],
               [3, 'Pune', '13:45', 22, 34, 25],
               [25, 'Mumbai', '13:45', 29, 20, 25],
               [6, 'Kolkata', '14:10', 29, 41, 15],
               [36, 'Delhi', '14:30', 32, 50, 40],
               [7, 'Bengalore', '15:33', 25, 51, 20],
               [46, 'Kolkata', '15:50', 30, 90, 95],
               [48, 'Pune', '17:00', 25, 25, 21],
               [8, 'Pune', '17:13', 28, 32, 25],
               [11, 'Bengalore', '18:10', 28, 81, 15],
               [13, 'Pune', '18:29', 29, 20, 25],
               [30, 'Mumbai', '19:35', 21, 40, 50],
               [42, 'Kolkata', '21:00', 26, 28, 38],
               [21, 'Bengalore', '21:10', 23, 33, 15],
               [50, 'Mumbai', '22:00', 21, 50, 55],
               [22, 'Delhi', '22:10', 26, 66, 20],
               [44, 'Mumbai', '23:05', 21, 32, 38],
               [43, 'Bengalore', '23:10', 20, 28, 21],
               [12, 'Kolkata', '23:11', 31, 91, 20],
               [41, 'Delhi', '23:25', 27, 22, 11],
               [49, 'Bengalore', '23:30', 20, 32, 31],
               [47, 'Delhi', '23:59', 22, 80, 96]]

def InsertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i][1]
        j = i-1
        keyPosition = arr[i]
        while (j >= 0) and (arr[j][1] > key):
            arr[j+1] = arr[j]
            j = j-1

        arr[j+1] = keyPosition


InsertionSort(WeatherData)
print("Sorted data in ascending order with respect to Cities:")
for data in range(0, len(WeatherData)):
    print(WeatherData[data])