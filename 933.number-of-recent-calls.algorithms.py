class RecentCounter:

    def __init__(self):
        self.stamps = collections.deque()

    def ping(self, t: int) -> int:
        self.stamps.append(t)
        while t - self.stamps[0] > 3000:
            self.stamps.popleft()
        return len(self.stamps)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
