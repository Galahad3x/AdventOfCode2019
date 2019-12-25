import java.io.BufferedReader;
import java.io.IOException;
import java.util.ArrayList;

public class Shuffler {

    public int sizeOfDeck;

    public Shuffler(int sizeOfDeck) {
        this.sizeOfDeck = sizeOfDeck;
    }

    public <E> ArStack<E> dealIntoNewStack(ArStack<E> in) {
        ArStack<E> newS = new ArStack<>();
        int size = in.size();
        for (int i = 0; i < size; i++) {
            newS.push(in.pop());
        }
        return newS;
    }

    public <E> ArStack<E> cutN(ArStack<E> in, int N) {
        ArStack<E> newS = new ArStack<>();
        ArStack<E> tempS = new ArStack<>();
        if (N >= 0) {
            for (int i = 0; i < N; i++) {
                tempS.push(in.pop());
            }
            int tempSize = tempS.size();
            for (int i = 0; i < tempSize; i++) {
                newS.push(tempS.pop());
            }
            int size = in.size();
            for (int i = 0; i < size; i++) {
                tempS.push(in.pop());
            }
            tempSize = tempS.size();
            for (int i = 0; i < tempSize; i++) {
                newS.push(tempS.pop());
            }
        } else {
            for (int i = 0; i < (N + sizeOfDeck); i++) {
                tempS.push(in.pop());
            }
            int tempSize = tempS.size();
            for (int i = 0; i < tempSize; i++) {
                newS.push(tempS.pop());
            }
            int size = in.size();
            for (int i = 0; i < size; i++) {
                tempS.push(in.pop());
            }
            tempSize = tempS.size();
            for (int i = 0; i < tempSize; i++) {
                newS.push(tempS.pop());
            }
        }
        return newS;
    }

    public <E> ArStack<E> dealWithIncrement(ArStack<E> in, int increment) {
        ArrayList<E> result = new ArrayList<>(sizeOfDeck);
        for (int j = 0; j < sizeOfDeck; j++) {
            result.add(null);
        }
        int i = 0;
        while (!in.isEmpty()) {
            result.set(sizeOfDeck - 1 - (i * increment) % sizeOfDeck, in.pop());
            i++;
        }
        return new ArStack<>(result);
    }

    public <E> ArStack<E> doTheShuffle(ArStack<E> stack, BufferedReader br) throws IOException {
        String operation;
        while ((operation = br.readLine()) != null) {
            if (operation.split(" ")[0].equals("cut")) {
                stack = this.cutN(stack, Integer.parseInt(operation.split(" ")[1]));
            } else if (operation.split(" ")[0].equals("deal")) {
                if (operation.split(" ")[1].equals("with")) {
                    stack = this.dealWithIncrement(stack, Integer.parseInt(operation.split(" ")[3]));
                } else {
                    stack = this.dealIntoNewStack(stack);
                }
            }
        }
        return stack;
    }
}
