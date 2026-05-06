@Repository
public interface UserRepository extends CrudRepository<User, Long> {
	Optional<User> findByEmail(String userName);
}