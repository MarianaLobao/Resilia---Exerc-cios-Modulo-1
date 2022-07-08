def combat(health, damage):
    return( (health - damage) ,result)

health = int(input("enter a number for your health:"))
damage = int(input("enter a number for your damage: "))
result = health - damage

print ((health , damage), result )
