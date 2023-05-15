// Object Master
// Practice assignment but recommended as Core assignment

// Use map and filter to get data from immutable pokemon array
const pokémon = Object.freeze([
    { "id": 1, "name": "Bulbasaur", "types": ["poison", "grass"] },
    { "id": 5, "name": "Charmeleon", "types": ["fire"] },
    { "id": 9, "name": "Blastoise", "types": ["water"] },
    { "id": 12, "name": "Butterfree", "types": ["bug", "flying"] },
    { "id": 16, "name": "Pidgey", "types": ["normal", "flying"] },
    { "id": 23, "name": "Ekans", "types": ["poison"] },
    { "id": 24, "name": "Arbok", "types": ["poison"] },
    { "id": 25, "name": "Pikachu", "types": ["electric"] },
    { "id": 37, "name": "Vulpix", "types": ["fire"] },
    { "id": 52, "name": "Meowth", "types": ["normal"] },
    { "id": 63, "name": "Abra", "types": ["psychic"] },
    { "id": 67, "name": "Machamp", "types": ["fighting"] },
    { "id": 72, "name": "Tentacool", "types": ["water", "poison"] },
    { "id": 74, "name": "Geodude", "types": ["rock", "ground"] },
    { "id": 87, "name": "Dewgong", "types": ["water", "ice"] },
    { "id": 98, "name": "Krabby", "types": ["water"] },
    { "id": 115, "name": "Kangaskhan", "types": ["normal"] },
    { "id": 122, "name": "Mr. Mime", "types": ["psychic"] },
    { "id": 133, "name": "Eevee", "types": ["normal"] },
    { "id": 144, "name": "Articuno", "types": ["ice", "flying"] },
    { "id": 145, "name": "Zapdos", "types": ["electric", "flying"] },
    { "id": 146, "name": "Moltres", "types": ["fire", "flying"] },
    { "id": 148, "name": "Dragonair", "types": ["dragon"] }
]);

// list of Pokemon that have names that start w/ letter B
const bListPokemon = pokémon.filter( p => p.name[0] === "B");
// array of just the IDs
const pokemonIds = pokémon.map(p => p.id )

// divisible by 3
const div3 = pokémon.filter(p => p.id % 3 ===0);

// fire type
const isFire = pokémon.filter(p => p.types.includes('fire'));

// more than one type
// just names 
// names with id greater than 99
// array with poison type names
// array with first type of all pokemon who's second type is flying
// count of pokemon that are normal type

const isMultiType = pokémon.filter(p => p.types.length > 1);
const allNames = pokémon.map(p => p.name);
const names99Plus = pokémon.filter(p => p.id > 99).map(p => p.name);
const namesOnlyPoison = pokémon.filter(p => p.types.includes('poison') && p.types.length === 1).map(p => p.name);
const secondTypeFlying = pokémon.filter(p => p.types[1] === 'flying').map(p => p.types[0]);
const normalCount = pokémon.filter(p => p.types.includes('normal')).length;

console.log(div3)
console.log(isFire)
console.log(isMultiType)
console.log(allNames)
console.log(names99Plus)
console.log(namesOnlyPoison)
console.log(secondTypeFlying)
console.log(normalCount)
console.log(bListPokemon)
console.log(pokemonIds)