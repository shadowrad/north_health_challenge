from collections import defaultdict
from typing import Dict, List, Set, Tuple


class PairFinder:
    def __init__(self, unordered_array: List[int]):
        self.unrepeated_array = list(set(unordered_array))
        self.sum_map: Dict[int, Set[Tuple[int, int]]] = defaultdict(set)

    def find_pairs_with_equal_sum(
        self, minimum_required_pairs: int = 1
    ) -> Dict[int, Set[Tuple[int, int]]]:
        """Find all unique pairs grouped by equal sum."""
        n = len(self.unrepeated_array)
        for i in range(len(self.unrepeated_array)):
            self._add_unique_pairs_to_sum_map(n, i)

        return {
            s: pairs
            for s, pairs in self.sum_map.items()
            if len(pairs) >= minimum_required_pairs
        }

    def _add_unique_pairs_to_sum_map(self, n, i):
        for j in range(i + 1, n):
            a, b = self.unrepeated_array[i], self.unrepeated_array[j]
            pair = tuple(sorted((a, b)))
            self.sum_map[a + b].add(pair)
