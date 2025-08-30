import java.util.Scanner;
public class InputType{
   public static void main(String[] args){
     Scanner sc=new Scanner(System.in);
     System.out.println("Enter the EmpID: ");
     int EmpID= sc.nextInt();
     System.out.println("Enter the Employee name: ");
     String Empname=sc.next();
     System.out.println("Enter the salary of Employee: ");
     float sal=sc.nextFloat();
     
     System.out.println("the empid: "+EmpID);
     System.out.println("the Emp name is: "+Empname);
     System.out.println("the Emp salary is: "+sal);
}
}