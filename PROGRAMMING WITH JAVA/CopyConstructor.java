class Student{
   int rollno;
   String name;
   Student(int r,String n){
      this.rollno=r;
      this.name=n;
}
Student(Student s){
   rollno=s.rollno;
   name=s.name;
}
void display(){
    System.out.println("Roll no: "+ rollno +" Name: "+name);
}
}
public class CopyConstructor{
  public static void main(String[] args){
     Student s1=new Student(101,"Deepika");
     Student s2=new Student(s1);
     s1.display();
     s2.display();
}
}