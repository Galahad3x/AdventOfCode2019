import Stack

main = do
    putStrLn "Helou gais"
    let x = Stack { stackPile = [0..9] }
        y = dealWithIncrement x 3
    putStrLn $ (show x) ++ "\n" ++ (show y)

dealWithIncrement :: Stack a -> Int -> Stack a
dealWithIncrement EmptyStack _ = EmptyStack
dealWithIncrement stack inc = dealWith (stackPile stack) inc

dealWith :: [a] -> Int -> Stack a
dealWith listS inc =    

listWithPositions :: Int -> Int -> [Int]
listWithPositions size inc = map (calculatePos size inc) longList
    where longList = take size [0,1..]

calculatePos :: Int -> Int -> Int-> Int
calculatePos size inc pos = ((pos+1)*inc) `mod` size

cutNcards :: Stack a -> Int -> Stack a
cutNcards EmptyStack _ = EmptyStack
cutNcards stack n = if n > 0 then cutN stack n else cutN stack ((size stack)+n)

cutN :: Stack a -> Int -> Stack a
cutN stack n = dealTogether topStack bottomStack
    where topStack = dealIntoNewStack (multiPop stack n)
          bottomStack = dealIntoNewStack2 stack n

dealTogether :: Stack a -> Stack a -> Stack a
dealTogether topS bottomS = dealIntoNew topS (dealIntoNewStack bottomS)

multiPop :: Stack a -> Int -> Stack a
multiPop EmptyStack _ = EmptyStack
multiPop stack x = if x == 0 then stack else multiPop (pop stack) (x-1) 

dealIntoNewStack :: Stack a -> Stack a
dealIntoNewStack EmptyStack = EmptyStack
dealIntoNewStack stack = dealIntoNew stack EmptyStack

dealIntoNew :: Stack a -> Stack a -> Stack a
dealIntoNew stackIn stackOut = if size stackIn == 0 then stackOut else dealIntoNew (pop stackIn) (push stackOut (fromJust (top stackIn)))

dealIntoNewStack2 :: Stack a -> Int -> Stack a
dealIntoNewStack2 EmptyStack _ = EmptyStack
dealIntoNewStack2 stack n = dealIntoNew2 stack EmptyStack n

dealIntoNew2 :: Stack a -> Stack a -> Int -> Stack a
dealIntoNew2 stackIn stackOut n = if size stackIn == 0 || n == 0 then stackOut else dealIntoNew2 (pop stackIn) (push stackOut (fromJust (top stackIn))) (n-1)

set' :: Int -> Int -> a -> [a] -> [a]
set' _ _ _ [] = []
set' ind curr new arr@(x:xs)
    | curr > ind = arr
    | ind == curr = new:(set' ind (curr+1) new xs)
    | otherwise = x:(set' ind (curr+1) new xs)

set :: Int -> a -> [a] -> [a]
set ind new arr = (set' ind 0 new arr)

