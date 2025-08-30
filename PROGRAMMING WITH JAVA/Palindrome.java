class Palindrome{
 public static void main(String[] args){
    int num=12321;
    int og=num;
    int rev=0;
    while(num!=0){
      int dig=num%10;
      rev=rev*10+dig;
      num=num/10;
      if(og==rev){
        System.out.println("The given num is palindrome");
      }
      else{
        System.out.println("the given num is not palindrome");
}
}
}
}