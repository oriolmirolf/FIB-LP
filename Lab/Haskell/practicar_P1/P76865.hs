data Tree a = Empty | Node a (Tree a) (Tree a)
    deriving (Show)

instance Foldable Tree where
    foldr _ acc Empty               = acc
    foldr f acc (Node x left right) = f x acc''
        where 
            acc''   = foldr f acc' left
            acc'    = foldr f acc right

avg :: Tree Int -> Double
avg t = (fromIntegral $ sum t) / (fromIntegral $ length t) 


cat :: Tree String -> String
cat = foldr f ""
    where
        f = (\x acc -> 
            if (acc /= "") 
                then x ++ " " ++ acc
                else x)