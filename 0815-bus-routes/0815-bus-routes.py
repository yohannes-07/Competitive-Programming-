class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        busRoutes = defaultdict(set)
        for i, route in enumerate(routes):
            for node in route:
                busRoutes[node].add(i)
        ans = -1
        visited = set()
        queue = deque()
        queue.append(source)
        while queue:
            ans += 1
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur == target:
                    return ans
                for bus in busRoutes[cur]:
                    if bus not in visited:
                        visited.add(bus)
                        queue.extend(routes[bus])
        return -1

