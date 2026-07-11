class Solution:
    def findMedianSortedArrays(self, nums1, nums2):

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)

        l, r = 0, m

        while l <= r:

            cut1 = (l + r) // 2
            cut2 = (m + n + 1) // 2 - cut1

            l1 = float("-inf") if cut1 == 0 else nums1[cut1 - 1]
            r1 = float("inf") if cut1 == m else nums1[cut1]

            l2 = float("-inf") if cut2 == 0 else nums2[cut2 - 1]
            r2 = float("inf") if cut2 == n else nums2[cut2]

            if l1 <= r2 and l2 <= r1:

                if (m + n) % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2

                return max(l1, l2)

            elif l1 > r2:
                r = cut1 - 1

            else:
                l = cut1 + 1