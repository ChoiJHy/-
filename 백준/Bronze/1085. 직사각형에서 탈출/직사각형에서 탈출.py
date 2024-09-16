x, y, w ,h = map(int, input().split())
distance_x = x if x < (w - x) else (w - x)
distance_y = y if y < (h - y) else (h - y)

print(distance_x if distance_x < distance_y else distance_y)