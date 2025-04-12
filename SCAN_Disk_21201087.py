def scan_disk(requests, start, direction, disk_limit):
    # Sort the request list
    sorted_requests = sorted(requests)
    total_seek = 0
    seek_order = []
    
    # Divide requests based on head position
    lower = [r for r in sorted_requests if r < start]
    higher = [r for r in sorted_requests if r >= start]

    current = start

    if direction == "right":
        # Move towards higher tracks first
        for r in higher:
            seek_order.append(r)
            total_seek += abs(current - r)
            current = r

        # Move to disk end
        if higher:
            total_seek += (disk_limit - 1 - current)
            current = disk_limit - 1

        # Then move to lower tracks
        for r in reversed(lower):
            seek_order.append(r)
            total_seek += abs(current - r)
            current = r

    elif direction == "left":
        # Move towards lower tracks first
        for r in reversed(lower):
            seek_order.append(r)
            total_seek += abs(current - r)
            current = r

        # Move to start of disk
        if lower:
            total_seek += current
            current = 0

        # Then move to higher tracks
        for r in higher:
            seek_order.append(r)
            total_seek += abs(current - r)
            current = r

    # Ensure head is added at the beginning for display consistency
    seek_order.insert(0, start)

    return seek_order, total_seek

# Example Input
request_list = [0, 14, 41, 53, 65, 67, 98, 122, 124, 183, 199]
initial_head = 53
move_direction = "right"
max_disk_size = 200

result_sequence, seek_total = scan_disk(request_list, initial_head, move_direction, max_disk_size)

print("Seek Sequence:", result_sequence)
print("Total number of seek operations::", seek_total)
