from django.db import models

class Login(models.Model):
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    emailid = models.EmailField(max_length=50, primary_key=True)
    password = models.CharField(max_length=25)
    status = models.IntegerField(default=0)
    entry = models.CharField(max_length=6)

    class Meta:
        db_table = "login"

class UserProfile(models.Model):
    firstname = models.CharField(max_length=50, null=True)
    lastname = models.CharField(max_length=50, null=True)
    emailid = models.EmailField(max_length=50,primary_key=True)
    dob = models.CharField(max_length=25)
    gender = models.CharField(max_length=25)
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=25)
    qualification = models.CharField(max_length=25)
    profession = models.CharField(max_length=25)
    profilepic = models.FileField(upload_to='user/', null=True)

    class Meta:
        db_table = "user_register"

class ExpertProfile(models.Model):
    firstname = models.CharField(max_length=50, null=True)
    lastname = models.CharField(max_length=50, null=True)
    emailid = models.EmailField(max_length=50,primary_key=True)
    dob = models.CharField(max_length=25)
    gender = models.CharField(max_length=25)
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=25)
    qualification = models.CharField(max_length=25)
    registerno = models.CharField(max_length=25)
    yearofreg = models.CharField(max_length=25)
    experience = models.CharField(max_length=25)
    profilepic = models.FileField(upload_to='expert/', null=True)
    profstatement = models.TextField(null=True)
    languageknown = models.CharField(max_length=50,null=True)
    class Meta:
        db_table = "expert_register"

class UserAdvise(models.Model):
    emailid = models.EmailField(max_length=50)
    height = models.CharField(max_length=25)
    weight = models.CharField(max_length=25)
    hb = models.CharField(max_length=25)
    systolic = models.CharField(max_length=25)
    dystolic = models.CharField(max_length=25)
    fastingsugar = models.CharField(max_length=25)
    afterfood = models.CharField(max_length=25)
    hdl = models.CharField(max_length=25)
    ldl = models.CharField(max_length=25)
    tryglycerides = models.CharField(max_length=25)
    totalcholestrol = models.CharField(max_length=25)
    heartdisease = models.CharField(max_length=25)
    sedentaryperson = models.CharField(max_length=25)
    breakfast = models.CharField(max_length=15)
    lunch = models.CharField(max_length=10)
    snacks = models.CharField(max_length=10)
    dinner = models.CharField(max_length=10)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    class Meta:
        db_table = "health_profile"

class BMI(models.Model):
    agemin = models.IntegerField()
    agemax = models.IntegerField()
    bmimin = models.IntegerField()
    bmimax = models.IntegerField()

    class Meta:
        db_table = "bmi"

class BP(models.Model):
    agemin = models.IntegerField()
    agemax = models.IntegerField()
    lowmin = models.IntegerField()
    lowmax = models.IntegerField()
    normalmin = models.IntegerField()
    normalmax = models.IntegerField()
    highmin = models.IntegerField()
    highmax = models.IntegerField()

    class Meta:
        db_table = "bloodpressure"

class HB_MALE(models.Model):
    agemin = models.FloatField()
    agemax = models.FloatField()
    hbmin = models.FloatField()
    hbmax = models.FloatField()

    class Meta:
        db_table = "hb_male"


class HB_FEMALE(models.Model):
    agemin = models.FloatField()
    agemax = models.FloatField()
    hbmin = models.FloatField()
    hbmax = models.FloatField()

    class Meta:
        db_table = "hb_female"

class LDL(models.Model):
    LDLmin = models.CharField(max_length=5)
    LDLmax = models.CharField(max_length=5)
    status = models.CharField(max_length=25)

    class Meta:
        db_table = "LDL"

class HDL(models.Model):
    HDLmin = models.CharField(max_length=5)
    HDLmax = models.CharField(max_length=5)
    status = models.CharField(max_length=50)

    class Meta:
        db_table = "HDL"

class Tryglycerides(models.Model):
    trymin = models.CharField(max_length=5)
    trymax = models.CharField(max_length=5)
    status = models.CharField(max_length=50)

    class Meta:
        db_table = "Tryglycerides"

class TotalCholestrol(models.Model):
    totalmin = models.CharField(max_length=5)
    totalmax = models.CharField(max_length=5)
    status = models.CharField(max_length=50)

    class Meta:
        db_table = "Total_Cholestrol"

class FastingSugar(models.Model):
    fastingmin = models.CharField(max_length=5)
    fastingmax = models.CharField(max_length=5)
    status = models.CharField(max_length=50)

    class Meta:
        db_table = "Fasting_Sugar"

class AfterFood(models.Model):
    aftermin = models.CharField(max_length=5)
    aftermax = models.CharField(max_length=5)
    status = models.CharField(max_length=50)

    class Meta:
        db_table = "AfterFood"

class Report(models.Model):
    emailid = models.EmailField(max_length=50)
    bmi = models.CharField(max_length=50)
    bp = models.CharField(max_length=50)
    hb = models.CharField(max_length=50)
    sugar = models.CharField(max_length=50)
    afterfood = models.CharField(max_length=50)
    hdl = models.CharField(max_length=50)
    ldl = models.CharField(max_length=50)
    tryglycerine = models.CharField(max_length=50)
    totcholestrol = models.CharField(max_length=50)
    sedentary = models.CharField(max_length=50)
    heart = models.CharField(max_length=50)
    breakfast = models.CharField(max_length=50)
    lunch = models.CharField(max_length=50)
    snacks = models.CharField(max_length=50)
    dinner = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    status = models.IntegerField(default=0)
    
    class Meta:
        db_table = "user_report"

class Chat(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    sender = models.EmailField(max_length=50)
    receiver = models.EmailField(max_length=50)
    message = models.TextField()
    status = models.IntegerField(default=0)
    is_replyed = models.BooleanField(default=False)
    expert_read_status = models.BooleanField(default=False)
    user_read_status = models.BooleanField(default=False)

    class Meta:
        db_table = "chat"

class Feedback(models.Model):
    emailid = models.EmailField(max_length=50)
    profilepic = models.FileField(upload_to='user/', null=True)
    comment = models.TextField()

    class Meta:
        db_table = "feedback"