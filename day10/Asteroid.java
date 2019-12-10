import java.util.Objects;

public class Asteroid {

    public float cord_x;
    public float cord_y;

    public Asteroid(float cord_x, float cord_y) {
        this.cord_x = cord_x;
        this.cord_y = cord_y;
    }

    public Slope getSlope(Asteroid monitoringStation) {
        float slope_m = (this.cord_y - monitoringStation.cord_y) / (this.cord_x - monitoringStation.cord_x);
        float slope_b = this.cord_y - slope_m*this.cord_x;
        return new Slope(slope_m,slope_b);
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Asteroid asteroid = (Asteroid) o;
        return Float.compare(asteroid.cord_x, cord_x) == 0 &&
                Float.compare(asteroid.cord_y, cord_y) == 0;
    }
}
