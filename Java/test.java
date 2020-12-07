import java.util.logging.Logger;
import resource.*;

public class test {
    static GenericMemoryCell<String> hw = new GenericMemoryCell<>();
    static GenericMemoryCell<Integer> x = new GenericMemoryCell<>();
    private static Logger logger = Logger.getLogger("my logger");

    // public static void pout(int n) {
    //     if (n >= 10) {
    //         pout(n / 10);
    //     }
    //     String x = String.valueOf(n % 10);
    //     logger.info(x);
    // }
    public static void main(String[] args) {
        hw.write("Hello,world"); String h = hw.read();
        x.write(3123); String xx = String.valueOf(x.read()); //此处的int类型的3123在write()时被自动装箱成了Integer类型，read()时被自动拆箱成int类型
        logger.info(h);
        logger.info(xx);
    }

}