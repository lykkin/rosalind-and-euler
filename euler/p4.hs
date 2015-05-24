digits :: Integer -> [Integer]
digits x = let tcoDigits x acc | x == 0 = acc
                               | otherwise = tcoDigits (div x 10) ((rem x 10):acc)
           in tcoDigits x []

palindrome :: Integer -> Bool
palindrome x = digits x == (reverse $ digits x)

factorial :: Integer -> Integer
factorial n = let tcofact n acc | n == 1 = acc
                                | otherwise = tcofact (n - 1) (acc * n)
              in tcofact n 1
