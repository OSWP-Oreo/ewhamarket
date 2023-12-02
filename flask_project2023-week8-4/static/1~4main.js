//'학과' 동적 범위 변경


/* reg_item.html */
function addCommas(input) {
    // Remove existing commas and non-numeric characters
    input.value = input.value.replace(/[^0-9]/g, '');
    // Add commas every three digits
    input.value = input.value.replace(/\B(?=(\d{3})+(?!\d))/g, ',');
}


/* view_item.html */



// 초기 설정
updateDepartments();

//정렬
function sortby_regdate(){

}

function sortby_popular(){

}

function sortby_lowprice(){

}


/********3.html***********/
/*리뷰 또는 상세설명 보기 버튼 동작*/
document.addEventListener("DOMContentLoaded", function() {
    const reviewBtn = document.getElementById("review-btn");
    const descrBtn = document.getElementById("descr-btn");
    const reviewScreen = document.getElementById("review-screen");
    const descrScreen = document.getElementById("descr-screen");

    reviewBtn.addEventListener("click", function() {
        reviewScreen.style.display = "block";
        descrScreen.style.display = "none";
    });

    descrBtn.addEventListener("click", function() {
        reviewScreen.style.display = "none";
        descrScreen.style.display = "block";
    });
});
