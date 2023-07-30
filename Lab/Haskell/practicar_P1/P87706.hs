data BST a = E | N a (BST a) (BST a) deriving (Show)

insert :: Ord a => (BST a) -> a -> (BST a) 
insert E x      = N x E E
insert (N y l r) x
    | x == y    = N y l r
    | x < y     = N y (insert l x) r
    | x > y     = N y l (insert r x)

create :: Ord a => [a] -> BST a
create xs = foldl insert E xs

getmax :: BST a -> a
getmax (N x _ E) = x
getmax (N _ _ r) = getmax r

getmin :: BST a -> a
getmin (N x E _) = x
getmin (N _ l _) = getmin l

contains :: Ord a => BST a -> a -> Bool
contains E x      = False
contains (N y l r) x
    | x == y    = True
    | x < y     = contains l x
    | x > y     = contains r x

elements :: BST a -> [a]
elements E          = []
elements (N x l r)  = (elements l) ++ [x] ++ (elements r)

size :: BST a -> Int
size E = 0
size (N x l r) = 1 + (size l) + (size r)

-- El busquem i si no el trobem bé, si el trobem JA DECIDIM QUE FEM
remove :: Ord a => BST a -> a -> BST a
remove E _ = E
remove (N y l r) x
    | x < y     = N y (remove l x) r
    | x > y     = N y l (remove r x)
    | x == y    = case (l, r) of
                      (E, E) -> E
                      (E, _) -> r
                      (_, E) -> l
                      (_, _) -> let (minVal, rest) = deleteMin r
                                 in N minVal l rest

deleteMin :: BST a -> (a, BST a)
deleteMin (N x E r) = (x, r)
deleteMin (N x l r) = let (minVal, rest) = deleteMin l
                      in (minVal, N x rest r)

