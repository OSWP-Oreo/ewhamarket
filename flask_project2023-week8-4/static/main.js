// signup.html에서 드롭다운1, 2 복사해서 html에 넣어주시고 
//아래 함수 js 외부 스크립트로 적용하시면 될 것 같습니다!!

function updateDropdown2() {
    var dropdown1 = document.getElementById("dropdown1");
    var dropdown2 = document.getElementById("dropdown2");

    // 드롭다운2에 기존에 있던 option들 clear
    dropdown2.innerHTML = '';

    // 대학 선택되면 해당 단과대 학과 보여주기
    var selectedCollege = dropdown1.value;
    if (selectedCollege === '---대학---') {
        var options = ['---학과---', '대학을 선택해주세요.'];
    } else if (selectedCollege === '인문과학대학') {
        var options = ['국어국문학과', '중어중문학과', '불어불문학과', '독어독문학과', '사학과', '철학과', '기독교학과', '영어영문학부'];
    } else if (selectedCollege === '사회과학대학') {
        var options = ['정치외교학과', '행정학과', '경제학과', '문헌정보학과', '사회학과', '사회복지학과', '심리학과', '소비자학과', '커뮤니케이션·미디어학부'];
    }
    else if (selectedCollege === '자연과학대학') {
        var options = ['수학과', '통계학과', '물리학과', '화학·나노과학전공', '생명과학전공'];
    }
    else if (selectedCollege === '엘텍공과대학') {
        var options = ['컴퓨터공학전공', '사이버보안전공', '전자전기공학전공', '식품공학전공', '화학신소재공학전공', '건축학전공', '건축도시시스템전공', '환경공학전공', '기후·에너지시스템공학전공', '휴먼기계바이오공학부'];
    }
    else if (selectedCollege === '음악대학') {
        var options = ['건반악기과', '관현악기과', '성악과', '작곡과', '한국음악과', '무용과'];
    }
    else if (selectedCollege === '조형예술대학') {
        var options = ['동양화전공', '서양화전공', '조소전공', '도자예술전공', '디자인학부', '섬유예술전공', '패션디자인전공'];
    }
    else if (selectedCollege === '사범대학') {
        var options = ['교육학과', '유아교육과', '초등교육과', '교육공학과', '특수교육과', '영어교육과', '사회교육과', '국어교육과', '과학교육과', '수학교육과'];
    }
    else if (selectedCollege === '경영대학') {
        var options = ['경영학부'];
    }
    else if (selectedCollege === '신산업융합대학') {
        var options = ['융합콘텐츠학과', '의류산업학과', '국제사무학과', '식품영양학과', '융합보건학과', '체육과학부'];
    }
    else if (selectedCollege === '의과대학') {
        var options = ['의예과', '의학과'];
    }
    else if (selectedCollege === '간호대학') {
        var options = ['간호학부'];
    }
    else if (selectedCollege === '약학대학') {
        var options = ['약학과'];
    }
    else if (selectedCollege === '스크랜튼대학') {
        var options = ['스크랜튼학부', '뇌·인지과학전공', '국제학부'];
    }
    else if (selectedCollege === '호크마교양대학') {
        var options = ['호크마교양대학'];
    }

    //dropdown2에 option 배열 append
    for (var i = 0; i < options.length; i++) {
        var option = document.createElement("option");
        option.value = options[i];
        option.text = options[i];
        dropdown2.appendChild(option);
    }

    updateSessionData();
}

// 학과 session 저장
function updateSessionData() {
    var selectedDepartment = document.getElementById("dropdown2").value;

    // AJAX
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/signup_post", true);
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhr.send(JSON.stringify({ department: selectedDepartment }));
}

document.getElementById("dropdown2").addEventListener("change", updateSessionData);