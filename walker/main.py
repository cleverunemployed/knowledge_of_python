import datetime
import pprint

def custom_random(start: int = 0, end: int = 10) -> int:
    random_number: float = datetime.datetime.now().timestamp()
    return int((random_number % (end - start + 1)) + start)

def check_move(x: int, y: int, direction: "str") -> bool:
    match direction:
        case "l":
            return x > 0
        case "r":
            return x < 9
        case "f":
            return y > 0
        case "b":
            return y < 9
    

hero: dict = {
    "health": 10,
    "x": 0,
    "y": 0,
    "steps": 0,
    "have_key": False
}

fall_floors: list[list[int, int]] = []

exit_doors: list[int, int] = [custom_random(), custom_random()]
key_exit: list[int, int] = [custom_random(), custom_random()]

maps: list[list] = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]

print("Welcome to Hell Floor!")

while True:
    if hero["health"] <= 0:
        print("Game over")
        break
    
    print("Choose act:")
    print("""
 * left, rigth, forward, back (l, r, f, b)
 * check health (h)
 * check map (m)         
          """)
    act: str = input("Your act is: ")
    
    if act not in "lrfbmh":
        hero["health"] -= 1
        print("Health -1, don't stay!")
        continue
    
    match act:
        case "m":

            maps[hero["x"]][hero["y"]] = 1
            pprint.pprint(maps)
            maps[hero["x"]][hero["y"]] = 0
        case "h":
            print(f"Your health: {hero['health']}")
        case _:
            result = check_move(hero["x"], hero["y"], act)   
            if result:
                fall_floors.append([hero["x"], hero["y"]])
                hero["steps"] += 1
                if hero["steps"] % 3 == 0:
                    hero["health"] -= 1
                    print("Health -1, rapid!")
                match act:
                    case "l":
                        hero["x"] -= 1
                    case "r":
                        hero["x"] += 1
                    case "f":
                        hero["y"] -= 1
                    case "b":
                        hero["y"] += 1
            else:
                hero["health"] -= 1
                print("Health -1, wrong move!")
                continue
    
    if [hero["x"], hero["y"]] in fall_floors:
        hero["health"] -= 1
        print("Health -1, hell floor!")
        continue
    
    if key_exit == [hero["x"], hero["y"]]:
        print("You find Key!")
        hero["have_key"] = True
    
    if exit_doors == [hero["x"], hero["y"]]:
        print("You find exit's door")
        if hero["have_key"]:
            print("You win!!!")
            break
        else:
            print("Where is key?")
            
