package activities;

import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;

public class Activity1 {
    public static void main(String[] args) {
        // Set up Firefox driver
        WebDriverManager.firefoxdriver().setup();
        // Create a new instance of the Firefox driver
        WebDriver driver = new FirefoxDriver();
        // Open the page
        driver.get("https://alchemy.hguy.co/jobs/");
        // Print the title of the page
        System.out.println("Home page title: " + driver.getTitle());
        // Close the browser
        driver.close();
    }

}
