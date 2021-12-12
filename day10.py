navigations = []
with open("day10_input.txt") as f:
    for line in f:
        navigations.append(line.rstrip())

open_chunk = ["(", "[", "{", "<"]
close_chunk = [")", "]", "}", ">"]

points = [3, 57, 1197, 25137]
completion_scores = []

syntax_error_score = 0

for navigation in navigations:
    chunks = []
    corrupt = False
    for char in navigation:
        if char in open_chunk:
            chunks.append(char)
        elif open_chunk.index(chunks[-1]) == close_chunk.index(char):
            chunks.pop()
        else:
            corrupt = True
            syntax_error_score += points[close_chunk.index(char)]
            break

    if not corrupt:
        score = 0
        for char in reversed(chunks):
            score = score * 5 + open_chunk.index(char) + 1

        completion_scores.append(score)

print(f"Syntax Score: {syntax_error_score}")
completion_scores.sort()
print(f"Completion Score: {completion_scores[len(completion_scores) // 2]}")
