class SwitchDemo{
  public static void main(String[] args){
     int marks=Integer.parseInt(args[0]);
     switch(marks/10){
         case 10:
         case 9:
         case 8:
         System.out.println("excellent");
         break;
         case 7:
         System.out.println("veryGood");break;
         case 6:
         System.out.println("good");break;
         case 5:
         System.out.println("workhard");break;
         case 4:
         System.out.println("Poor");break;
         case 3:
         case 2:
         case 1:
         case 0:
         System.out.println("Verypoor");break;
         default:
         System.out.println("invalid input");
       }
}
  }      