def cscan_disk(request_list, initial_head, max_cylinder=200):
    # Sort the request queue
    sorted_requests = sorted(request_list)
    seek_count = 0
    current = initial_head

    # Split requests into two halves based on head position
    upward = [req for req in sorted_requests if req >= current]
    downward = [req for req in sorted_requests if req < current]

    # Move towards the end (higher tracks)
    for req in upward:
        seek_count += abs(current - req)
        current = req

    # Jump from end to start
    seek_count += (max_cylinder - 1 - current) + (max_cylinder - 1)
    current = 0

    # Continue servicing the lower half
    for req in downward:
        seek_count += abs(current - req)
        current = req

    return seek_count

# Example usage
requests = [0, 14, 41, 53, 65, 67, 98, 122, 124, 183, 199]
start_head = 53

print("Total number of seek operations:", cscan_disk(requests, start_head))
