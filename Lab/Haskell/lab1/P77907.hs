absValue :: Int -> Int
absValue x
    | x < 0 = -x
    | otherwise = x

power :: Int -> Int -> Int
power x p
    | p == 0    = 1
    | otherwise = x^p

isPrime :: Int -> Bool
isPrime n
    | n <= 1    = False -- 1 and below are not prime
    | otherwise = go 2 -- start checking from 2

    where
        go k
            | k * k > n        = True -- if we get to sqrt(n), n is prime
            | n `mod` k == 0   = False -- n is divisible by k, so it's not prime
            | otherwise        = go (k + 1) -- check the next divisor

slowFib :: Int -> Int
slowFib n
    | n == 0    = 0
    | n == 1    = 1
    | otherwise = slowFib (n-1) + slowFib (n-2)

quickFib :: Integer -> Integer
quickFib n = round (phi ** fromIntegral n / sqrt 5)
  where
    phi = (1 + sqrt 5) / 2
