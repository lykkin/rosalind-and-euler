sieveNums (x:xs) | xs == []  = [x]
                 | otherwise = x:(sieveNums (filter (\n -> n `rem` x /= 0) xs))

primesLessThan n = sieveNums [2..n]

findFactor x (p:ps) | x `rem` p == 0 = p
                    | otherwise = findFactor x ps

getLF n = primesLessThan $ round $ sqrt n
