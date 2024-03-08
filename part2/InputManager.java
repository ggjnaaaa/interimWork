import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;

public class InputManager {
    String[] words;

    public InputManager(String inputPath) {
        this.words = getInputData(inputPath);
    }

    // Чтение файла
    private String[] getInputData(String inputPath) {
        try (BufferedReader br = new BufferedReader(new FileReader(inputPath));) {
            StringBuilder sb = new StringBuilder();
            String line = br.readLine();

            while (line != null) {
                sb.append(line);
                sb.append(System.lineSeparator());
                line = br.readLine();
            }

            return sb.toString().replaceAll("\\s+", " ").split(" ");
        }
        catch(IOException e) {
            System.out.println("Файл не найден");
            return null;
        }
    }

    // Количество слов
    public Integer getCountWords() {
        return words.length;
    }

    // Поиск самого длинного слова
    public String getLongestWord() {
        Integer max = 0;
        String maxWord = "";
        for (String string : words)
            if (string.length() >= max) {
                max = string.length();
                maxWord = string;
            }

        return maxWord;
    }

    // Подсчет частоты слов
    public HashMap<String, Integer> getFrequencyWords() {
        HashMap<String, Integer> frequency = new HashMap<>();

        for (String string : words)
            if (frequency.containsKey(string)) 
                frequency.put(string, frequency.get(string) + 1);
            else
                frequency.put(string, 1);

        return frequency;
    }
}
