@OneToMany(mappedBy = "representedAttribute", fetch = FetchType.LAZY)
private List<Model> models;

@ManyToOne(fetch = FetchType.LAZY)
@JoinColumn(name = "foreignKeyColumn")
private ModelName varName;

@ManyToMany(fetch = FetchType.LAZY)
@JoinTable(
    name = "categories_products", 
    joinColumns = @JoinColumn(name = "product_id"), 
    inverseJoinColumns = @JoinColumn(name = "category_id")
)
private List<Category> categories;


@ManyToMany(fetch = FetchType.LAZY)
@JoinTable(
    name = "categories_products", 
    joinColumns = @JoinColumn(name = "category_id"), 
    inverseJoinColumns = @JoinColumn(name = "product_id")
)
private List<Product> products;