import java.util.Scanner;

class Student{
	String name;
	int id;
	
	Student(){
		name="abc";
		id=123;
	}

	Student(String name, int id){
		this.name=name;
		this.id=id;
	}

 	Student(Student st){
		name=st.name;
		id=st.id;
	}

	void display(){
		System.out.println("name " + name +" id "+id);
	}
}
public class Constructor{
	public static void main(String[] args){
		Student s1 =new Student();
		s1.display();
		Student s2 =new Student("abcd" , 112233);
		s2.display();
		Student s3 =new Student(s2);
		s3.display();
}
}