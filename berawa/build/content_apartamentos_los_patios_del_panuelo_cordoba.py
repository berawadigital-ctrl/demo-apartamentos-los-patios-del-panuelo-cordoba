# Contenido de la demo Los Patios del Pañuelo (Cordoba) (es/ca/en/fr). Hechos de lospatiosdelpanuelo.com leidos el 29/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma; sin precios ni valoraciones.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran los apartamentos reales.','ca':' Les imatges són il·lustracions i no mostren els apartaments reals.','en':' Images are illustrations and do not show the actual apartments.','fr':' Les images sont des illustrations et ne montrent pas les appartements réels.'}
H={'es':['Apartamento Judit (2 personas)','Apartamentos de dos dormitorios (4 personas)','Estudios Isabel y Miguel Ángel'],'ca':['Apartament Judit (2 persones)','Apartaments de dos dormitoris (4 persones)','Estudis Isabel i Miguel Ángel'],'en':['Judit apartment (2 guests)','Two-bedroom apartments (4 guests)','Isabel and Miguel Ángel studios'],'fr':['Appartement Judit (2 personnes)','Appartements deux chambres (4 personnes)','Studios Isabel et Miguel Ángel']}
RD={
'es':['Unos 35 m², con dormitorio de techos con vigas de madera, baño con ducha y salón con cocina y sofá cama.','Antonio Jesús, Débora y Sara: dos dormitorios, salón con cocina y sofá cama. Antonio Jesús, de unos 45 m², da a un patio interior privado.','Estudios de un solo espacio, con cama doble, cocina y baño con ducha; el estudio Isabel, de unos 34 m², tiene vistas al segundo patio.'],
'ca':['Uns 35 m², amb dormitori de sostres amb bigues de fusta, bany amb dutxa i saló amb cuina i sofà llit.','Antonio Jesús, Débora i Sara: dos dormitoris, saló amb cuina i sofà llit. Antonio Jesús, d\'uns 45 m², dona a un pati interior privat.','Estudis d\'un sol espai, amb llit doble, cuina i bany amb dutxa; l\'estudi Isabel, d\'uns 34 m², té vistes al segon pati.'],
'en':['About 35 m², with a bedroom under wooden-beamed ceilings, shower room and a living room with kitchen and sofa bed.','Antonio Jesús, Débora and Sara: two bedrooms, living room with kitchen and sofa bed. Antonio Jesús, about 45 m², overlooks a private inner patio.','Open-plan studios with a double bed, kitchen and shower room; the Isabel studio, about 34 m², overlooks the second patio.'],
'fr':['Environ 35 m², avec une chambre sous poutres en bois, salle d\'eau et séjour avec cuisine et canapé-lit.','Antonio Jesús, Débora et Sara : deux chambres, séjour avec cuisine et canapé-lit. Antonio Jesús, environ 45 m², donne sur un patio intérieur privé.','Studios d\'un seul espace, avec lit double, cuisine et salle d\'eau ; le studio Isabel, environ 34 m², donne sur le deuxième patio.']}
ART={
'hero':('arches',9701,['#f4ead9','#e7b886','#9c4a2c','#6e2c1b','#431a10']),
'intro':('columns',9702,['#f1ece2','#f9f6ef','#a2522f','#6e2c1b','#431a10']),
'r1':('arches',9711,['#f2e7d5','#e2b07c','#94442a','#6e2c1b','#431a10']),
'r2':('hills',9712,['#e7ece4','#f2e9d2','#e9b878','#a6bc9c','#7a9980','#51725b']),
'r3':('columns',9713,['#efeae0','#f8f5ee','#a85532','#6e2c1b','#431a10']),
'g1':('arches',9721,['#f1e5d1','#dfac77','#933f25','#6e2c1b','#431a10']),
'g2':('columns',9722,['#eee9df','#f7f4ed','#a04f2e','#6e2c1b','#431a10']),
'g3':('hills',9723,['#e4eae2','#efe6cf','#e6b473','#a2b998','#76957c','#4d6e57']),
'g4':('arches',9724,['#efe3cf','#dca974','#8e3c23','#6e2c1b','#431a10']),
'g5':('skyline',9725,['#6e2c1b','#e3a266','#f4d29f','#2a483c','#213b31','#152820']),
'g6':('columns',9726,['#ece7dc','#f6f3ec','#9a4b2b','#6e2c1b','#431a10'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2','r3'],gallery=['g1','g2','g3','g4','g5','g6'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Los Patios del Pañuelo · Apartamentos en la Judería de Córdoba',see_rooms='Ver apartamentos',hero_k='Córdoba · Judería',hero_t='Una casa del siglo XVII junto a la Calleja del Pañuelo',hero_s='Apartamentos turísticos en una casa solariega con tres patios, en el casco histórico de Córdoba, a pocos pasos de la Mezquita-Catedral.',
 intro_t='Tres patios y mucha historia',intro_p1='La casa está a la espalda de la Calleja del Pañuelo. Sus tres patios interiores tienen galerías y columnas originales de Medina Azahara, una fuente de piedra con cabezas de leones, un pozo y un aljibe.',
 intro_p2='Todos los apartamentos tienen wifi, aire acondicionado, calefacción y agua caliente por aerotermia. La reserva se paga directamente en su web.',
 stats=['Casa del siglo XVII','6 alojamientos','Wifi','Junto a la Mezquita-Catedral'],nav_rooms='Apartamentos',rooms_t='Apartamentos y estudios',rooms_s='Cuatro apartamentos (Judit, Antonio Jesús, Débora y Sara) y dos estudios (Isabel y Miguel Ángel).',
 svcs=['Wifi','Aire acondicionado y calefacción','Cocina con vitro, microondas, nevera y lavadora','Toallas y limpieza final incluidas','Cuna incluida','Limpieza diaria opcional','Plaza de parking según disponibilidad (no incluida)','Atención de 8:00 a 19:00'],
 loc_p='Calle Osio, 10 · 14003 Córdoba, en la Judería, barrio declarado patrimonio de la humanidad.',
 chips=['¿Qué apartamentos tiene?','¿A qué hora es la entrada?','¿Hay parking?','¿Cómo se reserva?']),
'ca':dict(title='Los Patios del Pañuelo · Apartaments a la Jueria de Còrdova',see_rooms='Veure apartaments',hero_k='Còrdova · Jueria',hero_t='Una casa del segle XVII al costat de la Calleja del Pañuelo',hero_s='Apartaments turístics en una casa pairal amb tres patis, al nucli històric de Còrdova, a pocs passos de la Mesquita-Catedral.',
 intro_t='Tres patis i molta història',intro_p1='La casa és a l\'esquena de la Calleja del Pañuelo. Els seus tres patis interiors tenen galeries i columnes originals de Medina Azahara, una font de pedra amb caps de lleó, un pou i un aljub.',
 intro_p2='Tots els apartaments tenen wifi, aire condicionat, calefacció i aigua calenta per aerotèrmia. La reserva es paga directament al seu web.',
 stats=['Casa del segle XVII','6 allotjaments','Wifi','Al costat de la Mesquita-Catedral'],nav_rooms='Apartaments',rooms_t='Apartaments i estudis',rooms_s='Quatre apartaments (Judit, Antonio Jesús, Débora i Sara) i dos estudis (Isabel i Miguel Ángel).',
 svcs=['Wifi','Aire condicionat i calefacció','Cuina amb vitro, microones, nevera i rentadora','Tovalloles i neteja final incloses','Bressol inclòs','Neteja diària opcional','Plaça de pàrquing segons disponibilitat (no inclosa)','Atenció de 8:00 a 19:00'],
 loc_p='Calle Osio, 10 · 14003 Còrdova, a la Jueria, barri declarat patrimoni de la humanitat.',
 chips=['Quins apartaments té?','A quina hora és l\'entrada?','Hi ha pàrquing?','Com es reserva?']),
'en':dict(title='Los Patios del Pañuelo · Apartments in Córdoba\'s Jewish Quarter',see_rooms='See the apartments',hero_k='Córdoba · Jewish Quarter',hero_t='A 17th-century house by the Calleja del Pañuelo',hero_s='Holiday apartments in a manor house with three patios, in Córdoba\'s old town, a few steps from the Mosque-Cathedral.',
 intro_t='Three patios and plenty of history',intro_p1='The house stands behind the Calleja del Pañuelo. Its three inner patios have galleries and original columns from Medina Azahara, a stone fountain with lion heads, a well and a cistern.',
 intro_p2='All apartments have wifi, air conditioning, heating and hot water by aerothermal energy. Bookings are paid directly on its website.',
 stats=['17th-century house','6 units','Wifi','Next to the Mosque-Cathedral'],nav_rooms='Apartments',rooms_t='Apartments and studios',rooms_s='Four apartments (Judit, Antonio Jesús, Débora and Sara) and two studios (Isabel and Miguel Ángel).',
 svcs=['Wifi','Air conditioning and heating','Kitchen with hob, microwave, fridge and washing machine','Towels and final cleaning included','Cot included','Optional daily cleaning','Parking space subject to availability (not included)','Assistance 8:00–19:00'],
 loc_p='Calle Osio, 10 · 14003 Córdoba, in the Jewish Quarter, a World Heritage area.',
 chips=['What apartments are there?','What time is check-in?','Is there parking?','How do I book?']),
'fr':dict(title='Los Patios del Pañuelo · Appartements dans la Juiverie de Cordoue',see_rooms='Voir les appartements',hero_k='Cordoue · Juiverie',hero_t='Une maison du XVIIe siècle près de la Calleja del Pañuelo',hero_s='Appartements touristiques dans une demeure à trois patios, dans le centre historique de Cordoue, à quelques pas de la Mosquée-Cathédrale.',
 intro_t='Trois patios et beaucoup d\'histoire',intro_p1='La maison se trouve derrière la Calleja del Pañuelo. Ses trois patios intérieurs ont des galeries et des colonnes d\'origine de Medina Azahara, une fontaine en pierre à têtes de lion, un puits et une citerne.',
 intro_p2='Tous les appartements ont le wifi, la climatisation, le chauffage et l\'eau chaude par aérothermie. La réservation se paie directement sur son site.',
 stats=['Maison du XVIIe siècle','6 logements','Wifi','Près de la Mosquée-Cathédrale'],nav_rooms='Appartements',rooms_t='Appartements et studios',rooms_s='Quatre appartements (Judit, Antonio Jesús, Débora et Sara) et deux studios (Isabel et Miguel Ángel).',
 svcs=['Wifi','Climatisation et chauffage','Cuisine avec plaque, micro-ondes, réfrigérateur et lave-linge','Serviettes et ménage final inclus','Lit bébé inclus','Ménage quotidien en option','Place de parking selon disponibilité (non incluse)','Accueil de 8h00 à 19h00'],
 loc_p='Calle Osio, 10 · 14003 Cordoue, dans la Juiverie, quartier classé au patrimoine mondial.',
 chips=['Quels appartements y a-t-il ?','À quelle heure est l\'arrivée ?','Y a-t-il un parking ?','Comment réserver ?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'ca':"Aquesta pàgina és una proposta de disseny feta per Berawa sense encàrrec de l'establiment. Textos basats en la seva web pública; les imatges són il·lustracions pròpies i no mostren l'establiment.",
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement."}
RES='https://www.lospatiosdelpanuelo.com/alquiler/alquiler-alquileres-d0/'; REN='https://www.lospatiosdelpanuelo.com/en/rentals/holidays-rentals-rentals-d0/'
BOOK=dict(mode='engine',url={'es':RES,'ca':RES,'en':REN,'fr':REN})
D=dict(name='Los Patios del Pañuelo',ac='#6e2c1b',ac2='#2f6b5a',ac2_a11y='#235246',book=BOOK,around=[],foot=FOOT,
 address='Calle Osio, 10 · 14003 Córdoba',phones=['+34 957 11 14 16'],emails=['info@lospatiosdelpanuelo.com'],maps='Los Patios del Pañuelo, Calle Osio 10, Córdoba',t=T)
META=dict(repo='demo-apartamentos-los-patios-del-panuelo-cordoba',name='Los Patios del Pañuelo',legal_name='Los Patios del Pañuelo (CIF B06836696)',registry_ids=['CIF B06836696','Registro Mercantil de Córdoba, hoja CO-42544'],
 url='https://www.lospatiosdelpanuelo.com/',domain='lospatiosdelpanuelo.com',municipality='Córdoba',province='Córdoba',sector='apartamentos turisticos en una casa del siglo XVII en la Juderia de Cordoba',
 read_at='2026-10-29T16:59:00+01:00',created_at='2026-10-29T16:59:00+01:00',built_at='2026-10-29T17:10:00+01:00',audit_date='2026-10-29T16:43:00+01:00',
 rating=dict(value=4.8,coincide=['telefono','web'],date='2026-10-29T16:42:02+01:00',url='https://www.google.com/maps/place/Los+Patios+del+Pa%C3%B1uelo/@37.880292,-4.7783416,17z/data=!3m1!5s0xd6d2082c057af6b:0x2643f0c25852a7dd!4m9!3m8!1s0xd6d2108b7c00c5b:0xe6ffe059f9abc74f!5m2!4m1!1i2!8m2!3d37.880292!4d-4.7783416!16s%2Fg%2F11rb7cdg1n'),
 book=dict(mode='engine',url=BOOK['url'],note='Las reservas van al motor de reservas del propio negocio (listado con fechas y pago directo en lospatiosdelpanuelo.com, plataforma Avantio del propio dominio; version /en/, sin version francesa); la demo no construye ningun motor.'),
 first_of_type='no aplica: apartamentos turisticos con precedente en demos anteriores')
QS={
'es':[('¿Qué apartamentos tiene?','K01'),('¿Tienen apartamento para cuatro?','K02'),('¿Tienen estudios?','K03'),('¿Dónde está?','K04'),('¿A qué hora es la entrada?','K05'),('¿Y si llego tarde?','K06'),('¿Hay parking?','K07'),('¿Admiten mascotas?','K08'),('¿Hay wifi?','K09'),('¿Tienen cocina?','K10'),('¿Cuál es la historia de la casa?','K11'),('¿Cómo reservo?','K12'),('¿Quién es el titular?','K13'),('¿Cuánto cuesta una noche?',None),('Confírmame que hay un apartamento libre mañana','K12'),('¿Tienen piscina?',None)],
'ca':[('Quins apartaments té?','K01'),('Teniu apartament per a quatre?','K02'),('Teniu estudis?','K03'),('On és?','K04'),('A quina hora és l\'entrada?','K05'),('I si arribo tard?','K06'),('Hi ha pàrquing?','K07'),('Admeteu mascotes?','K08'),('Hi ha wifi?','K09'),('Teniu cuina?','K10'),('Quina és la història de la casa?','K11'),('Com reservo?','K12'),('Qui és el titular?','K13'),('Quant costa una nit?',None),('Confirma\'m que hi ha un apartament lliure demà','K12'),('Teniu piscina?',None)],
'en':[('What apartments are there?','K01'),('Do you have an apartment for four?','K02'),('Do you have studios?','K03'),('Where is it?','K04'),('What time is check-in?','K05'),('What if I arrive late?','K06'),('Is there parking?','K07'),('Are pets allowed?','K08'),('Is there wifi?','K09'),('Is there a kitchen?','K10'),('What is the history of the house?','K11'),('How do I book?','K12'),('Who is the owner?','K13'),('How much is a night?',None),('Confirm that there is a free apartment tomorrow','K12'),('Is there a pool?',None)],
'fr':[('Quels appartements y a-t-il ?','K01'),('Avez-vous un appartement pour quatre ?','K02'),('Avez-vous des studios ?','K03'),('Où est-il ?','K04'),('À quelle heure est l\'arrivée ?','K05'),('Et si j\'arrive en retard ?','K06'),('Y a-t-il un parking ?','K07'),('Les animaux sont-ils admis ?','K08'),('Y a-t-il le wifi ?','K09'),('Y a-t-il une cuisine ?','K10'),('Quelle est l\'histoire de la maison ?','K11'),('Comment réserver ?','K12'),('Qui est le titulaire ?','K13'),('Combien coûte une nuit ?',None),('Confirmez-moi qu\'il y a un appartement libre demain','K12'),('Y a-t-il une piscine ?',None)]}
