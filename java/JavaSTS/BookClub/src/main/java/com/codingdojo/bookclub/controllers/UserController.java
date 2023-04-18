package com.codingdojo.bookclub.controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;

import com.codingdojo.bookclub.models.LoginUser;
import com.codingdojo.bookclub.models.User;
import com.codingdojo.bookclub.services.UserService;

import jakarta.servlet.http.HttpSession;
import jakarta.validation.Valid;

@Controller //no prepends mapping here
public class UserController {
	// AUTOWIRED
	@Autowired
	private UserService userService;
	
	// ALL ROUTING OCCURS BELOW
	@GetMapping("")
	public String local() {
		return "redirect:/";
	}
	
	@GetMapping("/") //index.jsp
	public String index(@ModelAttribute("newUser") User newUser, @ModelAttribute("loginUser") LoginUser loginUser) {
		return "index.jsp";
	}
	
	@GetMapping("/logout") //get but redirect to /
	public String logout(HttpSession session) {
		session.setAttribute("userID", null);
		return "redirect:/";
	}
	
	// OTHER ROUTING
	@PostMapping("/register") //index.jsp or redirect/books
	public String register(@Valid @ModelAttribute("newUser") User newUser, BindingResult result, Model model, HttpSession session) {
		userService.registerUser(newUser, result);
		if(result.hasErrors()) {
			model.addAttribute("loginUser", new LoginUser());
			return "index.jsp";
		}
		session.setAttribute("userID", newUser.getId());
		model.addAttribute("user", newUser);
		return "redirect:/books";
	}
	
	@PostMapping("/login") //index.jsp or redirect/books
	public String pLogin(@Valid @ModelAttribute("loginUser") LoginUser loginUser, BindingResult result, Model model, HttpSession session) {
		User user = userService.findUserByEmail(loginUser.getEmail());
		userService.loginUser(loginUser, result);
		if(result.hasErrors()) {
			model.addAttribute("newUser", new User());
			return "index.jsp";
		}
		session.setAttribute("userID", user.getId());
		model.addAttribute("user", user);
		return "redirect:/books";
	}
}
