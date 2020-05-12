class Player:
    def __init__(self, first_name, last_name, height, weight):
        self.first_name = first_name
        self.last_name = last_name
        self.height = height
        self.weight = weight


class FootballPlayer(Player):
    def __init__(self, first_name, last_name, height, weight,  goals, yellow_cards, red_cards):
        super().__init__(first_name=first_name, last_name=last_name, height=height, weight=weight )
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards


class BasketballPlayer(Player):
    def __init__(self, first_name, last_name, height, weight, points, rebounds, assists):
        super().__init__(first_name=first_name, last_name=last_name, height=height, weight=weight)
        self.points = points
        self.rebounds = rebounds
        self.assists = assists


choice = input("Enter a new player's data. Enter A for football player or B for basketball player: ").upper()
f_name = input("Enter player's first name: ")
l_name = input("Enter player's last name: ")
height_cm = input("Enter player's height(cm): ")
weight_kg = input("Enter player's weight(kg): ")

if choice == "A":
    goals = input("Enter the number of player's goals: ")
    red_cards = input("Enter the number of player's red cards: ")
    yellow_cards = input("Enter the number of player's yellow cards: ")

    new_player = FootballPlayer(first_name=f_name, last_name=l_name, height=height_cm, weight=weight_kg, goals=goals,
                                red_cards=red_cards, yellow_cards=yellow_cards)

    with open("new_footbal_player.txt", "w") as info_file:
        info_file.write(str(new_player.__dict__))

if choice == "B":
    points = input("Enter the number of player's points: ")
    rebounds = input("Enter the number of player's rebounds: ")
    assists = input("Enter the number of player's assists: ")

    new_player = BasketballPlayer(first_name=f_name, last_name=l_name, height=height_cm, weight=weight_kg, points=points,
                                  rebounds=rebounds, assists=assists)

    with open("new_basketball_player.txt", "w") as info_file:
        info_file.write(str(new_player.__dict__))