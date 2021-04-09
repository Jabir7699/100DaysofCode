#!/bin/python3

def testcase(q):
    total = 0
    for tries in range(2):
        for i in range(len(q) - 2, -1, -1):
            if q[i] > q[i+1]:
                q[i], q[i+1] = q[i+1], q[i]
                total += 1

    for i in range(len(q) - 1):
        if q[i] > q[i+1]:
            print('Too chaotic')
            return

    print(total)

T = int(input().strip())
for a0 in range(T):
    n = int(input().strip())
    q = [int(q_temp) for q_temp in input().strip().split(' ')]
    testcase(q)
