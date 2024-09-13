from collections import deque

class Solution:
    def longestSubarray(self, nums, limit):
        min_deque = deque()  # To store the indices of min elements
        max_deque = deque()  # To store the indices of max elements
        left = 0  # Left pointer of the sliding window
        max_len = 0  # Result to track the longest subarray length

        for right in range(len(nums)):
            # Maintain the max deque (decreasing order)
            while max_deque and nums[max_deque[-1]] < nums[right]:
                max_deque.pop()
            max_deque.append(right)

            # Maintain the min deque (increasing order)
            while min_deque and nums[min_deque[-1]] > nums[right]:
                min_deque.pop()
            min_deque.append(right)

            # Check if the current window is valid
            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                left += 1
                # Remove elements out of the window
                if max_deque[0] < left:
                    max_deque.popleft()
                if min_deque[0] < left:
                    min_deque.popleft()

            # Update the maximum length of the valid subarray
            max_len = max(max_len, right - left + 1)

        return max_len

            

        