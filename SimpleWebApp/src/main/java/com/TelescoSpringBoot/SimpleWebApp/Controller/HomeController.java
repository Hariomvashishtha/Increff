package com.TelescoSpringBoot.SimpleWebApp.Controller;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HomeController
{
    @RequestMapping("/")
    public String greet()
    {
        return "welcome to home page";
    }
    @RequestMapping("/about")
    public String aboutPage()
    {
        return " this is the about page";
    }

}
