
 

import javax.swing.JFrame;

public class CloudViewer
{
    public static void main(String[] args)
    {
        JFrame frame = new JFrame();
        frame.setSize(1200, 750);
        frame.setTitle("Cloud");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        Cloud component = new Cloud();
        frame.add(component);
        
        frame.setVisible(true);
    }
}
