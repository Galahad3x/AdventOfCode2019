import java.util.ArrayList;
import java.util.List;

public class ArStack<E> implements BaseStack<E> {
    private ArrayList<E> stackArray;
    private int topOfStack;

    public ArStack() {
        stackArray = new ArrayList<E>();
        topOfStack = -1;
    }

    public ArStack(List<E> init) {
        stackArray = new ArrayList<E>();
        topOfStack = -1;
        for (E elem : init){
            this.push(elem);
        }
    }

    @Override
    public void push(E element) {
        stackArray.add(element);
        topOfStack++;

    }

    @Override
    public E pop() {
        if (isEmpty()) {
            throw new IllegalStateException("EmptyStack");
        }
        E res = stackArray.get(topOfStack);
        stackArray.remove(topOfStack);
        topOfStack--;
        return res;

    }

    @Override
    public E top() {
        if (isEmpty()) {
            throw new IllegalStateException("EmptyStack");
        }
        return stackArray.get(topOfStack);
    }

    @Override
    public int size() {
        return stackArray.size();
    }

    @Override
    public boolean isEmpty() {
        return stackArray.isEmpty();
    }

    public ArrayList<E> getStackArray() {
        return stackArray;
    }
}