import Stack

main = do
    let deck = Stack { stackPile = [0,1..10006] }
    cardloop deck

cardloop :: Stack Int -> IO ()
cardloop deck = do
    line <- getLine
    if null line  
        then do
            print (searchPosOfCard (stackPile deck) 2019)
            return ()
        else do
            if "deal" == (words line)!!0
                then if "into" == (words line)!!1
                         then do
                             putStrLn line
                             let deck2 = dealIntoNewStack deck
                             print (deck2 :: Stack Int)
                             cardloop deck2
                         else do
                             putStrLn line
                             let deck2 = dealWithIncrement deck (read ((words line)!!3))
                             print (deck2 :: Stack Int)
                             cardloop deck2
                else do
                    putStrLn line
                    let deck2 = cutNcards deck (read ((words line)!!1))
                    print (deck2 :: Stack Int)
                    cardloop deck2

searchPosOfCard :: (Eq a) => [a] -> a -> Maybe Int
searchPosOfCard [] _ = Nothing
searchPosOfCard xs elemn = if elemn `elem` xs then Just (posOfCard xs elemn 0) else Nothing

posOfCard :: (Eq a) => [a] -> a -> Int -> Int
posOfCard (x:xs) elm pos = if x == elm then pos else posOfCard xs elm pos+1 

dealWithIncrement :: Stack a -> Int -> Stack a
dealWithIncrement EmptyStack _ = EmptyStack
dealWithIncrement stack inc = dealWith (stackPile stack) inc

dealWith :: [a] -> Int -> Stack a
dealWith listS inc = Stack { stackPile = dwith listS resList inc 0 }
    where resList = replicate (length listS) listS!!0

type Counter = Int

dwith :: [a] -> [a] -> Int -> Counter -> [a]
dwith [] _ _ _ = []
dwith listS resList inc counter = if counter == length resList then resList else dwith listS (set (listWithPos!!counter) (listS!!counter) resList) inc (counter+1)
   where listWithPos = listWithPositions (length listS) inc

listWithPositions :: Int -> Int -> [Int]
listWithPositions size inc = map (calculatePos size inc) longList
    where longList = take size [0,1..]

calculatePos :: Int -> Int -> Int-> Int
calculatePos size inc pos = (pos*inc) `mod` size

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

