// import VoiceMessageUtil.printMessages;
// import VoiceMessageUtil.totalMessages;
public class JavaBasic {
     // our entry point to the function, need a main method
     // public - access modifier --> allows things outside class to call it
     // static --> tied to the class itself directly, don't have to reinstantiate the class
          // can just call JavaBasic.main();
     public static void main (String[] args) {
          VoiceMessageUtil voiceMessageUtil = new VoiceMessageUtil();

          System.out.println("Hello World");

          // VARIABLE DECLARATIONS
          String firstName = "Shreyas";
          String lastName = "Sriram";
          int age = 25;
          boolean isStudent = true;
          double weight = 175.52;
          char grade = 'A';
          System.out.println(firstName + " " + lastName); // have to be expanded
          System.out.println(age + "\n" + isStudent + "\n" + weight);
          System.out.println(Integer.MAX_VALUE);

          // CONDITIONALS
          if (weight < 100) {
               System.out.println("You have to gain some weight");
          } else {
               System.out.println("You are gucci gang");
               // our conditionals need to be considered as true or false
          }

          System.out.println(weight < 100 ? "Gain some weight" : "You're good");

          // MORE ON STRINGS

          String name = "Calvin Leong";
          System.out.println(name.length());

          String fullName = firstName.concat(lastName);
          System.out.println(fullName);

          String greeting = String.format("HELLO GREETINGS %s, you are %d years old", fullName, age);
          System.out.println(greeting);
          System.out.printf("Hi %s, you are %d years old \n", fullName, age);

          //CREATING A STRING
          String firstName1 = "Omar";
          String firstName2 = new String("Omar");
          String firstName3 = "Omar";

          System.out.println(firstName1 == firstName2); //false (backend to frontend input)
          System.out.println(firstName1 == firstName3); //true

          System.out.println(firstName1.equals(firstName2));
          System.out.println(firstName2.equals(firstName3));//wrapper classes, data from the frontend
          // gets the value of the string = value of the string in number2 (works both ways)

          // FIXED ARRAYS

          int[] messagesPerDay = new int[5];
          messagesPerDay[0] = 5;
          messagesPerDay[1] = 5;
          messagesPerDay[2] = 5;
          messagesPerDay[3] = 3;
          messagesPerDay[4] = 4;

          for (int i=0; i<messagesPerDay.length; i++) {
               System.out.println(messagesPerDay[i]);
          }

          int[] messagesPeryDay = {5, 4, 6};
          messagesPeryDay[2] = 25;

          String[] messages = {"String1", "String2", "String3"};

          for (int i=0; i<messagesPeryDay.length; i++) {
               System.out.println(messagesPeryDay[i]);
          }

          // for (int i=0; i<messages.length; i++) {
          //      System.out.println(messages[i]);
          // }

          System.out.println(voiceMessageUtil.totalMessages(messagesPeryDay));
          voiceMessageUtil.printMessages(messages);

          // REWATCH LECTURE VIDEO AND FILL IN THE BLANKS HERE FOR DYNAMIC ARRAYS

          // DAY 2 - OOP (might be a separate file)
     }
}
