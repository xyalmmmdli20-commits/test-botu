import os
from threading import Thread
from flask import Flask
import telebot
from telebot import types

# Server üçün Flask xidməti
app = Flask('')

@app.route('/')
def home():
    return "Bot aktivdir!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# TELEGRAM BOT KODLARI
API_TOKEN =  "8916781102:AAFXtvpZpxZCqgrPfj8wiAglYqJw7n0byyM" # Öz Bot Tokeninizi bura yazın
bot = telebot.TeleBot(API_TOKEN)

# Minatəmizləmə Agentliyi Hazırlıq Sualları (100 Ən Çətin Sual)
QUESTIONS = [
    {
        "question": "1. Minalardan Təmizləmə üzrə Beynəlxalq Standartlar (IMAS) hansı təşkilat tərəfindən idarə olunur?",
        "options": ["A) UNICEF", "B) UNMAS və GICHD", "C) ICRC", "D) UNHCR"],
        "correct": "B) UNMAS və GICHD"
    },
    {
        "question": "2. IMAS 09.10 standartına əsasən, minatəmizləmə əməliyyatlarında tələb olunan keyfiyyət və dəqiqlik dərəcəsi nə qədərdir?",
        "options": ["A) 90%", "B) 95%", "C) 99.6%", "D) 100%"],
        "correct": "C) 99.6%"
    },
    {
        "question": "3. Piyada əleyhinə minaların istifadəsini və toplanmasını qadağan edən beynəlxalq müqavilə hansıdır?",
        "options": ["A) Cenevrə Konvensiyası", "B) Ottava Müqaviləsi (1997)", "C) Qara Dəniz Sazişi", "D) Vyana Konvensiyası"],
        "correct": "B) Ottava Müqaviləsi (1997)"
    },
    {
        "question": "4. Tank əleyhinə minaların işə düşməsi üçün adətən nə qədər minimum təzyiq gücü tələb olunur?",
        "options": ["A) 1–5 kq", "B) 10–30 kq", "C) 150–350 kq və ya daha çox", "D) 500–1000 kq"],
        "correct": "C) 150–350 kq və ya daha çox"
    },
    {
        "question": "5. PFM-1 ('Kəpənək') minasının əsas fərqləndirici və təhlükəli xüsusiyyəti nədir?",
        "options": ["A) Yalnız kabel ilə patlayır", "B) Yağ hidrostatik təzyiqi ilə işləyir, plastik gövdəlidir", "C) Yalnız su altında işləyir", "D) Yalnız minalı tankı vurur"],
        "correct": "B) Yağ hidrostatik təzyiqi ilə işləyir, plastik gövdəlidir"
    },
    {
        "question": "6. Minaların axtarışında istifadə olunan Georadar (GPR) texnologiyasının əsas üstünlüyü nədir?",
        "options": ["A) Yalnız metali aşkar edir", "B) Torpağın dielektrik keçiriciliyini ölçərək plastik minaları tapır", "C) Partlayıcını məhv edir", "D) Şumlayır"],
        "correct": "B) Torpağın dielektrik keçiriciliyini ölçərək plastik minaları tapır"
    },
    {
        "question": "7. PHS / UXO zərərsizləşdirilməsində 'Deflaqrasiya' nə deməkdir?",
        "options": ["A) Yüksək detondasiyalı partlayış", "B) Detondasiyaya keçmədən, sürətli yanma ilə məhv etmə", "C) Dondurma", "D) Suya batırma"],
        "correct": "B) Detondasiyaya keçmədən, sürətli yanma ilə məhv etmə"
    },
    {
        "question": "8. OZM-72 sıçrayan minanın təsir radiusunda effektiv qəlpə paylanma yüksəkliyi nə qədərdir?",
        "options": ["A) 0.1–0.2 m", "B) 0.6–0.8 m", "C) 2.5–3.0 m", "D) 5.0–8.0 m"],
        "correct": "B) 0.6–0.8 m"
    },
    {
        "question": "9. Qeyri-Texniki Tədqiqatın (NTS) əsas məqsədi nədir?",
        "options": ["A) Ərazini qazmaq", "B) Sorğu və müşahidələrlə təhlükəli zonasının sərhədlərini müəyyən etmək", "C) Poliqonda patlatmaq", "D) Texnika sürümək"],
        "correct": "B) Sorğu və müşahidələrlə təhlükəli zonasının sərhədlərini müəyyən etmək"
    },
    {
        "question": "10. Texniki Tədqiqat (TS) zamanı istifadə olunan əsas üsul hansıdır?",
        "options": ["A) Yalnız kənd təsərrüfatı texnikası", "B) Minedetektor və cihazlarla torpağa fiziki müdaxilə etmək", "C) Peyk şəkillərinə baxmaq", "D) Şəkil çəkmək"],
        "correct": "B) Minedetektor və cihazlarla torpağa fiziki müdaxilə etmək"
    },
    {
        "question": "11. MON-50 yönəldilmiş qəlpəli minanın effektiv zədələmə məsafəsi və bucağı nə qədərdir?",
        "options": ["A) 10m, 30°", "B) 50m, 54°", "C) 100m, 90°", "D) 200m, 180°"],
        "correct": "B) 50m, 54°"
    },
    {
        "question": "12. Piyada minaları olan ərazidə minaaxtaranlar arasında təhlükəsizlik məsafəsi nə qədərdir?",
        "options": ["A) 5 m", "B) 10 m", "C) 25 m", "D) 50 m"],
        "correct": "C) 25 m"
    },
    {
        "question": "13. Tank əleyhinə minalar olan ərazidə minaaxtaranlar arası məsafə nə qədər olmalıdır?",
        "options": ["A) 15 m", "B) 30 m", "C) 50 m", "D) 100 m"],
        "correct": "D) 100 m"
    },
    {
        "question": "14. TM-62M tank əleyhinə minanın gövdəsi hansı materialdandır?",
        "options": ["A) Ağac", "B) Plastik", "C) Metal", "D) Parça"],
        "correct": "C) Metal"
    },
    {
        "question": "15. TM-62P3 minasını TM-62M-dən fərqləndirən əsas cəhət nədir?",
        "options": ["A) İçində partlayıcı yoxdur", "B) Gövdəsi plastikdir", "C) Yalnız su altında işləyir", "D) Pultla idarə olunur"],
        "correct": "B) Gövdəsi plastikdir"
    },
    {
        "question": "16. Partlamamış kasetli sursatların (Submunitions) ən böyük təhlükəsi nədir?",
        "options": ["A) Kiçik və toxunmaya həddən artıq həssas olmaları", "B) Tüstü vermələri", "C) Gecə partlamaları", "D) İy vermələri"],
        "correct": "A) Kiçik və toxunmaya həddən artıq həssas olmaları"
    },
    {
        "question": "17. 'Şiş' (Prober) torpağa hansı bucaq altında vurulmalıdır?",
        "options": ["A) 90°", "B) 30°-dən az (üfüqi bucaq altında)", "C) 60°", "D) Fərq etmir"],
        "correct": "B) 30°-dən az (üfüqi bucaq altında)"
    },
    {
        "question": "18. Şişlə torpaq yoxlanarkən vuruşlar arası məsafə nə qədər olmalıdır?",
        "options": ["A) 2.5 sm-dən çox olmamaqla", "B) 10 sm", "C) 20 sm", "D) 50 sm"],
        "correct": "A) 2.5 sm-dən çox olmamaqla"
    },
    {
        "question": "19. Sərhəd İşarələri (Boundary Markers) hansı rəngdə olur?",
        "options": ["A) Yaşıl-Mavi", "B) Qırmızı və Ağ (və ya Sarı)", "C) Bənövşəyi", "D) Qara"],
        "correct": "B) Qırmızı və Ağ (və ya Sarı)"
    },
    {
        "question": "20. Minalanmış sahədə 'Ağ Payalar' nəyi bildirir?",
        "options": ["A) Təhlükəli zonanı", "B) Təmizlənmiş təhlükəsiz zonanı", "C) Mina nöqtəsini", "D) Su quyusunu"],
        "correct": "B) Təmizlənmiş təhlükəsiz zonanı"
    },
    {
        "question": "21. Qırmızı uclu paya minatəmizləmədə nəyi simvolizə edir?",
        "options": ["A) İstirahət zonasını", "B) Təhlükəli / minalı tərəfi", "C) Tibbi məntəqəni", "D) Yolu"],
        "correct": "B) Təhlükəli / minalı tərəfi"
    },
    {
        "question": "22. Minedetektorun həssaslıq kalibrlənməsi nə vaxt aparılır?",
        "options": ["A) Ayda bir", "B) Xarab olduqda", "C) Hər dəfə işə başlamazdan öncə və torpaq dəyişdikdə", "D) Yalnız yağışda"],
        "correct": "C) Hər dəfə işə başlamazdan öncə və torpaq dəyişdikdə"
    },
    {
        "question": "23. Təhlükəsizlik vizorlu dəbilqə hansı standartlı olmalıdır?",
        "options": ["A) Tikinti dəbilqəsi", "B) Minimum 5mm polikarbonat, STANAG 2920", "C) Şüşə maska", "D) Plastik eynək"],
        "correct": "B) Minimum 5mm polikarbonat, STANAG 2920"
    },
    {
        "question": "24. Fərdi Qoruyucu Zireh (PPE) nəyə qarşı qoruyur?",
        "options": ["A) Birbaşa mərkəzi partlayışa", "B) Təzyiq dalğası, kiçik qəlpələr və alovdan", "C) Günəşdən", "D) Qazdan"],
        "correct": "B) Təzyiq dalğası, kiçik qəlpələr və alovdan"
    },
    {
        "question": "25. 'Tuzak' (Booby-trap) nədir?",
        "options": ["A) Çadır", "B) Zərərsiz obyektdən istifadə edərək qurulmuş gizli partladıcı", "C) İp", "D) Rasiya"],
        "correct": "B) Zərərsiz obyektdən istifadə edərək qurulmuş gizli partladıcı"
    },
    {
        "question": "26. Tələ simləri (Tripwire) axtarışı üçün nə işlədilir?",
        "options": ["A) Çəkic", "B) Yüngül hissiyyat çubuğu / sapı", "C) Kürək", "D) Dəmir çubuq"],
        "correct": "B) Yüngül hissiyyat çubuğu / sapı"
    },
    {
        "question": "27. PMN-2 minası hansı mexanizmlə işləyir?",
        "options": ["A) Kabel", "B) Pnevmatik membranlı təzyiq mexanizmi", "C) Pult", "D) Lazer"],
        "correct": "B) Pnevmatik membranlı təzyiq mexanizmi"
    },
    {
        "question": "28. PMN-4 minasının fərqləndirici cəhəti nədir?",
        "options": ["A) Böyük olması", "B) Kiçik olması və hidrostatik qoruyuculu plastik olması", "C) Dəmirdən olması", "D) Uzaqdan idarə olunması"],
        "correct": "B) Kiçik olması və hidrostatik qoruyuculu plastik olması"
    },
    {
        "question": "29. İkiqat təsirli (Dual-purpose) kasetli sursat nəyə qarşıdır?",
        "options": ["A) Təyyarəyə", "B) Həm zirehli texnikaya, həm canlı qüvvəyə", "C) Gəmiyə", "D) Evlərə"],
        "correct": "B) Həm zirehli texnikaya, həm canlı qüvvəyə"
    },
    {
        "question": "30. Mina Xidmət İtlərinin (MDD) işinə mənfi təsir edən faktor?",
        "options": ["A) Otlar", "B) Yüksək temperatur, küfəkli külək və güclü qoxular", "C) Geyim", "D) Səhər vaxtı"],
        "correct": "B) Yüksək temperatur, küfəkli külək və güclü qoxular"
    },
    {
        "question": "31. Mina təmizləyən it minanı tapdıqda nə etməlidir?",
        "options": ["A) Qazmalıdır", "B) Yanında passiv oturmalı/uzanmalı, minaya dəyməməlidir", "C) Ağzına götürməlidir", "D) Hürməlidir"],
        "correct": "B) Yanında passiv oturmalı/uzanmalı, minaya dəyməməlidir"
    },
    {
        "question": "32. Mexaniki Minatəmizləmə Maşınlarının çatışmazlığı nədir?",
        "options": ["A) Sürətli olması", "B) Torpaq altındakı minanı atması və 100% zəmanət verməməsi", "C) Yanacaq yeməməsi", "D) Ağır olması"],
        "correct": "B) Torpaq altındakı minanı atması və 100% zəmanət verməməsi"
    },
    {
        "question": "33. IMSMA sistemi nə üçün nəzərdə tutulub?",
        "options": ["A) Partlatmaq üçün", "B) Minalı ərazilər haqqında məlumatlar bazasını idarə etmək üçün", "C) Bilet üçün", "D) Şəkil çəkmək üçün"],
        "correct": "B) Minalı ərazilər haqqında məlumatlar bazasını idarə etmək üçün"
    },
    {
        "question": "34. Turniket nə vaxt tətbiq olunur?",
        "options": ["A) Baş yaralanmasında", "B) Ətraflardan həyatı təhlükəli kritik arterial qanaxmada", "C) Yüngül cızıqda", "D) Gövdədə"],
        "correct": "B) Ətraflardan həyatı təhlükəli kritik arterial qanaxmada"
    },
    {
        "question": "35. Minalı sahədən yaralı təxliyə edərkən ilk addım?",
        "options": ["A) Yaralıya tərəf qaçmaq", "B) Təmizlənmiş cığırla təhlükəsiz yaxınlaşmaq", "C) Avtomobillə girmək", "D) Xərəklə qaçmaq"],
        "correct": "B) Təmizlənmiş cığırla təhlükəsiz yaxınlaşmaq"
    },
    {
        "question": "36. Partlayış dalğası (Blast Injury) ilk növbədə hansı orqana zərər vurur?",
        "options": ["A) Dırnaqlara", "B) Eşitmə pərdəsi və ağciyərlərə", "C) Saçlara", "D) Dişlərə"],
        "correct": "B) Eşitmə pərdəsi və ağciyərlərə"
    },
    {
        "question": "37. Detondasiya sürəti nədir?",
        "options": ["A) Tüstünün sürəti", "B) Partlayış dalğasının maddə daxilində yayılma sürəti (m/s)", "C) Çəki", "D) İy"],
        "correct": "B) Partlayış dalğasının maddə daxilində yayılma sürəti (m/s)"
    },
    {
        "question": "38. Brizant partlayıcı maddələrə misal?",
        "options": ["A) Qara barıt", "B) Trofil (TNT), Heksogen, Plastit", "C) Kükürd", "D) Kömür"],
        "correct": "B) Trofil (TNT), Heksogen, Plastit"
    },
    {
        "question": "39. Kapsul-detonatorun funksiyası nədir?",
        "options": ["A) Partlayışı kəsmək", "B) İlkin impuls verərək əsas partlayıcını detondasiya etmək", "C) Su kəsmək", "D) Səs azaltmaq"],
        "correct": "B) İlkin impuls verərək əsas partlayıcını detondasiya etmək"
    },
    {
        "question": "40. Kumulyativ şırnaq (HEAT) effekti nəyə əsaslanır?",
        "options": ["A) Qəlpəyə", "B) Qazların və ərimiş metalın fokuslanaraq zirehi dəlməsinə", "C) İşıq saçmağa", "D) Qaza"],
        "correct": "B) Qazların və ərimiş metalın fokuslanaraq zirehi dəlməsinə"
    },
    {
        "question": "41. Nəzarət Məntəqəsi (Control Point) harada qurulmalıdır?",
        "options": ["A) Zonan ortasında", "B) Minalı zonadan kənarda təhlükəsiz yerdə", "C) Quyuda", "D) Ağac başında"],
        "correct": "B) Minalı zonadan kənarda təhlükəsiz yerdə"
    },
    {
        "question": "42. Təmizlənmiş sahələrin təhvil verilməsi necə adlanır?",
        "options": ["A) İcarə", "B) Land Release", "C) Tikinti", "D) Sənədləşmə"],
        "correct": "B) Land Release"
    },
    {
        "question": "43. Keçid zolağının (Lane) standart eni minimum neçə metr olmalıdır?",
        "options": ["A) 0.5 m", "B) 1.0 m", "C) 3.0 m", "D) 5.0 m"],
        "correct": "B) 1.0 m"
    },
    {
        "question": "44. Mina aşkar edildikdə ilk qayda?",
        "options": ["A) Çıxarmaq", "B) Dayanmaq, dəyməmək, işarələyib komandirə xəbər vermək", "C) Basmaq", "D) Ələ almaq"],
        "correct": "B) Dayanmaq, dəyməmək, işarələyib komandirə xəbər vermək"
    },
    {
        "question": "45. PDM-1M hansı növ minadır?",
        "options": ["A) Aviasiya bombası", "B) Dəniz/Sahil desant əleyhinə mina", "C) Tank minası", "D) Siqnal minası"],
        "correct": "B) Dəniz/Sahil desant əleyhinə mina"
    },
    {
        "question": "46. Minatəmizləmədə 'Key Point' (Əsas İstinad Nöqtəsi) nədir?",
        "options": ["A) Dəqiq koordinatlı sabit coğrafi obyekt", "B) Cihazın açarı", "C) Maşın yeri", "D) Quyunun başı"],
        "correct": "A) Dəqiq koordinatlı sabit coğrafi obyekt"
    },
    {
        "question": "47. Minanın yanında rasiya istifadə edərkən risk nədir?",
        "options": ["A) Risk yoxdur", "B) Radio dalğaları elektro-detonatoru partlada bilər", "C) Rasiya xarab olar", "D) Batareya bitər"],
        "correct": "B) Radio dalğaları elektro-detonatoru partlada bilər"
    },
    {
        "question": "48. SOP açılışı nədir?",
        "options": ["A) Standard Operating Procedures", "B) System Of Protection", "C) Safety Plan", "D) State Policy"],
        "correct": "A) Standard Operating Procedures"
    },
    {
        "question": "49. İki fərqli komanda arası təhlükəsizlik paralellik məsafəsi?",
        "options": ["A) 2 m", "B) 5 m", "C) Minimum 25-50 m", "D) 100 m"],
        "correct": "C) Minimum 25-50 m"
    },
    {
        "question": "50. ANAMA ilk dəfə neçənci ildə yaradılmışdır?",
        "options": ["A) 1998", "B) 1990", "C) 2010", "D) 2020"],
        "correct": "A) 1998"
    },
    {
        "question": "51. Trofil (TNT) maddəsinin ərimə temperaturu təxminən neçə dərəcədir?",
        "options": ["A) 50°C", "B) 80.8°C", "C) 150°C", "D) 300°C"],
        "correct": "B) 80.8°C"
    },
    {
        "question": "52. Heksogen (RDX) maddəsinin detondasiya sürəti təxminən nə qədərdir?",
        "options": ["A) 2000 m/s", "B) 5000 m/s", "C) 8750 m/s", "D) 12000 m/s"],
        "correct": "C) 8750 m/s"
    },
    {
        "question": "53. Plastit-4 (C-4) partlayıcısının tərkibində əsas maddə hansıdır?",
        "options": ["A) Nitroqliserin", "B) Heksogen (RDX)", "C) Qara barıt", "D) Ammonit"],
        "correct": "B) Heksogen (RDX)"
    },
    {
        "question": "54. Partlayıcı maddələrin 'Həssaslığı' dedikdə nə başa düşülür?",
        "options": ["A) Rəngi", "B) Xarici təsirə (zərbə, sürtünmə, qızma) qarşı partlama meylliliyi", "C) Qiyməti", "D) Çəkisi"],
        "correct": "B) Xarici təsirə (zərbə, sürtünmə, qızma) qarşı partlama meylliliyi"
    },
    {
        "question": "55. İlkin (İnisial) partlayıcı maddələrə misal hansıdır?",
        "options": ["A) TNT", "B) Civə fulminatı və Qurğuşun azid", "C) Heksogen", "D) Plastit"],
        "correct": "B) Civə fulminatı və Qurğuşun azid"
    },
    {
        "question": "56. Qara barıt hansı partlayıcı növünə aiddir?",
        "options": ["A) Brizant", "B) Atıcı / Yanan partlayıcı", "C) Kumulyativ", "D) Nüvə"],
        "correct": "B) Atıcı / Yanan partlayıcı"
    },
    {
        "question": "57. Sualtı minalarda istifadə olunan torpaq dərinliyi sensoru necə adlanır?",
        "options": ["A) Lazer", "B) Qravimetrik / Hidrostatik sensor", "C) Barometr", "D) Termometr"],
        "correct": "B) Qravimetrik / Hidrostatik sensor"
    },
    {
        "question": "58. MON-90 minasının zədələmə məsafəsi neçə metrdir?",
        "options": ["A) 30m", "B) 50m", "C) 90m", "D) 180m"],
        "correct": "C) 90m"
    },
    {
        "question": "59. MON-100 minasının forması necədir?",
        "options": ["A) Düz kvadrat", "B) Çökək disk (Tabaq) formalı", "C) Silindrik şam", "D) Üçbucaq"],
        "correct": "B) Çökək disk (Tabaq) formalı"
    },
    {
        "question": "60. MON-200 minasının fəaliyyət radiusu nə qədərdir?",
        "options": ["A) 50m", "B) 100m", "C) 200m", "D) 500m"],
        "correct": "C) 200m"
    },
    {
        "question": "61. OZM-3 və OZM-4 minaları necə fəaliyyət göstərir?",
        "options": ["A) Torpaq altında qalır", "B) Sıçrayaraq havada partlayır", "C) Su altında üzür", "D) Yalnız səs çıxarır"],
        "correct": "B) Sıçrayaraq havada partlayır"
    },
    {
        "question": "62. PMN minasının korpusu hansı materialdandır?",
        "options": ["A) Dəmir", "B) Plastik və ya rezin örtüklü bakelit", "C) Alüminium", "D) Şüşə"],
        "correct": "B) Plastik və ya rezin örtüklü bakelit"
    },
    {
        "question": "63. POMZ-2 piyada əleyhinə minanın korpusu nə dən ibarətdir?",
        "options": ["A) Hamar plastik", "B) Çuqun (qəlpəli naxışlı)", "C) Ağac", "D) Kağız"],
        "correct": "B) Çuqun (qəlpəli naxışlı)"
    },
    {
        "question": "64. TM-57 tank əleyhinə minasının partladıcı mexanizmi adətən hansıdır?",
        "options": ["A) MVZ-57", "B) MUV-2", "C) VPF", "D) ZEV"],
        "correct": "A) MVZ-57"
    },
    {
        "question": "65. TM-62P2 minasının gövdəsi hansı materialdandır?",
        "options": ["A) Metal", "B) Plastik", "C) Ağac", "D) Parça"],
        "correct": "B) Plastik"
    },
    {
        "question": "66. TM-62T minasının 'T' hərfi neyi bildirir?",
        "options": ["A) Tank", "B) Parça (Tkan) gövdəli", "C) Torpaq", "D) Ağır"],
        "correct": "B) Parça (Tkan) gövdəli"
    },
    {
        "question": "67. TM-62B minasının 'B' hərfi neyi bildirir?",
        "options": ["A) Böyük", "B) Karton / Kağız (Bumajnaya) gövdəli", "C) Beton", "D) Bazalt"],
        "correct": "B) Karton / Kağız (Bumajnaya) gövdəli"
    },
    {
        "question": "68. MUV tipli partladıcı mexanizmlər adətən hansı minalarda istifadə olunur?",
        "options": ["A) Tank əleyhinə", "B) Çəkilmə/Gərilmə (Tripwire) fəaliyyətli piyada minalarında", "C) Aviasiya bombalarında", "D) Dəniz minalarında"],
        "correct": "B) Çəkilmə/Gərilmə (Tripwire) fəaliyyətli piyada minalarında"
    },
    {
        "question": "69. MUV-2 partladıcısında təhlükəsizlik gecikməsi ne tərəfindən təmin edilir?",
        "options": ["A) Saat mexanizmi", "B) Qurğuşun milin kəsilməsi (metal rezak)", "C) Su", "D) İşıq sensoru"],
        "correct": "B) Qurğuşun milin kəsilməsi (metal rezak)"
    },
    {
        "question": "70. VFD tipli partladıcılar hansı prinsiplə işləyir?",
        "options": ["A) Maqnit", "B) Elektrik / Pnevmatik", "C) Təzyiq", "D) İşıq"],
        "correct": "B) Elektrik / Pnevmatik"
    },
    {
        "question": "71. GIS (Geoqrafik İnformasiya Sistemi) minatəmizləmədə nə işə yarayır?",
        "options": ["A) Minanı çıxarmaq", "B) Xəritəçəkmə və koordinatların təhlili", "C) Maşın sürmək", "D) Su axtarmaq"],
        "correct": "B) Xəritəçəkmə və koordinatların təhlili"
    },
    {
        "question": "72. DGPS cihazının adi GPS-dən fərqi nədir?",
        "options": ["A) Ucuzdur", "B) Dəqiqliyi santimetr səviyyəsindədir", "C) Səsi çoxdur", "D) Rənglidir"],
        "correct": "B) Dəqiqliyi santimetr səviyyəsindədir"
    },
    {
        "question": "73. Minedetektorun 'Ground Balance' (Torpaq Balansı) funksiyası neyə lazımdır?",
        "options": ["A) Səsi artırmaq", "B) Torpaqdakı mineralların (dəmirli torpaq) yaratdığı yanlış siqnalları ləğv etmək", "C) İşıq saçmaq", "D) Batareya qorumaq"],
        "correct": "B) Torpaqdakı mineralların (dəmirli torpaq) yaratdığı yanlış siqnalları ləğv etmək"
    },
    {
        "question": "74. İki pilləli detektorlar (Dual-sensor) hansı texnologiyaları birləşdirir?",
        "options": ["A) İşıq və Səs", "B) Metal Detektor (MI) və Georadar (GPR)", "C) Lazer və Ultrabənövşəyi", "D) Rasiya və GPS"],
        "correct": "B) Metal Detektor (MI) və Georadar (GPR)"
    },
    {
        "question": "75. Minatəmizləmədə 'Safety Lane' nədir?",
        "options": ["A) Magistral yol", "B) Yoxlanılmış və tam təhlükəsiz keçid zolağı", "C) Xəndək", "D) Meşə zolağı"],
        "correct": "B) Yoxlanılmış və tam təhlükəsiz keçid zolağı"
    },
    {
        "question": "76. 'Benchmark' (BM) topoqrafiyada nədir?",
        "options": ["A) Taxta masa", "B) Hündürlüyü və koordinatı tam dəqiq bililən daimi nizamlayıcı nöqtə", "C) Cihaz qutusu", "D) Bayraq"],
        "correct": "B) Hündürlüyü və koordinatı tam dəqiq bililən daimi nizamlayıcı nöqtə"
    },
    {
        "question": "77. 'Turning Point' (TP) minatəmizləmə xəritəsində neyi göstərir?",
        "options": ["A) Avtomobilin döndüyü yer", "B) Sərhəd xəttinin bucaq dəyişdiyi istiqamət nöqtəsi", "C) Yolu", "D) Evləri"],
        "correct": "B) Sərhəd xəttinin bucaq dəyişdiyi istiqamət nöqtəsi"
    },
    {
        "question": "78. Minalanmış sahədə bitkilərin və otların kəsilməsi (Vegetation clearance) necə aparılmalıdır?",
        "options": ["A) Yandırmaqla", "B) Minaya toxunmadan, ehtiyatla zolaq-zolaq üst hissədən kəsməklə", "C) Traktorla biçməklə", "D) Elle dartıb kökündən çıxarmaqla"],
        "correct": "B) Minaya toxunmadan, ehtiyatla zolaq-zolaq üst hissədən kəsməklə"
    },
    {
        "question": "79. Ot kəsərkən minimum nə qədər hündürlük saxlanmalıdır?",
        "options": ["A) 0 sm", "B) 5–10 sm (tələ simlərini görmək üçün)", "C) 50 sm", "D) 1 metr"],
        "correct": "B) 5–10 sm (tələ simlərini görmək üçün)"
    },
    {
        "question": "80. Minatəmizləmə zamanı 'Tripwire Feeler' naqilə toxunduqda nə edilməlidir?",
        "options": ["A) İpi bərk dartmaq", "B) Hərəkəti dayandırmaq və ehtiyatla zolaqdan geriyə çəkilmək", "C) İpi kəsmək", "D) İpi tapdalamaq"],
        "correct": "B) Hərəkəti dayandırmaq və ehtiyatla zolaqdan geriyə çəkilmək"
    },
    {
        "question": "81. Təhlükəli sahədə siqaret çəkmək və ya açıq alovdan istifadə etmək niyə qadağandır?",
        "options": ["A) Tüstü itləri gicəlləndirir", "B) Partlayıcı qazları və ya açıq partlayıcı maddələri alışdıra bilər", "C) Qanuna ziddir", "D) Çirkləndirir"],
        "correct": "B) Partlayıcı qazları və ya açıq partlayıcı maddələri alışdıra bilər"
    },
    {
        "question": "82. İnsident zamanı 'Casevac' ne deməkdir?",
        "options": ["A) Yolu təmizləmək", "B) Yaralının təcili tibbi təxliyəsi (Casualty Evacuation)", "C) Avtomobil təmiri", "D) Yemək daşınması"],
        "correct": "B) Yaralının təcili tibbi təxliyəsi (Casualty Evacuation)"
    },
    {
        "question": "83. Minatəmizləmə sahəsində 'Medevac' planı nə vaxt hazır olmalıdır?",
        "options": ["A) Yaralanma olduqdan sonra", "B) Əməliyyatlar başlamazdan əvvəl", "C) Günün sonunda", "D) Həftədə bir"],
        "correct": "B) Əməliyyatlar başlamazdan əvvəl"
    },
    {
        "question": "84. Təhlükəli sahədən təxliyə olunan yaralıya hansı sənəd bərkidilməlidir?",
        "options": ["A) Pasport", "B) Təxliyə kartı / Tibbi kart (vuruş vaxtı, vurulan turniket vaxtı qeyd olunmaqla)", "C) Sürücülük vəsiqəsi", "D) Xəritə"],
        "correct": "B) Təxliyə kartı / Tibbi kart (vuruş vaxtı, vurulan turniket vaxtı qeyd olunmaqla)"
    },
    {
        "question": "85. Turniket vurulduqdan sonra maksimum neçə saat saxlanıla bilər (toxuma ölümünün qarşısını almaq üçün)?",
        "options": ["A) 10 dəqiqə", "B) 1.5 - 2 saat", "C) 12 saat", "D) 24 saat"],
        "correct": "B) 1.5 - 2 saat"
    },
    {
        "question": "86. Sümük sınıqları zamanı ilkin yardımda ne edilir?",
        "options": ["A) Sümüyü düzəltməyə çalışmaq", "B) Ətrafı şina (шина) ilə təsbit edib hərəkətsizləşdirmək", "C) İsti su tökmək", "D) Masaj etmək"],
        "correct": "B) Ətrafı şina (шина) ilə təsbit edib hərəkətsizləşdirmək"
    },
    {
        "question": "87. Partlayışdan sonra gözə yabançı cisim düşərsə ne edilməlidir?",
        "options": ["A) Gözü ovxalamaq", "B) Gözü ovalamadan sarğı ilə bağlamaq və həkimə çatdırmaq", "C) Barmaqla çıxarmaq", "D) Sabunla yumaq"],
        "correct": "B) Gözü ovalamadan sarğı ilə bağlamaq və həkimə çatdırmaq"
    },
    {
        "question": "88. Yanıq zamanı ilk yardım necədir?",
        "options": ["A) Yanıq üstünə yağ yaxmaq", "B) Sərin axar su altında 10-15 dəqiqə saxlamaq", "C) Buz yapışdırmaq", "D) Yoğurt sürtmək"],
        "correct": "B) Sərin axar su altında 10-15 dəqiqə saxlamaq"
    },
    {
        "question": "89. PHS (UXO) aşkar edildikdə onun gövdəsinə vurmaq və ya tərpətmək niyə təhlükəlidir?",
        "options": ["A) Paslanar", "B) Daxilindəki mexanizm və ya kimyəvi qoruyucu hər an işə düşə bilər", "C) Rəngi getsin", "D) Səsi çıxar"],
        "correct": "B) Daxilindəki mexanizm və ya kimyəvi qoruyucu hər an işə düşə bilər"
    },
    {
        "question": "90. Minatəmizləmə maşını olan 'Bozena' hansı ölkə istehsalıdır?",
        "options": ["A) ABŞ", "B) Slovakiya", "C) Almaniya", "D) Çin"],
        "correct": "B) Slovakiya"
    },
    {
        "question": "91. 'MV-4' mexaniki minatəmizləmə maşını hansı ölkənindir?",
        "options": ["A) Xorvatiya (DOK-ING)", "B) Rusiya", "C) Türkiyə", "D) İngiltərə"],
        "correct": "A) Xorvatiya (DOK-ING)"
    },
    {
        "question": "92. MEMATT minatəmizləmə maşını hansı ölkənin istehsalıdır?",
        "options": ["A) Azərbaycan", "B) Türkiyə (ASFAT)", "C) İsrail", "D) Fransa"],
        "correct": "B) Türkiyə (ASFAT)"
    },
    {
        "question": "93. 'Tiller' tipi maşınların 'Flail' tipi maşınlardan fərqi nədir?",
        "options": ["A) Flail zəncirlə vurur, Tiller fırlanan kəsici dişli rotorla torpağı üyüdür", "B) Tiller su ilə işləyir", "C) Flail uçur", "D) Heç bir fərqi yoxdur"],
        "correct": "A) Flail zəncirlə vurur, Tiller fırlanan kəsici dişli rotorla torpağı üyüdür"
    },
    {
        "question": "94. İt ilə minatəmizləmə zamanı 'Aroma Box' (Qoxu qutusu) ne üçün istifadə olunur?",
        "options": ["A) İtə yemək vermək üçün", "B) İtin maddə qoxusunu tanıması və test edilməsi üçün", "C) İti yatırtmaq üçün", "D) Su qabı kimi"],
        "correct": "B) İtin maddə qoxusunu tanıması və test edilməsi üçün"
    },
    {
        "question": "95. Mina İtlərinin iş vaxtı adətən nə qədər olur?",
        "options": ["A) Fasiləsiz 8 saat", "B) 30-40 dəqiqə iş, sonra fasilə və istirahət", "C) 10 dəqiqə", "D) Bütün gün"],
        "correct": "B) 30-40 dəqiqə iş, sonra fasilə və istirahət"
    },
    {
        "question": "96. IMAS 08.20 standartı nəyi tənzimləyir?",
        "options": ["A) Yeməkləri", "B) Sahənin Texniki Tədqiqatını (Technical Survey)", "C) Avtomobilləri", "D) Sənədləri"],
        "correct": "B) Sahənin Texniki Tədqiqatını (Technical Survey)"
    },
    {
        "question": "97. IMAS 10.20 standartı nəyə aiddir?",
        "options": ["A) Tibbi təminat və ilk yardıma", "B) İtlərin təliminə", "C) Maşınların təmirinə", "D) İmtahanlara"],
        "correct": "A) Tibbi təminat və ilk yardıma"
    },
    {
        "question": "98. Minatəmizləmə əməliyyatlarında QA / QC ne deməkdir?",
        "options": ["A) Quality Assurance (Keyfiyyətə Təminat) / Quality Control (Keyfiyyətə Nəzarət)", "B) Quick Action", "C) Quality Area", "D) Quiet Zone"],
        "correct": "A) Quality Assurance (Keyfiyyətə Təminat) / Quality Control (Keyfiyyətə Nəzarət)"
    },
    {
        "question": "99. QA (Keyfiyyətə Təminat) nə vaxt həyata keçirilir?",
        "options": ["A) Əməliyyat bitəndən sonra", "B) Əməliyyat gedişatında (iş zamanı)", "C) İllər sonra", "D) İşdən əvvəl"],
        "correct": "B) Əməliyyat gedişatında (iş zamanı)"
    },
    {
        "question": "100. QC (Keyfiyyətə Nəzarət) nə vaxt həyata keçirilir?",
        "options": ["A) İş gedişatında", "B) Təmizləmə işləri tam bitdikdən sonra seçmə yoxlama ilə", "C) Başlamazdan əvvəl", "D) Yalnız gecələr"],
        "correct": "B) Təmizləmə işləri tam bitdikdən sonra seçmə yoxlama ilə"
    }
]

user_data = {}

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton('📝 Testə Başla')
    btn2 = types.KeyboardButton('📊 Nəticələrim')
    keyboard.add(btn1, btn2)
    
    bot.send_message(
        message.chat.id,
        "🇦🇿 **Minatəmizləmə Agentliyi (ANAMA) İmtahan Botu**\n\n"
        "Siz burada 100 ədəd peşəkar imtahan sualı ilə biliklərinizi test edə bilərsiniz.\n\n"
        "Başlamaq üçün **📝 Testə Başla** düyməsinə klikləyin.",
        reply_markup=keyboard,
        parse_mode="Markdown"
    )

@bot.message_handler(content_types=['text'])
def handle_text(message):
    chat_id = message.chat.id
    
    if message.text == '📝 Testə Başla':
        user_data[chat_id] = {'current_q': 0, 'score': 0}
        send_question(chat_id)
        
    elif message.text == '📊 Nəticələrim':
        score = user_data.get(chat_id, {}).get('score', 0)
        bot.send_message(
            chat_id, 
            f"📊 **Son nəticəniz:** {score} / {len(QUESTIONS)} doğru cavab.",
            parse_mode="Markdown"
        )

def send_question(chat_id):
    q_idx = user_data[chat_id]['current_q']
    
    if q_idx >= len(QUESTIONS):
        score = user_data[chat_id]['score']
        total = len(QUESTIONS)
        bot.send_message(
            chat_id,
            f"🎉 **Təbriklər! İmtahanı başa vurdunuz.**\n\nYekun nəticəniz: {total} sualdan **{score}** doğru cavab!",
            parse_mode="Markdown"
        )
        return

    q = QUESTIONS[q_idx]
    markup = types.InlineKeyboardMarkup(row_width=1)
    
    for opt in q['options']:
        markup.add(types.InlineKeyboardButton(text=opt, callback_data=opt))
        
    bot.send_message(
        chat_id, 
        f"**Sual {q_idx + 1} / {len(QUESTIONS)}:**\n\n{q['question']}", 
        reply_markup=markup,
        parse_mode="Markdown"
    )

@bot.callback_query_handler(func=lambda call: True)
def handle_answer(call):
    chat_id = call.message.chat.id
    
    if chat_id not in user_data:
        bot.answer_callback_query(call.id, "Zəhmət olmasa testi yenidən başladın.")
        return
    
    q_idx = user_data[chat_id]['current_q']
    correct_ans = QUESTIONS[q_idx]['correct']
    
    if call.data == correct_ans:
        user_data[chat_id]['score'] += 1
        bot.answer_callback_query(call.id, "✅ Doğru cavab!")
    else:
        bot.answer_callback_query(call.id, f"❌ Səhvdir! Doğru cavab: {correct_ans}", show_alert=True)
        
    user_data[chat_id]['current_q'] += 1
    bot.delete_message(chat_id, call.message.message_id)
    send_question(chat_id)

if __name__ == '__main__':
    keep_alive()
    bot.infinity_polling()
