def human_years_cat_years_dog_years(human_years):
    if human_years == 1:
        catyears = 15
        dogyears = 15
    elif human_years == 2:
        catyears = 15 + 9
        dogyears = 15 + 9
    else:
        catyears = 15 + 9 + (4 * (human_years - 2))
        dogyears = 15 + 9 + (5 * (human_years - 2))

    return [human_years, catyears, dogyears]