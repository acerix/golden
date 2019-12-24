#!/usr/bin/env python3

from random import random

phi = (1 - 5 ** .5) * -.5

def golden_point_generator(N):
  points = [x[:] for x in [[None] * 2] * N]

  # set the initial first coodinate
  x = minx = random()
  idx = 0

  # set the first coodinates
  for i in range(N):
    points[i][1] = x

    # keep the minimum
    if x < minx:
      minx = x
      idx = i

    # increment the coordinate
    x += phi

    if x >= 1:
      x -= 1

  # find the first Fibonacci >= N
  f, fp, parity = 1, 1, 0
  while f + fp < N:
    f, fp = fp, f+fp
    parity += 1

  # set the increment and decrement
  inc, dec = fp, f
  if parity & 1:
    inc, dec = f, fp

  # permute the first coordinates
  points[0][0] = points[idx][1]
  for i in range(1, N):
    if idx < dec:
      idx += inc
      if idx >= dec:
        idx -= dec
    else:
      idx -= dec
    points[i][0] = points[idx][1]

  # set the second initial coordinate
  y = random()

  # set the second coordinates
  for i in range(N):
    points[i][1] = y

    # increment the coordinate
    y += phi

    if y >= 1:
      y -= 1

  return points

if __name__ == '__main__':

  import sys
  N = int(sys.argv[1]) if len(sys.argv) > 1 else 6

  points = golden_point_generator(N)

  from pprint import pprint
  pprint(points)

  import matplotlib.pyplot as plt
  plt.scatter(*zip(*points))
  plt.show()
