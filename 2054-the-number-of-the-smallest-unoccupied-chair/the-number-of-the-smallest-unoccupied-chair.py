class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        targetArrival = times[targetFriend][0]
        
        # Add index so we can track who is who
        friends = sorted([(arr, leave, i) for i, (arr, leave) in enumerate(times)])
        
        heap = []        # (leave_time, chair_number)
        chairheap = []   # Available chairs
        nextChair = 0    # Next chair number to use

        for arr, leave, idx in friends:
            # Free up chairs whose owner has left
            while heap and heap[0][0] <= arr:
                _, freedChair = heappop(heap)
                heappush(chairheap, freedChair)
            
            # Assign a chair
            if chairheap:
                chair = heappop(chairheap)
            else:
                chair = nextChair
                nextChair += 1
            
            heappush(heap, (leave, chair))

            if arr == targetArrival and idx == targetFriend:
                return chair
