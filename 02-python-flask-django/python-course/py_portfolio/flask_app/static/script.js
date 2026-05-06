let th = document.getElementById('titleHolder');
const colors = [
     'lemonchiffon',
     'peachpuff',
     'peachpuff',
     'lightcoral',
     'lightgreen',
     'lemonchiffon',
     'peachpuff',
     'peachpuff',
     'lightcoral',
     'lightgreen',
     'lemonchiffon',
     'peachpuff',
     'peachpuff',
     'lightcoral',
     'lightgreen'
]
function changeColor() {
     th.style.color = colors[Math.floor(Math.random() * colors.length)];
}

th.onload(setInterval(changeColor, 1000));