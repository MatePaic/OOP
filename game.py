import random
import json
import datetime

def get_score_list():
    with open("score_list.txt", "r") as score_file:
        score_list = json.loads(score_file.read())
        return score_list


class Result:
    def __init__(self, score, player_name, date):
        self.score = score
        self.player_name = player_name
        self.date = date

def play_game(level='easy'):
    player = input('Hi, what is your name? ')
    secret = random.randint(1, 30)
    attempts = 0
    wrong_attempts = []
    score_list = get_score_list()

    while True:
        guess = int(input("Guess the secret number (between 1 and 30): "))
        attempts += 1

        if guess == secret:
            new_result_object = Result(score=int(attempts), player_name=player, date=str(datetime.datetime.now()))
            score_list.append(new_result_object.__dict__)

            with open("score_list.txt", "w") as score_file:
                score_file.write(json.dumps(score_list))

                print("You've guessed it - congratulations! It's number " + str(secret))
                print("Attempts needed: " + str(attempts))
                break
        elif guess > secret and level == 'easy':
            print("Your guess is not correct... try something smaller")
        elif guess < secret and level == 'easy':
            print("Your guess is not correct... try something bigger")
        wrong_attempts.append(guess)

def get_top_scores():
    score_list = get_score_list()
    top_score_list = sorted(score_list, key=lambda k: k['score'])[:3]
    return top_score_list


def main():
    while True:
        selection = input("Would you like to A) play a new game, B) see the best scores, or C) quit? ")

        if selection.upper() == "A":
            level = input('Choose your level (easy/hard): ')
            play_game(level = level)
        elif selection.upper() == "B":
            for score_dict in get_top_scores():
                text = "Player {0} had {1} attempts on {2}.".format(score_dict.get("player_name"),
                                                             str(score_dict.get("score")),
                                                             score_dict.get("date"))
                print(text)
        else:
            break
if __name__ == "__main__":
    main()




