possibleSums n | n == 200 = 1
               | n > 200 = 0
               | otherwise = let divs = [1,2,5,10,20,50,100]
                             in (sum $ map (\x -> possibleSums (n + x)) divs)

possibleSums = 0:1:():[]

