from django.contrib import admin
from .models import Todo

# 내가 직접 추가한 모델을 관리자 페이지에도 반영하기.
@admin.register(Todo)
class ItemAdmin(admin.ModelAdmin):
    #관리자 페이지 게시판에 표시할 내용 정하는 속성
    pass