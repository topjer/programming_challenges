# Bricks and Water Challenge

This repository contains my solution to the Bricks and Water challenge found here
(https://platform.entwicklerheld.de/challenge/bricks-and-water?technology=python)

## Problem description

The problem is roughly the following:

You are given an array of non-negative integers that represents a 2-D configuration for bricks (or think lego blocks).

For example: [2, 0, 2] would be a configuration with two blocks on the left, none in the middle and two on the right.
It is possible to store water between blocks and it behaves as one would expect. If there is no boundary to the left or
the right it will just spill over.

So in our given example, we can store 2 blocks of water. Whereas for example [2, 0, 1] would only allow to store a single
block of water.

The questions is: How much water can be stored in a given array.

## Solution approach

One possible approach would be "local" in nature. One iterates over the entire array and searches for every position
the biggest block the the left and to the right, excluding the current position.

Given that information, one can compute how much water can be stored in the current column.

Alternatively, a "global" approach is also possible. You determine the indices of the two largest columns. Next compute
the amount of water that would be possible between the two if there were no other blocks and substract the number of 
blocks in between.

Next, remove all considered portions of the array except for the highest column (second highest is also possible )
and repeat this step with the remaining array until nothing is left.

For example: Given [1, 0, 2, 0, 3, 0, 1], the algorithm first extracts the sub-arry [2, 0, 3] which can hold 2 water 
blocks and continues with the array [1, 0, 3, 0, 1]. Note that we could also use the array [1, 0, 2, 0, 1] since we know
that there cannot be another column that is truely higher than 2.