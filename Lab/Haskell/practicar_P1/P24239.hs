roman2int :: String -> Int
roman2int []                        = 0
roman2int [x]                       = (valorEnRoma x) 
roman2int (x:y:xs)
    | simbolMesPetit x y            = (roman2int (y:xs)) - (valorEnRoma x)
    | otherwise                     = (roman2int (y:xs)) + (valorEnRoma x)

valorEnRoma :: Char -> Int
valorEnRoma c = case c of
    'I' -> 1
    'V' -> 5
    'X' -> 10
    'L' -> 50
    'C' -> 100
    'D' -> 500
    'M' -> 1000

simbolMesPetit :: Char -> Char -> Bool
simbolMesPetit x y = (valorEnRoma x) < (valorEnRoma y)


roman2int' :: String -> Int
roman2int' []   = 0
roman2int' [x]  = (valorEnRoma x)
roman2int' xs   = foldl (\acc (x, y) -> 
    if simbolMesPetit x y
        then acc - valorEnRoma x
        else acc + valorEnRoma x) 0 (zip xs (tail xs ++ [last xs]))

arrels :: Float -> [Float]
arrels x = iterate (\an -> (an + x / an) / 2) x

arrel :: Float -> Float -> Float
arrel x e = foo e (arrels x)
    where
        foo e (x:y:xs)
            | x - y <= e    = y
            | otherwise     = foo e (y:xs)


data LTree a = Leaf a | Node (LTree a) (LTree a)

instance Show a => Show (LTree a) where
    show (Leaf x)       = "{" ++ show x ++ "}"
    show (Node lt rt)   = "<" ++ (show lt) ++ "," ++ (show rt) ++ ">"

build :: [a] -> LTree a
build [x]   = Leaf x
build xs    = Node (build left) (build right)
    where
        (left, right) = splitAt half xs
        half = (length xs +1) `div` 2


zipLTrees :: LTree a -> LTree b -> Maybe (LTree (a,b))
zipLTrees (Leaf x) (Leaf y) = Just (Leaf (x,y))
zipLTrees (Node l1 r1) (Node l2 r2) = do
    l <- zipLTrees l1 l2
    r <- zipLTrees r1 r2
    return (Node l r)
zipLTrees _ _   = Nothing    

    
