def number(bus_stops):
    dentro = 0

    for i in bus_stops:
        dentro += i[0]
        dentro -= i[1]

    return dentro