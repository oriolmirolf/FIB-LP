main :: IO ()
main = do
  -- Llegir l'entrada estàndard
  input <- getContents
  -- Convertir la cadena d'entrada en una llista d'enters
  let numbers = map read (words input) :: [Int]
  -- Calcular la suma dels enters i mostrar el resultat
  putStrLn $ show $ sum numbers
