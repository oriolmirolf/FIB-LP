# Problema 1

eval1 :: String -> Int
eval1 input = recResolve [] (words input)

recResolve :: [Int] -> [String] -> Int
recResolve L (H:T)
    | isDigit H   = recResolve ((read(H) :: Int) : L) T
    | otherwise = recResolve ((applyOp H (head L) (head tail L))) T

applyOp :: Char -> Int -> Int