import java.util.Scanner;

public class mathSkills {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        //data initialization
        int diff;


        System.out.println("Welcome to the mathskillz, where your math skills is challenged.");
        System.out.println("What difficulty would you like to play in ?(1 = easy, 2 = medium, 3 = hard):");
        diff = input.nextInt();

        switch (diff) {
            case 1:
                System.out.println("You chose easy mode"); 
                break;
            case 2:
                System.out.println("You chose medium mode");
                break;
            case 3:
                System.out.println("You chose hard mode");
                break;
            default:
                break;
        }



    }
}
