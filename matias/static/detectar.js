var comidasub = document.getElementById("comidasub");
var comidasub2 = document.getElementById("comidasub2");
var comidasub3 = document.getElementById("comidasub3");

//|--------------------------------------------comidasub------------------------|
comidasub.addEventListener("mouseover", function(e) {
    document.getElementById("textocomida1").style.display = 'block';
});

// Creamos el evento mouseout para cada imagen
comidasub.addEventListener("mouseout", function(e) {
    document.getElementById("textocomida1").style.display = 'none';
});

//|--------------------------------------------comidasub2------------------------|
comidasub2.addEventListener("mouseover", function(e) {
    document.getElementById("textocomida2").style.display = 'block';
});

// Creamos el evento mouseout para cada imagen
comidasub2.addEventListener("mouseout", function(e) {
    document.getElementById("textocomida2").style.display = 'none';
});

//|--------------------------------------------comidasub3------------------------|
comidasub3.addEventListener("mouseover", function(e) {
    document.getElementById("textocomida3").style.display = 'block';
});

// Creamos el evento mouseout para cada imagen
comidasub3.addEventListener("mouseout", function(e) {
    document.getElementById("textocomida3").style.display = 'none';
});