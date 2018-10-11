from heapq import heappush, heappop, heapify
from collections import defaultdict

def encode(symb2freq):
    """Huffman encode the given dict (map symbols to weights)"""
    heap = [[weight, [symbol, ""]] for symbol, weight in symb2freq.items()]
    heapify(heap) #https://www.cs.princeton.edu/~wayne/kleinberg-tardos/pdf/DemoHeapify.pdf
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

# Get input from the user and create dictionary
raw_txt = raw_input("Type your desired text to be decoded below.\n")
txt = raw_txt
symb2freq = defaultdict(int)
for ch in txt:
    symb2freq[ch] += 1
# For python 3:
# symb2freq = collections.Counter(txt)
huff = encode(symb2freq) #Call our encoding function
print "Symbol\tWeight\tHuffman Code"
for p in huff:
    print "%s\t%s\t%s" % (p[0], symb2freq[p[0]], p[1])
