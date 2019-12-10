import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.LinkedList;

public class day10 {

    public LinkedList<Asteroid> asteroids = new LinkedList<>();

    public int part_one(String file_route) throws IOException {
        BufferedReader fr = new BufferedReader(new FileReader(file_route));
        String st;
        int cord_y = 0;
        while ((st = fr.readLine()) != null) {
            for (int i = 0; i < st.length(); i++) {
                if (st.charAt(i) == '#') {
                    asteroids.add(new Asteroid(i, cord_y));
                }
            }
            cord_y++;
        }
        int max_detectable = 0;
        for (Asteroid asteroid : asteroids) {
            int current = detectableFrom(asteroid);
            if (current > max_detectable) max_detectable = current;
        }
        System.out.println(max_detectable);
        return max_detectable;
    }

    private int detectableFrom(Asteroid asteroid) {
        LinkedList<Slope> slopes = new LinkedList<>();
        int detectable_from = 0;
        for (Asteroid current_ast : asteroids) {
            if (!current_ast.equals(asteroid)) {
                boolean visible = true;
                for(Slope current_slope : slopes){
                    if (current_slope.hasAsteroid(current_ast)){
                        visible = false;
                    }
                }
                if(visible){
                    slopes.add(asteroid.getSlope(current_ast));
                    detectable_from++;
                }
            }
        }
        return detectable_from;
    }

    private int detectable(Asteroid asteroid) {
        LinkedList<Displacement> displacements = new LinkedList<>();
        int detectable_from = 0;
        for (Asteroid current_ast : asteroids) {
            if (!current_ast.equals(asteroid)) {
                boolean visible = true;
                for(Displacement current_disp : displacements){
                    if (current_disp.is_proportional_to(Displacement.getDisplacement(asteroid,current_ast))){
                        visible = false;
                    }
                }
                if(visible){
                    displacements.add(Displacement.getDisplacement(asteroid,current_ast));
                    detectable_from++;
                }
            }
        }
        return detectable_from;
    }
}

