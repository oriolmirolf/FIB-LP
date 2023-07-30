flatten :: [[Int]] -> [Int]
flatten xs = foldl (++) [] xs

myLength :: String -> Int
myLength xs = foldl (+) 0 (map (const 1) xs)

myLength2 :: String -> Int
myLength2 x = foldl (\x _ -> x+1) 0 x

myReverse :: [Int] -> [Int]
myReverse xs = foldl (\x y -> y:x) [] xs

countIn :: [[Int]] -> Int -> [Int]
countIn xs y = map (length . filter (== y)) xs

firstWord :: String -> String
firstWord xs = takeWhile (/= ' ') (dropWhile (== ' ') xs)