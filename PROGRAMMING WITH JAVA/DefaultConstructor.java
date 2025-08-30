class Student{
   int rollno;
   String name;
   Student(){
     rollno=10;
     name="deepika";
}
  void display(){
   System.out.println("Roll No"+rollno+ " Name: "+name);
}
}
public class DefaultConstructor{
    public static void main(String[] args){
       Student s1=new Student();
       s1.display();
}
}
