data Tree a = Empty | Node a (Tree a) (Tree a) 

instance Show a => Show (Tree a) where
    show Empty          = "()"
    show (Node x l r)   = "(" ++ show l ++ "," ++ show x ++ "," ++ show r ++ ")"

instance Functor Tree where
    fmap f Empty        = Empty
    fmap f (Node x l r) = (Node (f x) (fmap f l) (fmap f r))

doubleT :: Num a => Tree a -> Tree a
doubleT = fmap (*2)

data Forest a = Forest [Tree a] deriving Show

instance Functor Forest where
  fmap _ (Forest [])    = Forest []
  fmap f (Forest xs)    = Forest (map (fmap f) xs)

doubleF :: Num a => Forest a -> Forest a
doubleF = fmap (2*)