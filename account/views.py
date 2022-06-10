from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.conf import settings
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.template.loader import render_to_string, get_template
from django.utils.html import strip_tags
from django.template import Context
from django.contrib.auth.models import User
from django.views import View

from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from .utils import token_generator


# Create your views here.
def register(request):
    if request.method=='POST':
        Email = request.POST['email']
        Password = request.POST['password']
        if Registers.objects.filter(username=Email).exists() or User.objects.filter(username=Email).exists():
            messages.error(request, "Looks like you're already a Peep, click on Log in below and enjoy life🙃")
            return redirect('register')
        elif Registers.objects.filter(email=Email).exists() or User.objects.filter(email=Email).exists():
            messages.error(request, 'Email is already Taken')
            return redirect('register')
        else:
            request.session['email'] = Email
            request.session['password'] = Password
            return redirect('yourdetail')
    return render(request, 'signup.html')

def yourdetail(request):
    if request.method=='POST':
        FirstName= request.POST['fname']
        LastName = request.POST['lname']
        Gender = request.POST['Gender']
        Date = request.POST['date']
        Month = request.POST['month']
        Year = request.POST['year']

        request.session['fname'] = FirstName
        request.session['lname'] = LastName
        request.session['gender'] = Gender
        request.session['date'] = Date
        request.session['month'] = Month
        request.session['year'] = Year
        value = {
            'FirstName' : FirstName,
            'LastName' : LastName,
            'Date' : Date,
            'Month' : Month,
            'Year' : Year,
        }
        
        return redirect('signup')
        data = {
                'values' : value
            }
        return render(request, 'signup2.html', data)
    return render(request, 'signup2.html')

    return render(request, 'signup2.html')

def signup(request):
    Institution = {
        'Aayojan- School of Architecture Jaipur ':'ayojan.edu.in',
        'Adamas University':'stu.adamasuniversity.ac.in',
        'AIHM Chandigarh':'ihmchandigarh.org',
        'Aligarh Muslim University':['amu.ac.in','myamu.ac.in'],
        'Alliance University':['alliance.edu.in','bus.alliance.edu.in','ced.alliance.edu.in','law.alliance.edu.in'],
        'Amity University':['amity.edu','amitystudent.com','amityopenuniversity.com','amityonline.com'],
        'Amity University Chhattisgarh':['rpr.amity.edu','s.amity.edu'],
        'Amity University Gwalior (Madhya Pradesh)':'gwa.amity.edu',
        'Amity University Mumbai':'mum.amity.edu',
        'Amity university, Noida':'s.amity.edu',
        'Anna University, Chennai':'annauniv.edu',
        'Aryabhatta College, University Of Delhi':'aryabhattacollege.ac.in',
        'Ashoka University':'ashoka.edu.in',
        'Banasthali Vidyapith':'banasthali.in',
        'Bangalore University':['bangaloreuniversity.ac.in','bub.ernet.in'],
        'Bennett university':'bennett.edu.in',
        'Bhartiya Vidyapeeth College of Engineering , Pune':'deccansociety.org',
        'Birla Institute of Technology - Mesra':['student.biticrak.ae','bitmesra.ac.in'],        ''
        'Birla Institute of Technology and Science (BITS)':['bits-pilani.ac.in','dubai.bits-pilani.ac.in','goa.bits-pilani.ac.in','hyderabad.bits-pilani.ac.in','pilani.bits-pilani.ac.in','wilp.bits-pilani.ac.in'],
        'BITS Pilani, Goa Campus':'bits-goa.ac.in',
        'Biyani College':'biyanicolleges.org',
        'BMS College of Engineering':['bmsce.edu.in','bmsce.ac.in'],
        'BMS college of Law':['bmscl.edu.in','bmscl.ac.in'],
        'BMS Institute of Technology and Management':['bmsit.edu.in','bmsit.in','bmsit.ac.in'],
        'BMS School of Architecture':['bmssa.edu.in','bmsca.org','bmssa.ac.in'],
        'BMSCCM - BMS College of Commerce and Management':['bmsccm.edu.in','bmsccm.ac.in','bmsccm.in'],
        'Calcutta University, Kolkata':'caluniv.ac.in',
        'Chandigarh university':'cumail.in',
        'Chitkara University':'chitkara.edu.in',
        'Christ University, Bangalore':['soc.christuniversity.in','science.christuniversity.in','psy.christuniversity.in','pme.christuniversity.in','phl.christuniversity.in','mtech.christuniversity.in','mcom.christuniversity.in','mca.christuniversity.in','mba.christuniversity.in','maths.christuniversity.in','law.christuniversity.in','it.christuniversity.in','eng.christuniversity.in','cse.christuniversity.in','cs.christuniversity.in','commerce.christuniversity.in','christuniversity.in','btech.christuniversity.in','bba.christuniversity.in','barch.christuniversity.in','arts.christuniversity.in',],
        'Christ University, Ghaziabad':['soc.christuniversity.in','science.christuniversity.in','psy.christuniversity.in','pme.christuniversity.in','phl.christuniversity.in','mtech.christuniversity.in','mcom.christuniversity.in','mca.christuniversity.in','mba.christuniversity.in','maths.christuniversity.in','law.christuniversity.in','it.christuniversity.in','eng.christuniversity.in','cse.christuniversity.in','cs.christuniversity.in','commerce.christuniversity.in','christuniversity.in','btech.christuniversity.in','bba.christuniversity.in','barch.christuniversity.in','arts.christuniversity.in',],
        'Christ University, Lavasa ':['soc.christuniversity.in','science.christuniversity.in','psy.christuniversity.in','pme.christuniversity.in','phl.christuniversity.in','mtech.christuniversity.in','mcom.christuniversity.in','mca.christuniversity.in','mba.christuniversity.in','maths.christuniversity.in','law.christuniversity.in','it.christuniversity.in','eng.christuniversity.in','cse.christuniversity.in','cs.christuniversity.in','commerce.christuniversity.in','christuniversity.in','btech.christuniversity.in','bba.christuniversity.in','barch.christuniversity.in','arts.christuniversity.in',],
        'College of Vocational Studies, University of Delhi':'cvs.edu.in',
        'Daulat Ram College':'dr.du.ac.in',
        'Delhi Technological University':['cumsdtu.in','dtu.co.in','dtu.ac.in','dce.edu'],
        'Deshbandu College':['deshbandhucollege.ac.in','du.ac.in'],
        'DKTE Societys Textile & Engineering Institute':['dktes.com','dkte.in','dkte.ac.in'],
        'Dr Akhilesh Das Gupta Institute of Technology & Management':'adgitmdelhi.ac.in',
        'Faculty of Management, Delhi (FMS)':'fms.edu',
        'Flame University':'flame.edu.in',
        'Galgotias University':'galgotiasuniversity.edu.in',
        'Gandhi Institute of Technology and Management University (GITAM)':['gitam.in','gitam.edu'],
        'Gargi College (University of Delhi)':['gargi.du.ac.in','gargicollege.in'],
        'GD Goenka University Gurgaon':['gdgu.org','gdgoenka.ac.in'],
        'Guru Gobind Singh Indraprastha University':'ipu.ac.in',
        'Guru Nanak Dev University, Amritsar. (GNDU)':'gndu.ac.in',
        'Hansraj College':['hansrajcollege.du.ac.in','hansrajcollege.ac.in'],
        'Hindu College, Delhi University':['hinducollege.co.in','hinducollege.ac.in'],
        'Hindustan University':'hindustanuniv.ac.in',
        'HR College of Economics':'hrcollege.edu',
        'ICT College of Vocational Studies':'Ict.edu.rs',
        'IIIT - Indian Institute of Information Technology, Kota':'iiitkota.ac.in',
        'IIM Ahmedabad':'iima.ac.in',
        'IIM Amritsar':'iimamritsar.ac.in',
        'IIM Bangalore':'iimb.ac.in',
        'IIM Bodh Gaya':'iimbg.ac.in',
        'IIM Calcutta':['iimcal.ac.in','email.iimcal.ac.in'],
        'IIM Indore':'iimidr.ac.in',
        'IIM Kozhikode':['iimk.ac.in','iimk.edu.in'],
        'IIM Lucknow':'iiml.ac.in',
        'IIM Ranchi':'iimranchi.ac.in',
        'IIM Rohtak':'iimrohtak.ac.in',
        'IIM Sambalpur':'iimsambalpur.ac.in',
        'IIM Shillong':'iimshillong.ac.in',
        'IIM Sirmaur':'iimsirmaur.ac.in',
        'IIM Udaipur':'iimu.ac.in',
        'IIS University, Jaipur ':'iisuniv.ac.in',
        'IIT Bhilai':'iitbhilai.ac.in',
        'IIT Bhubaneswar':'iitbbs.ac.in',
        'IIT Bombay':['aero.iitb.ac.in','cse.iitb.ac.in','iitbombay.org','sjmsom.in','ee.iitb.ac.in','chem.iitb.ac.in','iitb.ac.in'],
        'IIT Delhi':['student.iitd.ac.in','physics.iitd.ac.in','mech.iitd.ac.in','maths.iitd.ernet.in','maths.iitd.ac.in','iitd.ac.in','dms.iitd.ernet.in','ee.iitd.ac.in','dbeb.iitd.ac.in','cse.iitd.ernet.in','cse.iitd.ac.in','chemical.iitd.ac.in','care.iitd.ernet.in','am.iitd.ac.in','textile.iitd.ac.in'],
        'IIT Dharwad':'iitdh.ac.in',
        'IIT Gandinagar':'iitgn.ac.in',
        'IIT Goa':'iitgoa.ac.in',
        'IIT Guwahati':'iitg.ac.in',
        'IIT Hyderabad':'ee.iith.ac.in',
        'IIT Indore':'iitdh.ac.in',
        'IIT Jammu':'iitjammu.ac.in',
        'IIT Jodhpur':'iitj.ac.in',
        'IIT Kanpur':'iitk.ac.in',
        'IIT Kharagpur (IITK)':['sit.iitkgp.ernet.in','metal.iitkgp.ernet.in','mech.iitkgp.ernet.in','iitkgp.ac.in','gg.iitkgp.ernet.in','ee.iitkgp.ernet.in','cse.iitkgp.ernet.in','ece.iitkgp.ernet.in','cse.iitkgp.ac.in'],
        'IIT Mandi (IITM)':'students.iitmandi.ac.in',
        'IIT Palakkad':'smail.iitpkd.ac.in',
        'IIT Patna':'iitp.ac.in',
        'IIT Ropar':'iitrpr.ac.in',
        'IIT Rorkee':'ar.iitr.ac.in',
        'IIT Tirupati':'iittp.ac.in',
        'IITM - Indian Institute of Technology Madras':['smail.iitm.ac.in','student.onlinedegree.iitm.ac.in','onlinedegree.iitm.ac.in','imail.iitm.ac.in','iitm.ac.in','htic.iitm.ac.in','ee.iitm.ac.in','cse.iitm.ac.in'],
        'Indian Institute of Foreign Trade (IIFT)':'iift.edu',
        'Indian Institute of Science, Bangalore':['ug.iisc.in','ssl.serc.iisc.in','serc.iisc.in','mecheng.iisc.ernet.in','mbu.iisc.ernet.in','math.iisc.ernet.in','iisc.ac.in','grads.cds.iisc.ac.in','ece.iisc.ernet.in','csa.iisc.ernet.in','ces.iisc.ernet.in'],
        'Indian Institute of Technology Varanasi (BHU)':['itbhu.ac.in','tbhu.ac.in','iitbhu.ac.in','bhu.ac.in'],
        'Indian School of Business (ISB)':['tep.isb.edu','pgppro.isb.edu','pgp.isb.edu','isb.edu','cba.isb.edu'],
        'Indian Statistical Institute':['isical.ac.in','isibang.ac.in'],
        'Indraprastha Institute of Information Technology, Delhi':'iiitd.ac.in',
        'Institute of Management Studies Noida (IMS Noida)':'imsnoida.com',
        'Integral University':'student.iul.ac.in',
        'International Institute of Information Technology - IIIT Hyderabad':['students.iiit.ac.in','research.iiit.ac.in','iiit.ac.in'],
        'ISBF - Indian School of Business & Finance':'isbf.edu.in',
        'Jagan Institute of Management Studies':'jimsindia.org',
        'Jai Hind College':'jaihindcollege.edu.in',
        'Jain (Deemed-to-be University), Bangalore':['Jainuniversity.ac.in','Cms.ac.in'],
        'Jaipuria Institute of Management':'jaipuria.ac.in',
        'Jamia Millia Islamia - A Central University':['st.jmi.ac.in','jmi.ac.in'],
        'Jawaharlal Nehru University':['jnu.ac.in','mail.jnu.ac.in'],
        'JECRC University':['jecrcmail.com','jecrcu.edu.in'],
        'Jesus And Mary College , Delhi University':['jmc.ac.in','jmc.du.ac.in'],
        'JIIT - Jaypee Institute of Information Technology, Noida':'mail.jiit.ac.in',
        'JK Lakshmipat University':'jklu.edu.in',
        'Kalinga Institute of Industrial Technology, (KIIT)':['Kiitbiotech.ac.in','Kiit.ac.in'],
        'KIIT University (Kalinga Institute of Industrial Technology)':['kiitbiotech.ac.in','kiit.ac.in','biotech.kiit.ac.in'],
        'Kirori Mal College, University of Delhi':['kmc.du.ac.in','kmcollege.ac.in'],
        'Lady Shri Ram College for Women':['lsrcollege.org','lsr.du.ac.in','lsr.edu.in'],
        'Lloyd Law College':['lloydbusinessschool.edu.in','lloydlawcollege.edu.in',''],
        'Lovely Professional University (LPU)':['lpu.co.in','lpu.in'],
        'Loyola Law School':'lls.edu',
        'Manipal University ':['manipal.edu','muj.manipal.edu'],
        'Mata Sundri College for Women(University Of Delhi)':'ms.du.ac.in',
        'Maulana Azad National Institute of Technology (MANIT) Bhopal':['manitacin.onmicrosoft.com','manit.ac.in'],
        'Miranda House, University College for Women':'mirandahouse.ac.in',
        'MNIT Allahabad':['mnnit.ac.in','ecellmnnit.in'],
        'MNIT Jaipur':'mnit.ac.in',
        'Mount Caramel College, Bangalore':'mccblr.edu.in',
        'Narsee Monjee Institute of Management Studies (NMIMS)':['nmims.edu','nmims.edu.in'],
        'National Rail and Transportation Institute':'nrti.edu.in',
        'Nirma University':'nirmauni.ac.in',
        'NIT Agartala':'nita.ac.in',
        'NIT Andhra P':'nitandhra.ac.in',
        'NIT Arunachal Pradesh':['nitap.in','nitap.ac.in'],
        'NIT Calicut':'nitc.ac.in',
        'NIT Delhi':'nitdelhi.ac.in',
        'NIT Durgapura':['phd.nitdgp.ac.in','mtech.nitdgp.ac.in','mca.nitdgp.ac.in','btech.nitdgp.ac.in'],
        'NIT Goa':'nitgoa.ac.in',
        'NIT Hamirpur':'nith.ac.in',
        'NIT Jamshedpur':'nitjsr.ac.in',
        'NIT Karnataka':['nitk.ac.in','nitk.edu.in'],
        'NIT Kurukshetra':['nitkkr.edu.in','nitkkr.ac.in'],
        'NIT Manipur':['nitmanipur.edu.in','nitmanipur.ac.in'],
        'NIT Meghalaya':['nitm.edu.in','nitm.ac.in'],
        'NIT Mizoram':['nitmz.edu.in','nitmz.ac.in'],
        'NIT Nagaland':['nitnagaland.edu.in','nitnagaland.ac.in'],
        'NIT Patna':['nitp.edu.in','nitp.ac.in'],
        'NIT Raipur':['nitrr.edu.in','nitrr.ac.in'],
        'NIT Roukela':['nitrkl.edu.in','nitrkl.ac.in'],
        'NIT Sikkim':['nitsikkim.edu.in','nitsikkim.ac.in'],
        'NIT Silchar':['nits.edu.in','nits.ac.in'],
        'NIT Srinagar':['nitsri.edu.in','nitsri.ac.in'],
        'NIT Surat':['svnit.edu.in','svnit.ac.in'],
        'NIT Surathkal':['nitk.edu.in','nitk.ac.in'],
        'NIT Tiruchirapalli':'nitt.edu',
        'NIT Uttarakhand':['nituk.edu.in','nituk.ac.in'],
        'NLU, Lucknow':['rmlnlu.edu.in','rmlnlu.ac.in'],
        'NSUT - Netaji Subhas Institute of Technology':['nsut.ac.in','nsit.net.in','aiactr.ac.in'],
        'O.P. Jindal Global University':['opju.ac.in','jgu.edu.in'],
        'Pandit Deendayal Energy University (PDEU) (Formerly PDPU)':['spt.pdpu.ac.in','spm.pdpu.ac.in','sot.pdpu.ac.in','sls.pdpu.ac.in'],
        'Poornima Institute of Engineering & Technology':['poornima.org','poornima.edu.in'],
        'Poornima University':'poornima.ac.in',
        'Presidency University, Bangalore':'presidency.edu.in',
        'Ramaiah Institute of Technology':'msrit.edu',
        'Ramanujan College, University of Delhi':'ramanujan.du.ac.in',
        'Ramjas College':'ramjas.du.ac.in',
        'RV College of Engineering (RVCE)':'rvce.edu.in',
        'Shaheed Bhagat Singh College':'sbsc.in ',
        'Shaheed Sukhdev College of Business Studies':'Sscbs.du.ac.in',
        'Sharda University':['ug.sharda.ac.in','sharda.ac.in','sgei.org','pg.sharda.ac.in'],
        'Shiv Nadar University':'snu.edu.in',
        'Shivaji College, University of Delhi':'shivaji.du.ac.in',
        'Shri Ram College of Commerce (SRCC)':'srcc.du.ac.in',
        'Sikkim Manipal University':['smude.edu.in','smims.smu.edu.in'],
        'Sophia College for Women, Mumbai':['sophiacollegemumbai.com','sophiacollege.edu.in'],
        'Sri Aurobindo College, University of Delhi':'aurobindoe.du.ac.in',
        'Sri Venkateswara College, Delhi University':'svc.edu.du.ac.in',
        'Sri Venkateswara College, Delhi University':['svc.edu.in','svc.ac.in','svc.du.ac.in'],
        'Sri Venkateswara University':'svuniversity.edu.in',
        'SRM University':'srmist.edu.in',
        'SRM University, Amaravati, AP':'srmap.edu.in',
        'St. Joseph’s College of Commerce':'sjcc.edu.in',
        'St. Xavier University':['sxu.edu','mymail.sxu.edu'],
        'St. Xaviers College (Autonomous), Kolkata':'sxccal.edu',
        'St. Xaviers College, Mumbai':'xaviers.edu.in',
        'Suresh Gyan Vihar University':'mygyanvihar.com',
        'Sushant University ( Previously Ansal University)':['ansaluniversity.edu.in','sushantuniversity.edu.in'],
        'Symbiosis Center for Distance Learning':'student.scdl.net',
        'Symbiosis Institute of Business Management, Pune':['sibmpune.edu.in','associates.sibmpune.edu.in'],
        'Symbiosis Institute of Design':'sid.edu.in',
        'Symbiosis Institute of International Business':'siib.ac.in',
        'Symbiosis Institute of Management Studies, Noida':['symlaw.edu.in','scmsnoida.ac.in'],
        'Symbiosis Institute of Media and Communication (SIMC)':'simc.edu',
        'Symbiosis Institute of Technology':'sitpune.edu.in',
        'Symbiosis International University ':'siu.edu.in',
        'Symbiosis Law School':['symlaw.ac.in','symlaw.edu.in','student.slsh.edu.in','slsh.edu.in'],
        'Symbiosis School for Liberal Arts':'ssla.edu.in',
        'Symbiosis School of Economics':'sse.ac.in',
        'Symbiosis Skills and Professional University':['student.sspu.ac.in','student.ssou.ac.in'],
        'Symbiosis Statistical Institute':'ssi.edu.in',
        'Symbiosis University, Nagpur':'slsnagpur.edu.in',
        'Thapar University ':'thapar.edu',
        'The Northcap University':'ncuindia.edu',
        'University of Delhi (DU)':['svc.edu.du.ac.in','ss.du.ac.in','sol.du.ac.in','sol-du.ac.in','shivaji.du.ac.in','sgndkc.du.ac.in','rla.du.ac.in','ramanujan.du.ac.in','pg.du.ac.in','one.ducic.ac.in','lc2.du.ac.in','lb.du.ac.in','kmcollege.ac.in','kmc.du.ac.in','keshav.du.ac.in','kalindi.du.ac.in','ihe.du.ac.in','fms.edu','dbe-du.org','cs.du.ac.in','clc.du.ac.in','bcas.du.ac.in','aurobindoe.du.ac.in','arsd.edu.du.ac.in','arsd.du.ac.in','andc.du.ac.in'],
        'University of Petroleum and Energy Studies - UPES':['stu.upes.ac.in','ddn.upes.ac.in'],
        'Vellore Institute of Technology (VIT)':['vit.ac.in','vitstudent.ac.in','vitalum.ac.in'],
        'Vellore Institute of Technology (VIT)':['vit.ac.in','vitstudent.ac.in'],
        'VIT Bhopal University (Vellore Institute of Technology Bhopal':'vitbhopal.ac.in',
        'Xavier School of Management (XLRI)':['xlri.ac.in','astra.xlri.ac.in'],

    }

    if request.method == 'POST':
        institution = request.POST['institution']
        domain = request.POST['domain']
        Email = request.POST['institution_email']
        graduation_year = request.POST['graduation_year']
        request.session['institution_name'] = institution
        request.session['institution_email'] = Email
        request.session['graduation_year'] = graduation_year
        domains = Institution.get(institution)
        if domains is None:
            messages.error(request,"Ohh! Looks like your college email doesn't match with your institution database. If you think it's a mistake, please shoot us a mail at verify@studentpeeps.club")
            return render(request, 'signup3.html', {'Institution': Institution})

        # print(domains)
        afterSlice = Email.split("@")
        sliceValue = afterSlice[1]
        i=0
        for i in domains:
            dom = i
            if(dom==sliceValue):
                domains=sliceValue
                break
        print(domains)
        if(sliceValue=='gmail.com'):
            username = request.session.get('email')
            firstname = request.session.get('fname')
            lastname = request.session.get('lname')
            Password = request.session.get('password')
            user = User.objects.create_user(username=username, password=Password, email=Email, first_name=firstname)
            user.is_active = False
            user.save()
            a = request.user
            request.session['user'] = user.email

            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            domain = get_current_site(request).domain
            link = reverse('activate', kwargs={'uidb64': uidb64, 'token': token_generator.make_token(user)})

            activate_url = 'http://' + domain + link

            message = render_to_string('mail_body.html', {'fname': firstname,'lname' : lastname ,'activate_url': activate_url})
            msg = EmailMessage(
                'Activation Link StudentPeeps',
                message,


            settings.EMAIL_HOST_USER,
                [user.email],
            )
            msg.content_subtype = "html"  # Main content is now text/html
            msg.send(fail_silently=False)
            gender = request.session.get('gender')
            date = request.session.get('date')
            month = request.session.get('month')
            year = request.session.get('year')
            unverified = UnVerified(username=username,password=Password,email=username,firstname=firstname,lastname=lastname,gender=gender,
                            date=date,month=month,year=year,institution=institution,institution_email=Email,graduation_year=graduation_year)
            unverified.save()
            return redirect('Verificationmsg')
        else:
            messages.error(request, "Ohh! Looks like your college email doesn't match with your institution database. If you think it's a mistake, please shoot us a mail at verify@studentpeeps.club")
            return render(request,'signup3.html', {'Institution':Institution})

    return render(request,'signup3.html', {'Institution':Institution})

def login(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Looks like you've haven't signed up yet. Join 2000+ students. Sign up now!")
            return redirect('login')
    else:
        return render(request, 'login.html')

def upload(request):
    if request.method == "POST":
        images = request.FILES['image']
        username = request.session.get('email')
        password = request.session.get('password')
        email = request.session.get('email')
        fname = request.session.get('fname')
        lname = request.session.get('lname')
        gender = request.session.get('gender')
        date = request.session.get('date')
        month = request.session.get('month')
        year = request.session.get('year')
        
        user = User.objects.create_user(username=username, password=password, email=email)
        user.is_active = False
        user.save()
        register = Upload(username=username, password=password, email=email, firstname=fname, lastname=lname,
                             gender=gender,date=date, month=month, year=year,image=images)
        register.save()
        return redirect('Uploadmsg')
    return render(request,'signup4.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

class VerificationView(View):
    def get(self, request, uidb64, token):
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
        print(user)
        print(user.username)
        user.is_active = True
        if UnVerified.objects.filter(username=user.username).exists():
            profile = UnVerified.objects.get(username=user.username)
            register = Registers(username=profile.username,password=profile.password,email=profile.email,firstname=profile.firstname,lastname=profile.lastname,gender=profile.gender,
                            date=profile.date,month=profile.month,year=profile.year,institution=profile.institution,institution_email=profile.institution_email,graduation_year=profile.graduation_year)
            register.save()
            user.save()
            UnVerified.objects.filter(username=profile.username).delete()
            user = auth.authenticate(username=profile.username, password=profile.password)
            if user is not None:
                auth.login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Invalid Credentials')
                return redirect('login')
        return redirect('login')


def edit_profile(request):
    users = request.user.username
    if Registers.objects.filter(username=users).exists():

        profile = Registers.objects.get(username=users)
        if request.method == "POST":
            FirstName = request.POST['fname']
            LastName = request.POST['lname']
            Gender = request.POST['Gender']
            Date = request.POST['date']
            Month = request.POST['month']
            Year = request.POST['year']
            images = request.FILES['image']
            profile.firstname=FirstName
            profile.lastname=LastName
            profile.gender=Gender
            profile.date=Date
            profile.month=Month
            profile.year=Year
            profile.profile_image=images
            profile.save()
        return render(request, 'edit_profile.html',{'profile':profile})
    else:
        profile = Upload.objects.get(username=users)
        if request.method == "POST":
            FirstName = request.POST['fname']
            LastName = request.POST['lname']
            Gender = request.POST['Gender']
            Date = request.POST['date']
            Month = request.POST['month']
            Year = request.POST['year']
            images = request.FILES['image']
            profile.firstname = FirstName
            profile.lastname = LastName
            profile.gender = Gender
            profile.date = Date
            profile.month = Month
            profile.year = Year
            profile.profile_image = images
            profile.save()
        return render(request, 'edit_profile.html',{'profile':profile})