fibb = 1:1:(zipWith (+) fibb (tail fibb))
getSum (x:xs) acc | x > 4000000 = acc
                  | x `rem` 2 == 0 = getSum xs (acc+x)
                  | otherwise = getSum xs acc
