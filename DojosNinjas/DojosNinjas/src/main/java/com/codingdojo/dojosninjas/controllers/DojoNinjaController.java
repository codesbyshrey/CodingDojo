package com.codingdojo.dojosninjas.controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;

import com.codingdojo.dojosninjas.models.Dojo;
import com.codingdojo.dojosninjas.models.Ninja;
import com.codingdojo.dojosninjas.services.DojoService;
import com.codingdojo.dojosninjas.services.NinjaService;

import jakarta.validation.Valid;

@Controller
public class DojoNinjaController {
	//Autowired enables us to inject
	@Autowired DojoService dojoService;
	@Autowired NinjaService ninjaService;
	
	// GET MAPPING FOR CREATING DOJO
	@GetMapping("/dojos/new")
	public String newDojo(@ModelAttribute("dojo") Dojo dojo) {
		return "createDojo.jsp";
	}
	
	// GET MAPPING FOR SHOWING DOJO
	@GetMapping("/dojos/{id}")
	public String showDojo(@PathVariable("id") Long id, Model model) {
		model.addAttribute("dojo", dojoService.findDojo(id));
		return "showDojo.jsp";
	}
	
	// GET MAPPING FOR NEW NINJA
	@GetMapping("/ninjas/new")
	public String newNinja(@ModelAttribute("ninja") Ninja ninja, Model model) {
		model.addAttribute("dojos", dojoService.getAllDojos());
		return "newNinja.jsp";
	}
	
	// RESTFUL ROUTING
	@PostMapping("/dojos/new")
	public String postNewDojo(@Valid @ModelAttribute("dojo") Dojo dojo, BindingResult result) {
		if(result.hasErrors()) {
			return "createDojo.jsp";
		}
		dojoService.createDojo(dojo);
		return "redirect:/ninjas/new";
	}
	
	@PostMapping("/ninjas/new")
	public String postNewNinja(@Valid @ModelAttribute("ninja") Ninja ninja, BindingResult result) {
		if (result.hasErrors()) {
			return "newNinja.jsp";
		}
		Ninja newNinja = ninjaService.createNinja(ninja);
		return "redirect:/dojos/" + newNinja.getDojo().getId();
	}
}
