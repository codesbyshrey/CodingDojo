package com.codingdojo.helloworld.controllers;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class FruitController {
	@RequestMapping("/fruit")
	public String fruitIndex(Model model) {
		model.addAttribute("fruit", "banana");
		return "index.jsp";
	}
}
