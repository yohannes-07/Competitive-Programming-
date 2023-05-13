
class Solution:
    def longestCycle(self, edges):

        n = len(edges)
        visited = [False] * n
        incoming = [0] * n

        for edge in edges:
            if edge != -1:
                incoming[edge] += 1

       
        queue = deque()
        for i in range(n):
            if incoming[i] == 0:
                queue.append(i)

        while queue:
            node = queue.popleft()

            visited[node] = True
            neighbor = edges[node]

            #if it's not leaf node
            if neighbor != -1:
                incoming[neighbor] -= 1

                if incoming[neighbor] == 0:
                    queue.append(neighbor)
     
        # after completeing Khan's algorithm, it means all nodes excpet nodes
        # in the cycle are visited
        answer = -1
        for i in range(n):
            if not visited[i]:
                neighbor = edges[i]
                count = 1
                visited[i] = True

                # Iterate in the cycle.
                while neighbor != i:
                    visited[neighbor] = True
                    count += 1
                    neighbor = edges[neighbor]

                answer = max(answer, count)

        return answer
