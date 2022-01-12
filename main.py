def direction(facing, turn):
    if turn % 45 != 0:
        return -1

    directions = {}
    cardinal = ['N', 'E', 'S', 'W']
    cardinal_len = len(cardinal)

    azimuth = 0
    for i in range(cardinal_len):
        directions[cardinal[i]] = azimuth
        azimuth += 45

        current = cardinal[i]
        next = cardinal[(i + 1) % cardinal_len]
        if i % 2 == 0:
            dir = current + next
        else:
            dir = next + current

        directions[dir] = azimuth
        azimuth += 45

    if facing not in directions.keys():
        return -1

    res = (directions[facing] + turn)
    if res < 0:
        res = 360 - abs(res) % 360
    else:
        res = res % 360

    for key, value in directions.items():
        if value == res:
            return key
    return -1
