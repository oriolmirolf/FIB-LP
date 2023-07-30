import Data.List (sort)
type Pos = (Int, Int) 

dins :: Pos -> Bool
dins (x,y) = (1<=x && x<=8) && (1<=y && y<=8)

moviments :: Pos -> [Pos]
moviments (x, y) = filter dins [(x+2, y+1), (x+2, y-1), (x-2, y+1), (x-2, y-1), (x+1, y+2), (x+1, y-2), (x-1, y+2), (x-1, y-2)]

potAnar3 :: Pos -> Pos -> Bool
potAnar3 p q = any (==q) z
    where
        x = moviments p
        y = [(s,t)| r<-x, (s,t) <- moviments r]
        z = [(s,t)| r<-y, (s,t) <- moviments r]



potAnar3' :: Pos -> Pos -> Bool
potAnar3' p q = any (==q) l 
    where 
        l = moviments p >>= moviments >>= moviments