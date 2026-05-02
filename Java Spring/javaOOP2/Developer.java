import java.util.ArrayList;

public class Developer {
     // ATTRIBUTES (private/protected) -------------------------------------
     // want them to be private (means we need getters and setters)
     // more we address inside the class, the better we can focus on logic in our test file
     private String name;
     private int workingHours;
     private double salary;

     // STATIC VARIABLES ----------------------------------------------------
     private static int devCount;
     private static double totalSalary;
     private static int totalProjects;

     //tied to the class itself, not every instantiation

     public ArrayList<String> languages;
     public ArrayList<Project> projects = new ArrayList<Project>();
          // don't forget to initialize in the class to declare 

     // CONSTRUCTOR METHOD (attributes first, methods after)
     // we could have overloaded constructors (think about game development)
     public Developer(){
          this.languages = new ArrayList<String>();
          this.projects = new ArrayList<Project>();
          Developer.devCount++;
          Developer.totalSalary += salary;
     }

     public Developer(String name, int workingHours, double salary) {
          this.name = name;
          this.workingHours = workingHours;
          this.salary = salary;
          this.languages = new ArrayList<String>();
          this.projects = new ArrayList<Project>();
          Developer.devCount++;
          Developer.totalSalary += salary;
     }

     // METHODS --------------------------------------------------------

     // GETTERS AND SETTERS-------------------------------------------
     public String getName(){
          return this.name;
     }
     public void setName(String name){
          this.name = name;
     }
     public int getWorkingHours(){
          return this.workingHours;
     }
     public void setWorkingHours(int workingHours){
          this.workingHours = workingHours;
     }
     public double getSalary(){
          return this.salary;
     }
     public void setSalary(double salary){
          Developer.totalSalary -= this.salary;
          Developer.totalSalary += salary;
          this.salary = salary;
     }


     // STATIC METHODS -----------------------
     public static int getDevCount(){
          return devCount;
     }
     public static double getTotalSalary(){
          return Developer.totalSalary;
     }
     public static int getTotalProjects(){
          return Developer.totalProjects;
     }

     // NON TRADITIONAL METHODS ---------------------------------------------

     public void addProject(Project project) {
          this.projects.add(project);
          Developer.totalProjects += 1; //Developer.totalProjects++;
     }

     public void displayStatus() {
          System.out.println("Name: " + this.name);
          System.out.println("workingHours: " + this.workingHours);
          System.out.println("salary: " + this.salary);
          System.out.println("languages: " + this.languages);
          System.out.println("projects: " + this.projects);
          //still getting location at memory

          for (Project project : this.projects) {
               project.displayInfo();
          }
     }

     //NullPointerException --> using dot notation from array list class

     // public static void main (String[] args) {
           // attributes and methods
           // constructors, getters, setters
     // }
}