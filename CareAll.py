class Register:
    registered=[]
    retired_folk=[]
    young_folk=[]
    def __init__(self,name,gender,age,email,contact,locality,user_name,password):
        self.name=name
        self.gender=gender
        self.age=age
        self.email=email
        self.contact=contact
        self.locality=locality
        self.user_name=user_name
        self.password=password
        self.is_active=True
        self.count=1
        self.amount=0
        Register.registered.append(self)
    def active(self):
        if self in Register.young_folk:
            if self.count>4:
                return self.is_active==False
            else:
                return self.is_active==True
        else:
            if self.count>1:
                return self.is_active==False
            else:
                return self.is_active==True
    def get_details(self):
        if self.active()==True:
            temp=[]
            d={}
            d['Name']=self.name
            d['Age']=self.age
            d['Email']=self.email
            d['Contact']=self.contact
            d['Locality']=self.locality
            d['User Name']=self.user_name
            temp.append(d)
            return temp
    def retired_folk_details(self):
        if self in Register.young_folk:
            temp=[]
            for i in Register.retired_folk:
                temp.append(Register.get_details(i))
            return temp
        else:
            return f'Sorry You are a part of retaired folk. So you only get your details and the details is {Register.get_details(self)}'
    proposals=[]
    def send_proposal(self,proposal,retire_folk_user_name):
        if self.active()==True:
            d=[]
            if self in Register.young_folk:
                d.append(Register.get_details(self))
                d.append(proposal)
                d.append(retire_folk_user_name)
                return Register.proposals.append(d)
            else:
                return "sorry you are not able to send_proposal"
    def my_proposal(self):
        if self in Register.retired_folk:
            temp=[]
            for i in Register.proposals:
                if self.user_name==i[-1]:
                    temp.append(i[:-1])
            return temp
        else:
            temp=[]
            for i in Register.proposals:
                if Register.get_details(self)==i[0]:
                    temp.append(i[1:])
            return temp
    def aproved(self,user_name):
        if self.active()==True:
            if self in Register.retired_folk:
                self.count+=1
                for i in self.my_proposal():
                    for j in i[0]:
                        for k,v in j.items():
                            if user_name == v:
                                for i in Register.young_folk:
                                    if i.active()==True:
                                        self.amount-=2000
                                        if user_name == i.user_name:
                                            i.count+=1
                                            i.amount+=2000
                                            return f'You hired him. he reach at your door soon.'
                                        else:
                                            return 'you enter wrong no.'
                                    else:
                                        return 'The younger is not availabe'
            else:
                return 'sorry, This is only aproved by retired folk.'
        else:
            return 'you already in work'
    About_Care_All=[]
    def give_reviews(self,review,rating):
        d={}
        d['Name']=self.name
        d['Review']=review
        d['Rating']= rating
        return Register.About_Care_All.append(d)

User1=Register('ABC','M',24,"Abc@gmail.com","7787030497",'Hydrabad','abc1','9988776655')
User2=Register('PQR','M',54,"Pqr@gmail.com","7787030497",'Bangalur','pqr2','9994546844')
User3=Register('XYZ','M',24,"Xyz@gmail.com","7787030497",'Kolkata','xyz3','6545656545')
User4=Register('MNO','M',78,"mno@gmail.com","7787030497",'Hydrabad','mno4','9665465465')
User5=Register('GHI','M',43,"ghi@gmail.com","7787030497",'bangalure','ghi5','9654658585')
User6=Register('STU','M',93,"stu@gmail.com","7787030497",'bangalure','stu6','9654658585')
User7=Register('DEF','M',26,"def@gmail.com","7787030497",'bangalure','def7','9654658585')
User8=Register('JKL','M',62,"jkl@gmail.com","7787030497",'bangalure','jkl8','9654658585')
User9=Register('OPQ','M',39,"opq@gmail.com","7787030497",'bangalure','opq9','9654658585')
User10=Register('RST','M',69,"rst@gmail.com","7787030497",'bangalure','rst10','9654658585')
User11=Register('QMS','M',56,"qms@gmail.com","7787030497",'bangalure','qms11','9654658585')
User12=Register('WUZ','M',96,"wuz@gmail.com","7787030497",'bangalure','wuz12','9654658585')

for i in Register.registered:
    if i.age>50:
        Register.retired_folk.append(i)
    else:
        Register.young_folk.append(i)

# print(User1.retired_folk_details())
# print("-----------------------------------")
# print(User2.retired_folk_details())
# print("-----------------------------------")
# print(User3.retired_folk_details())
# print("-----------------------------------")
# print(User4.retired_folk_details())

User1.send_proposal('i want to serve you','mno4')
User1.send_proposal('i want to serve you','stu6')
User1.send_proposal('i want to serve you','qms11')
User1.send_proposal('i want to serve you','wuz12')
User1.send_proposal('i want to serve you','jkl8')

User3.send_proposal('dear sir i want to serve for you','pqr2')
User3.send_proposal('i want to serve you','mno4')

User5.send_proposal('i want to serve you','pqr2')
User5.send_proposal('i want to serve you','mno4')
User5.send_proposal('i want to serve you','qms11')

# print(User1.my_proposal())
# print("-----------------------------------")
# print(User7.my_proposal())
# print("-----------------------------------")
# print(User4.my_proposal()) #user4 is a retired folk
# print("-----------------------------------")
# print(User4.aproved('abc1'))
# print(User2.aproved('abc1'))
# print("-----------------------------------")
# print(User6.aproved('abc1'))
# print("-----------------------------------")
# print(User7.aproved('abc1'))
# print("-----------------------------------")
# print(User11.aproved('abc1'))
# print("-----------------------------------")
# print(User8.aproved('abc1'))
# print("-----------------------------------")
# print(User11.aproved('ghi5'))
# print("-----------------------------------")
# print(User12.aproved('abc1'))

# print(User1.amount)
# print(User4.amount)
# print(User2.amount)
# print(User12.amount)
# print(User11.amount)

User1.give_reviews('this is the best way to serve for old people',4.5)
User2.give_reviews('i am very happy',4.8)
User4.give_reviews('i am doing now for 5 people',4.3)
User8.give_reviews('this is worst aplication',1)
print(User3.About_Care_All)


# print(User8.amount)