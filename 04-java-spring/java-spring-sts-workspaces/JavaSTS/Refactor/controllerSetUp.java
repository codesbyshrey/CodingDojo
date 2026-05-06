// AUTOWIRED CAN TAKE CARE OF THIS EASILY FOR US
@Autowired SomeService someServ;

// ALTERNATIVELY, THIS IS WHAT AUTOWIRED TAKES CARE O
private static SomeService someServ;

// builds basic constructor for passing in
public HomeController(SomeService someServ) {
     this.someServ = someServ;
}