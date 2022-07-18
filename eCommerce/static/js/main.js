let addToCartButtons = document.getElementsByClassName('addToCart-button')
for (let i = 0; i < addToCartButtons.length; i++){
    let myButton = addToCartButtons[i]
    myButton.addEventListener('click', addToCart)
}

function addToCart(event){
    try {
        let productId = event.srcElement.id
        // console.log(productId, 'product id')
        let myUrl = `/add/${productId}`
        axios.get(myUrl).then((response) =>{
            // console.log('response from addToCart', response)
            let cartTotal = document.getElementById('cartTotal') 
            cartTotal.innerText = response.data.cart_total
            document.querySelector("#myToast").className += " show";
            setTimeout(
                () => (document.querySelector("#myToast").classList.remove('show')),
                2000 );
        })
    }
    catch(e) {
        console.log("Toast Failed.")
    }
}   