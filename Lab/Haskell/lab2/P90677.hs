myFoldl :: (a -> b -> a) -> a -> [b] -> a
myFoldl f acc [] = acc
myFoldl f acc (x:xs) = myFoldl f (f acc x) xs

myFoldr :: (a -> b -> b) -> b -> [a] -> b
myFoldr f acc [] = acc
myFoldr f acc (x:xs) = f x (myFoldr f acc xs)

myIterate :: (a -> a) -> a -> [a]
myIterate f x = x : myIterate f (f x)

myUntil :: (a -> Bool) -> (a -> a) -> a -> a
myUntil b f n  
    | b n       = n
    | otherwise = myUntil b f (f n)
            
myMap :: (a -> b) -> [a] -> [b]
myMap f [] = []
myMap f (x:xs) = (f x) : myMap f xs

myFilter :: (a -> Bool) -> [a] -> [a]
myFilter b [] = []
myFilter b (x:xs)
    | b x       = x : myFilter b xs
    | otherwise = myFilter b xs

myAll :: (a -> Bool) -> [a] -> Bool
myAll b xs = foldr (\x acc -> b x && acc) True xs

myAny :: (a -> Bool) -> [a] -> Bool
myAny b xs = foldr (\x acc -> b x || acc) False xs

myZip :: [a] -> [b] -> [(a, b)]
myZip _ [] = []
myZip [] _ = []
myZip (x:xs) (y:ys) = (x, y) : myZip xs ys

myZipWith :: (a -> b -> c) -> [a] -> [b] -> [c]
myZipWith f _ [] = []
myZipWith f [] _ = []
myZipWith f (x:xs) (y:ys) = (f x y) : myZipWith f xs ys
