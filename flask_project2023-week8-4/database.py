import pyrebase
import json 
class DBhandler:
    def __init__(self ):
        with open('./authentication/firebase_auth.json') as f:
            config=json.load(f )

        firebase = pyrebase.initialize_app(config)
        self.db = firebase.database()
    
    # 회원가입
    def insert_user(self,data,pw,pw2):
        user_info={
            "id": data['id'],
            "pw":pw,
            "pw2":pw2,
            "email":data['email'],
            "hp":data['HP'],
            "college":data['dropdown1'],
            "major":data['dropdown2'],
            "nickname":data['nickname'],
            "point":30000,
            "rankingpoint":0
        }
        if self.id_duplicate_check(str(data['id'])) and self.nickname_duplicate_check(str(data['nickname'])):
            self.db.child("user").child(data['id']).set(user_info)
            print(data)
            return True
        else:
            return False
        
    # 회원가입 시 아이디 중복확인
    def id_duplicate_check(self, id_string):
        users = self.db.child("user").get()
        
        print("users###",users.val())
        if str(users.val()) == "None": # first registration
            return True
        else:
            for res in users.each():
                value = res.val()
                if value['id'] == id_string:
                    return False
            return True
    # 회원가입 시 닉네임 중복확인
    def nickname_duplicate_check(self, name_string):
        users = self.db.child("user").get()
        for res in users.each():
            value = res.val()
            if value['nickname'] == name_string:
                return False
        return True

    #유저 찾기
    def find_user(self, id_, pw_):
        users = self.db.child("user").get()
        for res in users.each():
            value = res.val()
            if value['id'] == id_ and value['pw'] == pw_:
                return True
        return False
    
    #구매하기
    #가격 가져오기
    def get_price(self, name):
        point=int(self.db.child("item").child(name).get().val()['price'])
        return point
    #판매자 가져오기
    def get_seller(self, name):
        seller=self.db.child("item").child(name).get().val()['writer']
        return seller
    
    #구매자 포인트 감소
    def update_point(self, user_id, point):
        user_data = self.db.child("user").child(user_id).get().val()
        if user_data is not None and 'point' in user_data:
            b_point = int(user_data['point'])
            a_point = b_point - point
            point_info = {
                "point": a_point
            }
            self.db.child("user").child(user_id).update(point_info)
        return True
    #판매자 포인트 증가
    def update_point_2(self, user_id, point):
        user_data = self.db.child("user").child(user_id).get().val()
        if user_data is not None and 'point' in user_data:
            b_point = int(user_data['point'])
            a_point = b_point + point
            point_info = {
                "point": a_point
            }
            self.db.child("user").child(user_id).update(point_info)
        return True
    #구매자 판매자 랭킹 포인트 증가
    def update_ranking_point(self, user_id, point):
        user_data = self.db.child("user").child(user_id).get().val()
        if user_data is not None and 'rankingpoint' in user_data:
            b_point = int(user_data['rankingpoint'])
            a_point = b_point + point
            point_info = {
                "rankingpoint": a_point
            }
            self.db.child("user").child(user_id).update(point_info)
        return True
    
    #리뷰 데이터베이스에 저장
    def reg_review(self, data, user_id, img_path):
        find_name = data['seller_id']+"_"+data['name']
        dbname = self.db.child("item").get() #db에 저장되어 있는 판매자id_상품명 찾기.
        for res in dbname.each():
            key_value = res.key() #판매자id_상품명
            if key_value == find_name:
                target_value=res.val() #내가 찾던 판매자id_상품명
        review_info ={
            "name": data['name'], #상품명
            "title": data['title'],
            "review": data['review'],
            "rate": data['reviewStar'],
            "keyword": data['keyword'],
            "img_path": img_path,
            "reviewer": user_id
        }
        name_id = target_value + '_' + user_id #판매자id_상품명_구매자id
        self.db.child("review").child(name_id).set(review_info)
        return True
    
    #상품별 리뷰 불러오기
    def get_reviews(self, target_name):
        all_review = self.db.child("review").get().val()
        target_reviews = {}
        
        for review in all_review.each():
            name = all_review.child("name").get().val()
            if name == target_name:
                target_reviews[review.key()] = review.val()
    
        return target_reviews

    #전체리뷰불러오기
    def get_all_reviews(self):
        reviews = self.db.child("review").get().val()
        return reviews
    
    #이름으로 리뷰불러오기
    def get_review_byname(self, name):
        reviews = self.db.child("review").get()
        target_value=""
        print("###########",name)
        for res in reviews.each():
            key_value = res.key()
            if key_value == name:
                target_value=res.val()
        return target_value
    

    #상품 정보 등록하기
    def insert_item(self, name, data, item_path, photo_path, user_id):
        item_info = {
            "writer": user_id,
            "item_name": data['item_name'],
            "item_type": data['item_type'],
            "price": data['price'],
            "course_type": data.get('course_type'),
            "faculty": data.get('faculty'),
            "major": data['major'],
            "course_number": data['course_number'],
            "professor": data['professor'],
            "description": data['description'],
            "tag": data['tag'],
            "item_path": item_path,
            "photo_path": photo_path,
            "writer": user_id
        }
        user_and_item = user_id + '_' + data['item_name']
        self.db.child("item").child(user_and_item).set(item_info)
        print(data, item_path)
        print(data, photo_path)
        return True
    
    #상품 정보 불러오기
    def get_items(self):
        items = self.db.child("item").get().val()
        return items
    
    #상품 이름으로 상품 정보 가져오기
    def get_item_byname(self, name):
        items = self.db.child("item").get()
        target_value=""
        print("#############", name)
        for res in items.each():
            key_value = res.key()
            if key_value == name:
                target_value=res.val()
        return target_value
    

    #heart 정보 가져오기
    def get_heart_byname(self, uid, name):
        hearts = self.db.child("heart").child(uid).get()
        target_value=""
        if hearts.val() == None:
            return target_value
        
        for res in hearts.each():
            key_value = res.key()
        
            if key_value == name:
                target_value=res.val()
        return target_value
        
    #heart 값 변경하기    
    def update_heart(self, user_id, isHeart, item):
        heart_info ={
            "interested": isHeart
        }
        self.db.child("heart").child(user_id).child(item).set(heart_info)
        return True


    #사용자 포인트 가져오기
    def get_user_point(self, name):
        point=int(self.db.child("user").child(name).get().val()['point'])
        return point
    #사용자 랭킹포인트 가져오기
    def get_user_ranking_point(self, name):
        point=int(self.db.child("user").child(name).get().val()['rankingpoint'])
        return point
    #랭킹
    #유저 전체 가져오기
    def get_users(self ):
        items = self.db.child("user").get().val()
        return items
    #유저 대학 별 정렬
    def get_items_bycollege(self, cate):
        items = self.db.child("user").get()
        target_value=[]
        target_key=[]
        for res in items.each():
            value = res.val()
            key_value = res.key()
            if value['college'] == cate:
                target_value.append(value)
                target_key.append(key_value)
        print("######target_value",target_value)
        new_dict={}
        for k,v in zip(target_key,target_value):
            new_dict[k]=v
        return new_dict