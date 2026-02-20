from yatzy import Yatzy

# These unit tests can be run using the py.test framework
# available from http://pytest.org/

# CHANCE
def test_ShouldSumAllDice_WhenChanceIsCalled():
    expected = 15
    actual = Yatzy.chance(1, 2, 3, 4, 5)
    assert expected == actual

# YATZY
def test_ShouldReturn50_WhenAllDiceEqual():
    expected = 50
    actual = Yatzy.yatzy([6, 6, 6, 6, 6])
    assert expected == actual

def test_ShouldReturn0_WhenNotAllDiceEqual():
    expected = 0
    actual = Yatzy.yatzy([6, 6, 6, 6, 5])
    assert expected == actual

# ONES / TWOS / THREES
def test_ShouldSumOnes_WhenOnesCalled():
    expected = 3
    actual = Yatzy.ones(1, 1, 2, 3, 1)
    assert expected == actual


def test_ShouldSumTwos_WhenTwosCalled():
    expected = 6
    actual = Yatzy.twos(2, 2, 2, 3, 4)
    assert expected == actual

def test_ShouldSumThrees_WhenThreesCalled():
    expected = 9
    actual = Yatzy.threes(3, 3, 3, 4, 5)
    assert expected == actual

# FOURS / FIVES / SIXES
def test_ShouldSumFours_WhenFoursCalled():
    y = Yatzy(4, 4, 2, 4, 5)
    expected = 12
    actual = y.fours()
    assert expected == actual

def test_ShouldSumFives_WhenFivesCalled():
    y = Yatzy(5, 5, 5, 1, 2)
    expected = 15
    actual = y.fives()
    assert expected == actual

def test_ShouldSumSixes_WhenSixesCalled():
    y = Yatzy(6, 6, 6, 6, 1)
    expected = 24
    actual = y.sixes()
    assert expected == actual

# PAIRS
def test_ShouldReturnHighestPair_WhenScorePairCalled():
    expected = 12
    actual = Yatzy.score_pair(6, 6, 5, 4, 3)
    assert expected == actual

def test_ShouldReturn0_WhenNoPairExists():
    expected = 0
    actual = Yatzy.score_pair(1, 2, 3, 4, 5)
    assert expected == actual

def test_ShouldReturnScore_WhenTwoPairsExist():
    expected = 10
    actual = Yatzy.two_pair(3, 3, 2, 2, 5)
    assert expected == actual

# THREE / FOUR OF A KIND
def test_ShouldReturnScore_WhenThreeOfAKindExists():
    expected = 9
    actual = Yatzy.three_of_a_kind(3, 3, 3, 4, 5)
    assert expected == actual

def test_ShouldReturnScore_WhenFourOfAKindExists():
    expected = 16
    actual = Yatzy.four_of_a_kind(4, 4, 4, 4, 5)
    assert expected == actual

# STRAIGHTS
def test_ShouldReturn15_WhenSmallStraight():
    expected = 15
    actual = Yatzy.smallStraight(1, 2, 3, 4, 5)
    assert expected == actual

def test_ShouldReturn20_WhenLargeStraight():
    expected = 20
    actual = Yatzy.largeStraight(2, 3, 4, 5, 6)
    assert expected == actual

# FULL HOUSE
def test_ShouldReturnScore_WhenFullHouseExists():
    expected = 13
    actual = Yatzy.fullHouse(2, 2, 3, 3, 3)
    assert expected == actual

def test_ShouldReturn0_WhenNotFullHouse():
    expected = 0
    actual = Yatzy.fullHouse(1, 2, 3, 4, 5)
    assert expected == actual