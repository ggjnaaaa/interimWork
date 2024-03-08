import java.util.Map;

/**
 * program
 */
public class Program {
    public static void main(String[] args) {
        InputManager im = new InputManager("input.txt");

        System.out.println("\nВсего слов: " + im.getCountWords());

        System.out.println("\nСамое длинное слово: " + im.getLongestWord());

        System.out.println("\nЧастота слов: ");
        for (Map.Entry<String, Integer> entry : im.getFrequencyWords().entrySet()) {
            System.out.println(entry.getKey() + " : " + entry.getValue());
        }
    }
    
}