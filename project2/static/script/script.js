
function addProductToCart() {
    // Make an AJAX request to add the product to the cart
    fetch('/add_to_cart', {
        method: 'POST',
        body: new FormData(document.querySelector('form#add-to-cart-form'))
    })
    .then(response => response.json())
    .then(data => {
        // Handle the response and reload the previous page
        window.location.href = data.redirect_url;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
