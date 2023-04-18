package com.codingdojo.helloworld.controllers;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class DemoController {
	@RequestMapping("/{number}")
	public String index(@PathVariable("number") Integer number, Model model) {
		model.addAttribute("number", number);
		model.addAttribute("secretNumber", 4);
		return "conditional.jsp";
	}

}
