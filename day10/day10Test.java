import org.junit.jupiter.api.Test;

import java.io.IOException;

import static org.junit.jupiter.api.Assertions.*;

class day10Test {
    @Test
    void puzzle() throws IOException {
        day10 day = new day10();
        day.part_one("/home/joel/Escriptori/AdventOfCode/day10/input.txt");
    }

    @Test
    void tests() throws IOException {
        day10 day = new day10();
        int medium = day.part_one("/home/joel/Escriptori/AdventOfCode/day10/medium_input.txt");
        assertEquals(33,medium);
        int hard = day.part_one("/home/joel/Escriptori/AdventOfCode/day10/hard_input.txt");
        assertEquals(210,hard);
    }

    @Test
    void easy() throws IOException{
        day10 day = new day10();
        int easy = day.part_one("/home/joel/Escriptori/AdventOfCode/day10/easy_input.txt");
        assertEquals(8,easy);
    }
}