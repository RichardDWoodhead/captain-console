window.onload = function () {
    let products = [
        {"id": 1, "name": "ps2", "price": 15000, "image": "images/ps2.png", "type": "Console"},
        {"id": 2, "name": "ps2", "price": 15000, "image": "images/ps2.png", "type": "Console"},
        {"id": 3, "name": "ps2", "price": 15000, "image": "images/ps2.png", "type": "Game"},
        {"id": 4, "name": "ps3", "price": 20000, "image": "images/ps3.jpg", "type": "Console"},
        {"id": 5, "name": "ps3", "price": 20000, "image": "images/ps3.jpg", "type": "Game"},
        {"id": 6, "name": "ps3", "price": 20000, "image": "images/ps3.jpg", "type": "Console"},
        {"id": 7, "name": "ps3", "price": 20000, "image": "images/ps3.jpg", "type": "Console"},
        {"id": 8, "name": "ps3", "price": 20000, "image": "images/ps3.jpg", "type": "Game"},
        {"id": 9, "name": "ps3", "price": 20000, "image": "images/ps3.jpg", "type": "Game"},
        {"id": 10, "name": "ps3", "price": 20000, "image": "images/ps3.jpg", "type": "Console"},
        {"id": 11, "name": "ps4", "price": 35000, "image": "images/ps4.jpg", "type": "Console"},
        {"id": 12, "name": "ps4", "price": 35000, "image": "images/ps4.jpg", "type": "Game"},
        {"id": 13, "name": "ps4", "price": 35000, "image": "images/ps4.jpg", "type": "Game"},
        {"id": 14, "name": "ps4", "price": 35000, "image": "images/ps4.jpg", "type": "Game"},
    ]
    function display_products(){
        let counter = 0
        let container = document.getElementById("container")
        container.innerHTML = ""
        let row = document.createElement("div")
        row.classList = "row"
        let search_field = document.getElementById("search")
        let filter_slider = document.getElementById("slider")
        let checkboxes = document.getElementsByClassName("checkbox")
        let checked = false
        for (let i = 0; i <checkboxes.length; i++){
            if(checkboxes[i].checked){
                checked = true
            }
        }
        for(let i = 0; i <products.length; i++) {
            let is_type = false
            for(let x = 0; x < checkboxes.length; x++ ){
                    if(products[i].type === checkboxes[x].name && checkboxes[x].checked){
                        is_type = true
                        console.log("yes")
                    }
                }
            if(products[i].name.indexOf(search_field.value) > -1 && products[i].price <= filter_slider.value && (is_type || !checked )){

                if (counter % 3 === 0 && counter !== 0) {
                    container.appendChild(row)
                    row = document.createElement("div")
                    row.classList = "row"
                }
                let card = document.createElement("div")
                card.classList = "card col-3"
                let card_img = document.createElement("img")
                card_img.classList = "card-top-img cardimg"
                let card_body = document.createElement("div")
                card_body.classList = "card-body border-top"
                let card_title = document.createElement("h5")
                card_title.classList = "card-title"
                card_title.innerHTML = products[i].name
                let card_price = document.createElement("p")
                card_price.classList = "card-text"
                card_price.innerHTML = "price: " + products[i].price
                let card_link = document.createElement("a")
                card_link.classList = "btn btn-primary"
                card_link.href = "/store/product/" + products[i].id
                card_link.innerHTML = "more details"
                card_body.appendChild(card_img)
                card_body.appendChild(card_title)
                card_body.appendChild(card_price)
                card_body.appendChild(card_link)
                card.appendChild(card_body)
                row.appendChild(card)
                counter++
            }
        }
        container.appendChild(row)
    }
    const urlParams = new URLSearchParams(window.location.search);
    const query = urlParams.get('query');
    let search = document.getElementById("search")
    document.getElementById("main_nav").appendChild(search)
    document.getElementById("search_form").style="display:none;"
    search.value = query
    display_products()
    search.oninput = function(){
        display_products();
    }
    let filter_slider = document.getElementById("slider")
    filter_slider.oninput = function(){
        document.getElementById("slider_info").innerText =filter_slider.value
        display_products();
    }
    document.getElementsByClassName("storeIndex")[0].onclick = function(){
        display_products();
    }

}