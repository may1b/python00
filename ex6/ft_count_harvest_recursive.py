def hv_rec(day_rn: int, day_max: int):
    print(f"Day {day_rn}")
    if day_rn < day_max:
        hv_rec(day_rn + 1, day_max)


def ft_count_harvest_recursive():
    print("Days until harvest: ", end='')
    days = int(input())
    if days > 0:
        hv_rec(1, days)
    print("Harvest Time!")
