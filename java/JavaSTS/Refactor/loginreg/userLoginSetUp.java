@Entity
@Table(name = "user")
public class User {

	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Long id;

	@NotEmpty(message = "User name is required")
	@Size(min = 5, max = 15, message = "User name needs to be between 5-15 characters")
	private String userName;
	@NotEmpty(message = "Email is required")
	@Email(message = "Invalid Email!")
	private String email;
	@NotEmpty(message = "Password is required")
	@Size(min = 8, message = "Password must be 8 characters or longer")
	private String password;

	@NotEmpty(message = "Confirm Password is required")

	@Transient
	private String confirm;

	@Column(updatable = false)
	private Date createdAt;
	@Column(updatable = false)
	private Date updatedAt;

	@OneToMany(mappedBy = "referanceInJoinColum", fetch = FetchType.LAZY)
	private List<ConnectedModel> connectedModelVariable;


	public User() {
	}


	    @PrePersist // adds the created at date and time to sql on creation 
	protected void onCreate() {
		this.createdAt = new Date();
	}

	@PreUpdate // add the updated at date and time when being updated
	protected void onUpdate() {
		this.updatedAt = new Date();
	}
}