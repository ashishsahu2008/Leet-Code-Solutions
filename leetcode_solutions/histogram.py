class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        lt = []
        max_area = 0
        area = 0
        tp = None
        i=0
        while i < len(heights):
            if not lt or heights[lt[-1]] <= heights[i]:
                lt.append(i)
                i+=1
            else:
                print(lt)
                tp = lt[-1]
                lt.pop()
                x = (i-lt[-1]-1) if lt else i
                area = heights[tp] * x
                if max_area < area:
                    print('1: %d' % area)
                    max_area = area

        while(lt):
            tp = lt[-1]
            lt.pop()
            x = (i-lt[-1]-1) if lt else i
            area = heights[tp] * x
            if max_area < area:
                print('2: %d' % area)
                max_area = area
        return max_area

sol = Solution()
print(sol.largestRectangleArea([2,1,5,6,2,3]))
