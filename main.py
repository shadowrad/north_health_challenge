
from models.pair_finder import PairFinder

def print_pairs_by_sum(arr: list[int]) -> None:
    find_pairs = PairFinder(arr)
    result = find_pairs.find_pairs_with_equal_sum(2)
    result = dict(sorted(result.items()))
    for total, pairs in result.items():
        formatted_pairs = " ".join(f"({a}, {b})" for a, b in pairs)
        print(f"Pairs : {formatted_pairs} have sum : {total}")


if __name__ == "__main__":
    sample_inputs = [
        [6, 4, 12, 10, 22, 54, 32, 42, 21, 11],
        [4, 23, 65, 67, 24, 12, 86]
    ]
    
    for arr in sample_inputs:
        print(f"Input: {arr}")
        print_pairs_by_sum(arr)
        print()
