package com.codingdojo.fruityloops.models;

// Include member variables, constructors, getters and setters
// STS can automate the getters and setters

public class Item {
	
	private String name;
	private double price;
	
	//CONSTRUCTORS
	public Item (String name, double price) {
		this.name = name;
		this.price = price;
	}
	
	// GETTERS AND SETTERS
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public double getPrice() {
		return price;
	}
	public void setPrice(double price) {
		this.price = price;
	}

}
