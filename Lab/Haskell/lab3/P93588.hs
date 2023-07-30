myMap :: (a -> b) -> [a] -> [b]
myMap f xs = [f x | x <- xs];

myFilter :: (a -> Bool) -> [a] -> [a]
myFilter b xs = [x | x <- xs, b x]

myZipWith :: (a -> b -> c) -> [a] -> [b] -> [c]
myZipWith f xs ys = [f x y | (x, y) <- zip xs ys]

thingify :: [Int] -> [Int] -> [(Int, Int)]
thingify xs ys = [(x, y) | x <- xs, y <- ys, x `mod` y == 0]

factors :: Int -> [Int]
factors x = [y | y <- [1..x], x `mod` y == 0]