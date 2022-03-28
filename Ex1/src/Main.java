import Enums.Algorithm;
import Enums.ArraySize;
import Enums.ArrayStatus;
import Enums.Type;
import org.json.JSONObject;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class Main {

    public static void main(String[] args) throws IOException {
        long start = System.nanoTime();
        JSONObject json_a = new JSONObject();
        for (Algorithm algorithm : Algorithm.values()) {
            JSONObject json_t = new JSONObject();
            for (Type<?> type : Type.TYPES) {
                JSONObject json_si = new JSONObject();
                for (ArraySize size : ArraySize.values()) {
                    JSONObject json_st = new JSONObject();
                    for (ArrayStatus status : ArrayStatus.values()) {
                        Instance<?> in = new Instance<>(type, algorithm, size, status);
                        json_st.put(status.name(), in.run());
                    }
                    json_si.put(size.name(), json_st);
                }
                json_t.put(type.name(), json_si);
            }
            json_a.put(algorithm.name(), json_t);
        }
        BufferedWriter writer = new BufferedWriter(new FileWriter("output.json"));
        writer.write(json_a.toString());
        writer.close();
        System.out.println("Process completed in " + (System.nanoTime() - start) + "ns!");
    }

}
