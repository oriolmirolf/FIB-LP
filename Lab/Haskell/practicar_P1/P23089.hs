myUnfoldr :: (b -> Maybe (a, b)) -> b -> [a]
myUnfoldr f b = case f b of
    Just (a, b')    -> a : myUnfoldr f b'
    Nothing         -> []

myReplicate :: a -> Int -> [a]
myReplicate x n = myUnfoldr (\n -> if n == 0 then Nothing else Just (x, n-1)) n

myIterate :: (a -> a) -> a -> [a]
myIterate f x = myUnfoldr (\acc -> Just (acc, f acc)) x

myMap :: (a -> b) -> [a] -> [b]
myMap f ls = myUnfoldr (\xs -> if null xs then Nothing else Just (f (head xs), tail xs)) ls

data Bst a = Empty | Node a (Bst a) (Bst a)

add :: Ord a => a -> (Bst a) -> (Bst a)

add x Empty = Node x Empty Empty
add x (Node y l r)
    | x < y     = Node y (add x l) r
    | x > y     = Node y l (add x r)
    | otherwise = Node y l r

instance Show a => Show (Bst a) where
    show Empty          = "."
    show (Node a l r)   = show a ++ show l ++ show r

--adder :: Ord a => (Bst a, [a]) -> Maybe (Bst a, (Bst a, [a]))
