import org.junit.jupiter.api.Test;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

class ShufflerTest {

    @Test
    void shuffle_into_new_deck_test() {
        Shuffler shuffle = new Shuffler(10);
        ArStack<Integer> first = new ArStack<>();
        List<Integer> firstElems = List.of(9, 8, 7, 6, 5, 4, 3, 2, 1, 0);
        for (Integer elem : firstElems) {
            first.push(elem);
        }
        assertEquals(first.getStackArray(), new ArrayList<>(List.of(9, 8, 7, 6, 5, 4, 3, 2, 1, 0)));
        ArStack<Integer> second = shuffle.dealIntoNewStack(first);
        assertEquals(second.getStackArray(), new ArrayList<>(List.of(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)));
    }

    @Test
    void cutN_positive_test() {
        Shuffler shuffle = new Shuffler(10);
        ArStack<Integer> first = new ArStack<>();
        List<Integer> firstElems = List.of(9, 8, 7, 6, 5, 4, 3, 2, 1, 0);
        for (Integer elem : firstElems) {
            first.push(elem);
        }
        ArStack<Integer> second = shuffle.cutN(first, 3);
        assertEquals(second.getStackArray(), new ArrayList<>(List.of(2, 1, 0, 9, 8, 7, 6, 5, 4, 3)));
    }

    @Test
    void cutN_negative_test() {
        Shuffler shuffle = new Shuffler(10);
        ArStack<Integer> first = new ArStack<>();
        List<Integer> firstElems = List.of(9, 8, 7, 6, 5, 4, 3, 2, 1, 0);
        for (Integer elem : firstElems) {
            first.push(elem);
        }
        ArStack<Integer> second = shuffle.cutN(first, -4);
        assertEquals(second.getStackArray(), new ArrayList<>(List.of(5, 4, 3, 2, 1, 0, 9, 8, 7, 6)));
    }

    @Test
    void ArStack_from_list() {
        List<Integer> inits = List.of(9, 8, 7, 6, 5, 4, 3, 2, 1, 0);
        ArStack<Integer> stack = new ArStack<>(inits);
        assertEquals(stack.getStackArray(), inits);
    }

    @Test
    void deal_with_increment_test() {
        Shuffler shuffle = new Shuffler(10);
        List<Integer> firstElems = List.of(9, 8, 7, 6, 5, 4, 3, 2, 1, 0);
        ArStack<Integer> first = new ArStack<>(firstElems);
        ArStack<Integer> second = shuffle.dealWithIncrement(first, 3);
        assertEquals(second.getStackArray(), new ArrayList<>(List.of(3, 6, 9, 2, 5, 8, 1, 4, 7, 0)));
    }

    @Test
    void easy_case() throws IOException {
        Shuffler shuffle = new Shuffler(10);
        BufferedReader br = new BufferedReader(new FileReader("easy.txt"));
        ArStack<Integer> stack = new ArStack<>(List.of(9, 8, 7, 6, 5, 4, 3, 2, 1, 0));
        ArStack<Integer> endS = shuffle.doTheShuffle(stack, br);
        assertEquals(endS.getStackArray(), new ArrayList<>(List.of(7, 4, 1, 8, 5, 2, 9, 6, 3, 0)));
    }

    @Test
    void hard_case() throws IOException {
        Shuffler shuffle = new Shuffler(10);
        BufferedReader br = new BufferedReader(new FileReader("hard.txt"));
        ArStack<Integer> stack = new ArStack<>(List.of(9, 8, 7, 6, 5, 4, 3, 2, 1, 0));
        ArStack<Integer> endS = shuffle.doTheShuffle(stack, br);
        assertEquals(endS.getStackArray(), new ArrayList<>(List.of(6, 3, 0, 7, 4, 1, 8, 5, 2, 9)));
    }

    @Test
    void part1() throws IOException {
        Shuffler shuffle = new Shuffler(10007);
        BufferedReader br = new BufferedReader(new FileReader("input.txt"));
        ArStack<Integer> stack = new ArStack<>();
        int i = 10006;
        while (i >= 0) {
            stack.push(i);
            i--;
        }
        System.out.println(stack.getStackArray());
        ArStack<Integer> endS = shuffle.doTheShuffle(stack, br);
        System.out.println(endS.getStackArray());
        System.out.println(10006 - endS.getStackArray().indexOf(2019));
    }

    @Test
    void part2() throws IOException {
        Shuffler shuffle = new Shuffler((int) 119315717514047L);
        ArStack<Integer> stack = new ArStack<>();
        long i = 119315717514047L;
        while (i >= 0) {
            stack.push((int) i);
            i--;
        }
        ArStack<Integer> endS = shuffle.doTheShuffle(stack, new BufferedReader(new FileReader("input.txt")));
        long shuffleCounter = 0;
        while (shuffleCounter < 101741582076660L) {
            endS = shuffle.doTheShuffle(endS, new BufferedReader(new FileReader("input.txt")));
            shuffleCounter++;
            System.out.println("Everyday i'm shuffling");
        }
        System.out.println(endS.getStackArray().get((int) (119315717514047L - 2020L)));
    }
}