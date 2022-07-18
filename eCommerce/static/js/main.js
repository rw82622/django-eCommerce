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

function getCartInfo(){
    try {
        axios.get('/cartcontents').then((response) => {
            // let cart = (response.data.cart)
            console.log(response)
            // for (let item of response.data.cart){
            //     let cartRow = document.createElement('tr')
            //     let itemName = document.createElement('td')
            //     itemName.innerText = item.product_id.name
            //     cartRow.append(itemName)
            //     let itemPrice = document.createElement('td')
            //     itemPrice.innerText = `$${item.product_id.price}`
            //     cartRow.append(itemPrice)
            //     let itemQuantity = document.createElement('td')
            //     itemQuantity.innerText = item.quantity
            //     cartRow.append(itemQuantity)
            //     let subTotal = document.createElement('td')
            //     subTotal.innerText = `$${(item.quantity * item.product_id.price).toFixed(2)}`
            //     cartRow.append(subTotal)
            //     let cartItems = document.querySelector('#cartTable')
            //     cartItems.append(cartRow)
            // }
        })
    }
    catch(e) {
        console.log("Soemthind went wrong in getCartInfo() in main.js")
    }
}