import random
import math

def generate_thue_morse(seq_length: int):
    """Thue–Morse sequence.
    Code from wikipedia: https://en.wikipedia.org/wiki/Thue%E2%80%93Morse_sequence"""
    value = 1
    for n in range(seq_length):
        # Note: assumes that (-1).bit_length() gives 1
        x = (n ^ (n - 1)).bit_length() + 1
        if x & 1 == 0:
            # Bit index is even, so toggle value
            value = 1 - value
        yield not value

def roll():
    return random.randint(1, 6)

def basic_alternation(turn):
    return turn % 2 == 1 

def snake_draft(turn):
    if turn == 1:
        return True
    else:
        return basic_alternation(1 + math.floor(turn / 2))
    
def thue_morse(turn):
    *_, last = generate_thue_morse(turn)
    return last

def simulate(turn_function):
    "Returns TRUE if A wins a simulated game, governed by the provided turn function"
    turn = 1
    while True:
        result = roll()
        if result == 5:
            return turn_function(turn)
        turn += 1

def summarize(simulation, label):
    print(f'Simulated results of {label} turn order')
    print(f'A won {sum(simulation)} out of {len(simulation)} simulated games, a {100 * sum(simulation) / len(simulation):.3f}% win rate')

def analyze_thue_morse_to_limit(limit):
    sequence = generate_thue_morse(limit)
    misses_required = 0
    prob_a_wins = 0
    for turn in sequence:
        prob_here = (5/6)**misses_required
        misses_required += 1
        if turn == 0:
            continue
        prob_a_wins += (1/6) * prob_here

    print(f'A wins {100 * prob_a_wins:.3f}% of the time, with {100*(5/6)**limit:.3f}% unaccounted for')


if __name__ == '__main__':
    
    print('\n')
    print('Running basic simulation...')
    basic_simulation = [simulate(basic_alternation) for i in range(1000000)]
    summarize(basic_simulation, 'basic alternating (ABABAB...)')

    print('\n')
    print('Running snake simulation...')
    snake_simulation = [simulate(snake_draft) for i in range(1000000)]
    summarize(snake_simulation, 'snake draft (ABBAABBAA...)')
    
    print('\n')
    print('Running thue_morse simulation...')
    thue_morse_simulation = [simulate(thue_morse) for i in range(1000000)]
    summarize(thue_morse_simulation, 'thue_morse (ABBABAABBAABABBA...)')

    
    print('\n')
    print('Computing theoretical finite thue morse...')
    analyze_thue_morse_to_limit(500)


