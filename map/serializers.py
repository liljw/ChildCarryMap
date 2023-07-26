from rest_framework import serializers
from .models import Accounts, Bookmarkwp, Waterplay
from .models import Toilet, Conv, Medi, Safe112, Safe119, Parking


class AccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = [
            "userid",
            "userpw",
            "username",
            "useremail",
        ]


class BookmarkwpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmarkwp
        fields = [
            "bookmarkwpid",
            "bookmarkwpuserid",
            "bookmarkwpwpid",
        ]


class WaterplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Waterplay
        fields = [
            "waterplayid",
            "waterplayname",
            "waterplayimgurl",
            "waterplayaddrold",
            "waterplayaddrnew",
            "waterplaytelno",
            "waterplayurl",
            "waterplayla",
            "waterplaylo",
            "waterplaysubname",
            "waterplaysubid",
            "waterplayvalue01",
            "waterplayname01",
            "waterplayvalue02",
            "waterplayname02",
            "waterplayvalue03",
            "waterplayname03",
            "waterplayvalue04",
            "waterplayname04",
            "waterplayvalue05",
            "waterplayname05",
            "waterplayvalue06",
            "waterplayname06",
            "waterplayvalue07",
            "waterplayname07",
            "waterplayunitescore",
            "waterplayreviewscore",
        ]


class ToiletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Toilet
        fields = [
            "toiletid",
            "toiletfcltyname",
            "toiletctprvnname",
            "toiletsignguname",
            "toiletlegaldongcd",
            "toiletlegaldongname",
            "toiletaddrnew",
            "toiletaddrold",
            "toiletla",
            "toiletlo",
            "toiletaditdc",
        ]


class ConvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conv
        fields = [
            "convid",
            "convpoiname",
            "convclname",
            "convctprvnname",
            "convsignguname",
            "convlegaldongcd",
            "convlegaldontoiletgname",
            "convla",
            "convlo",
            "convclnamectg",
        ]


class MediSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medi
        fields = [
            "mediid",
            "medipoiname",
            "mediclname",
            "medictprvnname",
            "medisignguname",
            "medilegaldongcd",
            "medilegaldongname",
            "medila",
            "medilo",
            "mediclnamectg",
        ]


class Safe112Serializer(serializers.ModelSerializer):
    class Meta:
        model = Safe112
        fields = [
            "safe112id",
            "safe112mlsfcname",
            "safeconv112fcltyname",
            "safe112ctprvnname",
            "safe112signguname",
            "safe112legaldongname",
            "safe112legaldongcd",
            "safe112la",
            "safe112lo",
        ]


class Safe119Serializer(serializers.ModelSerializer):
    class Meta:
        model = Safe119
        fields = [
            "safe119id",
            "safe119fcltyname",
            "safe119mlsfcname",
            "safe119la",
            "safe119lo",
        ]


class ParkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parking
        fields = [
            "Parkingid",
            "Parkingfcltyname",
            "Parkingctprvnname",
            "Parkingsignguname",
            "Parkinglegaldongcd",
            "Parkinglegaldongname",
            "Parkingaddrnew",
            "parkingla",
            "parkinglo",
            "parkingflagname",
            "parkingparkingspceco",
            "parkingutiliizalmttflagname",
            "parkingwkdayname",
            "parkingworkdayopenbsnstime",
            "parkingworkdayclostime",
            "parkingsatopenbsnstime",
            "parkingsatclostime",
            "parkingsunopenbsnstime",
            "parkingsunclostime",
            "parkingutiliizachrgecn",
        ]
