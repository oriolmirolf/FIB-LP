eql :: [Int] -> [Int] -> Bool
eql xs ys = (and (zipWith (==) xs ys)) && length xs == length ys

prod :: [Int] -> Int
prod xs = foldl (*) 1 xs

prodOfEvens :: [Int] -> Int
prodOfEvens xs = foldl (*) 1 (filter even xs)

powersOf2 :: [Int]
powersOf2 = iterate (*2) 1

scalarProduct :: [Float] -> [Float] -> Float
scalarProduct xs ys = foldl (+) 0 (zipWith (*) xs ys)