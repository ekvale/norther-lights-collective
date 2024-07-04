import matplotlib.pyplot as plt



""" 1. Soccer Game """

def soccer_game():
    explanation = "This is also sum of the consecutive numbers of Team A - 1 (1-11) -1 * the number of " \
                  "players on Team B"
    highfives_a = []
    highfives_b = []
    diff = []
    team_a = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]
    team_b = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]
    for x in range(len(team_a)):
        highfives_b.append(len(team_b))
        team_a.pop()
        highfives_a.append(len(team_a))

        diff.append(sum(highfives_b) - sum(highfives_a))
    print(sum(highfives_a + highfives_b), highfives_a, highfives_b, diff)
    # x axis values
    x = highfives_a
    # corresponding y axis values
    y = diff

    # plotting the points
    plt.polar(x, y)

    # naming the x axis
    plt.xlabel('Own Team High Fives')
    # naming the y axis
    plt.ylabel('Diff')

    # giving a title to my graph
    plt.title('High Fives!')

    # function to show the plot
    plt.show()

soccer_game()

"Soccer Game B"
def soccer_game_b(a, b):
    num_players_on_a = a
    num_players_on_b = b
    gaussing_sum = ((num_players_on_a -1)/2) * a
    total_high_fives = (num_players_on_a * num_players_on_b) + gaussing_sum
    return print(gaussing_sum, total_high_fives)


soccer_game_b(11, 11)

"""2 .Elevator"""


def elevator():
    explanation = """ The assumption seems to be that
     childern and adults are interchangable and only the ratio is important."""
    adult_capacity = 15
    child_capacity = 20
    num_child = 12
    temp_occupancy = (adult_capacity / child_capacity) * num_child
    room_for_adults = adult_capacity - temp_occupancy

    return print(f"Room for Adults: {(int(room_for_adults))}"
            f"\n{explanation}")

elevator()

"3. Theater Group"
def theater_group():
    total_group = 0
    women = 0
    men = 8
    while total_group < 44:
        women = women + 1
        men = men + 1
        total_group = (women + men)
        print(total_group, women, men)

print(theater_group())


"4. Ducks and Cows"
def ducks_and_cows():
    """ This is a weird way of doing it. Farmer keeps the leg/ratio as close to the
    given ratio as possible with every new animal that comes in."""
    cow = 4
    duck = 2
    heads = 12
    legs = 32
    animal_pen = [duck]

    while len(animal_pen) < 12:
        magic_ratio = legs/heads
        pen_switch = sum(animal_pen) / len(animal_pen)
        if pen_switch > legs/heads:
            print(f'Magic Ratio: {magic_ratio}  Pen Switch: {pen_switch}')
            animal_pen.append(duck)
        else:
            animal_pen.append(cow)

    return(animal_pen, animal_pen.count(cow), animal_pen.count(duck), len(animal_pen))

print(ducks_and_cows())


"5. Strange Number"

def strange_number(magic_num):
    strange_numbers = []
    for x in range(10, 99):
       y = int(str(x)[::-1])
       if x + y == magic_num:
           strange_numbers.append([x, y])

    x, y = zip(*strange_numbers)
    plt.polar(x, y)
    plt.show()

    def first_num_of_each_sub_list(strange_numbers):
        return [n[0] for n in strange_numbers]

    print(first_num_of_each_sub_list(strange_numbers))
    just_first = first_num_of_each_sub_list(strange_numbers)
    for x in just_first:
        y = 0
        print(just_first[y + 1] - x)
        y += 1

    return strange_numbers


print(strange_number(121))