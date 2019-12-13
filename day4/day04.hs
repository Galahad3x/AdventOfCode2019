import Data.List

input_start = 272091
input_end = 815432

main = do
    putStrLn "AdventOfCode: day04"
    putStrLn "Solutions should be 931 and 609"
    putStrLn "*---------------------------------------*"    
    putStrLn "Part one: "
    putStrLn $ show $ part_one input_start input_end
    putStrLn "Part two: "
    putStrLn $ show $ part_two input_start input_end

part_one :: Int -> Int -> Int
part_one start end
    | start == end = if good_pass start == True then 1 else 0
    | otherwise = if good_pass start == True then (1 + part_one (start+1) end) else part_one (start+1) end

good_pass :: Int -> Bool
good_pass x = has_atleast_2 (show x) && never_dec (show x)

has_atleast_2 :: String -> Bool
has_atleast_2 [] = False
has_atleast_2 (x:xs) = x `elem` xs || has_atleast_2 xs

never_dec :: String -> Bool
never_dec [] = True
never_dec (x:[]) = True
never_dec (x:xs) = if x <= foldr1 min xs then never_dec xs else False

has_only_2 :: String -> Int -> Bool
has_only_2 xs i = if i < length xs then length (elemIndices (xs!!i) xs) == 2 || (has_only_2 xs (i+1)) else False 

good_pass_2 :: Int -> Bool
good_pass_2 x = has_only_2 (show x) 0 && never_dec (show x)

part_two :: Int -> Int -> Int
part_two start end
    | start == end = if good_pass_2 start == True then 1 else 0
    | otherwise = if good_pass_2 start == True then (1 + part_two (start+1) end) else part_two (start+1) end
