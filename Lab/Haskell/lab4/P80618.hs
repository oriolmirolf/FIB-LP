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

