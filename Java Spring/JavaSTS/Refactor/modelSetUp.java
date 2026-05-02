@Entity // declares that it is going to be apart of mysql
@Table(name = "book") // gives the table name of the model
public class Book {
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY) // generates an auto incrementing 
	private Long id;
	
	@NotEmpty(message = "Title is required!") // validation for strings
	private String title;
	
	@NotEmpty(message = "Description is required!")
	private String desc;
	
	@Min(0) // validation for ints
	private String numOfPages;

    @Column(updatable = false)
	private Date createdAt;
    @Column(updatable = false)
	private Date updatedAt;

    // empty constructor
	public Book() {
	}

    // populated constructor for API and using forms that are not utilizing the form:form tag
    public Book(Long id, @NotEmpty(message = "Title is required!") String title,
			@NotEmpty(message = "Description is required!") String desc, @Min(0) String numOfPages) {
		super();
		this.id = id;
		this.title = title;
		this.desc = desc;
		this.numOfPages = numOfPages;
	}

    public 

    @PrePersist // adds the created at date and time to sql on creation 
	protected void onCreate() {
		this.createdAt = new Date();
	}

	@PreUpdate // add the updated at date and time when being updated
	protected void onUpdate() {
		this.updatedAt = new Date();
	}
}



	@ManyToOne(fetch = FetchType.LAZY)
	@JoinColumn(name = "connectedModel_id")
	private ConnectedModel model;