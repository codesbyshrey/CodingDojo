import java.util.ArrayList;

public class Test {
     // entry point
     public static void main (String[] args ) {
          Developer dev = new Developer(); 
          System.out.println(dev);

          dev.name = "Shreyas";
          dev.workingHours = 40;
          dev.salary = 120000.52;
          dev.languages = new ArrayList<String>(); //don't forget to initialize
          // isn't the test's job to initialize, its the class job
          dev.languages.add("Python");
          dev.languages.add("JavaScript");
          dev.languages.add("Java");

          

          Project project1 = new Project();
          project1.title = "Navigation";
          project1.language = "Java";

          Project project2 = new Project();
          project2.title = "DojoCommerce";
          project2.language = "Python";

          dev.addProject(project1);
          dev.addProject(project2);
          
          dev.displayStatus();
     }
}