data Tree a = Node a (Tree a) (Tree a) | Empty 
    deriving (Show)

size :: Tree a -> Int
size Empty          = 0
size (Node _ fe fd) = 1 + size fe + size fd

height :: Tree a -> Int
height Empty        = 0
height (Node _ fe fd) = 1 + max (height fe) (height fd)

equal :: Eq a => Tree a -> Tree a -> Bool
equal Empty Empty                           = True
equal (Node x1 fe1 fd1) (Node x2 fe2 fd2)   = (x1 == x2) && (equal fe1 fe2) && (equal fd1 fd2)
equal _ _                                   = False

isomorphic :: Eq a => Tree a -> Tree a -> Bool
isomorphic Empty Empty          = True
isomorphic Empty _              = False
isomorphic _ Empty              = False
isomorphic (Node a la ra) (Node b lb rb) = a == b && (cas1 || cas2)
    where
        cas1 = (isomorphic la lb) && (isomorphic ra rb)
        cas2 = (isomorphic la rb) && (isomorphic ra lb)

preOrder :: Tree a -> [a]
preOrder Empty = []
preOrder (Node x fe fd) = [x] ++ preOrder fe ++ preOrder fd

postOrder :: Tree a -> [a]
postOrder Empty = []
postOrder (Node x fe fd) = postOrder fe ++ postOrder fd ++ [x]

inOrder :: Tree a -> [a]
inOrder Empty = []
inOrder (Node x fe fd) = inOrder fe ++ [x] ++ inOrder fd

build :: Eq a => [a] -> [a] -> Tree a 
build _ [] = Empty
build [] _ = Empty
build (x:preorder) inorder =
    let (leftInorder, _:rightInorder) = span (/= x) inorder
        leftPreorder = take (length leftInorder) preorder
        rightPreorder = drop (length leftInorder) preorder
    in Node x (build leftPreorder leftInorder) (build rightPreorder rightInorder)

overlap :: (a -> a -> a) -> Tree a -> Tree a -> Tree a
overlap _ Empty Empty                           = Empty
overlap _ (Node x fe fd) Empty                  = Node x fe fd
overlap _ Empty (Node x fe fd)                  = Node x fe fd
overlap f (Node x1 fe1 fd1) (Node x2 fe2 fd2)   = Node (f x1 x2) (overlap f fe1 fe2) (overlap f fd1 fd2)

breadthFirst :: Tree a -> [a]
breadthFirst t = bf [t]
    where
        bf [] = []
        bf (Empty:xs) = bf xs
        bf ((Node x tl tr):xs) = [x] ++ bf (xs ++ [tl, tr])

