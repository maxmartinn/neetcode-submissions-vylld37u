class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A  # always binary search smaller array
        
        total = len(A) + len(B)
        half = total // 2
        
        l, r = 0, len(A)
        
        while True:
            i = (l + r) // 2      # partition index for A
            j = half - i          # partition index for B
            
            # edge cases: use inf when partition is at boundary
            leftA  = A[i-1] if i > 0 else float('-inf')
            rightA = A[i]   if i < len(A) else float('inf')
            leftB  = B[j-1] if j > 0 else float('-inf')
            rightB = B[j]   if j < len(B) else float('inf')
            
            if leftA <= rightB and leftB <= rightA:
                # valid partition found
                if total % 2 == 1:
                    return min(rightA, rightB)
                return (max(leftA, leftB) + min(rightA, rightB)) / 2
            
            elif leftA > rightB:
                r = i - 1  # took too many from A, go left
            else:
                l = i + 1  # took too few from A, go right