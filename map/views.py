from django.shortcuts import render
from rest_framework import mixins, generics
from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Accounts, Bookmarkwp, Waterplay
from .serializers import AccountsSerializer, BookmarkwpSerializer, WaterplaySerializer


# 데이터 조회 / 저장용 클래스
# 데이터 조회 (SELECT : list(), 리액트에서는 get() 호출)
# 데이터 저장 (INSERT : create(), 리액트에서는 post() 호출)
class AccountsAPIMixins(
    mixins.ListModelMixin, 
    mixins.CreateModelMixin, 
    generics.GenericAPIView
):
    queryset = Accounts.objects.all()
    serializer_class = AccountsSerializer

    # GET : 모든 회원 정보 조회 
    # 관리자 전용 
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)  # mixins.ListModelMixin과 연결
    
    # POST : 회원가입 
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)  # mixins.CreateModelMixin과 연결


# 데이터 상세 조회 (1개 SELECT) / 수정 / 삭제 용 클래스
class AccountAPIMixins(
    mixins.RetrieveModelMixin, 
    mixins.UpdateModelMixin, 
    mixins.DestroyModelMixin, 
    generics.GenericAPIView
):
    queryset = Accounts.objects.all()
    serializer_class = AccountsSerializer
    lookup_field = "userid"  # 기본키 설정

    # GET : 마이페이지 - 개인정보 조회 
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)  # mixins.RetrieveModelMixin과 연결

    # PUT : 마이페이지 - 개인정보 수정 
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)  # mixins.UpdateModelMixin과 연결

    # DELETE : 마이페이지 - 회원 탈퇴 
    def delete(self, request, *args, **kwargs):  # DELETE 메서드 처리 함수 (1권 삭제)
        return self.destroy(request, *args, **kwargs)  # mixins.DestroyModelMixin과 연결


class WPsAPIMixins(
    mixins.ListModelMixin, 
    mixins.CreateModelMixin, 
    generics.GenericAPIView
):
    queryset = Waterplay.objects.all()
    serializer_class = WaterplaySerializer
    
    # GET : 지도 - 모든 바닥분수/물놀이장 위치 반환 
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)  # mixins.ListModelMixin과 연결

    # POST : 바닥분수/물놀이장 정보 추가 
    # 관리자 전용
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)  # mixins.CreateModelMixin과 연결


class WPsTypeAPIMixins(generics.ListAPIView):
    serializer_class = WaterplaySerializer
    lookup_field = "waterplaysubid"
    
    def get_queryset(self):
        print(self.kwargs["waterplaysubid"])
        
        if self.kwargs["waterplaysubid"] == 1:
            return Waterplay.objects.filter(
                waterplaysubid = 1
            )
        elif self.kwargs["waterplaysubid"] == 2:
            return Waterplay.objects.filter(
                waterplaysubid = 2
            )
        else:
            return Waterplay.objects.filter(
                waterplaysubid = 3
            )


class WPAPIMixins(
    mixins.RetrieveModelMixin, 
    mixins.UpdateModelMixin, 
    mixins.DestroyModelMixin, 
    generics.GenericAPIView
):
    queryset = Waterplay.objects.all()
    serializer_class = WaterplaySerializer
    lookup_field = "waterplayid"  # 기본키 설정

    # GET : 지도/상세페이지 - 1개의 바닥분수/물놀이장 정보 반환 
    def get(self, request, *args, **kwargs):  # GET 메서드 처리 함수 (1권 조회)
        return self.retrieve(request, *args, **kwargs)  # mixins.RetrieveModelMixin과 연결

    # PUT : 바닥분수/물놀이장 정보 수정 
    # 관리자 전용 
    def put(self, request, *args, **kwargs):  # PUT 메서드 처리 함수
        return self.update(request, *args, **kwargs)  # mixins.UpdateModelMixin과 연결

    # DELETE : 바닥분수/물놀이장 정보 삭제 
    # 관리자 전용 
    def delete(self, request, *args, **kwargs):  # DELETE 메서드 처리 함수 (1권 삭제)
        return self.destroy(request, *args, **kwargs)  # mixins.DestroyModelMixin과 연결
