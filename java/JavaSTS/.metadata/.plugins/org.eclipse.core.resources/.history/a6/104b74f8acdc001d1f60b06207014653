package com.codingdojo.daikichi.controllers;

import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

// annotate as RestController
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

	
	@RequestMapping("/travel/{locationName}")
	public String location(@PathVariable("locationName") String locationName){
		return "Congratulations! You will soon travel to " + locationName +"!";
	}
	
	@RequestMapping(value="/lotto/{lottoId}", method = RequestMethod.GET)
	// requestmapping defaults to get, but can be specific if needed
	public String lotto(@PathVariable("lottoId") int lottoId){
		// if statement for odd vs even number output (modulo)
		if (lottoId % 2 == 0) {
			return "You will take a grand journey in the near future, but be weary of tempting offers.";
		} else {
			return "You have enjoyed the fruits of your labor but now is a great time to spend time with family and friends.";
		}
	}
	
}
