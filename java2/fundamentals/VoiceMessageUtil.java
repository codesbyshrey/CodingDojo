import java.util.Date;

public class VoiceMessageUtil {
     public String greeting() {
          return "Hello You";
     }
     public String greeting(String name){
          return "Hello " + name;
     } // this process is called overloading
     public String greeting(String name, Integer age) {
          return "Hello " + name + ", your Age is " + age;
     }

     public String getCurrentData() {
          Date today = new Date();
          return "Hey, the current date is: " + today;
     }

     public void getCurrentDateAsDate(){
          Date today = new Date();
          System.out.println(today);
     }

     public int totalMessages(int[] intArray) {
          int output = 0;
          for (int i = 0; i <intArray.length; i++){
               output += intArray[i];
          }
          return output;
     }

     public void printMessages(String[] msgArr) {
          // for (int i = 0; i <msgArr.length; i++){
          //       System.out.println( msgArr[i]);
          // }
          // return output;

          for (String message : msgArr) {
               System.out.println(message);
          }
     }
}