package com.codingdojo.helloworld.controllers;

import java.util.ArrayList;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model; //new import needed
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping("/jsp")
public class JSPController {
	@RequestMapping("")
	public String jspIndex(Model model) {
		model.addAttribute("dojoName", "Burbank");
		return "index2.jsp";
	}
	
	@RequestMapping("/")
	public String user(Model model) {
		String firstName = "Shreyas";
		String lastName = "Sriram";
		String email = "coding@dojo.com";
		Integer age = 25;
		
		model.addAttribute("first", firstName);
		model.addAttribute("last", lastName);
		model.addAttribute("email", email);
		model.addAttribute("age", age);
		
		return "index3.jsp";
	}
	
	@RequestMapping("/dojos")
	public String index(Model model) {
		ArrayList<String> dojos = new ArrayList<String>();
		dojos.add("Burbank");
        dojos.add("Chicago");
        dojos.add("Bellevue");
        model.addAttribute("dojosFromMyController", dojos);
        return "index4.jsp";
	}
}
