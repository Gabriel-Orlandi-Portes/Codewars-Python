def duty_free(price, discount, holiday_cost):
    economia = (price * discount) / 100
    quantidade = holiday_cost // economia

    return int(quantidade)