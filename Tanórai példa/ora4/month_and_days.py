days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month = ['január', 'február', 'március', 'április', 'május', 'június', 'július',
         'augusztus', 'szeptember', 'október', 'november', 'december']
month_and_days = []
for i in range(len(month)):
    month_and_days.append(month[i])
    month_and_days.append(days_in_month[i])
print(month_and_days)
