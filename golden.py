#!/usr/bin/env python3

from scipy.constants import golden as ϕ
from random import random

def golden_point_generator(seed, N):
  points = [x[:] for x in [[None] * 2] * N]

  # set the initial first coodinate
  x = minx = random()
  idx = 0

  # set the first coodinates
  for i in range(N):
    points[i][1] = x

    # keep the minimum
    # @todo seems this can't happen since python doens't overflow ints
    if x < minx:
      minx = x
      idx = i

    # increment the coordinate
    x += ϕ

    if x >= 1:
      x -= 1

  # find the first Fibonacci >= N
  f, fp, parity = 1, 1, 0
  while (f + fp < N):
    f, fp = fp, f+fp
    parity += 1

  # set the increment and decrement
  inc, dec = fp, f
  if parity & 1:
    inc, dec = f, fp

  # permute the first coordinate

  # set the second initial coordinate

  print(inc, dec)

  num = 0
  while num < 10:
    yield num
    num += ϕ

for i in golden_point_generator(seed=0, N=16):
  print(i)
