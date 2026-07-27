numbers = [1, 54, 76, 12, 111, 23, 45, 67, 89, 90, 34, 56, 78, 100, 200, 300, 400, 500, -1, -122, 5, -30];

numbers.sort(key=int);
print(f"Sorted numbers: {numbers}");


def avg(data):
    avg = sum(data) / len(data);
    print(data, f"Average: {avg}");
    return avg;

data = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [5, 5, 5], [3, 4, 5], [3, -3, 0], [1, 10, 1, 20], [1, 1, 1, 79]];

print(sorted(data, key=avg)); 

print(dir());