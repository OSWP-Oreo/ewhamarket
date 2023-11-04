/* 1.html */
function addCommas(input) {
    // Remove existing commas and non-numeric characters
    input.value = input.value.replace(/[^0-9]/g, '');
    // Add commas every three digits
    input.value = input.value.replace(/\B(?=(\d{3})+(?!\d))/g, ',');
}


/* 2.html */
function sortby_regdate(){

}

function sortby_popular(){

}

function sortby_lowprice(){

}