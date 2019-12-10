import java.math.BigDecimal;
import java.util.Objects;

public class Slope {

    public float slope;
    public float b;

    public Slope(float slope, float b){
        this.slope = slope;
        this.b = b;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Slope slope1 = (Slope) o;
        return Float.compare(slope1.slope, slope) == 0 &&
                Float.compare(slope1.b, b) == 0;
    }

    public boolean hasAsteroid(Asteroid asteroid){
        return asteroid.cord_y == (this.slope*asteroid.cord_x + this.b);
    }

}
