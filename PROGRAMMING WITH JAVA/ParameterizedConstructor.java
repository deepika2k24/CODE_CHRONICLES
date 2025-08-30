class Student{
       int rollno;
       String name;
   Student(int r,String n){
       rollno=r;
       name=n;
}
   void display(){
   System.out.println("Roll No: "+rollno+ "Name: "+name);
}
}
public class ParameterizedConstructor{
 public static void main(String[] args){
    Student s1=new Student(101,"DEEPIKA");
    Student s2=new Student(102,"Deepi");
    Student s3=new Student(103,"dimpy");
    s1.display();
    s2.display();
    s3.display();
}
}