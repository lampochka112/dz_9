n = int(input("введите количество секунд:"))
hours = n // 3600
minutes = (n - hours * 3600) // 60
second = (n - ((hours * 3600) + (minutes * 60)))
print(hours, minutes seconds)  