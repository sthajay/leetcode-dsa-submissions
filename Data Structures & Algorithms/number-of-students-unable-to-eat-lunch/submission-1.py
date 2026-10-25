class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # Brute Force Solution - Queue
        res = n = len(students)
        q = deque(students)

        for s in sandwiches:
            cnt = 0
            while cnt < n and q[0] != s:
                cur = q.popleft()
                q.append(cur)
                cnt += 1

            if q[0] == s:
                q.popleft()
                res -= 1
            else:
                break

        return res
        # Time Complexity = O(n^2)
        # Space Complexity = O(n)

        # Optimal Solution
        res = len(students)
        cnt = Counter(students)

        for s in sandwiches:
            if cnt[s] > 0:
                cnt[s] -= 1
                res -= 1
            else:
                break
        
        return res

        # Time Complexity = O(n)
        # Space Complexity = O(1)