class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        maxFreq = max(counts.values())
        numMax = list(counts.values()).count(maxFreq)
        req = (maxFreq - 1) * (n + 1) + numMax

        return max(req, len(tasks))