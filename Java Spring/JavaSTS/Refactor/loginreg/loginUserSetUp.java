// first create a LoginUser class in the models package.
// LoginUser is not getting saved in the database so no need for @Entity and @Table
// example of LoginUser class

public class LoginUser {

	@NotEmpty(message = "User name is required")
	private String email;

	@NotEmpty(message = "Password is required")
	@Size(min = 8, message = "Password must be 8 characters or longer")
	private String password;

	public LoginUser() {
	}

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

}