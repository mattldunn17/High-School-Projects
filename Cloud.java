
 
/** 
 * Draws cloud
 * @author (Matt Dunn) 
 * @version (1.26.17)
 */
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.geom.Ellipse2D;
import java.awt.geom.Line2D;
import javax.swing.JComponent;
import java.util.Random;
import java.util.ArrayList;
public class Cloud extends JComponent
{
    public void paintComponent(Graphics g)
    {
        Random generator = new Random();
        // Recover Graphics2D
        Graphics2D g2 = (Graphics2D) g;
        
        for (int i = 1; i <= 100; i++)
        {
            int random = generator.nextInt(51);
            //Draw the head
            Ellipse2D.Double head = new Ellipse2D.Double(generator.nextInt(1800), generator.nextInt(900), 50, 50);
            g2.fill(head);
        }
    }
}
