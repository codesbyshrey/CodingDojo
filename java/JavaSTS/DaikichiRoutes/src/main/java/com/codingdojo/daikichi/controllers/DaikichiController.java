package com.codingdojo.daikichi.controllers;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

// annotate as restcontroller
@RestController
@RequestMapping("/daikichi") //prepends all routes with daikichi
public class DaikichiController {
	@RequestMapping("") 
		// if inserted /, error would show on the blank page
		public String welcome() {
			return "Welcome!";
		}
	
	@RequestMapping("/today")
	public String today() {
		return "Today you will find luck in all your endeavors!";
	}
	
	@RequestMapping("tomorrow")
	public String tomorrow() {
		return "Tomorrow, an opportunity will arise, so be sure to open to new ideas!";
	}

}
