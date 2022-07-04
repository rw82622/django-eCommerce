updateStoreCart()

let addToCartButtons = document.getElementsByClassName('addToCart-button')
for (let i = 0; i < addToCartButtons.length; i++){
    let myButton = addToCartButtons[i]
    myButton.addEventListener('click', updateLocalStorage)
}

function updateLocalStorage(event){
    let clickedButton = event.target
    let myRow = clickedButton.parentElement.parentElement
    let productImage = myRow.getElementsByClassName('productImage')[0].src
    let productName = myRow.getElementsByClassName('card-title')[0].innerText
    let productPrice = myRow.getElementsByClassName('card-text')[0].innerText
    let productId = myRow.getAttribute('data-id')

    let temp = {"id": productId, "name": productName,"imageUrl": productImage,"price": productPrice, 'quantity': 1}
    let currentStorage = JSON.parse(localStorage.getItem('storeCart'))
    if (currentStorage) {
        let duplicateFound = false
        for (let index in currentStorage){
            if (currentStorage[index]['imageUrl'] === temp['imageUrl']){
                currentStorage[index]['quantity'] += 1
                duplicateFound = true
                break
            }
        }
        if (duplicateFound){
            localStorage.setItem('storeCart', JSON.stringify([...currentStorage]))
        }
        else {
            localStorage.setItem('storeCart', JSON.stringify([...currentStorage, temp]))
        }
    }
    else {
        localStorage.setItem('storeCart', JSON.stringify([temp]))
    }
    updateStoreCart()
}

function updateStoreCart(){
    let localCart = localStorage.getItem('storeCart')
    if (localCart){
        localCart = [...JSON.parse(localCart)]
        document.querySelector("#cartTotal").innerText = localCart.length
        myCartTable = document.querySelector('#cartTable')
        while (myCartTable.firstChild) {
            myCartTable.removeChild(myCartTable.firstChild);
          }
        let cartTotalPrice = 0
        for (let item of localCart){
            cartTotalPrice += (item.quantity * Number(item.price.replace('$','')))
            addItemToCart(item.imageUrl, item.name, item.price, item.quantity)
        }
        document.querySelector('#cartTotalPrice').innerText = `TOTAL: $${cartTotalPrice.toFixed(2)}`
    }
}

function addItemToCart(image, name, price, quantity=1){
        let cartRow = document.createElement('tr')
        let itemName = document.createElement('td')
        itemName.innerText = name
        cartRow.append(itemName)
        let itemPrice = document.createElement('td')
        itemPrice.innerText = price
        cartRow.append(itemPrice)
        let itemQuantity = document.createElement('td')
        itemQuantity.innerText = quantity
        cartRow.append(itemQuantity)
        let subTotal = document.createElement('td')
        subTotal.innerText = `$${(quantity * Number(price.replace('$',''))).toFixed(2)}`
        cartRow.append(subTotal)
        let cartItems = document.querySelector('#cartTable')
        cartItems.append(cartRow)
}