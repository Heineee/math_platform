from ..models import Posttext,User,Answer_question

def get_history_post():
    post_texts = list(Posttext.objects.filter(Judge=True))

    def get_post_text(post_text):
        return {
            'text': post_text.text,
            'username': post_text.username,
            'index': post_text.index,
            'likes': post_text.likes,
            'dislikes': post_text.dislikes,
            'date': post_text.date,
            'recommended_developer': post_text.recommended_developer,
            "viewers": post_text.viewers
        }

    post_texts = list(map(get_post_text, post_texts))
    return post_texts

def get_history_post2():
    post_texts = list(Posttext.objects.filter(Judge=False))

    def get_post_text(post_text):
        return {
            'text': post_text.text,
            'username': post_text.username,
            'index': post_text.index,
            'likes': post_text.likes,
            'dislikes': post_text.dislikes,
            'date': post_text.date,
            'recommended_developer': post_text.recommended_developer,
            "viewers": post_text.viewers,
            'title': post_text.title,
        }

    post_texts = list(map(get_post_text, post_texts))
    return post_texts

def get_check_post():
    answer= list(Answer_question.objects.filter(Judge=False))

    def get_post_text(post_text):
        return {
            'text': post_text.answer,
            'username': post_text.username,
            "answer": post_text.answer,
            'question_title': post_text.question_title,
        }

    answer = list(map(get_post_text, answer))
    return answer

def get_text_information(username):
    post_texts = list(Posttext.objects.filter(username=username))

    def get_post_text(post_text):
        return {
            'title': post_text.title,
            'text': post_text.text,
            'likes': post_text.likes,
            'dislikes': post_text.dislikes,
            'date': post_text.date,
            'recommended_developer': post_text.recommended_developer,
            "viewers": post_text.viewers,
            'rate':post_text.likes/(post_text.likes+post_text.dislikes)*100  if post_text.likes+post_text.dislikes!=0 else 0
        }
    post_texts = list(map(get_post_text, post_texts))
    return post_texts

def get_users_information():
    user_information=list(User.objects.all())
    def get_user_information(user):
        return {
            'gender': user.gender,
            'birthday': user.birthday,
            'address': user.address,
            'last_login': user.last_login,
            'last_exit': user.last_exit,
        }
    user_information = (map(get_user_information, user_information))
    return user_information

def get_only_user_information():
    user_information=list(User.objects.all())
    def get_user_information(user):
        return {
            "username": user.username,
            "email": user.email,
            "gender": user.gender,
            "birthday": user.birthday,
            "address": user.address,
            "last_login": user.last_login,
            "last_exit": user.last_exit,
        }
    user_information = list(map(get_user_information, user_information))
    return user_information

