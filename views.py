from django.shortcuts import render,HttpResponse,redirect,loader,get_object_or_404
from django.db.models import Q,Max,Count,query,Sum
from django.contrib import messages
from django import forms
from datetime import datetime,date,time
from mydiet.models import Login
from mydiet.models import UserProfile
from mydiet.models import ExpertProfile
from mydiet.models import UserAdvise
from mydiet.models import BMI,BP,HB_FEMALE,HB_MALE,HDL,LDL,Tryglycerides,TotalCholestrol,FastingSugar,AfterFood
from mydiet.models import Report
from mydiet.models import Chat
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
                return redirect('/expert_home/?expertemail=%s'% dbemail)
            elif dbemail == userid and dbpass == passw and dbstatus == 1  and dbentry == "Admin" :
                return redirect('/admin_home/?expertemail=%s'% dbemail)
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
"******** HOME PAGE OF USER ********"
def user_home(request):
    useremail = request.GET.get('email')
    print("useremail = ",useremail)
    request.session['email'] = useremail
    userregister = Login.objects.filter(emailid=useremail).values()
    print(userregister)
    userprofile = UserProfile.objects.filter(emailid = useremail).values()
    print(userprofile)
    return render(request, 'user_home.html', {'userhomepage': userregister,'userprofile' : userprofile},)

"******** DIET AND NUTRITION PAGE FOR USER ********"
def user_dn(request):
    useremail = request.GET.get('email')
    userregister = Login.objects.filter(emailid=useremail).values()
    reportstatus = ''
    chatstatus = ''
    try:
        userreport = Report.objects.filter(emailid=useremail)
        print("UR = ",userreport)
          # Checking if query exist or not
        if userreport.count() == 0:
            reportstatus = 0
        else:
            reportstatus = 1
    except Report.DoesNotExist:
        pass
    try:
        chathistory = Chat.objects.filter(sender=useremail)
        print("Chat History = ",chathistory)
        # Checking if query exist or not
        if chathistory.count() == 0:
            chatstatus = 0
        else:
            chatstatus = 1
    except Chat.DoesNotExist:
        pass
    request.session['email'] = useremail # passing email so as to fetch history
    return render(request, 'user_d & n.html', {'userdn' : userregister,'reportstatus' : reportstatus,'chatstatus' : chatstatus})

"******** COMPLETE HEALTH PROFILE OF USER ********"
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

"******** STANDARD RESULT OF USER ********"
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

"******** HEALTH REPORT OF USER ********"
def user_report(request):
    useremail = request.session['email']
    print("my email = ",useremail)
    report = Report.objects.filter(emailid = useremail).values().order_by('-date','-time')
    print(report)
    name = Login.objects.filter(emailid=useremail).values()
    return render(request, 'user_report.html', {'userreport' : report, 'name': name})

"******** LIST OF AVAILABLE DOCTORS FOR THE USER ********"
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

"******** VIEW DOCTOR PROFILE FOR USER ********"
def user_expertview(request):
    regno = request.GET.get('regno')
    print("Regno = ",regno)
    experts = ExpertProfile.objects.filter(registerno=regno).values()
    print("Experts = ",experts)
    request.session['regno'] = regno
    return render(request,'user_expertview.html',{'experts' : experts})

"******** CHAT PREVIEW FOR USER ********"
def user_preview(request):
    sender = request.session['email']
    print("Sender = ", sender)  # Getting the email of the user
    obj1 = Login.objects.get(emailid=sender)  # Fetching Name of user from Login table
    print("obj1 = ", obj1)
    sname = obj1.firstname + obj1.lastname

    regno = request.session['regno']
    print(regno)
    obj2 = ExpertProfile.objects.get(registerno=regno)
    print("OBJ2 = ", obj2)
    receiver = obj2.emailid # Getting the email of the Expert
    rname = obj2.firstname + obj2.lastname # Getting the Name of the Expert
    try:
        #select * from chat where (sender = "nikhilprakash95@gmail.com" and receiver = "drtinynair@gmail.com")
        #  or (sender = "drtinynair@gmail.com" and receiver = "nikhilprakash95@gmail.com");
        obj3 = Chat.objects.filter(Q(sender=sender,receiver=receiver)|Q(sender=receiver,receiver=sender))
        print("Object = ", obj3)
        if obj3.count() == 0:
            status = 0
        else:
            status = 1
    except Chat.DoesNotExist:
        pass
    print("Status = ",status)
    #sessioning these to user_chat
    request.session['sender'] = sender  # sender emailid
    request.session['receiver'] = receiver  # receiver emailid
    #passing Query object, Sender and Receiver email along with their names respectively and status
    context = {'myobj' : obj3,'sender' : sender,'receiver' : receiver,'sname' : sname,'rname' : rname,'status' : status}
    return render(request, 'userchat.html',context)

"******** SENDING & DB SAVING CHAT MESSAGE OF THE USER ********"
def user_chat(request):
    #sessions from user_preview...
    sender = request.session['sender'] #sender emailid
    receiver = request.session['receiver'] #receiver emailid
    if request.method == 'POST':
        msg = request.POST.get('msgbox', None)
        form = Chat()
        form.sender = sender
        form.receiver = receiver
        form.message = request.POST.get('chat-msg')
        form.status = 1
        form.save()
        return redirect('/user_preview')
    else:
        form = Chat()
        return render(request,'user_chat.html')

"******** CHAT CONVERSATION HEAD FOR THE USER ********"
def user_chathistory(request):
    useremail = request.session['email']
    # select receiver from chat where sender = "nikhilprakash95@gmail.com" GROUP BY receiver;
    #obj1 = Chat.objects.values('receiver').filter(sender=useremail)
    obj1 = Chat.objects.filter(sender=useremail).values('receiver').annotate(rec = Count('receiver'))
    print(obj1.query)
    return render(request,'user_chathistory.html',{'myobj' :obj1})

"******** CHAT HISTORY PREVIEW OF USER ********"
def user_chatpreview(request):
    sender = request.session['email'] #user email
    obj1 = Login.objects.get(emailid=sender)  # Fetching Name of user from Login table
    print("obj1 = ", obj1)
    sname = obj1.firstname + obj1.lastname

    receiver = request.GET.get('emailid')  # expert email
    print("Rec = ",receiver)
    obj2 = ExpertProfile.objects.get(emailid=receiver)
    print("OBJ2 = ", obj2)
    rname = obj2.firstname + obj2.lastname  # Getting the Name of the Expert
    try:
        #select * from chat where (sender = "nikhilprakash95@gmail.com" and receiver = "drtinynair@gmail.com")
        #  or (sender = "drtinynair@gmail.com" and receiver = "nikhilprakash95@gmail.com");
        obj3 = Chat.objects.filter(Q(sender=sender,receiver=receiver)|Q(sender=receiver,receiver=sender))
        print("Object = ", obj3)
        if obj3.count() == 0:
            status = 0
        else:
            status = 1
    except Chat.DoesNotExist:
        pass
    print("Status = ",status)
    #sessioning these to user_chat
    request.session['user'] = sender  # sender emailid
    request.session['expert'] = receiver  # receiver emailid
    #passing Query object, Sender and Receiver email along with their names respectively and status
    context = {'myobj' : obj3,'sender' : sender,'receiver' : receiver,'sname' : sname,'rname' : rname,'status' : status}
    return render(request, 'user_chatpreview.html',context)

"******** SENDING CHAT MESSAGES VIA CHAT HISTORY OF THE USER ********"
def user_chatp(request):
    sender = request.session['user']  # sender emailid
    receiver = request.session['expert']  # receiver emailid
    if request.method == 'POST':
        msg = request.POST.get('msgbox', None)
        form = Chat()
        form.sender = sender
        form.receiver = receiver
        form.message = request.POST.get('chat-msg')
        form.status = 1
        form.save()
        return redirect('/user_chatpreview/?emailid=%s'%receiver)
    else:
        form = Chat()
        return render(request, 'user_chatpreview.html')

"******** FRAMESET OF CHAT WINDOWS ********"
def chatpreview(request):
    template = loader.get_template('chatpreview.html')
    return HttpResponse(template.render())

"******** VIEWING ARTICLE OF EXPERTS FOR THE USER ********"
def user_articles(request):
    useremail = request.GET.get('email')
    userregister = Login.objects.filter(emailid=useremail).values()
    return render(request, 'user_articles.html', {'userarticle': userregister})

"******** HOME PAGE OF EXPERT ********"
def expert_home(request):
    useremail = request.GET.get('expertemail')
    print("useremail = ", useremail)
    userregister = Login.objects.filter(emailid=useremail).values()
    print(userregister)
    expertprofile = ExpertProfile.objects.filter(emailid=useremail).values()
    print(expertprofile)
    return render(request, 'experts_home.html', {'experthomepage': userregister, 'expertprofile': expertprofile})

"******** VIEWING DOCTOR LIST FOR EXPERT ********"
def expert_doctor(request):
    useremail = request.GET.get('expertemail')
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

"******** PAGE TO VIEW REQUEST FROM USER(IF AVAILABLE) ********"
def expert_dn(request):
    useremail = request.GET.get('expertemail')
    expertregister = Login.objects.filter(emailid=useremail).values()
    try:
        obj1 = Chat.objects.filter(receiver=useremail,status=1)
        if obj1.count() == 0:
            stat = 0
        else:
            stat = 1
    except Chat.DoesNotExist:
        pass
    return render(request, 'experts_d and n.html', {'expertdn': expertregister,'status' : stat}, )

"******** VIEWING CHAT REQUEST FROM USER(CHAT CONVERSATION HEAD) ********"
def expert_viewreq(request):
    useremail = request.GET.get('expertemail')
    print("Useremail = ",useremail)
    expertregister = Login.objects.filter(emailid=useremail).values()
    # Listing out conversation head and latest message of users
    #select * from chat where id IN(select max(id) from chat where receiver = "drtinynair@gmail.com" GROUP BY sender) GROUP BY ID DESC;



    # select distinct(sender) from chat where receiver="drtinynair@gmail.com";
    obj1 = Chat.objects.values_list('sender', flat=True).filter(receiver=useremail).distinct()
    print("obj1 = ", obj1)
    print("obj1 Query = ", obj1.query)
    #SENDER IS NOT CORRECT
    sender = obj1[0]
    print("S = ", sender)
    try:
        #select sender from chat where receiver = "drtinynair@gmail.com" GROUP BY sender;
        #obj2 = Chat.objects.filter(receiver=useremail).values('sender','message').annotate(sen=Count('sender'))
        #print(obj2.query)
        #sender = obj2[0]
        #print("S = ", sender)
        receiver = useremail
        print("R = ",receiver)
        #UPDATING LATEST MESSAGES OF EACH USERS....
        obj3 = Chat.objects.all()
        # select id,sender,message from chat where id IN(select max(id) from chat GROUP BY sender)
        #  and receiver ="drtinynair@gmail.com" GROUP BY ID DESC
        latest = obj3.filter(receiver=useremail).annotate(count=Max('id'))
        print("latest = ",latest.query)
        obj3 = obj3.filter(id__in = latest.values('count')).order_by('-id')
        print("Object 2 = ",obj3)
        print("Object 2 QUERY = ", obj3.query)
        myobj = zip(obj1,obj3)
        print(myobj)
    except Chat.DoesNotExist:
        pass
    request.session['expertemail'] = useremail #Email of Expert
    request.session['sender'] = sender # Email of User"
    context = {'expertview': expertregister,'myobj' : myobj,'receiver' : receiver}
    return render(request, 'experts_viewreq.html',context )

"******** CHAT HISTORY OF EXPERT ********"
def expert_preview(request):
    sender = request.session['expertemail']
    print("Sender = ", sender)  # Getting the email of the sender(Expert)
    obj1 = ExpertProfile.objects.get(emailid=sender)  # Fetching Name of Expert from Expert table
    print("obj1 = ", obj1)
    sname = obj1.firstname + obj1.lastname
    print("Sname = ",sname)

    receiver = request.session['sender'] # Getting the email of the Receiver(user)
    print("R = ", receiver)
    obj2 = Login.objects.get(emailid=receiver)  # Fetching Name of User from Login table
    print("OBJ2 = ", obj2)
    rname = obj2.firstname + obj2.lastname
    print("Rname = ",rname)
    try:
        #select * from chat where (sender = "drtinynair@gmail.com" and receiver = "nikhilprakash95@gmail.com")
        #  or (sender = "nikhilprakash95@gmail.com" and receiver = "drtinynair@gmail.com");
        obj3 = Chat.objects.filter(Q(sender=sender, receiver=receiver) | Q(sender=receiver, receiver=sender))
        print("Object = ", obj3)
        if obj3.count() == 0:
            status = 0
        else:
            status = 1
    except Chat.DoesNotExist:
        pass
    print("Status = ", status)
    # sessioning these to user_chat
    request.session['expert'] = sender  # Expert emailid
    request.session['user'] = receiver  # User emailid
    # passing Query object, Sender and Receiver email along with their names respectively and status
    context = {'myobj': obj3, 'sender': sender, 'receiver': receiver, 'sname': sname, 'rname': rname, 'status': status}
    return render(request, 'expertchat.html', context)

"******** SENDING CHAT MESSAGES AND DB SAVING FROM EXPERT ********"
def expert_chat(request):
    sender = request.session['expert']
    receiver = request.session['user']
    if request.method == 'POST':
        msg = request.POST.get('msgbox', None)
        form = Chat()
        form.sender = sender
        form.receiver = receiver
        form.message = request.POST.get('chat-msg')
        form.status = 1
        form.save()
        return redirect('/expert_preview')
    else:
        form = Chat()
        return render(request, 'expertchat.html')

"******** UPLOADING ARTICLES FOR EXPERT ********"
def expert_articles(request):
    useremail = request.GET.get('expertemail')
    expertregister = Login.objects.filter(emailid=useremail).values()
    return render(request, 'experts_articles.html', {'expertarticle': expertregister}, )

"------------------ADMIN PAGES----------------------------------"
"******** HOMEPAGE OF ADMIN ********"
def admin_home(request):
    template = loader.get_template('admin_home.html')
    return HttpResponse(template.render())

"******** VIEWING REGISTERED USER ********"
def admin_user(request):
    template = loader.get_template('admin_user.html')
    return HttpResponse(template.render())

"******** VIEWING PROFILE OF REGISTERED USER ********"
def admin_userview(request):
    template = loader.get_template('admin_userview.html')
    return HttpResponse(template.render())

"******** VIEWING REGISTERED EXPERTS ********"
def admin_doctor(request):
    template = loader.get_template('admin_doctor.html')
    return HttpResponse(template.render())

"******** VIEWING PROFILE OF REGISTERED EXPERT ********"
def admin_viewexpert(request):
    template = loader.get_template('admin_viewexpert.html')
    return HttpResponse(template.render())







