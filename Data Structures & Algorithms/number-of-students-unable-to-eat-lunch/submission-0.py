class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
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