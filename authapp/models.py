from typing import Any
from django.db import models

# Create your models here.

class Members(models.Model):

    user_name = models.CharField(max_length = 255)
    email = models.EmailField()
    password = models.CharField(max_length = 255)
        
    @property
    def get_members_obj(self):
        return Members.objects.all()

    def get_users(self) -> dict:
        #existing usernames and emails
        members = Members.objects.all()
        usernames = []
        emails = []
        for member in members:
            usernames.append(member.user_name)
            emails.append(member.email)
        return {
            'usernames': usernames,
            'emails' : emails
        }


    def is_valid(self ,posted_info : list) -> bool:
        self.posted_info = posted_info
        user_name_sent = posted_info['username']
        email_sent = posted_info['email']
        
        
        #existing usernames and emails
        users = self.get_users(self)
        usernames = users['usernames']
        emails = users['emails']
        
        #check if user exists
        if user_name_sent in usernames or email_sent in emails:
            return False
        
        return True
    
    def register_user(self):
        posted_info = self.posted_info
        user_name_sent = posted_info['username']
        email_sent = posted_info['email']
        password_sent = posted_info['password']

        member = Members(user_name = user_name_sent, email = email_sent, password = password_sent)
        member.save()

    def check_user_exist(self, username_sent):
        if username_sent in self.get_users(self)['usernames']:
            return True
        return False
    
    def login_user(self, info):
        if self.check_user_exist(self ,info['username']):
            data = Members.objects.filter(user_name=info['username']).get()
            if info['password'] == data.password:
                return True
        
        return False

            

        
    # def delete_user_by_id(self, id : int):
    #     for member in self.get_members_obj:
    #         id_search = member.id
    #         if id_search == id:
    #             member.delete()

    # def delete_all():
    #     member = Members.objects.all()
    #     member.delete()