def better_than_average(class_points, your_points):
    total = 0

    for nota in class_points:
        total += nota

    media = total / len(class_points)

    return your_points > media
