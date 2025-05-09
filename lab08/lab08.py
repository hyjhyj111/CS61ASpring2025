def add_d_leaves(t, v):
    """Add d leaves containing v to each node at every depth d.

    >>> t_one_to_four = Tree(1, [Tree(2), Tree(3, [Tree(4)])])
    >>> print(t_one_to_four)
    1
      2
      3
        4
    >>> add_d_leaves(t_one_to_four, 5)
    >>> print(t_one_to_four)
    1
      2
        5
      3
        4
          5
          5
        5

    >>> t0 = Tree(9)
    >>> add_d_leaves(t0, 4)
    >>> t0
    Tree(9)
    >>> t1 = Tree(1, [Tree(3)])
    >>> add_d_leaves(t1, 4)
    >>> t1
    Tree(1, [Tree(3, [Tree(4)])])
    >>> t2 = Tree(2, [Tree(5), Tree(6)])
    >>> t3 = Tree(3, [t1, Tree(0), t2])
    >>> print(t3)
    3
      1
        3
          4
      0
      2
        5
        6
    >>> add_d_leaves(t3, 10)
    >>> print(t3)
    3
      1
        3
          4
            10
            10
            10
          10
          10
        10
      0
        10
      2
        5
          10
          10
        6
          10
          10
        10
    """
    "*** YOUR CODE HERE ***"


def has_path(t, target):
    """Return whether there is a path in a Tree where the entries along the path
    spell out a particular target.

    >>> greetings = Tree('h', [Tree('i'),
    ...                        Tree('e', [Tree('l', [Tree('l', [Tree('o')])]),
    ...                                   Tree('y')])])
    >>> print(greetings)
    h
      i
      e
        l
          l
            o
        y
    >>> has_path(greetings, 'h')
    True
    >>> has_path(greetings, 'i')
    False
    >>> has_path(greetings, 'hi')
    True
    >>> has_path(greetings, 'hello')
    True
    >>> has_path(greetings, 'hey')
    True
    >>> has_path(greetings, 'bye')
    False
    >>> has_path(greetings, 'hint')
    False
    """
    assert len(target) > 0, 'no path for empty target.'
    "*** YOUR CODE HERE ***"


def level_mutation_link(t, funcs):
	"""Mutates t using the functions in the linked list funcs.

	>>> t = Tree(1, [Tree(2, [Tree(3)])])
	>>> funcs = Link(lambda x: x + 1, Link(lambda y: y * 5, Link(lambda z: z ** 2)))
	>>> level_mutation_link(t, funcs)
	>>> t    # At level 0, apply x + 1; at level 1, apply y * 5; at level 2 (leaf), apply z ** 2
	Tree(2, [Tree(10, [Tree(9)])])
	>>> t2 = Tree(1, [Tree(2), Tree(3, [Tree(4)])])
	>>> level_mutation_link(t2, funcs)
	>>> t2    # Level 0: 1+1=2; Level 1: 2*5=10 => 10**2 = 100, 3*5=15; Level 2 (leaf): 4**2=16
	Tree(2, [Tree(100), Tree(15, [Tree(16)])])
	>>> t3 = Tree(1, [Tree(2)])
	>>> level_mutation_link(t3, funcs)
	>>> t3    # Level 0: 1+1=2; Level 1: 2*5=10; no further levels, so apply remaining z ** 2: 10**2=100
	Tree(2, [Tree(100)])
	"""
	if _____________________:
		return
	t.label = _____________________
	remaining = _____________________
	if __________________ and __________________:
		while _____________________:
			_____________________
			remaining = remaining.rest
	for b in t.branches:
		_____________________


def merge_numbers(n1, n2):
    """Merges two numbers that have decreasing digits.

    >>> merge_numbers(31, 42)
    4321
    >>> merge_numbers(21, 0)
    21
    >>> merge_numbers(21, 31)
    3211
    """
    "*** YOUR CODE HERE ***"


def insert_into_all(item, nested_list):
    """Return a new list consisting of all the lists in nested_list,
    but with item added to the front of each. You can assume that
    nested_list is a list of lists.

    >>> nl = [[], [1, 2], [3]]
    >>> insert_into_all(0, nl)
    [[0], [0, 1, 2], [0, 3]]
    """
    "*** YOUR CODE HERE ***"

def subseqs(s):
    """Return a nested list (a list of lists) of all subsequences of S.
    The subsequences can appear in any order. You can assume S is a list.

    >>> seqs = subseqs([1, 2, 3])
    >>> sorted(seqs)
    [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    >>> subseqs([])
    [[]]
    """
    if ________________:
        ________________
    else:
        ________________
        ________________


def non_decrease_subseqs(s):
    """Return a nested list of all subsequences of S (a list of lists) 
    for which the elements of the subsequence are nondecreasing. The 
    subsequences can appear in any order. You can assume S is a list.

    >>> seqs = non_decrease_subseqs([1, 3, 2])
    >>> sorted(seqs)
    [[], [1], [1, 2], [1, 3], [2], [3]]
    >>> non_decrease_subseqs([])
    [[]]
    >>> seqs2 = non_decrease_subseqs([1, 1, 2])
    >>> sorted(seqs2)
    [[], [1], [1], [1, 1], [1, 1, 2], [1, 2], [1, 2], [2]]
    """
    def subseq_helper(s, prev):
        if not s:
            return ____________________
        elif s[0] < prev:
            return ____________________
        else:
            a = ______________________
            b = ______________________
            return insert_into_all(________, ______________) + ________________
    return subseq_helper(____, ____)


def perms(seq):
    """Generates all permutations of the given sequence. Each permutation is a
    list of the elements in SEQ in a different order. The permutations may be
    yielded in any order.

    >>> p = perms([100])
    >>> type(p)
    <class 'generator'>
    >>> next(p)
    [100]
    >>> try: # Prints "No more permutations!" if calling next would cause an error
    ...     next(p)
    ... except StopIteration:
    ...     print('No more permutations!')
    No more permutations!
    >>> sorted(perms([1, 2, 3])) # Returns a sorted list containing elements of the generator
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    >>> sorted(perms((10, 20, 30)))
    [[10, 20, 30], [10, 30, 20], [20, 10, 30], [20, 30, 10], [30, 10, 20], [30, 20, 10]]
    >>> sorted(perms("ab"))
    [['a', 'b'], ['b', 'a']]
    """
    "*** YOUR CODE HERE ***"


def shuffle_pairs(lst):
    """Swap adjacent pairs of elements in place.

    >>> nums = list(range(6))
    >>> shuffle_pairs(nums)
    >>> nums
    [1, 0, 3, 2, 5, 4]
    >>> letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    >>> shuffle_pairs(letters)
    >>> letters
    ['b', 'a', 'd', 'c', 'f', 'e', 'h', 'g']
    >>> multiples = [10, 20, 30, 40]
    >>> shuffle_pairs(multiples)
    >>> multiples
    [20, 10, 40, 30]
    >>> pair = [1, 2]
    >>> shuffle_pairs(pair)
    >>> pair
    [2, 1]
    >>> empty = []
    >>> shuffle_pairs(empty)
    >>> empty
    []
    """
    assert len(lst) % 2 == 0, 'len(lst) must be even'
    half = ________________
    for ____ in ____:
        _____, _____ = _____, _____


def common_players(roster):
    """Returns a dictionary containing values along with a corresponding
    list of keys that had that value from the original dictionary.
    >>> full_roster = {
    ...     "bob": "Team A",
    ...     "barnum": "Team B",
    ...     "beatrice": "Team C",
    ...     "bernice": "Team B",
    ...     "ben": "Team D",
    ...     "belle": "Team A",
    ...     "bill": "Team B",
    ...     "bernie": "Team B",
    ...     "baxter": "Team A"
    ... }
    >>> player_dict = common_players(full_roster)
    >>> type(player_dict) == dict
    True
    >>> for key, val in sorted(player_dict.items()):
    ...     print(key, list(sorted(val)))
    Team A ['baxter', 'belle', 'bob']
    Team B ['barnum', 'bernice', 'bernie', 'bill']
    Team C ['beatrice']
    Team D ['ben']
    """
    "*** YOUR CODE HERE ***"
    


# You do not need to understand what this function does. It is used for testing.
def make_test_random():
    """A deterministic random function that cycles between
    [0.0, 0.1, 0.2, ..., 0.9] for testing purposes.

    >>> random = make_test_random()
    >>> random()
    0.0
    >>> random()
    0.1
    >>> random2 = make_test_random()
    >>> random2()
    0.0
    """
    rands = [x / 10 for x in range(10)]
    def random():
        rand = rands[0]
        rands.append(rands.pop(0))
        return rand
    return random

### Phase 1: The Player Class
class Player:
    """
    >>> random = make_test_random()
    >>> p1 = Player('Hill', random)
    >>> p2 = Player('Don', random)
    >>> p1.popularity
    100
    >>> p1.debate(p2)  # random() should return 0.0
    >>> p1.popularity
    150
    >>> p2.popularity
    100
    >>> p2.votes
    0
    >>> p2.speech(p1)
    >>> p2.votes
    10
    >>> p2.popularity
    110
    >>> p1.popularity
    135
    >>> p1.speech(p2)
    >>> p1.votes
    13
    >>> p1.popularity
    148
    >>> p2.votes
    10
    >>> p2.popularity
    99
    >>> for _ in range(4):  # 0.1, 0.2, 0.3, 0.4
    ...     p1.debate(p2)
    >>> p2.debate(p1)
    >>> p2.popularity
    49
    >>> p2.debate(p1)
    >>> p2.popularity
    0
    """
    def __init__(self, name, random_func):
        self.name = name
        self.votes = 0
        self.popularity = 100
        self.random_func = random_func

    def debate(self, other):
        "*** YOUR CODE HERE ***"

    def speech(self, other):
        "*** YOUR CODE HERE ***"

    def choose(self, other):
        return self.speech


### Phase 2: The Game Class
class Game:
    """
    >>> random = make_test_random()
    >>> p1, p2 = Player('Hill',random), Player('Don', random)
    >>> g = Game(p1, p2)
    >>> winner = g.play()
    >>> p1 is winner
    True
    >>> # Additional correctness tests
    >>> winner is g.winner()
    True
    >>> g.turn
    10
    >>> p1.votes = p2.votes
    >>> print(g.winner())
    None
    """
    def __init__(self, player1, player2):
        self.p1 = player1
        self.p2 = player2
        self.turn = 0

    def play(self):
        while not self.game_over():
            "*** YOUR CODE HERE ***"
        return self.winner()

    def game_over(self):
        return max(self.p1.votes, self.p2.votes) >= 50 or self.turn >= 10

    def winner(self):
        "*** YOUR CODE HERE ***"


### Phase 3: New Players
class AggressivePlayer(Player):
    """
    >>> random = make_test_random()
    >>> p1, p2 = AggressivePlayer('Don', random), Player('Hill', random)
    >>> g = Game(p1, p2)
    >>> winner = g.play()
    >>> p1 is winner
    True
    >>> # Additional correctness tests
    >>> p1.popularity = p2.popularity
    >>> p1.choose(p2) == p1.debate
    True
    >>> p1.popularity += 1
    >>> p1.choose(p2) == p1.debate
    False
    >>> p2.choose(p1) == p2.speech
    True
    """
    def choose(self, other):
        "*** YOUR CODE HERE ***"

class CautiousPlayer(Player):
    """
    >>> random = make_test_random()
    >>> p1, p2 = CautiousPlayer('Hill', random), AggressivePlayer('Don', random)
    >>> p1.popularity = 0
    >>> p1.choose(p2) == p1.debate
    True
    >>> p1.popularity = 1
    >>> p1.choose(p2) == p1.debate
    False
    >>> # Additional correctness tests
    >>> p2.choose(p1) == p2.speech
    True
    """
    def choose(self, other):
        "*** YOUR CODE HERE ***"


def every_other(s):
    """Mutates a linked list so that all the odd-indiced elements are removed
    (using 0-based indexing).

    >>> s = Link(1, Link(2, Link(3, Link(4))))
    >>> every_other(s)
    >>> s
    Link(1, Link(3))
    >>> odd_length = Link(5, Link(3, Link(1)))
    >>> every_other(odd_length)
    >>> odd_length
    Link(5, Link(1))
    >>> singleton = Link(4)
    >>> every_other(singleton)
    >>> singleton
    Link(4)
    """
    "*** YOUR CODE HERE ***"


def slice_link(link, start, end):
    """Slices a linked list from start to end (as with a normal Python list).

    >>> link = Link(3, Link(1, Link(4, Link(1, Link(5, Link(9))))))
    >>> new = slice_link(link, 1, 4)
    >>> print(new)
    <1 4 1>
    """
    "*** YOUR CODE HERE ***"


class Tree:
    """A tree has a label and a list of branches.

    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """
    def __init__(self, label, branches=[]):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(repr(self.label), branch_str)

    def __str__(self):
        return '\n'.join(self.indented())

    def indented(self):
        lines = []
        for b in self.branches:
            for line in b.indented():
                lines.append('  ' + line)
        return [str(self.label)] + lines


class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'

