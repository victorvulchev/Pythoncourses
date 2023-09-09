liters = int(input())
filled_times = liters // 5

if liters % 5 == 0:
    print(f"the buckets are filled {filled_times} times")
else:
    print(f"the buckets are filled {filled_times} times and a bit of the 2 liter bucket.")
