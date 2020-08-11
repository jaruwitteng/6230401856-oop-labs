weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekend = ["Saturday", "Sunday"]
allday = weekday + weekend
sort_allday = sorted(allday)
print("Weekday are", weekday)
print("Weekend are", weekend)
print("Days are", allday)
print("Sorted days are", sort_allday)
allday.reverse()
print("Reversed days are", allday)
allday.reverse()
print("The last two days are", allday[-2], allday[-1])
