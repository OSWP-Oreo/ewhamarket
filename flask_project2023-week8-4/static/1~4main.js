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
function showHeart() {
    $.ajax({
        type: 'GET',
        url: '/show_heart/{{item_name}}/',
        data: {},
        success: function (response){
            let my_heart = response['my_heart'];
            if (my_heart['interested'] == 'Y')
            {
                $("#heart").css("color","red");
                $("#heart").attr("onclick","unlike()");
            }
            else
            {
                $("#heart").css("color","grey");
                $("#heart").attr("onclick","like()");
            }
            //alert("showheart!")
            }
        }); 
    } 

    function like() {
        $.ajax({
            type: 'POST',
            url: '/like/{{item_name}}/',
            data: {
                interested : "Y"
            },
            success: function (response) {
                alert(response['msg']);
                window.location.reload()
            }
        });
    }
    
    function unlike() {
        $.ajax({
            type: 'POST',
            url: '/unlike/{{item_name}}/',
            data: {
                interested : "N"
            },
            success: function (response) {
                alert(response['msg']);
                window.location.reload()
            }
            });
        }
        
    $(document).ready(function () {
        showHeart();
    });