public interface BaseStack<E> {
    void push(E element);

    E pop();

    E top();

    int size();

    boolean isEmpty();
}