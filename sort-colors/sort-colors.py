class Solution:
    def sortColors(self, colors: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # l: rightmost boundary of 0s, r: leftmost boundary of 2s, cur: current element being examined
        # When cur encounters a 0, we swap it with l and increment l and cur
        # When cur encounters a 1, we simply move forward
        # When cur encounters a 2, we swap it with r without incrementing cur, as the swapped element needs to be checked
        n=len(colors)
        l,r,cur=0,n-1,0
        while cur<=r:
            if colors[cur]==0:
                if colors[l]!=0:
                    colors[l],colors[cur]=colors[cur],colors[l]
                
                # The 'else' case is not needed here because:
                # 1. The left pointer (l) will never point to a 2, as 2s are always swapped to the right.
                # 2. If colors[l] is 0, no swap is needed, and we can safely move both pointers.
                # 3. If colors[l] is 1, we've just swapped it with a 0, so we should move both pointers.
                # Therefore, we can always increment 'cur' along with 'l'.
                cur += 1
                
                l+=1
            elif colors[cur]==1:
                cur+=1
            else: #color[cur] is 2
                if colors[r]!=2:
                    colors[cur],colors[r]=colors[r],colors[cur]
                r-=1

        # Time Complexity: O(n)
        # Space Complexity: O(1)