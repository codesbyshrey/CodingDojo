import java.util.ArrayList;

public class Developer {
     // ATTRIBUTES
     public String name;
     public int workingHours;
     public double salary;
     public ArrayList<String> languages;
     public ArrayList<Project> projects = new ArrayList<Project>();
          // don't forget to initialize in the class to declare 

     // METHODS
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

     public void addProject(Project project) {
          this.projects.add(project);
     }

     //NullPointerException --> using dot notation from array list class

     // public static void main (String[] args) {
           // attributes and methods
           // constructors, getters, setters
     // }
}