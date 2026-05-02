package com.codingdojo.bookclub.models;

import jakarta.validation.constraints.Email;
import jakarta.validation.constraints.NotEmpty;
import jakarta.validation.constraints.Size;

public class LoginUser {
	
	@NotEmpty(message="Email is required!")
	@Email(message="Please enter a valid email")
	private String email;
	
	@NotEmpty(message="Password is required!")
	@Size(min=8, max=128, message="Password must be between 8 and 128 characters!")
	private String password;
	
	// CONSTRUCTOR
	public LoginUser() {
		// EMPTY CONSTRUCTOR FOR JAVA BEAN
	}

    // GETTERS AND SETTERS
	public String getEmail() {
		return email;
	}

	public void setEmail(String email) {
		this.email = email;
	}

	public String getPassword() {
		return password;
	}

	public void setPassword(String password) {
		this.password = password;
	}

    // IMPORT GETTERS AND SETTERS (no set for CA DA)
}
