/**
 * Example of switch operation.
 * 
 * @version 1.0 2023-04-21
 * @author Zhao Chonghao
 */

public class A02_Switch {

    enum Size {
        SMALL, MEDIUM, LARGE, EXTRA_LARGE
    };

    public static void main(String[] args) {

        // Switch.
        int seasonCode = 2;
        String seasonName = switch (seasonCode) {
            case 0 -> "Spring";
            case 1 -> "Summer";
            case 2 -> "Fall";
            case 3 -> "Winter";
            default -> "???";
        };
        System.out.println("The season is " + seasonName + ".");

        // Multi switch.
        int numLetters = switch (seasonName) {
            case "Spring", "Summer", "Winter" -> 6;
            case "Fall" -> 4;
            default -> -1;
        };
        System.out.println("The number of letters in " + seasonName + " is " + numLetters + ".");

        // Enumerated case.
        Size itemSize = Size.LARGE;
        String label = switch (itemSize) {
            case SMALL -> "S"; // No need to use Size.SMALL
            case MEDIUM -> "M";
            case LARGE -> "L";
            case EXTRA_LARGE -> "XL";
            // and it's ok to omit default.
        };
        System.out.println("The size is " + label + ".");

    }
}
