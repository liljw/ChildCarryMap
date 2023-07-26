from django.db import models


# 유저 
class Accounts(models.Model):
    userid = models.CharField(db_column='userId', primary_key=True, max_length=20)  # Field name made lowercase.
    userpw = models.CharField(db_column='userPw', max_length=20)  # Field name made lowercase.
    username = models.CharField(db_column='userName', max_length=10)  # Field name made lowercase.
    useremail = models.CharField(db_column='userEmail', max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'accounts'


# 북마크 
class Bookmarkva(models.Model):
    bookmarkvaid = models.IntegerField(db_column='bookmarkvaId', primary_key=True)  # Field name made lowercase.
    bookmarkvauserid = models.ForeignKey(Accounts, models.DO_NOTHING, db_column='bookmarkvaUserId')  # Field name made lowercase.
    bookmarkvawpid = models.ForeignKey('Valley', models.DO_NOTHING, db_column='bookmarkvaWpId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bookmarkva'


class Bookmarkwp(models.Model):
    bookmarkwpid = models.IntegerField(db_column='bookmarkwpId', primary_key=True)  # Field name made lowercase.
    bookmarkwpuserid = models.ForeignKey(Accounts, models.DO_NOTHING, db_column='bookmarkwpUserId')  # Field name made lowercase.
    bookmarkwpwpid = models.ForeignKey('Waterplay', models.DO_NOTHING, db_column='bookmarkwpWpId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bookmarkwp'


# 물놀이 
class Valley(models.Model):
    valleyid = models.AutoField(db_column='valleyId', primary_key=True)  # Field name made lowercase.
    valleyname = models.CharField(db_column='valleyName', max_length=30)  # Field name made lowercase.
    valleyaddrnew = models.CharField(db_column='valleyAddrNew', max_length=50, blank=True, null=True)  # Field name made lowercase.
    valleytelno = models.CharField(db_column='valleyTelNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    valleyla = models.FloatField(db_column='valleyLa')  # Field name made lowercase.    
    valleylo = models.FloatField(db_column='valleyLo')  # Field name made lowercase.    
    valleyunitescore = models.IntegerField(db_column='valleyUniteScore')  # Field name made lowercase.
    valleyreviewscore = models.IntegerField(db_column='valleyReviewScore')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'valley'


class Waterplay(models.Model):
    waterplayid = models.AutoField(db_column='waterplayId', primary_key=True)  # Field name made lowercase.
    waterplayname = models.CharField(db_column='waterplayName', max_length=30)  # Field name made lowercase.
    waterplayimgurl = models.CharField(db_column='waterplayImgUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    waterplayaddrold = models.CharField(db_column='waterplayAddrOld', max_length=50, blank=True, null=True)  # Field name made lowercase.
    waterplayaddrnew = models.CharField(db_column='waterplayAddrNew', max_length=50, blank=True, null=True)  # Field name made lowercase.
    waterplaytelno = models.CharField(db_column='waterplayTelNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    waterplayurl = models.CharField(db_column='waterplayUrl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    waterplayla = models.FloatField(db_column='waterplayLa')  # Field name made lowercase.
    waterplaylo = models.FloatField(db_column='waterplayLo')  # Field name made lowercase.
    waterplaysubname = models.CharField(db_column='waterplaySubName', max_length=10)  # Field name made lowercase.
    waterplaysubid = models.IntegerField(db_column='waterplaySubId')  # Field name made lowercase.
    waterplayvalue01 = models.CharField(db_column='waterplayValue01', max_length=100, blank=True, null=True)  # Field name made lowercase.
    waterplayname01 = models.CharField(db_column='waterplayName01', max_length=100, blank=True, null=True)  # Field name made lowercase.
    waterplayvalue02 = models.CharField(db_column='waterplayValue02', max_length=100, blank=True, null=True)  # Field name made lowercase.
    waterplayname02 = models.CharField(db_column='waterplayName02', max_length=100, blank=True, null=True)  # Field name made lowercase.
    waterplayvalue03 = models.CharField(db_column='waterplayValue03', max_length=100, blank=True, null=True)  # Field name made lowercase.
    waterplayname03 = models.CharField(db_column='waterplayName03', max_length=100, blank=True, null=True)  # Field name made lowercase.
    waterplayvalue04 = models.CharField(db_column='waterplayValue04', max_length=100, blank=True, null=True)  # Field name made lowercase.
    waterplayname04 = models.CharField(db_column='waterplayName04', max_length=100, blank=True, null=True)  # Field name made lowercase.
    waterplayvalue05 = models.CharField(db_column='waterplayValue05', max_length=100, blank=True, null=True)  # Field name made lowercase.
    waterplayname05 = models.CharField(db_column='waterplayName05', max_length=100, blank=True, null=True)  # Field name made lowercase.
    waterplayvalue06 = models.CharField(db_column='waterplayValue06', max_length=100, blank=True, null=True)  # Field name made lowercase.
    waterplayname06 = models.CharField(db_column='waterplayName06', max_length=100, blank=True, null=True)  # Field name made lowercase.
    waterplayvalue07 = models.CharField(db_column='waterplayValue07', max_length=100, blank=True, null=True)  # Field name made lowercase.
    waterplayname07 = models.CharField(db_column='waterplayName07', max_length=100, blank=True, null=True)  # Field name made lowercase.
    waterplayunitescore = models.IntegerField(db_column='waterplayUniteScore')  # Field name made lowercase.
    waterplayreviewscore = models.IntegerField(db_column='waterplayReviewScore')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'waterplay'


# 편의시설 
class Conv(models.Model):
    convid = models.CharField(db_column='convId', primary_key=True, max_length=30)  # Field name made lowercase.
    convpoiname = models.CharField(db_column='convPoiName', max_length=30)  # Field name made lowercase.
    convclname = models.CharField(db_column='convClName', max_length=10, blank=True, null=True)  # Field name made lowercase.
    convctprvnname = models.CharField(db_column='convCtprvnName', max_length=10, blank=True, null=True)  # Field name made lowercase.
    convsignguname = models.CharField(db_column='convSignguName', max_length=10, blank=True, null=True)  # Field name made lowercase.
    convlegaldongcd = models.CharField(db_column='convLegaldongCd', max_length=10, blank=True, null=True)  # Field name made lowercase.
    convlegaldongname = models.CharField(db_column='convLegaldongName', max_length=10, blank=True, null=True)  # Field name made lowercase.
    convla = models.FloatField(db_column='convLa')  # Field name made lowercase.        
    convlo = models.FloatField(db_column='convLo')  # Field name made lowercase.        
    convclnamectg = models.CharField(db_column='convClNameCtg', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'conv'


class Medi(models.Model):
    mediid = models.CharField(db_column='mediId', primary_key=True, max_length=30)  # Field name made lowercase.
    medipoiname = models.CharField(db_column='mediPoiName', max_length=30)  # Field name made lowercase.
    mediclname = models.CharField(db_column='mediClName', max_length=10, blank=True, null=True)  # Field name made lowercase.
    medictprvnname = models.CharField(db_column='mediCtprvnName', max_length=10, blank=True, null=True)  # Field name made lowercase.
    medisignguname = models.CharField(db_column='mediSignguName', max_length=10, blank=True, null=True)  # Field name made lowercase.
    medilegaldongcd = models.CharField(db_column='mediLegaldongCd', max_length=10, blank=True, null=True)  # Field name made lowercase.
    medilegaldongname = models.CharField(db_column='mediLegaldongName', max_length=10, blank=True, null=True)  # Field name made lowercase.
    medila = models.FloatField(db_column='mediLa')  # Field name made lowercase.        
    medilo = models.FloatField(db_column='mediLo')  # Field name made lowercase.        
    mediclnamectg = models.CharField(db_column='mediClNameCtg', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'medi'


class Parking(models.Model):
    parkingid = models.CharField(db_column='parkingId', primary_key=True, max_length=30)  # Field name made lowercase.
    parkingfcltyname = models.CharField(db_column='parkingFcltyName', max_length=30)  # Field name made lowercase.
    parkingctprvnname = models.CharField(db_column='parkingCtprvnName', max_length=10, blank=True, null=True)  # Field name made lowercase.
    parkingsignguname = models.CharField(db_column='parkingSignguName', max_length=10, blank=True, null=True)  # Field name made lowercase.
    parkinglegaldongcd = models.CharField(db_column='parkingLegaldongCd', max_length=10, blank=True, null=True)  # Field name made lowercase.
    parkinglegaldongname = models.CharField(db_column='parkingLegaldongName', max_length=10, blank=True, null=True)  # Field name made lowercase.
    parkingaddrnew = models.CharField(db_column='parkingAddrNew', max_length=50, blank=True, null=True)  # Field name made lowercase.
    parkingla = models.FloatField(db_column='parkingLa')  # Field name made lowercase.  
    parkinglo = models.FloatField(db_column='parkingLo')  # Field name made lowercase.  
    parkingflagname = models.CharField(db_column='parkingFlagName', max_length=10, blank=True, null=True)  # Field name made lowercase.
    parkingparkingspceco = models.IntegerField(db_column='parkingParkingSpceCo', blank=True, null=True)  # Field name made lowercase.
    parkingutiliizalmttflagname = models.CharField(db_column='parkingUtiliizaLmttFlagName', max_length=10, blank=True, null=True)  # Field name made lowercase.
    parkingwkdayname = models.CharField(db_column='parkingWkdayName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    parkingworkdayopenbsnstime = models.CharField(db_column='parkingWorkdayOpenBsnsTime', max_length=10, blank=True, null=True)  # Field name made lowercase.
    parkingworkdayclostime = models.CharField(db_column='parkingWorkdayClosTime', max_length=10, blank=True, null=True)  # Field name made lowercase.
    parkingsatopenbsnstime = models.CharField(db_column='parkingSatOpenBsnsTime', max_length=10, blank=True, null=True)  # Field name made lowercase.
    parkingsatclostime = models.CharField(db_column='parkingSatClosTime', max_length=10, blank=True, null=True)  # Field name made lowercase.
    parkingsunopenbsnstime = models.CharField(db_column='parkingSunOpenBsnsTime', max_length=10, blank=True, null=True)  # Field name made lowercase.
    parkingsunclostime = models.CharField(db_column='parkingSunClosTime', max_length=10, blank=True, null=True)  # Field name made lowercase.
    parkingutiliizachrgecn = models.CharField(db_column='parkingUtiliizaChrgeCn', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'parking'


class Safe112(models.Model):
    safe112id = models.CharField(db_column='safe112Id', primary_key=True, max_length=30)  # Field name made lowercase.
    safe112mlsfcname = models.CharField(db_column='safe112MlsfcName', max_length=10)  # Field name made lowercase.
    safe112fcltyname = models.CharField(db_column='safe112FcltyName', max_length=30)  # Field name made lowercase.
    safe112ctprvnname = models.CharField(db_column='safe112CtprvnName', max_length=10, blank=True, null=True)  # Field name made lowercase.
    safe112signguname = models.CharField(db_column='safe112SignguName', max_length=10, blank=True, null=True)  # Field name made lowercase.
    safe112legaldongname = models.CharField(db_column='safe112LegaldongName', max_length=10, blank=True, null=True)  # Field name made lowercase.
    safe112legaldongcd = models.CharField(db_column='safe112LegaldongCd', max_length=10, blank=True, null=True)  # Field name made lowercase.
    safe112la = models.FloatField(db_column='safe112La')  # Field name made lowercase.  
    safe112lo = models.FloatField(db_column='safe112Lo')  # Field name made lowercase.  

    class Meta:
        managed = False
        db_table = 'safe112'


class Safe119(models.Model):
    safe119id = models.CharField(db_column='safe119Id', primary_key=True, max_length=30)  # Field name made lowercase.
    safe119fcltyname = models.CharField(db_column='safe119FcltyName', max_length=30)  # Field name made lowercase.
    safe119mlsfcname = models.CharField(db_column='safe119MlsfcName', max_length=10)  # Field name made lowercase.
    safe119la = models.FloatField(db_column='safe119La')  # Field name made lowercase.  
    safe119lo = models.FloatField(db_column='safe119Lo')  # Field name made lowercase.  

    class Meta:
        managed = False
        db_table = 'safe119'


class Toilet(models.Model):
    toiletid = models.CharField(db_column='toiletId', primary_key=True, max_length=30)  # Field name made lowercase.
    toiletfcltyname = models.CharField(db_column='toiletFcltyName', max_length=30)  # Field name made lowercase.
    toiletctprvnname = models.CharField(db_column='toiletCtprvnName', max_length=10, blank=True, null=True)  # Field name made lowercase.
    toiletsignguname = models.CharField(db_column='toiletSignguName', max_length=10, blank=True, null=True)  # Field name made lowercase.
    toiletlegaldongcd = models.CharField(db_column='toiletLegaldongCd', max_length=10, blank=True, null=True)  # Field name made lowercase.
    toiletlegaldongname = models.CharField(db_column='toiletLegaldongName', max_length=10, blank=True, null=True)  # Field name made lowercase.
    toiletaddrnew = models.CharField(db_column='toiletAddrNew', max_length=50, blank=True, null=True)  # Field name made lowercase.
    toiletaddrold = models.CharField(db_column='toiletAddrOld', max_length=50, blank=True, null=True)  # Field name made lowercase.
    toiletla = models.FloatField(db_column='toiletLa')  # Field name made lowercase.    
    toiletlo = models.FloatField(db_column='toiletLo')  # Field name made lowercase.    
    toiletaditdc = models.CharField(db_column='toiletAditDc', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'toilet'
