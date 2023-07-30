ones :: [Integer]
ones = 1 : ones

nats :: [Integer]
nats = [0..]

ints :: [Integer]
ints = 0 : concat [[x, -x] | x <- [1..]]

triangulars :: [Integer]
triangulars = scanl (+) 0 [1..]

factorials :: [Integer]
factorials = scanl (*) 1 [1..]

fibs :: [Integer]
fibs = 0 : 1 : zipWith (+) fibs (tail fibs)

primes :: [Integer]
primes = garbell [2..]
    where
        garbell (p : xs) = p : garbell [x | x <- xs, x `mod` p /= 0]

hammings :: [Int]
hammings = 1 : merge (map (2*) hammings) (merge (map (3*) hammings) (map (5*) hammings))
  where merge (x:xs) (y:ys) | x > y     = y : merge (x:xs)  ys
                            | x < y     = x : merge xs      (y : ys)
                            | otherwise = x : merge xs      ys 

tartaglia :: [[Integer]]
tartaglia = iterate next [1]
  where
    next xs = zipWith (+) ([0] ++ xs) (xs ++ [0])

lookNsay :: [Integer]
lookNsay = iterate digitify 1
  where
    digitify x
      | penultim == 0     = 10 + x
      | penultim == ultim = rec + 10
      | otherwise         = rec * 100 + 10 + ultim
      where
        ultim     = x `mod` 10
        penultim  = (x `mod` 100) `div` 10
        rec       = digitify (x `div` 10)

