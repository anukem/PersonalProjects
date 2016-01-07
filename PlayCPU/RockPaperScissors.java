import java.util.Scanner;
public class RockPaperScissors {

	public static void main(String[] args) {
		//Plays one game of Rock Paper Scissors
		
		//Display menu
		System.out.println("Welcome to the Rock/Paper/Scissors Showdown!");
		System.out.println("Choose 0 for Rock, 1 for Paper, 2 for Scissors ");
		int userRecord = 0 ;
		int computerRecord = 0;
	
		//start the game loop
		while(computerRecord < 10 || userRecord < 10) {
			
			//invoke the methods to get both answers
			int computerChoice = computerChoice();
			int userChoice = userChoice();
			
			
			//Computer: 1 is rock 2 is paper 3 is scissors
			//Human: 0 is rock 1 is paper 2 is scissors
			
			//All the possible outcomes if computer chooses rock
			if(computerChoice == 1 && userChoice == 0) {
							
				System.out.println("You tied! ");	
				System.out.println("Computer " + computerRecord);
				System.out.println("You: " + userRecord);
			}
			if(computerChoice == 1 && userChoice == 2) {
				
				System.out.println("The computer won! ");
				computerRecord ++;
				System.out.println("Computer: " + computerRecord);
				System.out.println("You: " + userRecord);
			}
			if(computerChoice == 1 && userChoice == 1) {
				System.out.println("You won! ");
				userRecord ++;
				System.out.println("Computer " + computerRecord);
				System.out.println("You: " + userRecord);
			}
			
			
			//All the possible outcomes if computer chooses paper
			if(computerChoice == 2 && userChoice == 2) {
				System.out.println("You won! ");
				userRecord ++;
				System.out.println("Computer: " + computerRecord);
				System.out.println("You: " + userRecord);
			}
			if(computerChoice == 2 && userChoice == 1) {
				
				System.out.println("You tied! ");
				System.out.println("Computer: " + computerRecord);
				System.out.println("You: " + userRecord);
			}
			if(computerChoice == 2 && userChoice == 0) {
				
				System.out.println("The computer won! ");
				computerRecord ++;
				System.out.println("Computer: " + computerRecord);
				System.out.println("You: " + userRecord);
			}
			
			
			
			//All the possible outcomes if computer chooses scissors
			if(computerChoice == 3 && userChoice == 1) {
				
				System.out.println("The computer won! ");
				computerRecord ++;
				System.out.println("Computer: " + computerRecord);
				System.out.println("You: " + userRecord);
			}
			if(computerChoice == 3 && userChoice == 0){
				
				System.out.println("You won! ");
				userRecord ++;
				System.out.println("Computer: " + computerRecord);
				System.out.println("You: " + userRecord);
			}
			if(computerChoice == 3 && userChoice == 2) {
							
				System.out.println("You tied! ");
				System.out.println("Computer: " + computerRecord);
				System.out.println("You: " + userRecord);
			}
			//End loop when game is over
			if(computerRecord == 10 || userRecord == 10 ) {
				System.out.println("Game over");
				break;
			}
		}


	}
		

	public static int computerChoice() {
		//Generates a random number between 1 and 3 and returns it as an int
		int choice = (int) (Math.random() * 3) + 1;
		return choice;
	}
	public static int userChoice() {
		//Prompts the user for a number between 1 and 3 using the Scanner Class
		Scanner input = new Scanner(System.in);
		System.out.print("Please choose a number ");
		int response = input.nextInt();
		return response;


	}
}