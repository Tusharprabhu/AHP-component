import numpy as np
import heapq

# Define the symbols and their probabilities
S = ["s"+str(i) for i in range(5)]
pk = [0.4,0.2,0.2,0.1,0.1]

# Create a priority queue with the probabilities and symbols
queue = [[weight, [symbol, ""]] for weight, symbol in zip(pk, S)]
heapq.heapify(queue)

# While there are more than one items in the queue
while len(queue) > 1:
    # Get the two symbols with the smallest probabilities
    lo = heapq.heappop(queue)
    hi = heapq.heappop(queue)
    
    # Append '0' to the Huffman code of the first symbol and '1' to the second
    for pair in lo[1:]:
        pair[1] = '0' + pair[1]
    for pair in hi[1:]:
        pair[1] = '1' + pair[1]
    
    # Add a new item to the queue with the combined probability and both symbols
    heapq.heappush(queue, [lo[0] + hi[0]] + lo[1:] + hi[1:])

# Print the Huffman codes
huff_codes = sorted(heapq.heappop(queue)[1:], key=lambda p: (len(p[-1]), p))
for symbol, huff_code in huff_codes:
    print(f"{symbol} : {huff_code}")