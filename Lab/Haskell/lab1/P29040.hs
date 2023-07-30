insert :: [Int] -> Int -> [Int]
insert [] y = [y]
insert (x:xs) y
    | y <= x        = y : x : xs
    | otherwise     = x : insert xs y

isort :: [Int] -> [Int]
isort []        = []
isort (x:xs)    = insert (isort xs) x

remove :: [Int] -> Int -> [Int]
remove (x:xs) y
    | y == x    = xs
    | otherwise = x : remove xs y

ssort :: [Int] -> [Int]
ssort []    = []
ssort xs    = (minimum xs) : ssort(remove xs (minimum xs))

merge :: [Int] -> [Int] -> [Int]
merge x [] = x
merge [] y = y
merge (x:xs) (y:ys)
    | x <= y    = x : merge xs  (y:ys)
    | y < x     = y : merge (x:xs) ys

msort :: [Int] -> [Int]
msort []    = []
msort [x]   = [x]
msort xs    = merge (msort left) (msort right)
    where
        left    = take half xs
        right   = drop half xs
        half    = div (length xs) 2

qsort :: [Int] -> [Int]
qsort [] = []
qsort (x:xs) = qsort smaller ++ [x] ++ qsort larger
    where
        smaller = [y | y <- xs, y <= x]
        larger  = [y | y <- xs, y > x]

genQsort :: Ord a => [a] -> [a]
genQsort [] = []
genQsort (x:xs) = genQsort smaller ++ [x] ++ genQsort larger
    where
        smaller = [y | y <- xs, y <= x]
        larger  = [y | y <- xs, y > x]