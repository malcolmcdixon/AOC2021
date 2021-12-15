commands = []

with open("day2_input.txt") as f:
    lines = f.readlines()
    for line in lines:
        command = line.split(" ")
        direction = command[0]
        distance = int(command[1])
        commands.append([direction, distance])

forward = sum(command[1] for command in commands if command[0] == "forward")

aim = 0
depth = 0
for command in commands:
    if command[0] == "forward":
        depth += aim * command[1]
        continue

    aim += command[1] if command[0] == "down" else -command[1]

print(forward, depth, forward * depth)
