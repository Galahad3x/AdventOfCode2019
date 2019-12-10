import java.util.Objects;

public class Displacement {

    public int horizontal;
    public int vertical;

    public Displacement(int horizontal, int vertical) {
        this.horizontal = horizontal;
        this.vertical = vertical;
    }

    public boolean is_proportional_to(Displacement other) {
        if (this.equals(other)) return true;
        if (this.horizontal == other.horizontal && this.horizontal == 0 || this.vertical == other.vertical && this.vertical == 0) {
            return true;
        }
        try{
            if (this.vertical % other.vertical == 0) {
                return this.horizontal / other.horizontal == this.vertical / other.vertical && this.horizontal % other.horizontal == 0;
            } else if (this.horizontal % other.horizontal == 0) {
                return this.horizontal / other.horizontal == this.vertical / other.vertical && this.horizontal % other.horizontal == 0;
            }
            return false;
        }catch (ArithmeticException a){
            if (other.horizontal == 0){
                return !(this.vertical > 0 && other.vertical < 0 || this.vertical < 0 && other.vertical > 0);
            }
            return !(this.horizontal > 0 && other.horizontal < 0 || this.horizontal < 0 && other.horizontal > 0);
        }

    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Displacement that = (Displacement) o;
        return horizontal == that.horizontal &&
                vertical == that.vertical;
    }

    public static Displacement getDisplacement(Asteroid comand, Asteroid other) {
        return new Displacement((int) (other.cord_x - comand.cord_x), (int) (other.cord_y - comand.cord_y));
    }
}
