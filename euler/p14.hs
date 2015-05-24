collatzLength:: Int -> Int
collatzLength n = let collatz k step | k == 1 = step
                                     | k `rem` 2 == 0 = collatz (k `div` 2) (step + 1)
                                     | otherwise = collatz (3*k + 1) (step + 1)
                  in collatz n 0
