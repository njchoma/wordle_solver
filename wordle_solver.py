from tqdm import tqdm
import numpy as np
from math import log2

import utils

# GET ENTROPY
def print_word_entropy(W, S, num_print):
    entropies = []
    # print("WARNING: reducing number guess words")
    # W = W[:12000]
    for i, w in enumerate(tqdm(W)):
        entropies.append(get_entropy(w, S))
    entropies = np.array(entropies)
    sorted_entropy = np.argsort(entropies)

    topk_H = entropies[sorted_entropy[-num_print:]][::-1]
    topk_w = np.asarray(W)[sorted_entropy[-num_print:]][::-1]
    for i in range(num_print):
        w = topk_w[i]
        w = w.upper() if w in S else w
        print("{:2d}:  {:5s} {:4.2f}".format(i+1, w, topk_H[i]))

def get_entropy(w, S):
    num_solutions = len(S)
    configs = [0] * 3**len(w)
    for s in S:
        c = get_configuration(w, s)
        config_number = convert_config_to_int(c)
        configs[config_number] += 1
    probs = [c for c in configs if c != 0]
    probs = [p * 1.0 / num_solutions for p in probs]
    entropy = -1 * sum([p * log2(p) for p in probs])
    return entropy


def get_configuration(w, s):
    letters = set(s)
    config = [int(cw==cs) for cw, cs in zip(w, s)]
    for i, c in enumerate(w):
        if c in letters:
            config[i] += 1
    return config
        
def convert_config_to_int(config):
    config_number = 0
    config.reverse()
    for i, e in enumerate(config):
        config_number += 3**i * e
    return config_number


# ELIMINATE SOLUTIONS
def eliminate_solutions(S, guess, result):
    result = [int(r) for r in result]
    reduced_S = []
    for s in S:
        config = get_configuration(guess, s)
        if config == result:
            reduced_S.append(s)
    print("\n{} contained {:4.2f} bits".format(guess, log2(1.0*len(S)/len(reduced_S)) ))
    print("Reduced {:4.2f} bits to {:4.2f}".format(log2(len(S)), log2(len(reduced_S)) ))
    print("Reduced {} solutions to {}\n".format(len(S), len(reduced_S) ))
    if len(reduced_S) < 10:
        print("POSSIBLE SOLUTIONS:")
        print(reduced_S)
    return reduced_S


# MAIN SOLVER
def solve_wordle(W, S, print_no_info=False):
    step = 0
    if print_no_info:
        print_word_entropy(W, S, num_print=30)
    else:
        print("Not printing with no info. Use raise as first guess")
    while len(S) > 1:
        guess = input("\nEnter guessed word: ")
        result = input("Enter result (0=none, 1=letter found, 2=correct letter): ")
        S = eliminate_solutions(S, guess, result)
        print("Next best guesses:")
        print_word_entropy(W, S, num_print=30)
        step += 1
        if len(S) <= 2:
            break
        if step > 6:
            print("Time's up")
            break


if __name__ == "__main__":
    W = utils.load_word_list("lists/words_wordle.txt")
    S = utils.load_word_list("lists/words_wordle_solutions.txt")

    solve_wordle(W, S, False)

