# Read number of songs
n = int(input().strip())

# Read the singers for each song
singers = list(map(int, input().split()))

# Step 1: Count frequency of each singer manually
freq = {}
for singer in singers:
    if singer not in freq:
        freq[singer] = 0
    freq[singer] += 1

# Step 2: Find the maximum frequency manually
max_count = 0
for singer in freq:
    if freq[singer] > max_count:
        max_count = freq[singer]

# Step 3: Count how many singers have this maximum frequency
favourite_singers = 0
for singer in freq:
    if freq[singer] == max_count:
        favourite_singers += 1

# Output the result
print(favourite_singers)
