from django.shortcuts import render,HttpResponse,redirect,loader,get_object_or_404
from django.contrib import messages
from django import forms
from datetime import datetime,date,time
from mydiet.models import Login
from mydiet.models import UserProfile
from mydiet.models import ExpertProfile
from mydiet.models import UserAdvise
from mydiet.models import BMI,BP,HB_FEMALE,HB_MALE,HDL,LDL,Tryglycerides,TotalCholestrol,FastingSugar,AfterFood
from mydiet.models import Report
from mydiet.models import UserChat
"-----------------------HomePages-------------------------------"
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
def expert(request):
    obj1 = Login.objects.filter(entry="Expert")
    length = len(obj1)
    mydict = []
    for i in range(len(obj1)):
        mylogin = obj1[i]
        useremail = mylogin.emailid
        obj2 = ExpertProfile.objects.filter(emailid=useremail).values().distinct()
        mydict.append(obj2)
    print(mydict)
    length = len(mydict)
    print(length)
    print(type(obj1))
    print(type(mydict))
    context = {'expert': mydict}
    return render(request,'experts.html',context)
def dietandnutrition(request):
    template = loader.get_template('dietandnutrition.html')
    return HttpResponse(template.render())
def article(request):
    template = loader.get_template('article.html')
    return HttpResponse(template.render())
def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())

"-----------------------Login and Register-------------------------------"
def user_register(request):
    if request.method == "POST":
        if request.POST.get('firstname') and request.POST.get('lastname') and request.POST.get('email') and request.POST.get('password') and request.POST.get('confirmpassword'):
            form = Login()
            form.firstname = request.POST.get('firstname')
            form.lastname = request.POST.get('lastname')
            form.emailid = request.POST.get('email')
            form.password = request.POST.get('password')
            cnfpassword = request.POST.get('confirmpassword')

            if form.password == cnfpassword:
                form.entry = "User"
                form.save()
                return redirect('/login')
            else:
                #messages.warning(request, 'Password does not match')
                form = Login()
                return render(request, 'user_register.html')
        else:
            messages.warning(request, 'Please fill all the fields to continue...')

    else:
        return render(request, 'user_register.html')
def expert_register(request):
    if request.method == "POST":
        if request.POST.get('firstname') and request.POST.get('lastname') and request.POST.get('emailid') and request.POST.get('password') and request.POST.get('confirmpassword'):
            form = Login()
            form.firstname = request.POST.get('firstname')
            form.lastname = request.POST.get('lastname')
            form.emailid = request.POST.get('emailid')
            form.password = request.POST.get('password')
            cnfpassword = request.POST.get('confirmpassword')

            if form.password == cnfpassword:
                form.entry = "Expert"
                form.save()
                return redirect('/login')
            else:
                #messages.warning(request, 'Password does not match')
                form = Login()
                return render(request, 'expert_register.html')
        else:
            messages.warning(request, 'Please fill all the fields to continue...')

    else:
        return render(request, 'expert_register.html')

def login(request):
    if request.method == "POST":
        if request.POST.get('emailaddress') and request.POST.get('pass'):
            userid = request.POST.get('emailaddress')
            passw = request.POST.get('pass')

            obj1 = Login.objects.get(emailid = userid)
            dbfirstname = obj1.firstname
            dblastname = obj1.lastname
            dbemail = obj1.emailid
            dbpass = obj1.password
            dbstatus = obj1.status
            dbentry = obj1.entry

            if dbemail == userid and dbpass == passw and dbstatus == 0  and dbentry == "User" :
                request.session['firstname'] = dbfirstname
                request.session['lastname'] = dblastname
                return redirect('/user_profile/?email=%s'%dbemail)
            elif dbemail == userid and dbpass == passw and dbstatus == 1  and dbentry == "User" :
                return redirect('/user_home/?email=%s'% dbemail)
            elif dbemail == userid and dbpass == passw and dbstatus == 0  and dbentry == "Expert" :
                request.session['firstname'] = dbfirstname
                request.session['lastname'] = dblastname
                return redirect('/expert_profile/?email=%s'% dbemail)
            elif dbemail == userid and dbpass == passw and dbstatus == 1  and dbentry == "Expert" :
                return redirect('/expert_home/?email=%s'% dbemail)
            elif dbemail == userid and dbpass == passw and dbstatus == 1  and dbentry == "Admin" :
                return redirect('/admin_home/?email=%s'% dbemail)
            else:
                return render(request, 'Login.html')
    else:
        return render(request, 'Login.html')

def user_profile(request):
    if request.method == "POST":
        if request.POST.get('emailid') and request.POST.get('birthday') and request.POST.get('gender') and request.POST.get('address') and request.POST.get('phone') and request.POST.get('qualification') and request.POST.get('profession'):
            myform = UserProfile()
            myform.emailid = request.POST.get('emailid')
            myform.dob = request.POST.get('birthday')
            myform.gender = request.POST.get('gender')
            myform.address = request.POST.get('address')
            myform.phone = request.POST.get('phone')
            myform.qualification = request.POST.get('qualification')
            myform.profession = request.POST.get('profession')
            firstname = request.session['firstname']
            lastname = request.session['lastname']
            myform.firstname = firstname
            myform.lastname = lastname
            myform.profilepic = request.FILES['picture']

            em = request.POST.get('emailid')
            obj1 = Login.objects.get(emailid = em)
            dbemail = obj1.emailid
            print(dbemail)
            if em == dbemail:
                obj1.status = 1
                obj1.save()
                myform.save()
                return redirect('/user_home/?email=%s'%dbemail)
            else:
                messages.add_message(request,'emailid doesnot exist')
        else:
            myform = UserProfile()
            return render(request, 'user_profile.html')

    return render(request, 'user_profile.html')

def expert_profile(request):
    if request.method == "POST":
        if request.POST.get('emailid') and request.POST.get('birthday') and request.POST.get('gender') and request.POST.get('address') and request.POST.get('phone') and request.POST.get('qualification') and request.POST.get('regno') and request.POST.get('year') and request.POST.get('experience') and request.POST.get('about') and request.POST.get('language'):
            myform = ExpertProfile()
            myform.emailid = request.POST.get('emailid')
            myform.dob = request.POST.get('birthday')
            myform.gender = request.POST.get('gender')
            myform.address = request.POST.get('address')
            myform.phone = request.POST.get('phone')
            myform.qualification = request.POST.get('qualification')
            myform.registerno = request.POST.get('regno')
            myform.yearofreg = request.POST.get('year')
            myform.experience = request.POST.get('experience')
            firstname = request.session['firstname']
            lastname = request.session['lastname']
            myform.firstname = firstname
            myform.lastname = lastname
            myform.profilepic = request.FILES['picture']
            myform.profstatement = request.POST.get('about')
            myform.languageknown = request.POST.get('language')

            em = request.POST.get('emailid')
            obj1 = Login.objects.get(emailid=em)
            dbemail = obj1.emailid
            print(dbemail)
            if em == dbemail:
                obj1.status = 1
                obj1.save()
                myform.save()
                return redirect('/expert_home/?email=%s' % dbemail)
            else:
                messages.add_message(request, 'emailid doesnot exist')
        else:
            myform = ExpertProfile()
            return render(request, 'expert_profile.html')

    return render(request, 'expert_profile.html')

"-----------------------Login Profiles-------------------------------"
def user_home(request):
    useremail = request.GET.get('email')
    print("useremail = ",useremail)
    request.session['email'] = useremail
    userregister = Login.objects.filter(emailid=useremail).values()
    print(userregister)
    userprofile = UserProfile.objects.filter(emailid = useremail).values()
    print(userprofile)
    return render(request, 'user_home.html', {'userhomepage': userregister,'userprofile' : userprofile},)

def user_dn(request):
    useremail = request.GET.get('email')
    userregister = Login.objects.filter(emailid=useremail).values()
    stat = ''
    try:
        userreport = Report.objects.get(emailid=useremail)
        print("UR = ",userreport)
        status = userreport.status  # if status = 0 then preview history will be disabled
        stat = status
    except Report.DoesNotExist:
        stat = 0
    request.session['email'] = useremail # passing email so as to fetch history
    return render(request, 'user_d & n.html', {'userdn' : userregister,'status' : stat})

def user_advise(request):
    if request.method == "POST":
        if request.POST.get('emailid') and request.POST.get('height') and request.POST.get('weight') and request.POST.get('hb') and request.POST.get('systolic') and request.POST.get('dystolic') and request.POST.get('fasting sugar') and request.POST.get('after food') and request.POST.get('hdl') and request.POST.get('ldl') and request.POST.get('try') and request.POST.get('total') and request.POST.get('heartdiseases') and request.POST.get('sedentary') and request.POST.get('breakfast') and request.POST.get('lunch') and request.POST.get('snacks') and request.POST.get('dinner'):
            form = UserAdvise()
            form.emailid = request.POST.get('emailid')
            form.height = request.POST.get('height')
            form.weight = request.POST.get('weight')
            form.hb = request.POST.get('hb')
            form.systolic = request.POST.get('systolic')
            form.dystolic = request.POST.get('dystolic')
            form.fastingsugar = request.POST.get('fasting sugar')
            form.afterfood = request.POST.get('after food')
            form.hdl = request.POST.get('hdl')
            form.ldl = request.POST.get('ldl')
            form.tryglycerides = request.POST.get('try')
            form.totalcholestrol = request.POST.get('total')
            form.heartdisease = request.POST.get('heartdiseases')
            form.sedentaryperson = request.POST.get('sedentary')
            form.breakfast = request.POST.get('breakfast')
            form.lunch = request.POST.get('lunch')
            form.snacks = request.POST.get('snacks')
            form.dinner = request.POST.get('dinner')
            # Displaying Current date and time with Day #Current Date + Formating date with Day
            form.date = datetime.date(datetime.today()).strftime("%Y-%m-%d")
            # Current Time
            Time = datetime.time(datetime.now())
            # Formating Time
            form.time = time.strftime(Time,"%H:%M:%S")

            obj1 = Login.objects.get(emailid = form.emailid)
            dbemail = obj1.emailid
            if form.emailid == dbemail:
                form.save()
                obj2 = UserAdvise.objects.filter(emailid = dbemail)
                print(obj2)
                length = len(obj2)
                if length > 1:
                    myobj = obj2[length-1]
                    print("IF CASE")
                    print(myobj)
                    myid = myobj.id
                    print(myid)
                    return redirect('/user_result/?id=%d'%myid)
                else:
                    myobj = obj2[0]
                    print("ELSE CASE")
                    print(myobj)
                    myid = myobj.id
                    print(myid)
                    return redirect('/user_result/?id=%d'%myid)
            else:
                form = UserAdvise()
                return HttpResponse("Emailid not matching")
        else:
            return HttpResponse("Fill all fields")
    return render(request, 'user_advise.html')

def user_result(request):
    userid = request.GET.get('id')
    print(userid)
    healthprofile = UserAdvise.objects.get(id=userid)
    print(healthprofile)
    useremail = healthprofile.emailid
    #Fetching all fields from healthprofile
    Height = float(healthprofile.height)
    Weight = float(healthprofile.weight)
    Hb = float(healthprofile.hb)
    Systolic = int(healthprofile.systolic)
    Dystolic = int(healthprofile.dystolic)
    Fsugar = int(healthprofile.fastingsugar)
    Affood = int(healthprofile.afterfood)
    print("af = ",Affood)
    Hdl = int(healthprofile.hdl)
    Ldl = int(healthprofile.ldl)
    Tryglyc = int(healthprofile.tryglycerides)
    TotalCholes = int(healthprofile.totalcholestrol)
    HeartDisease = healthprofile.heartdisease
    SedentaryPerson = healthprofile.sedentaryperson
    Breakfast = healthprofile.breakfast
    Lunch = healthprofile.lunch
    Snacks = healthprofile.snacks
    Dinner = healthprofile.dinner
    Date = healthprofile.date
    Time = healthprofile.time

    #To calculate BMI
    obj1 = UserProfile.objects.get(emailid=useremail)
    BirthDate = obj1.dob
    print("Date : ",BirthDate)
    #Converting String Date to Date Format
    dob = datetime.strptime(BirthDate, "%d/%m/%Y").date()
    print(dob)
    today = date.today()
    #Calculating age from Date of Birth
    age = today.year - dob.year
    print("Age = ",age)
    #Converting Height to metre
    heightinmetre = float(Height / 100)
    #Calculating my BMI
    mybmi = float(Weight / (heightinmetre * 2))
    print("My BMI = ",mybmi)
    #Picking age range from BMI table
    bmi = BMI.objects.get(agemin__lte=age, agemax__gte=age)
    print("BMI = ",bmi)
    minbmi = int(bmi.bmimin)
    print("min = ", minbmi)
    maxbmi = int(bmi.bmimax)
    print("max = ", maxbmi)
    #BMI Comparison
    if mybmi >= minbmi and mybmi <= maxbmi:
        BMIStatus = "Normal"
    elif mybmi < minbmi:
        BMIStatus = "Obese"
    elif mybmi > maxbmi:
        BMIStatus = "Over Weight"
    else:
        return HttpResponse("Invalid")

    #Picking age range from BP Table
    bp = BP.objects.get(agemin__lte=age, agemax__gte=age)
    print("BP = ",bp)
    minbp = float(bp.normalmin)
    print("minbp = ",minbp)
    maxbp = float(bp.normalmax)
    print("maxbp = ",maxbp)
    #BP Conversion
    if Systolic == maxbp and Dystolic == minbp:
        BPStatus = "Normal - Normal"
    elif Systolic == maxbp and Dystolic > minbp:
        BPStatus = "Normal - High"
    elif Systolic >= maxbp and Dystolic == minbp:
        BPStatus = "High - Normal"
    elif Systolic == maxbp and Dystolic <= minbp:
        BPStatus = "Normal - Low"
    elif Systolic <= maxbp and Dystolic == minbp:
        BPStatus = "Low - Normal"
    elif Systolic >= maxbp and Dystolic == minbp:
        BPStatus = "High - Normal"
    elif Systolic == maxbp and Dystolic >= minbp:
        BPStatus = "Normal - High"
    elif Systolic >= maxbp and Dystolic <= minbp:
        BPStatus = "High - Low"
    elif Systolic <= maxbp and Dystolic >= minbp:
        BPStatus = "Low - High"
    elif Systolic >= maxbp and Dystolic >= minbp:
        BPStatus = "High - High"
    else:
       BPStatus = "Low - Low"

    #Calculate HB based on Gender
    Gender = obj1.gender
    print("Gender = ", Gender)
    if Gender == "male":
        # Picking age range from HB_MALE
        hb = HB_MALE.objects.get(agemin__lte=age, agemax__gte=age)
        print("HB = ", hb)
        minhb = float(hb.hbmin)
        print(minhb)
        maxhb = float(hb.hbmax)
        print(maxhb)
        #HB COMPARISON FOR HB_MALE
        if Hb >= minhb and Hb <= maxhb:
            HBSTATUS = "Normal"
        elif Hb < minhb:
            HBSTATUS = "Low"
        else:
            HBSTATUS = "Not Valid"
    else:
        hb = HB_FEMALE.objects.get(agemin__lte=age, agemax__gte=age)
        print("HB = ", hb)
        minhb = float(hb.hbmin)
        print(minhb)
        maxhb = float(hb.hbmax)
        print(maxhb)
        # HB COMPARISON FOR HB_MALE
        if Hb >= minhb and Hb <= maxhb:
            HBSTATUS = "Normal"
        elif Hb < minhb:
            HBSTATUS = "Low"
        else:
            HBSTATUS = "Not Valid"

    #Picking fasting sugar range from fasting_sugar
    fasting = FastingSugar.objects.get(fastingmin__lte=Fsugar, fastingmax__gte=Fsugar)
    print(fasting)
    minfast = int(fasting.fastingmin)
    print(minfast)
    maxfast = int(fasting.fastingmax)
    #Fasting Sugar Comparison
    if Fsugar >= minfast and Fsugar <= maxfast:
        faststatus = fasting.status
        FastingStatus = faststatus
    else:
        return HttpResponse('Invalid measurement')
    #Picking after food range from afterfood table
    afterfood = AfterFood.objects.get(aftermin__lte = Affood, aftermax__gte = Affood)
    minafter = int(afterfood.aftermin)
    print("Min After = ",minafter)
    maxafter = int(afterfood.aftermax)
    print("Max After = ",maxafter)
    #After Food Comparison
    if Affood >= minafter and Affood <= maxafter:
        afterstatus = afterfood.status
        AfterFoodStatus = afterstatus
    else:
        return HttpResponse('Invalid measurement for After Food')

    #Picking HDL range from HDL Table
    hdl = HDL.objects.get(HDLmin__lte = Hdl, HDLmax__gte = Hdl)
    minhdl = int(hdl.HDLmin)
    print("Min hdl = ",minhdl)
    maxhdl = int(hdl.HDLmax)
    print("Max hdl = ",maxhdl)
    #HDL Comparison
    if Hdl >=minhdl and Hdl <= maxhdl:
        hdlstatus = hdl.status
        HDLStatus = hdlstatus
    else:
        return HttpResponse('Invalid measurements for HDL')

    #Picking LDL range from LDL Table
    ldl = LDL.objects.get(LDLmin__lte = Ldl, LDLmax__gte = Ldl)
    minldl = int(ldl.LDLmin)
    print("Min LDL = ",minldl)
    maxldl = int(ldl.LDLmax)
    print("Max LDL = ",maxldl)
    #LDL Comparison
    if Ldl >= minldl and Ldl <= maxldl:
        ldlstatus = ldl.status
        LDLStatus = ldlstatus
    else:
        return HttpResponse('Invalid measurements for LDL')
    #Picking Tryglycerides range from Tryglycerides tables
    trygly = Tryglycerides.objects.get(trymin__lte = Tryglyc, trymax__gte = Tryglyc)
    mintry = int(trygly.trymin)
    print("Min Try = ",mintry)
    maxtry = int(trygly.trymax)
    print("Max Try = ",maxtry)
    #Tryglycerides Comparison
    if Tryglyc >= mintry and Tryglyc <= maxtry:
        trystatus = trygly.status
        TryStatus = trystatus
    else:
        return HttpResponse('Invalid measurements for tryglycerides')
    #Picking Total Cholestrol range from Total Cholestrol Tables
    total = TotalCholestrol.objects.get(totalmin__lte = TotalCholes, totalmax__gte = TotalCholes)
    mintotal = int(total.totalmin)
    print("Min Total = ",mintotal)
    maxtotal = int(total.totalmax)
    print("Max Total = ",maxtotal)
    #Total Cholestrol Comparison
    if TotalCholes >= mintotal and TotalCholes <= maxtotal:
        totalstatus = total.status
        TotalStatus = totalstatus
    else:
        return HttpResponse('Invalid measurements for total cholestrol')
    #Sedentary, Heart Disease, Breakfast, Lunch, Snacks, Dinner
    if SedentaryPerson == 'Yes':
        SedentaryStatus = "Idle, No Exercise"
    else:
        SedentaryStatus = "Healthy, Regular Exercise"
    if HeartDisease == 'Yes' :
        HeartStatus = 'Need Medical Attention'
    else:
        HeartStatus = "Healthy Person"
    if Breakfast == 'veg':
        BreakfastStatus = 'Veg'
    else:
        BreakfastStatus = 'Non-Veg'
    if Lunch == 'veg':
        LunchStatus = 'Veg'
    else:
        LunchStatus = 'Non-Veg'
    if Snacks == 'veg':
        SnacksStatus = 'Veg'
    else:
        SnacksStatus = 'Non-Veg'
    if Dinner == 'veg':
        DinnerStatus = 'Veg'
    else:
        DinnerStatus = 'Non-Veg'

    #For displaying date,time and name
    DateStatus = Date
    TimeStatus = Time
    Name = Login.objects.filter(emailid=useremail).values()
    #For Homepage Links
    userregister = Login.objects.filter(emailid=useremail).values()
    print("User = ",userregister)
    userhealth = UserAdvise.objects.filter(emailid=useremail, id=userid).values()
    Context ={'bmi' : BMIStatus, 'bp' : BPStatus, 'hb' : HBSTATUS, 'fasting' : FastingStatus, 'after' : AfterFoodStatus, 'hdl' : HDLStatus, 'ldl' : LDLStatus, 'tryglyc' : TryStatus, 'total' : TotalStatus, 'sedentary' : SedentaryStatus, 'heart' : HeartStatus, 'breakfast' : BreakfastStatus, 'lunch' : LunchStatus, 'snacks' : SnacksStatus, 'dinner' : DinnerStatus, 'date' : DateStatus, 'time' : TimeStatus, 'name' : Name, 'age' : age, 'profile' : userhealth, 'result' : userregister}

    #Saving the above report to Report table
    form = Report()
    form.emailid = useremail
    form.bmi = BMIStatus
    form.bp = BPStatus
    form.hb = HBSTATUS
    form.sugar = FastingStatus
    form.afterfood = AfterFoodStatus
    form.hdl = HDLStatus
    form.ldl = LDLStatus
    form.tryglycerine = TryStatus
    form.totcholestrol = TotalStatus
    form.sedentary = SedentaryStatus
    form.heart = HeartStatus
    form.breakfast = BreakfastStatus
    form.lunch = LunchStatus
    form.snacks = SnacksStatus
    form.dinner = DinnerStatus
    form.date = DateStatus
    form.time = TimeStatus
    form.status = 1
    form.save()
    request.session['email'] = useremail
    return render(request, 'user_result.html',Context)

def user_report(request):
    useremail = request.session['email']
    print("my email = ",useremail)
    report = Report.objects.filter(emailid = useremail).values().order_by('-date','-time')
    print(report)
    name = Login.objects.filter(emailid=useremail).values()
    return render(request, 'user_report.html', {'userreport' : report, 'name': name})
def user_doctor(request):
    obj1 = Login.objects.filter(entry="Expert")
    length = len(obj1)
    mydict = []
    for i in range(len(obj1)):
        mylogin = obj1[i]
        useremail = mylogin.emailid
        obj2 = ExpertProfile.objects.filter(emailid=useremail).values().distinct()
        mydict.append(obj2)
    print(mydict)
    length = len(mydict)
    print(length)
    print(type(obj1))
    print(type(mydict))
    context = {'expert': mydict}
    return render(request, 'user_doctor.html', context)
def user_expertview(request):
    regno = request.GET.get('regno')
    print("Regno = ",regno)
    experts = ExpertProfile.objects.filter(registerno=regno).values()
    print("Experts = ",experts)
    request.session['regnum'] = regno
    return render(request,'user_expertview.html',{'experts' : experts})
def user_request(request):
    regno = request.session['regnum'] #For filtering data
    print("REG = ",regno)
    mysess = request.session['email'] #Calling email from user home to fetch patient name and emailid
    print("My session = ", mysess)
    user = UserProfile.objects.get(emailid=mysess)
    experts = ExpertProfile.objects.get(registerno=regno)
    print("Experts = ", experts)
    expobj = ExpertProfile.objects.filter(registerno=regno).values() #passing as context
    if request.method == "POST":
        if request.POST.get('chat'):
            myform = UserChat()
            "------------------Fetching user queries from User profile---------------------------"
            myform.patientname = user.firstname + user.lastname
            myform.patientemailid = user.emailid
            "------------Text area field from html-----------------"
            myform.question = request.POST.get('chat')
            "------------------Fetching expert queries from Expert profile---------------------------"
            myform.doctorname = experts.firstname + experts.lastname
            myform.doctoremailid = experts.emailid
            myform.status = 1
            myform.save()
        else:
            myform = UserChat()
    return render(request,'user_chat.html',{'experts' : expobj})
def user_articles(request):
    useremail = request.GET.get('email')
    userregister = Login.objects.filter(emailid=useremail).values()
    return render(request, 'user_articles.html', {'userarticle': userregister})

def expert_home(request):
    useremail = request.GET.get('email')
    print("useremail = ", useremail)
    userregister = Login.objects.filter(emailid=useremail).values()
    print(userregister)
    expertprofile = ExpertProfile.objects.filter(emailid=useremail).values()
    print(expertprofile)
    return render(request, 'experts_home.html', {'experthomepage': userregister, 'expertprofile': expertprofile})
def expert_doctor(request):
    useremail = request.GET.get('email')
    expertregister = Login.objects.filter(emailid=useremail).values()
    obj1 = Login.objects.filter(entry="Expert")
    length = len(obj1)
    mydict = []
    for i in range(len(obj1)):
        mylogin = obj1[i]
        useremail = mylogin.emailid
        obj2 = ExpertProfile.objects.filter(emailid=useremail).values().distinct()
        mydict.append(obj2)
    print(mydict)
    length = len(mydict)
    print(length)
    print(type(obj1))
    print(type(mydict))
    context = {'expert': mydict,'expertdoctor': expertregister}
    return render(request, 'experts_doctor.html',context)
def expert_dn(request):
    useremail = request.GET.get('email')
    expertregister = Login.objects.filter(emailid=useremail).values()
    return render(request, 'experts_d and n.html', {'expertdn': expertregister}, )
def expert_articles(request):
    useremail = request.GET.get('email')
    expertregister = Login.objects.filter(emailid=useremail).values()
    return render(request, 'experts_articles.html', {'expertarticle': expertregister}, )
def expert_viewreq(request):
    useremail = request.GET.get('email')
    expertregister = Login.objects.filter(emailid=useremail).values()
    return render(request, 'experts_viewreq.html', {'expertview': expertregister}, )
def expert_reply(request):
    template = loader.get_template('experts_reply.html')
    return HttpResponse(template.render())

"------------------ADMIN PAGES----------------------------------"
def admin_home(request):
    template = loader.get_template('admin_home.html')
    return HttpResponse(template.render())
def admin_user(request):
    template = loader.get_template('admin_user.html')
    return HttpResponse(template.render())
def admin_userview(request):
    template = loader.get_template('admin_userview.html')
    return HttpResponse(template.render())
def admin_doctor(request):
    template = loader.get_template('admin_doctor.html')
    return HttpResponse(template.render())
def admin_viewexpert(request):
    template = loader.get_template('admin_viewexpert.html')
    return HttpResponse(template.render())







