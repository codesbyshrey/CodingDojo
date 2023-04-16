public class Test {
     public static void main (String[] args) {
          VoiceMessageUtil voiceMessageUtil = new VoiceMessageUtil();

          System.out.println(voiceMessageUtil.greeting());
          System.out.println(voiceMessageUtil.greeting("Shreyas"));
          System.out.println(voiceMessageUtil.greeting("Shrey", 25));

          System.out.println(voiceMessageUtil.getCurrentData());
          voiceMessageUtil.getCurrentDateAsDate();
     }
}