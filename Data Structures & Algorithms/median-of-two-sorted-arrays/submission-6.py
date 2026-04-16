class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        A = nums1
        B = nums2
        if len(A) > len(B):
            A, B = B, A

        # A must be the smaller nums
        total = len(A) + len(B)
        half = total // 2

        # Left must have half
        # Right can have up to half or half + 1
        l = 0
        r = len(A)

        while True:
            i = (l + r) // 2
            j = half - i

            leftA = A[i - 1] if i > 0 else float("-inf")
            leftB = B[j - 1] if j > 0 else float("-inf")
            rightA = A[i] if i < len(A) else float("inf")
            rightB = B[j] if j < len(B) else float("inf")

            if leftA <= rightB and leftB <= rightA:
                if total % 2 == 1:
                    return min(rightA, rightB)
                else:
                    return (max(leftA, leftB) + min(rightA, rightB)) / 2
            elif leftB < rightA:
                r = i - 1
            else:
                l = i + 1

