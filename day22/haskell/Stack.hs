module Stack(
Stack(..),
push,
top,
pop,
size,
fromJust
)where


data Stack a = EmptyStack | Stack { stackPile :: [a] } deriving (Show, Eq)

push :: Stack a -> a -> Stack a
push EmptyStack elem = Stack { stackPile = [elem] }
push stack elem = Stack { stackPile = elem:(stackPile stack) }

top :: Stack a -> Maybe a
top EmptyStack = Nothing
top stack = Just $ head (stackPile stack)

pop :: Stack a -> Stack a
pop EmptyStack = EmptyStack
pop stack = if (size stack) == 1 then EmptyStack else Stack { stackPile = tail (stackPile stack) }

size :: Stack a -> Int
size EmptyStack = 0
size stack = length $ stackPile stack

fromJust :: Maybe a -> a
fromJust Nothing = error "Something went wrong"
fromJust (Just x) = x 

