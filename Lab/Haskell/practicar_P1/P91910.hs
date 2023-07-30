multEq :: Int -> Int -> [Int]
multEq x y = iterate (* (x * y)) 1

selectFirst :: [Int] -> [Int] -> [Int] -> [Int]
selectFirst [] _ _                      = []
selectFirst _ [] _                      = []
selectFirst (x:xs) ys zs
    | (position x ys) < (position x zs) = x : (selectFirst xs ys zs)
    | otherwise                         = selectFirst xs ys zs

position :: Int -> [Int] -> Int
position _ [] = 10000 -- MAL! Perdon
position x (l:ls)
    | x == l    = 1
    | otherwise = 1 + (position x ls) 


myIterate :: (a -> a) -> a -> [a]
myIterate f x = scanl (\acc _ -> f acc) x (repeat x)

type SymTab a = String -> Maybe a

empty :: SymTab a
empty _ = Nothing

get :: SymTab a -> String -> Maybe a
get st s = (st s)

-- retorna una nova taula de símbols definint un nou valor per a un símbol (i sobrescrivint el valor antic si el símbol ja era a la taula)
set :: SymTab a -> String -> a -> SymTab a
set st key val = \k -> if k == key then Just val else st k


data Expr a
    = Val a
    | Var String
    | Sum (Expr a) (Expr a)
    | Sub (Expr a) (Expr a)
    | Mul (Expr a) (Expr a)
    deriving Show

eval :: (Num a) => SymTab a -> Expr a -> Maybe a
eval _ (Val x) = Just x
eval dic (Var x) = dic x 
eval dic (Sum e1 e2) = case (eval dic e1, eval dic e2) of
    (Just x, Just y)    -> Just (x + y)
    _                   -> Nothing
eval dic (Sub e1 e2) = case (eval dic e1, eval dic e2) of
    (Just x, Just y)    -> Just (x - y)
    _                   -> Nothing
eval dic (Mul e1 e2) = case (eval dic e1, eval dic e2) of
    (Just x, Just y)    -> Just (x * y)
    _                   -> Nothing