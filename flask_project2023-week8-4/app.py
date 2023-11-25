from flask import Flask, render_template, request,flash,redirect,url_for,session, jsonify
from database import DBhandler
import hashlib
import sys
application = Flask(__name__)
application.config["SECRET_KEY"]= "thisisoreo"
DB=DBhandler() #database.py에 들어가면 클래스있음 (DB. 이용)
 
@application.route("/") 
def hello():
    return render_template("index.html")

@application.route("/index")
def comback_home():
    return render_template("index.html")

# 1~4
@application.route("/1~4/item_reg")
def view_reg_items():
    return render_template("1~4/item_reg.html")

@application.route("/1~4/view_item")
def view_items():
    return render_template("1~4/view_item.html")

@application.route("/1~4/item_detail")
def view_item_detail():
    return render_template("1~4/item_detail.html")

@application.route("/1~4/order")
def order():
    return render_template("1~4/order.html")

@application.route("/order_item")
def view_order_confirmation():
    #구매한후 구매자 포인트 감소
    flash('1000포인트가 차감되었습니다')
    DB.update_point(session['id'], 1000)
    DB.update_ranking_point(session['id'], 1000)
    return render_template("1~4/order.html")


# 5~7
@application.route("/5~7/reg_reviews")
def view_reg_review():
    return render_template("5~7/reg_reviews.html")

@application.route("/5~7/review")
def view_reviews():
    return render_template("5~7/review.html")

@application.route("/5~7/review_detail")
def view_review_detail():
    return render_template("5~7/review_detail.html")

#상품이름 가지고 와서 리뷰작성페이지 오픈
@application.route("/reg_review_init/<name>/")  
def reg_review_init(name):
    info = DB.reference('item')
    info_data = info.child(name).get()
    professor = info_data.get("professor",None)    
    subject = info_data.get("subject",None)       
    subject_id = info_data.get("subject_id",None)
    reviewer = session['id']
    return render_template("reg_reviews.html", reviewer=reviewer, name=name, subject=subject, professor=professor, subject_id=subject_id)

#작성된 리뷰 데이터 넘겨줌
@application.route("/reg_reviews", methods=['POST'])
def reg_reviews():
    image_file=request.files["chooseFile"]
    image_file.save("static/img/{}".format(image_file.filename))
    data=request.form
    DB.reg_review(data, image_file.filename)
    return redirect(url_for('view_all_review'))

# 8~10

#회원가입
@application.route("/signup")
def signup():
    return render_template("8~10/signup.html")
@application.route("/signup_post",methods=['POST'])
def register_user():
    data=request.form
    id=request.form['id']
    pw=request.form['pw']
    pw2=request.form['PWconfirm']
    nname=request.form['nickname']
    pw_hash=hashlib.sha256(pw.encode('utf-8')).hexdigest()
    pw_hash2=hashlib.sha3_256(pw.encode('utf-8')).hexdigest()
    #아이디중복확인
    if 'check_duplicate_id' in request.form:
        if DB.id_duplicate_check(id):
            flash('사용할 수 있는 아이디입니다.')
            return render_template("8~10/signup.html")
        else:
            flash('이미 존재하는 아이디입니다.')
            return render_template("8~10/signup.html")

    #닉네임중복확인
    if 'check_duplicate_nickname' in request.form:
        if DB.nickname_duplicate_check(nname):
            flash('사용할 수 있는 닉네임입니다.')
            return render_template("8~10/signup.html")
        else:
            flash('이미 존재하는 닉네임입니다.')
            return render_template("8~10/signup.html")
    if pw!=pw2:
        flash("비밀번호를 확인해주세요")
        return render_template("8~10/signup.html")
    else:
        if DB.insert_user(data,pw_hash,pw_hash2):
            flash("회원가입되었습니다.")
            return render_template("8~10/login.html")
        else:
            flash("중복확인를 눌러주세요")
            return render_template("8~10/signup.html")

    

# 로그인 하기
@application.route("/login")
def login():
    return render_template("8~10/login.html")
@application.route("/login_confirm", methods=['POST'])
def login_user():
    id_=request.form['id']
    pw=request.form['pw']
    pw_hash = hashlib.sha256(pw.encode('utf-8')).hexdigest()
    if DB.find_user(id_,pw_hash):
        session['id']=id_
        return redirect(url_for('hello')) #나중에 전체상품조회로 바꿀예정
    else:
        flash("Wrong ID or PW!")
        return render_template("8~10/login.html")

# 로그아웃
@application.route("/logout")
def logout_user():
    session.clear()
    return redirect(url_for('hello')) #나중에 전체상품조회로 바꿀예정
    
@application.route("/ranking")
def ranking():
    return render_template("8~10/ranking.html")



    ################
@application.route("/submit_item_post",methods=['POST'])
def reg_item_submit_post():
    image_file=request.files["file"]
    image_file.save("static/images/{}".format(image_file.filename))
    data = request.form
    return render_template("submit_item_result.html", data=data, img_path="static/images/{}".format(image_file.filename))

if __name__ == "__main__":
    application.run(host='0.0.0.0', debug = True)