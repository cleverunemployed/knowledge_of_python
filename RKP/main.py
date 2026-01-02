import datetime

print("Welcome to game!!!")

balance: int = 100

objects: dict = {
    1: "Бумага",
    2: "Камень",
    3: "Ножницы",
}

    
def custom_random(start: int = 1, end: int = 3) -> int:
    random_number: float = datetime.datetime.now().timestamp()
    return int((random_number % (end - start + 1)) + start)

while True:
    print(f"""
Выбери предмет:
 * Бумага {"(1)":>5}
 * Камень {"(2)":>5}
 * Ножницы {"(3)":>5}
          """)
    try: 
        object_player: int = int(input())
    except Exception as e:
        print(e)
        continue
    
    if not (1 <= object_player <= 3):
        print("Число от 1 до 3!")
        continue
    
    try:
        bet: int = int(input(f"Поставь ставку (баланс -> {balance}): "))
    
    except Exception as e:
        print(e)
        continue
    
    if not (1 <= bet <= balance):
        print("Недостаточный баланс или неправильная ставка")
        continue
    
    bet_bot: int = custom_random()
        
    if bet_bot == object_player:
        print("Ничья!")
        continue
    
    if  (bet_bot == 3 and object_player == 1) or\
        (bet_bot == 2 and object_player == 3) or\
        (bet_bot == 1 and object_player == 2):
        balance -= bet
        print(f"Поражение!\nБаланс: {balance}\nОбъект врага: {objects[bet_bot]}\nТвой объект: {objects[object_player]}")
        
    if  (bet_bot == 1 and object_playeret == 3) or\
        (bet_bot == 3 and object_player == 2) or\
        (bet_bot == 2 and object_player == 1):

        balance += bet
        print(f"Победа!\nБаланс: {balance}\nОбъект врага: {objects[bet_bot]}\nТвой объект: {objects[object_player]}")