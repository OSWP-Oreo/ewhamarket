//'학과' 동적 범위 변경


/* reg_item.html */
function addCommas(input) {
    // Remove existing commas and non-numeric characters
    input.value = input.value.replace(/[^0-9]/g, '');
    // Add commas every three digits
    input.value = input.value.replace(/\B(?=(\d{3})+(?!\d))/g, ',');
}

/* detail.html */
/*좋아요*/
