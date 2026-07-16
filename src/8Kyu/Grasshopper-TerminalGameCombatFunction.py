def combat(health, damage):
    health -= damage
    if health < 0:
        health = 0
    return health