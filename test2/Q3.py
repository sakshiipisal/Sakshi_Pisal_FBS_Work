import math
length = 50
breadth = 40
radius = 20
wire_layers = 5
cost_per_m = 35

perimeter = (2 * length) + breadth + (math.pi * radius)

total_wire_length = perimeter * wire_layers

total_cost = total_wire_length * cost_per_m

print("Total length of wire required:", round(total_wire_length, 2), "meters")
print("Total cost of fencing the field: Rs", round(total_cost, 2))
