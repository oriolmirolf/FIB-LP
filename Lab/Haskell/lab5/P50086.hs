data Queue a = Queue [a] [a]
     deriving (Show)
 
create :: Queue a
create = Queue [] []

push :: a -> Queue a -> Queue a
push x (Queue ll lr) = Queue ll (x:lr)

pop :: Queue a -> Queue a
pop (Queue (x:ll) lr)   = Queue ll lr
pop (Queue [] lr)       = Queue (tail $ reverse lr) []

top :: Queue a -> a
top (Queue [] lr)   = last lr
top (Queue ll _)    = head ll

empty :: Queue a -> Bool
empty (Queue [] []) = True
empty (Queue _ _)   = False

instance Eq a => Eq (Queue a)
    where
        (Queue ll1 lr1) == (Queue ll2 lr2) = (ll1 ++ reverse lr1) == (ll2 ++ reverse lr2)

instance Functor (Queue) where
    fmap f (Queue l r) = Queue (map f l) (map f r)

translation :: Num b => b -> Queue b -> Queue b
translation f q = fmap (+f) q

unio :: Queue a -> Queue a -> Queue a
unio (Queue lx rx) (Queue ly ry) = Queue (lx ++ reverse rx ++ ly ++ reverse ry) []

instance Applicative Queue where
    pure x = Queue [x] []
    Queue lf rf <*> Queue lx rx = Queue (lf <*> lx) (rf <*> rx)

instance Monad Queue where
    return              = pure
    Queue [] [] >>= _ = Queue [] []
    Queue (x:xs) rs >>= f = unio (f x) (Queue xs rs >>= f)
    Queue [] rs >>= f = Queue (reverse rs) [] >>= f

kfilter :: (p -> Bool) -> Queue p -> Queue p
kfilter b q = do
    x <- q
    if b x
        then return x
        else (Queue [] [])


