data Expr = Val Int | Add Expr Expr | Sub Expr Expr | Mul Expr Expr | Div Expr Expr

eval1 :: Expr -> Int
eval1 (Val x)       = x
eval1 (Add e1 e2)   = eval1 e1 + eval1 e2
eval1 (Sub e1 e2)   = eval1 e1 - eval1 e2
eval1 (Mul e1 e2)   = eval1 e1 * eval1 e2
eval1 (Div e1 e2)   = div (eval1 e1)  (eval1 e2)

eval2 :: Expr -> Maybe Int
eval2 (Val x) = return x
eval2 (Add e1 e2) = evalAux (+) e1 e2
eval2 (Sub e1 e2) = evalAux (-) e1 e2
eval2 (Mul e1 e2) = evalAux (*) e1 e2
eval2 (Div e1 e2) = do
    v1 <- eval2 e1
    v2 <- eval2 e2
    case v2 of
        0 -> Nothing
        _ -> return (div v1 v2)
 
evalAux :: (Int -> Int -> Int) -> Expr -> Expr -> Maybe Int
evalAux op e1 e2 = do
    v1 <- eval2 e1
    v2 <- eval2 e2
    return (op v1 v2)

eval3 :: Expr -> Either String Int
eval3 (Val x) = return x
eval3 (Add e1 e2) = evalAux2 (+) e1 e2
eval3 (Sub e1 e2) = evalAux2 (-) e1 e2
eval3 (Mul e1 e2) = evalAux2 (*) e1 e2
eval3 (Div e1 e2) = do
    v1 <- eval3 e1
    v2 <- eval3 e2
    case v2 of
        0 -> Left "div0"
        _ -> return (div v1 v2)
 
evalAux2 :: (Int -> Int -> Int) -> Expr -> Expr -> Either String Int
evalAux2 op e1 e2 = do
    v1 <- eval3 e1
    v2 <- eval3 e2
    return (op v1 v2)