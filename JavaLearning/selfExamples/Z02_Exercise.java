import java.awt.Container;
import java.awt.FlowLayout;
import java.text.SimpleDateFormat;
import java.util.Date;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;

public class Z02_Exercise {
    public static void main(String[] args) {
        createGUI();
    }

    private static void createGUI() {
        MyFrame frame = new MyFrame("DemoFrame");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(300, 300);
        frame.setLocationByPlatform(true);
        frame.setVisible(true);
    }
}

class MyFrame extends JFrame {
    JLabel timeLabel = new JLabel("00:00:00");
    JButton button = new JButton("显示时间");

    public MyFrame(String title) {

        super(title);

        Container contentPane = getContentPane();
        contentPane.setLayout(new FlowLayout());

        contentPane.add(button);
        contentPane.add(timeLabel);

        button.addActionListener(event -> showTime());
    }

    public void showTime() {
        SimpleDateFormat sdf = new SimpleDateFormat("HH:mm:ss");
        String timestr = sdf.format(new Date());
        timeLabel.setText(timestr);
    }
}