# Проект Dr.CAT

### Демо работы:
https://drive.google.com/file/d/1JpujOTksacPv11vwAMLU2_2j_-ZWn0l4/view

### Защита проекта на V Уральской Проектной смене 2021:
https://drive.google.com/file/d/1PRM3ZvSFCMBCeltpeH-_sXHYtVZxpP7t/view?usp=sharing

### Направление проекта
Цифровая медицина, применение искусственного интеллекта в медицине

### Аннотация проекта
Создание сервиса для врачей по определению типа инсульта и постановки тактики лечения на основе анализа КТ снимков головного мозга и анамнеза пациента.

### Как работает?
Врач авторизуется на сервисе, вводит данные о пациенте и загружает результат компьютерной томографии. Информация уходит на сервер, где свёрточные нейронные сети определяют тип инсульта, а алгоритм, работающий на основе рекомендаций Российской Ассоциации Нейрохирургов, формирует тактику лечения. Результат уходит обратно на сайт, где врач может ознакомиться с типом патологии, рекомендациями по лечению и действиями коллег в похожих случаях.

### Проблема, на решение которой направлен проект
По данным Всемирной Организации Здравоохранения инсульты являются второй по численности причиной смертности людей в мире [1]. Один из этапов лечения пациента, на котором возникают трудности, является этап диагностики. В настоящее время компьютерная томография остается основным методом диагностирования инсульта. Однако в маленьких городах, а также в ночное время, праздники или выходные в первичных сосудистых отделениях (ПСО), куда привозят пациентов с подозрением на инсульт, могут отсутствовать специалисты по КТ-диагностике. Как следствие, появляется необходимость использования телемедицины, из-за чего происходят потери во времени и точности диагностики. При этом установлено, что при инсульте 1 час без лечения равносилен 3.5 годам старения мозга [2].
Еще одна проблема, которая была выявлена при работе над проектом и консультации со специалистами-нейрохирургами, - формирование неполного медицинского заключения, которое содержит не все необходимые рекомендации к дальнейшему лечению пациента.

### Актуальность и значимость
Данный сервис призван стать помощником для врачей, их “старшим коллегой” для повышения скорости и точности диагностики инсульта и других патологий. Как следствие, повышается шанс на благополучный исход, полное восстановление после болезни и уменьшается риск инвалидизации пациента. Важным преимуществом данного приложения является не только определение типа патологии, но и формирование рекомендаций по дальнейшей тактике лечения.

### Потребители
Дежурные врачи, неврологи, нейрохирурги и КТ-диагносты, работающие в первичных сосудистых отделениях больниц.

### Современное состояние решений по данной проблеме (прямые или косвенные аналоги, их наличие/отсутствие)
На зарубежном рынке данной проблемой занимаются компании qure.ai [3] и brainscan [4]. Их функционал заключается в определении типа патологии, а также обозначении области поражения мозга и вычислении объема кровоизлияния. Однако они не дают рекомендаций по дальнейшему лечению, тем самым не решая проблему неполноты рекомендаций. 
В России подобными разработками занимается лаборатория по искусственному интеллекту Сбера [5], также выделяющая область поражения на КТ-снимке. Но данный проект классифицирует инсульты лишь по трём типам: нет инсульта, ишемический инсульт,  геморрагический инсульт. Однако в медицинской практике геморрагический инсульт тоже делится на разные категории, для каждой из которых формируется своя тактика лечения пациента. Кроме того, сервис Сбера, как и зарубежные аналоги, не предоставляет рекомендаций по дальнейшему лечению.

### Что уже сделано в проекте
- Реализован сервис, с демонстрацией работы которого вы можете ознакомиться в приложенном видеофрагменте: https://youtu.be/nuNDJuK8_R4. 
- Были осуществлены следующие пункты работ:
- Собрана и размечена база из 11 тысяч КТ-снимков, классифицированная по следующим патологиям: внутримозговая гематома, субарахноидальное кровоизлияние, внутрижелудочковое кровоизлияние, инфаркт мозга (ишемический инсульт), опухоль мозга.
- Составлены рекомендации по дальнейшей тактике лечения пациентов с учетом типа патологии и анамнеза пациента на основе клинических рекомендаций ассоциации нейрохирургов России [6].
- Созданы дизайн и структура приложения.
- Разработано 5 сверточных нейронных сетей, каждая из которых отвечает за определение отдельной патологии мозга. На данный момент работа нейронных сетей проверена на 40 тестовых снимков, 36 из которых были диагностированы верно.
- Разработана возможность поиска похожих КТ-снимков по методу машинного обучения k-ближайших соседей.
- Реализован механизм формирования медицинского заключения в docx-формате.
- Организован личный кабинет для врачей, где они могут просматривать свою историю проведенных диагностик по пациентам.
- Создан просмотр общей библиотеки всех загруженных КТ-снимков с фильтрацией по типу патологии, объему гематомы и другим необходимым для врача данным.
- Создана вкладка Люди для просмотра всех зарегистрированных на сервисе врачей (КТ-диагностов, дежурных врачей, неврологов, нейрохирургов).
- Написана справка по работе с сервисом.

### План работ
- Расширение датасета снимков, полученных из базы ПСО.
- Дообучение нейронных сетей, увеличение точности, разработка дополнительных нейронных сетей по отсутствующим на данный момент патологиям (субдуральное и эпидуральное кровоизлияния).
- Улучшение структуры сервиса по frontend-разработке. Реализация адаптивного интерфейса приложения.
- Реализация микросервисной архитектуры серверной части.
- Расширение функционала приложения: добавление возможности для врачей загружать не один срез головного мозга в формате jpeg, а полный файл стандарта DICOM. Разработка нейронных сетей по данным dcm-файлов.
- Добавление функционала: определение области поражения мозга (сегментация изображений), расчет объема кровоизлияния и смещения срединных структур.
- Развитие возможностей телемедицины: коммуникация врачей через сервис, отправка снимков и результатов диагностики приложения.
- Размещение приложения на закупленных серверах и создание домена сайта.
- Получение обратной связи от практикующих врачей: неврологов, нейрохирургов, КТ-диагностов и доработка приложения по их комментариям.
- Сертификация сервиса, клинические испытания.
- Распространение продукта в медицинских учреждениях.


### Перечень планируемых к приобретению ресурсов
- Google Colab Pro 9.99$ ~ 740 руб./мес
- Google Drive Pro 2 TB - 699 руб./мес
- Лицензия ПО RadiAnt DICOM Viewer для просмотра медицинских изображений стандарта DICOM PACS 129 eur. ~ 11953 руб. * 2шт = 23906 руб.
- Сервера 50-100$ / мес
- База данных Amazon AWS 120$ / мес.
- Домен 1800 руб. / год

____

1. World Health Organization. The top 10 causes of death - URL: https://www.who.int/news-room/fact-sheets/detail/the-top-10-causes-of-death
2. Jeffrey L. Saver. Time is Brain - Quantified. // AHA Journal V. 37 I. 1 (2006).
3. Qure Head CT - URL: https://qure.ai/headct.html
4. BrainScan - URL: https://brainscan.ai/en
5. Как нейросети от Лаборатории по ИИ Сбера помогают врачам определять инсульт и лечить пациентов с коронавирусом - URL: https://vc.ru/services/173165-kak-neyroseti-ot-laboratorii-po-ii-sbera-pomogayut-vracham-opredelyat-insult-i-lechit-pacientov-s-koronavirusom
6. Клинические рекомендации ассоциации нейрохирургов России - URL: https://ruans.org/Documents 


All the data used:
https://drive.google.com/file/d/1puvXfyNyHv23LyW4Z5QxTnzBGwMT8_gF/view?usp=sharing

Test files:
https://drive.google.com/drive/folders/1fw78lxpO3FEkv2PqDx1xFfAxIpHsS8La
 
