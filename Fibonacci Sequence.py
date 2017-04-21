#!/usr/bin/env python
# coding=utf-8
import os
import re
import shutil
import subprocess
import sys


def fibonacci_sequence(start, a):
    print("0")
    print(start)
    print(a)

    for x in range(1,11):
        ans = start + a
        print(ans)

        a = ans + start
        print(a)

        start = a + ans
        print(start)

fibonacci_sequence(1, 1)