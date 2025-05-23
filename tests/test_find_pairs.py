from main import PairFinder

FIRST_ARRAY = [6, 4, 12, 10, 22, 54, 32, 42, 21, 11]

def test_all_elements_are_unique():
    all_elements = set()
    find_pairs = PairFinder(FIRST_ARRAY)
    result = find_pairs.find_pairs_with_equal_sum()
    for pairs in result.values():
        for pair in pairs:
            all_elements.update(pair)
    assert len(all_elements) == len(FIRST_ARRAY)


def test_find_pairs_with_equal_sum():
    find_pairs = PairFinder(FIRST_ARRAY)
    result = find_pairs.find_pairs_with_equal_sum()

def test_pairs_count():
    find_pairs = PairFinder(FIRST_ARRAY)
    result = find_pairs.find_pairs_with_equal_sum()
    assert len(result) == 38

def test_pairs_count_when_more_than_one():
    find_pairs = PairFinder(FIRST_ARRAY)
    result = find_pairs.find_pairs_with_equal_sum(2)
    assert len(result) == 7