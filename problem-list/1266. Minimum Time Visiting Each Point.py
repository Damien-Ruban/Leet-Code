# O(N) complexity
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        seconds = 0
        for i in range(1, len(points)):
            diff_x = abs(points[i][0] - points[i-1][0])
            diff_y = abs(points[i][1] - points[i-1][1])
            big = max(diff_x, diff_y)
            small = min(diff_x, diff_y)
            straight = big // (1 if small == 0 else small)
            sideways = big - straight
            seconds += straight + sideways
        return seconds

    


        
