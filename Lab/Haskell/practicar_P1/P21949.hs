main :: IO ()
main = do
    input <- getLine
    fesCoses input

fesCoses :: String -> IO ()
fesCoses input = hanoi (read n :: Int) o d a
    where
        [n, o, d, a] = words input

hanoi :: Int -> String -> String -> String -> IO ()
hanoi 0 _ _ _ = return ()
hanoi n o d a = do
    hanoi (n-1) o a d
    putStrLn (o ++ " -> " ++ d) 
    hanoi (n-1) a d o
