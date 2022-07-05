"""
Exercise 3: Slice list into 3 equal chunks and reverse each chunk
Chunk  1 [11, 45, 8]
After reversing it  [8, 45, 11]
Chunk  2 [23, 14, 12]
After reversing it  [12, 14, 23]
Chunk  3 [78, 45, 89]
After reversing it  [89, 45, 78]
"""

sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

chunk_size = int(len(sample_list)/3)
print(chunk_size)
start = 0
end = chunk_size

for i in range(3):
    indexes = slice(start,end)

    chunk = sample_list[indexes]
    start = end
    end = end + chunk_size
    print("Chunk ", i+1," ",chunk)
    print("After Reversing it ", list(reversed(chunk)))
