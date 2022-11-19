let cartIcon = document.querySelector("#cart-icon");
let cart = document.querySelector(".cart");

cartIcon.onclick = () => {
    if (document.querySelector(".cart.active")) {
        cart.classList.remove("active");
    } else {
        cart.classList.add("active");
    }

};