from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib import messages
from django.core.exceptions import ValidationError
from .models import Teklif
from django.views.decorators.csrf import csrf_exempt
from .models import ContactFormSubmission
from django.core.mail import EmailMessage

@csrf_exempt
def contact_form(request):
    if request.method == 'POST':
        try:
            # Formdan gelen verileri alın
            name = request.POST.get('name', '').strip()
            email = request.POST.get('email', '').strip()
            message = request.POST.get('message', '').strip()

            # Gerekli alanların dolu olduğundan emin olun
            if not name or not email or not message:
                return HttpResponse('Tüm alanları doldurun.', status=400)

            # Veriyi veritabanına kaydetme
            ContactFormSubmission.objects.create(name=name, email=email, message=message)

            # E-posta gönderme
            send_mail(
                subject=f'Yeni İletişim Talebi: {name}',
                message=f'Ad: {name}\nEmail: {email}\nMesaj: {message}',
                from_email='baygoldyadkin@gmail.com',  # Gönderici e-posta adresiniz
                recipient_list=['bmb_1901@hotmail.com'],  # Alıcı e-posta adresleri
                fail_silently=False,
            )

            return HttpResponse('Mesajınız başarıyla gönderildi.', status=200)

        except Exception as e:
            # Hata durumunda bir hata mesajı döndür
            return HttpResponse(f'Bir hata oluştu: {e}', status=500)

    # GET isteğinde formu içeren şablon döndürülür
    return render(request, 'index.html')
def dokumanlar(request):
    
    return render(request, 'dokumanlar.html')

def esanjor2(request):
    
    return render(request, 'esanjor2.html')
def index2(request):
    
    return render(request, 'index2.html')

def esanjor(request):
    
    
    return render(request, 'esanjor.html')

def hakkimizda(request):
    
    return render(request, 'hakkimizda.html')
def hakkimizda2(request):
    
    return render(request, 'hakkimizda2.html')

def esanjoren(request):
    
    return render(request, 'esanjoren.html')

def esanjoren2(request):
    
    return render(request, 'esanjoren2.html')

def teklifal(request):
    
    return render(request, 'teklifal.html')

def teklifal2(request):
    
    return render(request, 'teklifal2.html')


def index(request):
    
    return render(request, 'index.html')

def iletisim(request):
    
    return render(request, 'iletisim.html')

def gp(request):
    
    return render(request, 'gp.html')
def gp2(request):
    
    return render(request, 'gp2.html')

def dokumanlar2(request):
    
    return render(request, 'dokumanlar2.html')


def process_form(request):
    if request.method == 'POST':
        try:
            # Form verilerini alın, varsayılan değer olarak 0 kullanın
            def get_numeric_value(value):
                try:
                    return float(value) if value else 0
                except ValueError:
                    return 0

            # Verileri almak ve boşlukları temizlemek
            genislik_1 = get_numeric_value(request.POST.get('genislik_1', ''))
            bitmis_uzunluk_1 = get_numeric_value(request.POST.get('bitmis_uzunluk_1', ''))
            diyagonal_1 = get_numeric_value(request.POST.get('diyagonal_1', ''))
            lamel_uzunluk_1 = get_numeric_value(request.POST.get('lamel_uzunluk_1', ''))
            hatve_1 = get_numeric_value(request.POST.get('hatve_1', ''))
            adet_1 = get_numeric_value(request.POST.get('adet_1', ''))

            genislik_2 = get_numeric_value(request.POST.get('genislik_2', ''))
            bitmis_uzunluk_2 = get_numeric_value(request.POST.get('bitmis_uzunluk_2', ''))
            diyagonal_2 = get_numeric_value(request.POST.get('diyagonal_2', ''))
            lamel_uzunluk_2 = get_numeric_value(request.POST.get('lamel_uzunluk_2', ''))
            hatve_2 = get_numeric_value(request.POST.get('hatve_2', ''))
            adet_2 = get_numeric_value(request.POST.get('adet_2', ''))

            genislik_3 = get_numeric_value(request.POST.get('genislik_3', ''))
            bitmis_uzunluk_3 = get_numeric_value(request.POST.get('bitmis_uzunluk_3', ''))
            diyagonal_3 = get_numeric_value(request.POST.get('diyagonal_3', ''))
            lamel_uzunluk_3 = get_numeric_value(request.POST.get('lamel_uzunluk_3', ''))
            hatve_3 = get_numeric_value(request.POST.get('hatve_3', ''))
            adet_3 = get_numeric_value(request.POST.get('adet_3', ''))

            genislik_4 = get_numeric_value(request.POST.get('genislik_4', ''))
            bitmis_uzunluk_4 = get_numeric_value(request.POST.get('bitmis_uzunluk_4', ''))
            diyagonal_4 = get_numeric_value(request.POST.get('diyagonal_4', ''))
            lamel_uzunluk_4 = get_numeric_value(request.POST.get('lamel_uzunluk_4', ''))
            hatve_4 = get_numeric_value(request.POST.get('hatve_4', ''))
            adet_4 = get_numeric_value(request.POST.get('adet_4', ''))

            genislik_5 = get_numeric_value(request.POST.get('genislik_5', ''))
            bitmis_uzunluk_5 = get_numeric_value(request.POST.get('bitmis_uzunluk_5', ''))
            diyagonal_5 = get_numeric_value(request.POST.get('diyagonal_5', ''))
            lamel_uzunluk_5 = get_numeric_value(request.POST.get('lamel_uzunluk_5', ''))
            hatve_5 = get_numeric_value(request.POST.get('hatve_5', ''))
            adet_5 = get_numeric_value(request.POST.get('adet_5', ''))

            name = request.POST.get('name', '').strip()
            email = request.POST.get('email', '').strip()
            phone = request.POST.get('phone', '').strip()
            message = request.POST.get('message', '').strip()

            # E-posta gönderimi
            email_subject = 'Yeni Teklif Talebi'
            email_body = f"""
            <html>
            <body>
                <h2>Yeni Teklif Talebi</h2>
                <p><strong>Ad:</strong> {name}</p>
                <p><strong>Email:</strong> {email}</p>
                <p><strong>Telefon:</strong> {phone}</p>
                <p><strong>Mesaj:</strong> {message}</p>
                <h3>Ürün Bilgileri</h3>
                <table border="1" cellpadding="5" cellspacing="0">
                    <tr>
                        <th>Genislik</th>
                        <th>Bitmis Uzunluk</th>
                        <th>Diyagonal</th>
                        <th>Lamel Uzunluk</th>
                        <th>Hatve</th>
                        <th>Adet</th>
                    </tr>
                    <tr>
                        <td>{genislik_1}</td>
                        <td>{bitmis_uzunluk_1}</td>
                        <td>{diyagonal_1}</td>
                        <td>{lamel_uzunluk_1}</td>
                        <td>{hatve_1}</td>
                        <td>{adet_1}</td>
                    </tr>
                    <tr>
                        <td>{genislik_2}</td>
                        <td>{bitmis_uzunluk_2}</td>
                        <td>{diyagonal_2}</td>
                        <td>{lamel_uzunluk_2}</td>
                        <td>{hatve_2}</td>
                        <td>{adet_2}</td>
                    </tr>
                    <tr>
                        <td>{genislik_3}</td>
                        <td>{bitmis_uzunluk_3}</td>
                        <td>{diyagonal_3}</td>
                        <td>{lamel_uzunluk_3}</td>
                        <td>{hatve_3}</td>
                        <td>{adet_3}</td>
                    </tr>
                    <tr>
                        <td>{genislik_4}</td>
                        <td>{bitmis_uzunluk_4}</td>
                        <td>{diyagonal_4}</td>
                        <td>{lamel_uzunluk_4}</td>
                        <td>{hatve_4}</td>
                        <td>{adet_4}</td>
                    </tr>
                    <tr>
                        <td>{genislik_5}</td>
                        <td>{bitmis_uzunluk_5}</td>
                        <td>{diyagonal_5}</td>
                        <td>{lamel_uzunluk_5}</td>
                        <td>{hatve_5}</td>
                        <td>{adet_5}</td>
                    </tr>
                </table>
            </body>
            </html>
            """

            email_message = EmailMessage(
                subject=email_subject,
                body=email_body,
                from_email='baygolyadkin@gmail.com',
                to=['bmb_1901@hotmail.com'],
            )
            email_message.content_subtype = 'html'  # E-posta içeriğini HTML olarak ayarla
            email_message.send()

            # Model örneğini oluştur ve kaydet
            teklif = Teklif(
                genislik_1=genislik_1, bitmis_uzunluk_1=bitmis_uzunluk_1, diyagonal_1=diyagonal_1,
                lamel_uzunluk_1=lamel_uzunluk_1, hatve_1=hatve_1, adet_1=adet_1,
                genislik_2=genislik_2, bitmis_uzunluk_2=bitmis_uzunluk_2, diyagonal_2=diyagonal_2,
                lamel_uzunluk_2=lamel_uzunluk_2, hatve_2=hatve_2, adet_2=adet_2,
                genislik_3=genislik_3, bitmis_uzunluk_3=bitmis_uzunluk_3, diyagonal_3=diyagonal_3,
                lamel_uzunluk_3=lamel_uzunluk_3, hatve_3=hatve_3, adet_3=adet_3,
                genislik_4=genislik_4, bitmis_uzunluk_4=bitmis_uzunluk_4, diyagonal_4=diyagonal_4,
                lamel_uzunluk_4=lamel_uzunluk_4, hatve_4=hatve_4, adet_4=adet_4,
                genislik_5=genislik_5, bitmis_uzunluk_5=bitmis_uzunluk_5, diyagonal_5=diyagonal_5,
                lamel_uzunluk_5=lamel_uzunluk_5, hatve_5=hatve_5, adet_5=adet_5,
                name=name, email=email, phone=phone, message=message
            )
            teklif.save()

            return redirect('/tr/teklifal')  # Başarı durumunda yönlendirme

        except ValidationError as e:
            return HttpResponse(f'Error: {e}', status=400)
        except Exception as e:
            return HttpResponse(f'Internal Server Error: {e}', status=500)

    return render(request, 'teklifal.html')

