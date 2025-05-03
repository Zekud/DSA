class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # Attach original indices to each task
        tasks = [(enqueue, process, i) for i, (enqueue, process) in enumerate(tasks)]
        tasks.sort()  # Sort by enqueue time
        
        result = []
        heap = []
        time = 0
        i = 0  # pointer for tasks

        while i < len(tasks) or heap:
            # If no task is available to process, move time forward
            if not heap and time < tasks[i][0]:
                time = tasks[i][0]
            
            # Push all tasks that have arrived by current time into heap
            while i < len(tasks) and tasks[i][0] <= time:
                heappush(heap, (tasks[i][1], tasks[i][2]))  # (processing_time, original_index)
                i += 1

           
            proc_time, index = heappop(heap)
            time += proc_time
            result.append(index)

        return result
