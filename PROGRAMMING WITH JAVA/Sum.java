class Sum{
   public static void main(String args[]){
      int sum=0;
      int i;
      for(i=100;i<200;i++)
          if(i%7==0)
             sum+=i;
      System.out.println("the sum is=" +sum);
}
}