from api import PetFriends
from settings import valid_email, valid_password
import os

pf = PetFriends()

def test_get_api_key_empty_user_mail_string(email='', password=valid_password):
    """ Проверяем что запрос api ключа возвращает статус 403 если email пустая строка"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert 'key' not in result

def test_get_api_key_invalid_user_mail_data(email='der@email.com', password=valid_password):
    """ Проверяем что запрос api ключа возвращает статус 403 если email не верный"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert 'key' not in result


def test_get_api_key_without_user_password(email=valid_email, password=''):
    """ Проверяем что запрос api ключа возвращает статус 403 если password пустая строка"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert 'key' not in result

def test_get_api_key_invalid_data_user_password(email=valid_email, password='00001'):
    """ Проверяем что запрос api ключа возвращает статус 403 если password введен не верно"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert 'key' not in result



def test_add_new_pet_with_name_of_255_values(name='ВЦЧЩнХтХби1егчФ1ушн7ТЯРуМкЮД1И05КМоц2лцЗъумЙ9лынрФкСМПхВЮМЧЯЁдЬХФ3кнЮфю1ШЧЯНхДя4ё0пЬ5зЙМШЙрЭщ9ЖМртЫЬЫхе0лС3чд7Р5ЁбЯч6фелИЕйёлфРемКШЧщДЦРдЭъвэОеОхечл5хд0МдСЧб9Р8Ф6й0ауНтйшРБиёЁ13тШФьУ9ЙХсЁХамлфхЮКсГЭмАзЯ5ВСъячАБЛ2бтЫИМРБэцъЖуоВ4эяФБЕДЩЦ8ъцШЩКЗЖфКБщиДю2ЧЖкУ', animal_type='двортерьер',
                                     age="5", pet_photo='images/cat.jpg'):
    """Проверяем можно ли добавить name питомца 255 символов """

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_add_new_pet_with_name_of_1000_values(name='ПКьюднОГ14иКёмЙжМая8МППБе9ЭБЪАЧжОъЧЦтшМРОцю3д0дрАяыЪЯОчЖОЛМ9ЬмЭКХш3ххУШзЪ6ДекЛлМИЪ0шьдивХфПшЩэЩ2ГчЦк5б4Тж3хъ8ФяЕпА5бёЫНЮЯБяАОТ8дДЦЖЖЬиГОфярПчэФ4ыЫ4НмСЁБШ3вДГ4ПтбжпР8РХЬоФКЁ4Ыл6П1муеФКХТлйУЗшВД8цфЙУГКгщбм08Ё3ЭИгйОЦ9ы8ъН2Ь8ОРь8дзЮзЩБэ3д4ФэдЩжюКйьме83У9УхЦтшм48БобЖДжзИЩЮКЮедСшлАПМшжадЫЩьК0чРЮъзакзМаёешОУЮЬЙ2Гюш2ЕДщлДЭУл7нзцфчхЁфУСУЖёЙЭоыПТллу72М0эЕЬйЧбоыСЬГьГЩъёхККы8иЩДГ7ЖёЦеГЁПпфХюз0ВКЪЖысДюдЭекЪгбЪЛЭРшмфодиНфАяТпЮгуОср1ШщЙРчыЧ5Чдон0ЯиВлМ1ИжазДъАВВЧЩ6Хк6ГцмнядЩРа6мАзк2ПЯ9хНщвсФН14сдЁм5яюБ00б6пЦЁсАкЗч1ЦеЮтХмБЮ8знИчрЗГф8цЕыиЛюЬВк9ЧЕхЯЭШДРЩИ636Зно9Хшч7Ящ0хг2ё7ъЪцё2ЕоУЭБЬДшЬы3ьбМеъчъщсхЦъщ6ючьЛЁч5ЧНФрЛэРрш6цЕуЭш9оФЬшЛч1роФям2ИшШщбщлвКцтпуМ8п6ыЙэЛуСЧЛК7лБЗъУьЧВэ2щФЩ5208щяН5оСЭ5аЦКжэнх3ЯхижОкммдШнИчЗяЁЛщГжГббрЪжЦаЬЕЦХщвФэРнТЖЮмЕэЦбВКывСМщНвгЮ9ЙИфёчЙыЙГЧьйбкКэн4рпТб4КЭДЭнйКшФЖдЗжпЕшЯПХЛзПкжддгръгПо4ккЖпнЪщлнЧО6СкьФЩбЭыа3ЙтУмУ4ЖгиЧчН2С1ОШ8яжеУ8РНОсббмужЖжягеЮБЭЁПоРрШьЩЗщЗШГгфЛЙрювущмэЖЩЫЪШИыеО5ДМяёДТИЩ9КУОЩЫдБ4ЯТ1Г8ъх2ГЧ9РЖ5Г4УЗЛхВфымфЦЁМДБДСмГФЗ4чяЮмг1фЁ5Ч8жъЖЬд3йБЁтАП4кАйвэжвлФзцЛОм5ъёНЖожЛемр', animal_type='двортерьер', age="5", pet_photo='images/cat.jpg'):
    """Проверяем можно ли добавить name питомца 1000 символов """

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом: ответ 200 является bag
    # assert status == 400
    # assert 'name' not in result
    assert status == 200
    assert result['name'] == name



def test_add_new_pet_255_values_animal_type(name='Барбоскин', animal_type='ВПлтзЁъ3цХ6ГФЦшН2ац8Иэожщр5ЧАхм53тЙЙн1ш802з6ШБс8тЕвЁЁ8эА5итбьЧУХф6Оьм7ДтМИсЭьХЦ2СЙхЬдкЁеХу04ДфПышС3Гш9ж9БЕчЖс2рп9Ыет1РЖееЯцз68бсЕу5ЧЗирБКЛ38ЮдьфЗ7эъЬЧСБсЩ2юЙЭЪДЕшАЙУ3ЩыЧМЦвж22уЩчИгжныё4лбХе3ф5ыьнЖАз1йттаРфЩРхАЭ2зЮЁЪРлугнЯлдЁёЧ6Нг5Ч1НЩЕЫРфгМЩцФхрмпкц09ОЖУё',
                                     age='4', pet_photo='images/cat.jpg'):
    """Проверяем что можно добавить питомца с 255 символов в animal_type"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом

    assert status == 200
    assert result['animal_type'] == animal_type




def test_add_new_pet_1000_values_animal_type(name='Барбоскин', animal_type='9ИжЛсЖС1РпафЗГа9Сфт2шЛу3бЭэФИцмбтВъ3жяБэъяЮ77шДЬСЁъ7к2ЗлаоНпПд5ЮфайЛЮЮоЫйецЗГЬВЮёуАЯААйЁЦОьЬЁеЗЮфЬЬуЕтюёЪ6рЯбМдЩуЖзДЛЬпоыбФКзящ2п0ъбоуяпЩШёЭеЦЦЮ3мН0ь50ЗХЧЙДхйпысРд0З7ю2ымъщ4йТ2ИцйыдуэаСЯсНэйь7ЖТтф9оЕЩ9Пб0ЁэюПщеЕДоЧАЗмЮ6изртд0Ш6гНЛджгфи46упеьэтШЬДЁзхст2ёт89мИпКОйСбЬвВВтуВоЩЮТзШ8КфХЕяЮесе9РВУщОЬодкхкмайхшацдтШ7ёыРу544асНпСлзШя9эЛбмшхф5цКфыЫКОАд03ШЯШЙъ16ГПя7ыЮГцУэЧЗ6ЧшД0ЩГКрЮХёЪи4цОНсЮЕЙЙжДЭДм0йбгфпбИЪСХЕЗЮпИУеЩоКбуяЫкПррмф7щКЛмпрьФюОЖПбпмЪр9ЕюзЗЦЭжпИВЭйв8оНсЙРДёУгоФыгЖС70Утдыз5я8ыящДд6чткППиюН0ёПиюаРЯцш7СЁ4ЮчЯ2лМУЫАЫедЫЮЁлЪЛуИЕ5ЮЯсэъмфШАж1ЧСЛ9еаьУ8ВблБМгМАНВ3гъЦ4ЗтРСЁУЕС3Ы3лаНВятДЪЬгЕЙя7ИъсэПпТб1мЦЧЯе5ГФм5уГБфЦЦыС6ёэОМи4йРшэЬЮЧн87ъУяРоюЯЖаэГ19ЙРИш6нЩЧеФПлЮщжЙуДрьЗыФфЬЦЙА3ж7ЧЁЮтУЩп7бчйГлтдвйэз7Еу6ЯМтрсЮЫАИТёщтОВуупкЯГЫзЮЦШшу0йДгиИБЗаХ737ъроЭ8АПОхЬлиЖ6кЧшр36ОеЯхбКЯфёсЛЭМ3чЕВДРгаж1рЬЮъдП2оПфЮГи1К8В8чъЙТёоаиЩШКЫоДьы3т37ЫЪЪирЯУёРж15ксЪМЪЭКяжЪЯЧ7КЫйфюъ8НЕйбйДфЬЖдРЁДМыТе6еа2л59ФсмЫИЁУМчьСшТЩфбдквйеЗхЪЕПнэУрИЛ13пщ0ЯЪФшЕкФ2шЦЧаК493тЮьР2ЫсМйзг4дтДХюеОКаЩБчФУ8хЙНПбУШыесЕФЪФВорфРХЩБтР2бСерХькЗЕнакъ0',
                                     age='4', pet_photo='images/cat.jpg'):
    """Проверяем что можно добавить питомца с 1000 символов в animal_type"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом: ответ 200 является bag
    # assert status == 400
    # assert 'animal_type' not in result
    assert status == 200
    assert result['animal_type'] == animal_type


def test_add_pet_age_negative_value(name='Барбоскин', animal_type='двортерьер',
                                     age='-4', pet_photo='images/cat.jpg'):
    """Проверяем что можно добавить в возраст питомца <age> отрицательное значение"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом: ответ 200 является bag
    # assert status == 400
    # assert 'age' not in result
    assert status == 200
    assert result['age'] == age


def test_add_pet_empty_value_only_photo(name='', animal_type='',
                                     age='', pet_photo='images/cat.jpg'):
    """Проверяем что можно добавить питомца только с pet_photo данными"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом: ответ 200 является bag
    # assert status == 400
    # assert 'name' not in result and assert 'animal_type' not in result and assert 'age' not in result
    assert status == 200
    assert result['name'] == name and result['animal_type'] == animal_type and result['age'] == age