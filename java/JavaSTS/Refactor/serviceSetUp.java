@Service
public class StudentService {

	private static StudentRepository studentRepo;

	public StudentService(StudentRepository studentRepo) {
		this.studentRepo = studentRepo;
	}

	public Student getOne(Long id) {
		Optional<Student> student = studentRepo.findById(id);
		return student.isPresent() ? student.get() : null;
	}

	public List<Student> getAll() {
		return (List<Student>) studentRepo.findAll();
	}

	public Student create(Student dojo) {
		return studentRepo.save(dojo);
	}

	public Student update(Student dojo) {
		return studentRepo.save(dojo);
	}

	public void delete(Long id) {
		studentRepo.deleteById(id);
	}

}