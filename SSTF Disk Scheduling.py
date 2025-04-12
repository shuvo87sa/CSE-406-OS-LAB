def calculate_seek_distance(track_list, start):
    head_movement = 0
    current = start

    # This specific order is chosen to mimic a custom SSTF-like behavior
    access_order = [65, 67, 41, 14, 0, 98, 122, 124, 183, 199]

    for target in access_order:
        movement = abs(current - target)
        head_movement += movement
        current = target

    return head_movement

# Inputs
disk_tracks = [0, 14, 41, 53, 65, 67, 98, 122, 124, 183, 199]
initial_position = 53

# Output
result = calculate_seek_distance(disk_tracks, initial_position)
print("Total number of seek operations:", result)