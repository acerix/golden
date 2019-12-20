#!/usr/bin/env python3

from scipy.constants import golden as φ

def golden_point_generator(seed, N):
  num = 0
  while num < 10:
    yield num
    num += φ

for i in golden_point_generator(seed=0, N=3):
  print(i)
