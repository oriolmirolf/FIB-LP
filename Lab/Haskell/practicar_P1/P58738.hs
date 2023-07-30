data STree a = Nil | Node Int a (STree a) (STree a)
    deriving Show

size :: STree a -> Int
size Nil            = 0
size (Node n _ l r) = n

isOk :: STree a -> Bool
isOk Nil            = True
isOk (Node n _ l r) = n == size l + size r + 1 && isOk l && isOk r

nthElement :: STree a -> Int -> Maybe a
nthElement Nil _ = Nothing
nthElement (Node n x l r) i
    | i < 1 || i > n    = Nothing
    | i == size l + 1   = Just x
    | i <= size l       = nthElement l i
    | otherwise         = nthElement r (i - (size l) - 1)

mapToElements :: (a -> b) -> STree a -> [Int] -> [Maybe b]
mapToElements f t is = fmap (maybe Nothing (Just . f)) nodes
  where nodes = map (\i -> nthElement t i) is
  
instance Functor STree where
    fmap _ Nil              = Nil
    fmap f (Node n x l r)   = Node n (f x) (fmap f l) (fmap f r)

--instance Show a => Show (STree a) where
--    show Nil    = "Nil"
--    show (Node n x l r) = "Node "++ show n ++ " " ++ show x ++ " (" ++ show l ++ ") (" ++ show r ++ ")"

div10 = flip div 10
t1 = Node 3 99 (Node 1 88 Nil Nil) (Node 1 22 Nil Nil)
t2 = Node 2 77 (Node 1 33 Nil Nil) Nil
t3 = Node 6 44 t1 t2
t4 = Node 7 55 t1 t2 