work_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"];

work_days.sort();
print("Sorted work days:", work_days);

#Another way is to use the sorted() function, which returns a new sorted list without modifying the original list.
sorted_work_days = sorted(work_days);
print("Sorted work days (new list):", sorted_work_days);

#Another way is to use the sort() method with the reverse parameter set to True, which sorts the list in descending order.
work_days.sort(reverse=True);
print("Work days in descending order:", work_days);