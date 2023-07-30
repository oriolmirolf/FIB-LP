countIf :: (Int -> Bool) -> [Int] -> Int
countIf b [] = 0
countIf b (x:xs)
    | b x       = 1 + countIf b xs
    | otherwise = countIf b xs

pam :: [Int] -> [Int -> Int] -> [[Int]]
pam _ [] = []
pam xs (y:ys) = map y xs : pam xs ys


apply2 :: Int -> [Int -> Int] -> [Int]
apply2 _ []     = []
apply2 x (y:ys) = y x : apply2 x ys 

pam2 :: [Int] -> [Int -> Int] -> [[Int]]
pam2 [] ys = []
pam2 (x:xs) ys = apply2 x ys : pam2 xs ys


filterFoldl :: (Int -> Bool) -> (Int -> Int -> Int) -> Int -> [Int] -> Int
filterFoldl b f acc []  = acc
filterFoldl b f acc (x:xs)
    | b x       = f x (filterFoldl b f acc xs)
    | otherwise = filterFoldl b f acc xs


insert :: (Int -> Int -> Bool) -> [Int] -> Int -> [Int]
insert _ [] y = [y]
insert r (x:xs) y
    | r y x     = y : x : xs
    | otherwise = x : insert r xs y 

insertionSort :: (Int -> Int -> Bool) -> [Int] -> [Int]
insertionSort _ [] = []
insertionSort b (x:xs) = insert b (insertionSort b xs) x