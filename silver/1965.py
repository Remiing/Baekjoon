import sys
input = sys.stdin.readline
n = int(input())
boxes = list(map(int, input().split()))
seq = [boxes[0]]
for box in boxes:
    if box > seq[-1]:
        seq.append(box)
    elif box < seq[-1]:
        for i in range(len(seq)):
            if box <= seq[i]:
                seq[i] = box
                break
print(len(seq))









