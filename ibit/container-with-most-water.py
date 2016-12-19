class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Take 2 extreme lines, find area.
        # Then keep removing shorter line and updating area
        maxArea = 0
        i = 0
        j = len(height) - 1
        while(i < j):
            area = (j-i) * min(height[i], height[j])
            maxArea = max(area, maxArea)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return maxArea


    # Brute Force Soln - O(n2)
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        tallCols = []
        maxArea = 0
        for i,h in enumerate(height):
            if not tallCols:
                tallCols.append((i,h))
            else:
                for col in tallCols:
                    area = min(col[1], h) * (i - col[0])
                    maxArea = max(area, maxArea)
                    if h > tallCols[-1][1]:
                        tallCols.append((i,h))
        return maxArea
