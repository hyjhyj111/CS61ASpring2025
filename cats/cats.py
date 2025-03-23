"""Typing test implementation"""

from utils import (
    lower,
    split,
    remove_punctuation,
    lines_from_file,
    count,
    deep_convert_to_tuple,
)
from ucb import main, interact, trace
from datetime import datetime
import random


###########
# Phase 1 #
###########


def pick(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which the SELECT function returns True.
    If there are fewer than K such paragraphs, return an empty string.

    Arguments:
        paragraphs: a list of strings representing paragraphs
        select: a function that returns True for paragraphs that meet its criteria
        k: an integer

    >>> ps = ['hi', 'how are you', 'fine']
    >>> s = lambda p: len(p) <= 4
    >>> pick(ps, s, 0)
    'hi'
    >>> pick(ps, s, 1)
    'fine'
    >>> pick(ps, s, 2)
    ''
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    # END PROBLEM 1
    for x in paragraphs:
        if select(x):
            k -= 1
        if k < 0:
            return x
    return ''


def about(keywords):
    """Return a function that takes in a paragraph and returns whether
    that paragraph contains one of the words in keywords.

    Arguments:
        keywords: a list of keywords

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> pick(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> pick(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in keywords]), "keywords should be lowercase."

    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    # END PROBLEM 2
    def f(l):
        for std in keywords:
            for x in l.split(' '):
                if lower(std) == lower(remove_punctuation(x)):
                    return True
        return False
    return f


def accuracy(typed, source):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    compared to the corresponding words in SOURCE.

    Arguments:
        typed: a string that may contain typos
        source: a model string without errors

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    >>> accuracy('', '')
    100.0
    """
    typed_words = split(typed)
    source_words = split(source)
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    # END PROBLEM 3
    if len(typed_words) == 0 and len(source_words) == 0:
        return 100.0
    error = 0
    for i in range(len(typed_words)):
        if i >= len(source_words):
            error += 1
        else:
            error += 1 if typed_words[i] != source_words[i] else 0
    if len(typed_words) == 0:
        return 0.0
    return 100 - error / len(typed_words) * 100


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string.

    Arguments:
        typed: an entered string
        elapsed: an amount of time in seconds

    >>> wpm('hello friend hello buddy hello', 15)
    24.0
    >>> wpm('0123456789',60)
    2.0
    """
    assert elapsed > 0, "Elapsed time must be positive"
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    # END PROBLEM 4
    return len(typed) * 12 / elapsed

################
# Phase 4 (EC) #
################


def memo(f):
    """A general memoization decorator."""
    cache = {}

    def memoized(*args):
        immutable_args = deep_convert_to_tuple(args)  # convert *args into a tuple representation
        if immutable_args not in cache:
            result = f(*immutable_args)
            cache[immutable_args] = result
            return result
        return cache[immutable_args]

    return memoized


def memo_diff(diff_function):
    """A memoization function."""
    cache = {}

    def memoized(typed, source, limit):
        # BEGIN PROBLEM EC
        "*** YOUR CODE HERE ***"
        # END PROBLEM EC

    return memoized


###########
# Phase 2 #
###########


def autocorrect(typed_word, word_list, diff_function, limit):
    """Returns the element of WORD_LIST that has the smallest difference
    from TYPED_WORD based on DIFF_FUNCTION. If multiple words are tied for the smallest difference,
    return the one that appears closest to the front of WORD_LIST. If the
    lowest difference is greater than LIMIT, return TYPED_WORD instead.

    Arguments:
        typed_word: a string representing a word that may contain typos
        word_list: a list of strings representing source words
        diff_function: a function quantifying the difference between two words
        limit: a number

    >>> ten_diff = lambda w1, w2, limit: 10 # Always returns 10
    >>> autocorrect("hwllo", ["butter", "hello", "potato"], ten_diff, 20)
    'butter'
    >>> first_diff = lambda w1, w2, limit: (1 if w1[0] != w2[0] else 0) # Checks for matching first char
    >>> autocorrect("tosting", ["testing", "asking", "fasting"], first_diff, 10)
    'testing'
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    # END PROBLEM 5
    if typed_word in word_list:
        return typed_word
    ans = typed_word
    mi = limit
    ok = True
    for x in word_list:
        if diff_function(typed_word, x, limit) <= mi:
            if diff_function(typed_word, x, limit) < mi:
                ok = True
            if ok:
                ok = False
                ans = x
            mi = diff_function(typed_word, x, limit)
    return ans


def furry_fixes(typed, source, limit):
    """A diff function for autocorrect that determines how many letters
    in TYPED need to be substituted to create SOURCE, then adds the difference in
    their lengths to this value and returns the result.

    Arguments:
        typed: a starting word
        source: a string representing a desired goal word
        limit: a number representing an upper bound on the number of chars that must change

    >>> big_limit = 10
    >>> furry_fixes("nice", "rice", big_limit)    # Substitute: n -> r
    1
    >>> furry_fixes("range", "rungs", big_limit)  # Substitute: a -> u, e -> s
    2
    >>> furry_fixes("pill", "pillage", big_limit) # Don't substitute anything, length difference of 3.
    3
    >>> furry_fixes("roses", "arose", big_limit)  # Substitute: r -> a, o -> r, s -> o, e -> s, s -> e
    5
    >>> furry_fixes("rose", "hello", big_limit)   # Substitute: r->h, o->e, s->l, e->l, length difference of 1.
    5
    """
    # BEGIN PROBLEM 6
    cur = abs(len(typed) - len(source))
    if cur > limit:
        return limit + 1
    def f(ind, cur):
        if cur > limit:
            return cur
        if ind == min(len(typed), len(source)):
            return cur
        cur += int(typed[ind] != source[ind])
        return f(ind + 1, cur)
    return f(0, cur)
    

def minimum_mewtations(typed, source, limit):
    """A diff function for autocorrect that computes the edit distance from TYPED to SOURCE.
    This function takes in a string TYPED, a string SOURCE, and a number LIMIT.

    Arguments:
        typed: a starting word
        source: a string representing a desired goal word
        limit: a number representing an upper bound on the number of edits

    >>> big_limit = 10
    >>> minimum_mewtations("cats", "scat", big_limit)       # cats -> scats -> scat
    2
    >>> minimum_mewtations("purng", "purring", big_limit)   # purng -> purrng -> purring
    2
    >>> minimum_mewtations("ckiteus", "kittens", big_limit) # ckiteus -> kiteus -> kitteus -> kittens
    3
    """
    if limit < 0: # Base cases should go here, you may add more base cases as needed.
        # BEGIN
        "*** YOUR CODE HERE ***"
        # END
        return 1000
    if not typed:
        return len(source)
    if not source:
        return len(typed)

    # Recursive cases should go below here
    if typed[0] == source[0]: # Feel free to remove or add additional cases
        # BEGIN
        "*** YOUR CODE HERE ***"
        # END
        return minimum_mewtations(typed[1:], source[1:], limit)
    else:
        add = minimum_mewtations(typed, source[1:], limit - 1) # Fill in these lines
        remove = minimum_mewtations(typed[1:], source, limit - 1)
        substitute = minimum_mewtations(typed[1:], source[1:], limit - 1)
        # BEGIN
        "*** YOUR CODE HERE ***"
        return 1 + min(add, remove, substitute)
    

# Ignore the line below
minimum_mewtations = count(minimum_mewtations)


def final_diff(typed, source, limit):
    """A diff function that takes in a string TYPED, a string SOURCE, and a number LIMIT.
    If you implement this function, it will be used."""
    if limit < 0:
        return float('inf')  # 超过限制，返回无穷大
    if not typed:
        return len(source)   # typed 为空，返回 source 的长度
    if not source:
        return len(typed)    # source 为空，返回 typed 的长度

    # 忽略大小写比较
    if typed[0].lower() == source[0].lower():
        # 如果首字母大小写不同，增加 0.5 的权重
        case_cost = 0 if typed[0] == source[0] else 0.5
        return case_cost + final_diff(typed[1:], source[1:], limit - case_cost)

    # 处理相邻字母互换的情况
    if len(typed) >= 2 and len(source) >= 2 and typed[0].lower() == source[1].lower() and typed[1].lower() == source[0].lower():
        swap = final_diff(typed[2:], source[2:], limit - 1)
        return 1 + swap  # 相邻字母互换视为一次操作

    # 添加、删除、替换操作
    add = final_diff(typed, source[1:], limit - 1)
    remove = final_diff(typed[1:], source, limit - 1)
    substitute = final_diff(typed[1:], source[1:], limit - 1)

    # 键盘邻近字母替换的权重调整
    if typed and source and is_keyboard_neighbor(typed[0].lower(), source[0].lower()):
        substitute -= 0.5  # 键盘邻近字母替换的权重降低

    # 返回最小的编辑次数加 1
    return 1 + min(add, remove, substitute)


def is_keyboard_neighbor(c1, c2):
    """Check if two characters are neighbors on a QWERTY keyboard."""
    keyboard = [
        ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
        ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
        ['z', 'x', 'c', 'v', 'b', 'n', 'm']
    ]
    for row in keyboard:
        if c1 in row and c2 in row:
            idx1 = row.index(c1)
            idx2 = row.index(c2)
            return abs(idx1 - idx2) <= 1  # 相邻或相同
    return False

FINAL_DIFF_LIMIT = 6  # REPLACE THIS WITH YOUR LIMIT


###########
# Phase 3 #
###########


def report_progress(typed, source, user_id, upload):
    """Upload a report of your id and progress so far to the multiplayer server.
    Returns the progress so far.

    Arguments:
        typed: a list of the words typed so far
        source: a list of the words in the typing source
        user_id: a number representing the id of the current user
        upload: a function used to upload progress to the multiplayer server

    >>> print_progress = lambda d: print('ID:', d['id'], 'Progress:', d['progress'])
    >>> # The above function displays progress in the format ID: __, Progress: __
    >>> print_progress({'id': 1, 'progress': 0.6})
    ID: 1 Progress: 0.6
    >>> typed = ['how', 'are', 'you']
    >>> source = ['how', 'are', 'you', 'doing', 'today']
    >>> report_progress(typed, source, 2, print_progress)
    ID: 2 Progress: 0.6
    0.6
    >>> report_progress(['how', 'aree'], source, 3, print_progress)
    ID: 3 Progress: 0.2
    0.2
    """
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    # END PROBLEM 8
    for i in range(len(typed)):
        if typed[i] != source[i]:
            upload({'id': user_id, 'progress': i / len(source)})
            return i / len(source)
    upload({'id': user_id, 'progress': len(typed) / len(source)})
    return len(typed) / len(source)


def time_per_word(words, timestamps_per_player):
    """Return a dictionary {'words': words, 'times': times} where times
    is a list of lists that stores the durations it took each player to type
    each word in words.

    Arguments:
        words: a list of words, in the order they are typed.
        timestamps_per_player: A list of lists of timestamps including the time
                          each player started typing, followed by the time each
                          player finished typing each word.

    >>> p = [[75, 81, 84, 90, 92], [19, 29, 35, 36, 38]]
    >>> result = time_per_word(['collar', 'plush', 'blush', 'repute'], p)
    >>> result['words']
    ['collar', 'plush', 'blush', 'repute']
    >>> result['times']
    [[6, 3, 6, 2], [10, 6, 1, 2]]
    """
    tpp = timestamps_per_player  # A shorter name (for convenience)
    # BEGIN PROBLEM 9
    times = []  # You may remove this line
    for p in timestamps_per_player:
        t = []
        for i in range(1, len(p)):
            t.append(p[i] - p[i - 1])
        times.append(t)

    # END PROBLEM 9
    return {'words': words, 'times': times}


def fastest_words(words_and_times):
    """Return a list of lists indicating which words each player typed fastest.
    In case of a tie, the player with the lower index is considered to be the one who typed it the fastest.

    Arguments:
        words_and_times: a dictionary {'words': words, 'times': times} where
        words is a list of the words typed and times is a list of lists of times
        spent by each player typing each word.

    >>> p0 = [5, 1, 3]
    >>> p1 = [4, 1, 6]
    >>> fastest_words({'words': ['Just', 'have', 'fun'], 'times': [p0, p1]})
    [['have', 'fun'], ['Just']]
    >>> p0  # input lists should not be mutated
    [5, 1, 3]
    >>> p1
    [4, 1, 6]
    """
    check_words_and_times(words_and_times)  # verify that the input is properly formed
    words, times = words_and_times['words'], words_and_times['times']
    player_indices = (len(times))  # contains an *index* for each player
    word_indices = (len(words))    # contains an *index* for each word
    # BEGIN PROBLEM 10
    "*** YOUR CODE HERE ***"
    # END PROBLEM 10
    a = [[] for _ in range(player_indices)]
    for i in range(word_indices):
        ind = 0
        for j in range(1, player_indices):
            if times[j][i] < times[ind][i]:
                ind = j
        a[ind].append(words[i])
    return a


def check_words_and_times(words_and_times):
    """Check that words_and_times is a {'words': words, 'times': times} dictionary
    in which each element of times is a list of numbers the same length as words.
    """
    assert 'words' in words_and_times and 'times' in words_and_times and len(words_and_times) == 2
    words, times = words_and_times['words'], words_and_times['times']
    assert all([type(w) == str for w in words]), "words should be a list of strings"
    assert all([type(t) == list for t in times]), "times should be a list of lists"
    assert all([isinstance(i, (int, float)) for t in times for i in t]), "times lists should contain numbers"
    assert all([len(t) == len(words) for t in times]), "There should be one word per time."


def get_time(times, player_num, word_index):
    """Return the time it took player_num to type the word at word_index,
    given a list of lists of times returned by time_per_word."""
    num_players = len(times)
    num_words = len(times[0])
    assert word_index < len(times[0]), f"word_index {word_index} outside of 0 to {num_words-1}"
    assert player_num < len(times), f"player_num {player_num} outside of 0 to {num_players-1}"
    return times[player_num][word_index]


enable_multiplayer = False  # Change to True when you're ready to race.

##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file("data/sample_paragraphs.txt")
    random.shuffle(paragraphs)
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        source = pick(paragraphs, select, i)
        if not source:
            print("No more paragraphs about", topics, "are available.")
            return
        print("Type the following paragraph and then press enter/return.")
        print("If you only type part of it, you will be scored only on that part.\n")
        print(source)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print("Goodbye.")
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print("Words per minute:", wpm(typed, elapsed))
        print("Accuracy:        ", accuracy(typed, source))

        print("\nPress enter/return for the next paragraph or type q to quit.")
        if input().strip() == "q":
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse

    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument("topic", help="Topic word", nargs="*")
    parser.add_argument("-t", help="Run typing test", action="store_true")

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)
