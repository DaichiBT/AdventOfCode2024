import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.lang.String;
import java.util.Scanner;

public class Day01 {
    public static void main(String[] args) {
        ArrayList<String> file = getFileData("src/Day01Input.txt");
        ArrayList<String> leftCol = new ArrayList<String>();
        ArrayList<Integer> rightCol = new ArrayList<Integer>();

        for (String line : file) {
//            String a = line.substring(0, line.indexOf(' '));
//            String b = line.substring(line.indexOf(' '), line.length() - 1);
/*            leftCol.add();*/
            System.out.println(line);
        }

    }

    public static ArrayList<String> getFileData(String fileName) {
        ArrayList<String> fileData = new ArrayList<String>();
        try {
            File f = new File(fileName);
            Scanner s = new Scanner(f);
            while (s.hasNextLine()) {
                String line = s.nextLine();
                if (!line.isEmpty())
                    fileData.add(line);
            }
            return fileData;
        }
        catch (FileNotFoundException e) {
            return fileData;
        }
    }
}