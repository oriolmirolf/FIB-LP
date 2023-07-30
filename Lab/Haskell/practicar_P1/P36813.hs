degree :: Eq a => [(a, a)] -> a -> Int
degree [] v = 0
degree ((x,y):xs) v
    | x == v || y == v  = degree xs v + 1
    | otherwise         = degree xs v   

degree' :: Eq a => [(a, a)] -> a -> Int
degree' xs v = foldl func 0 xs
    where
        func acc (x, y) 
            | x == v || y == v  = acc + 1 
            | otherwise         = acc

--degree' :: Eq a => [(a, a)] -> a -> Int
--degree' xs v = length deg
--    where
--        deg = [(y1, y2) | (y1, y2) <- xs, y1 == v || y2 == v]

--neighbors :: Ord a => [(a, a)] -> a -> [a]
