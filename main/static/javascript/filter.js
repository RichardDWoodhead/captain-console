function getAjax() {
    let xhr = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject('Microsoft.XMLHTTP');
    xhr.open('GET', "get_products");
    xhr.onreadystatechange = function() {
        if (xhr.readyState>3 && xhr.status===200) {
            window["products"] = JSON.parse(xhr.response)["products"]
            window["manufacturers"] = JSON.parse(xhr.response)["manufacturers"]
            display_products()
        }
    };
    xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
    xhr.send();
    return xhr;
}
function compare_products(product_a, product_b, ){
    let order_by_value = document.getElementById("sort_by").value
    let order = order_by_value === "name";
    if (order === true){
        if(product_a["name"] === product_b["name"]){
            if (parseInt(product_a["price"].replace(".","")) < parseInt(product_b["price"].replace(".",""))){return -1}else{return 1}
        }
        else if (product_a["name"] < product_b["name"]){
            return -1
        } else{
            return 1
        }
    } else{
        if(parseInt(product_a["price"].replace(".","")) === parseInt(product_b["price"].replace(".",""))){
            if (product_a["name"] < product_b["name"]){return -1}else{return 1}
        }
        else if (parseInt(product_a["price"].replace(".","")) < parseInt(product_b["price"].replace(".",""))){
            return -1
        } else{
            return 1
        }
    }

}

function is_checked(class_name) {
    let checkboxes = document.getElementsByClassName(class_name)
    for (let i = 0; i <checkboxes.length; i++){
        if(checkboxes[i].checked){
            return true
        }
    }
    return false
}

function is_type_filter(product) {
    let checkboxes = document.getElementsByClassName("check-box-type")
    for (let x = 0; x < checkboxes.length; x++) {
        if (product.type === checkboxes[x].name && checkboxes[x].checked) {
            console.log(product.manufacturer)
            return true
        }
    }
    return false
}

function is_manufacturer_filter(product) {
    let checkboxes = document.getElementsByClassName("check-box-manufacturer")
    for (let x = 0; x < checkboxes.length; x++) {
        if (product.manufacturer === checkboxes[x].name && checkboxes[x].checked) {
            console.log(product.manufacturer)
            return true
        }
    }
    return false
}

function display_products(){
    let products = window["products"]
    products.sort(compare_products)
    let counter = 0
    let container = document.getElementById("container")
    container.innerHTML = ""
    let row = document.createElement("div")
    row.classList = "row"
    let search_field = document.getElementById("search")
    let filter_slider = document.getElementById("slider")
    let type_checked = is_checked("check-box-type")
    let manufacturer_checked = is_checked("check-box-manufacturer")
    for (let i = 0; i < products.length; i++) {
        let is_type = false
        let is_manufacturer = false
        is_type = is_type_filter(products[i])
        is_manufacturer = is_manufacturer_filter(products[i])
        if(products[i].name.toLowerCase().indexOf(search_field.value.toLowerCase()) > -1 && products[i].price <= filter_slider.value && (is_type || !type_checked )&& (is_manufacturer || !manufacturer_checked )){
            if (counter % 3 === 0 && counter !== 0) {
                container.appendChild(row)
                row = document.createElement("div")
                row.classList = "row"
            }
            let card = document.createElement("div")
            card.classList = "card col-3"
            let card_img = document.createElement("img")
            card_img.classList = "card-top-img cardimg"
            card_img.src = products[i].image
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

window.onload = function () {
    getAjax()
    const urlParams = new URLSearchParams(window.location.search);
    const query = urlParams.get('query');
    let search = document.getElementById("search")
    document.getElementById("main_nav").appendChild(search)
    document.getElementById("search_form").style="display:none;"
    search.value = query


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
    let order_by_element = document.getElementById("sort_by")
    order_by_element.onclick = function () {
        display_products();
    }
}