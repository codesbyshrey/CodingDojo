import java.util.ArrayList;

public class Test {
     // entry point
     public static void main (String[] args ) {
          Developer dev = new Developer(); 
          System.out.println(dev);

          // won't have access to these once developer is privatized --> getters and setters in developer
          dev.setName("Shreyas");
          dev.setWorkingHours(40);
          dev.setSalary(120000.52);
          // dev.languages = new ArrayList<String>(); //don't forget to initialize
          // isn't the test's job to initialize, its the class job
          dev.languages.add("Python");
          dev.languages.add("JavaScript");
          dev.languages.add("Java");

          //

          Project project1 = new Project();
          project1.title = "Navigation";
          project1.language = "Java";

          Project project2 = new Project();
          project2.title = "DojoCommerce";
          project2.language = "Python";

          dev.addProject(project1);
          dev.addProject(project2);
          
          dev.displayStatus();

          System.out.println("-----------------------------------");
          Developer dev1 = new Developer("Shreyas2", 34, 120000.53);
          dev1.addProject(project1);
          dev1.displayStatus();

          // AFTERNOON LECTURE MATERIAL --> STATIC VARIABLES AND METHODS

          System.out.println("Dev Counter: " + Developer.getDevCount());
          
          //240K --> we want 260K
          dev1.setSalary(140000);

          System.out.println("Total salary from all developers: " + Developer.getTotalSalary());
          System.out.println("Total Projects: " + Developer.getTotalProjects());
     }
}