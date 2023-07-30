myLength :: [Int] -> Int
myLength []     = 0
myLength(_:xs)  = 1 + myLength xs

myMaximum :: [Int] -> Int
myMaximum [a]       = a
myMaximum (a:xs)    = max a (myMaximum (xs))

average :: [Int] -> Float
average xs = fromIntegral (sum xs) / fromIntegral (length xs)

buildPalindrome :: [Int] -> [Int]
buildPalindrome xs = reverse xs ++ xs

remove :: [Int] -> [Int] -> [Int]
remove [] _     = []
remove (x:xs) ys
    | elem x ys = remove xs ys
    | otherwise = x : remove xs ys

flatten :: [[Int]] -> [Int]
flatten []      = []
flatten (x:xs)  = x ++ flatten xs

--flatten2 :: [[Int]] -> [Int]
--flatten2 xs = concat xs

oddsNevens :: [Int] -> ([Int], [Int])
oddsNevens xs = (odds xs, evens xs)

odds :: [Int] -> [Int]
odds []         = []
odds (x:xs)
    | odd x     = x : odds xs
    | otherwise = odds xs

evens :: [Int] -> [Int]
evens []        = []
evens (x:xs)
    | even x    = x : evens xs
    | otherwise = evens xs

primeDivisors :: Int -> [Int]
primeDivisors n = filter isPrime (divisors n)
    where
        isPrime k   = null [x | x <- [2..k-1], k `mod` x == 0]
        divisors n  = [x | x <- [2..n], mod n x == 0] 