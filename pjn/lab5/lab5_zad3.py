#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from random import randint

def markow_dict_from_list(ngrams_list):
	tmplist = []
	markow_dict = {}
	for ng in ngrams_list:
		for i,j in enumerate(ngrams_list):
			if j==ng:
				if i+1<len(ngrams_list):
					tmplist.append(ngrams_list[i+1])
		markow_dict[ng] = tmplist
		tmplist = []
	return markow_dict
	
def get_ngram_list(ngram_size, sentence):
	sentence_vector = []
	splitted_sentences = sentence.split(" ")
	for sent in splitted_sentences:
		n=0
		while (n<len(sent)):
			if ' ' not in sent[n:n+ngram_size]:
				sentence_vector.append(sent[n:n+ngram_size])
				n=n+ngram_size
				#n=n+1
				pass
	return sentence_vector

def generate_word(first_ngram, markow_dict):
	word = first_ngram
	runner = ''
	while len(first_ngram) != len(runner):
		runner = get_one_for_word(markow_dict[first_ngram])
	for i in range(5):
		word = word + runner
		flag = 0
		while flag==0:
			runner = get_one_for_word(markow_dict[runner])
			if len(first_ngram) == len(runner):
				flag = 1
	return word
	
def get_one_for_word(list):
	if len(list) != 0:
		rand = randint(0,len(list)-1)
		out_list = list.pop(rand)
		return out_list
	else:
		return 'a'
	
sentence = u"Na początku XIII wieku książęta Władysław Odonic, Konrad mazowiecki, Mściwój I gdański[5], Leszek Biały i Henryk Brodaty prowadzili akcję chrystianizacyjną na terenach pogańskich Prus. Akcję misyjną prowadził opat zakonu cystersów w Łeknie i zakon rycerski braci dobrzyńskich, powołany w tym celu przez księcia Konrada. Akcje te – podobnie jak akcja biskupa Chrystiana w oparciu o fundację dobrowską – nie przyniosły jednak spodziewanych efektów.W tej sytuacji w 1226 roku książę mazowiecki Konrad zaprosił, za namową Jadwigi Śląskiej, na swoje ziemie zakon krzyżacki, oddając mu w dzierżawę ziemię chełmińską, gdzie zakon znalazł dogodną bazę do walk z plemionami Prusów, które zagrażały ciągłymi najazdami północnym rubieżom Mazowsza[6]. Cesarz Fryderyk II oraz papież Grzegorz IX oficjalnie zezwolili zakonowi założyć swoje własne księstwo na terenach odebranych Prusom. Formalnie Księstwo to miało stać się częścią Świętego Cesarstwa Rzymskiego i jednocześnie lennem książąt mazowieckich.Oprócz napływania kolejnych braci i kolonistów niemieckich[7], zakon otrzymał wsparcie papieża – wyprawy przeciw Prusom zyskały rangę krucjat, w których brali udział także polscy książęta. W 1235 do Krzyżaków przyłączyli się bracia dobrzyńscy[8], a w 1237 zakon kawalerów mieczowych zawarł z nimi sojusz polityczno-militarny, będący właściwie unią tych dwóch zakonówW XIII wieku stosunki polsko-krzyżackie były dobre, lecz wiek XIV – wraz ze wzrostem potęgi zakonu – przyniósł zmianę. Będąc królem Polski, Wacław II Czeski zawarł z Brandenburczykami umowę, na mocy której miał oddać Pomorze Gdańskie w zamian za Nową Marchię. Ostatecznie do zamiany nie doszło z powodu śmierci króla, jednak w 1308 Brandenburgia postanowiła skorzystać ze słabości państwa Władysława Łokietka i zajęła Pomorze[9]. Książę zmuszony był zwrócić się o pomoc do Krzyżaków, którzy wyparli najeźdźców. Za swoją pomoc zażądali jednak wysokiej zapłaty, przewyższającej wartość odbitych ziem. Wobec odmowy zapłaty przez Władysława zagarnęli całe Pomorze Gdańskie w 1309 roku. Osłabiona w tym czasie Polska, podzielona wciąż na dzielnice, nie była w stanie natychmiast przeciwstawić się agresji, co spowodowało utratę tych ziem na długie lata.W 1320 roku królem został Władysław I Łokietek, który wygrał proces z Krzyżakami przed sądem papieskim w Inowrocławiu. Wyrok z 1321 roku nakazał im zwrot Pomorza Gdańskiego Polsce, ale zakon, mimo polskich akcji dyplomatycznych i orzeczeń sądów papieskich, nie zamierzał zwrócić tych ziem[10].W 1331 doszło do zawarcia groźnego dla Polski sojuszu Jana Luksemburskiego z Krzyżakami. Ci ostatni, licząc na wspólną akcję pod Kaliszem, najechali kraj od północy. Łokietek postanowił zaatakować część ich sił. 27 września 1331 roku doszło do starcia pod Płowcami na Kujawach. Bitwa nie została jednoznacznie rozstrzygnięta, lecz to strona polska zrealizowała swój cel – kampania Krzyżaków na ziemiach polskich została przerwana. Jednak już 9 kwietnia 1332 roku zakon ponownie napadł na Polskę, zagarniając Kujawy i ziemię dobrzyńską.25 kwietnia 1333 na tronie polskim zasiadł syn poprzedniego króla, Kazimierz. Okazał się władcą niezwykle sprawnie poruszającym się w świecie dyplomacji. W 1335 doprowadził do I Zjazdu Wyszehradzkiego, na którym za cenę 20 tysięcy kop groszy praskich[11] oraz uznanie zwierzchności Jana Luksemburskiego nad Śląskiem, król Czech zrzekł się wszelkich praw do korony polskiej[12]. Oznaczało to ostateczne przekreślenie sojuszu czesko-krzyżackiego. Ponadto usiłowano rozstrzygnąć sprawę utraconych przez Polskę ziem – jednak ponieważ rezultaty nie zadowalały króla polskiego, zdecydował się on na oddanie sprawy pod sąd papieski. Wyrok z 16 września 1339 nakazywał zwrot Kujaw, ziemi dobrzyńskiej i Pomorza Gdańskiego. Był to już drugi wygrany przez stronę polską proces, ale Krzyżacy ponownie nie zgodzili się na oddanie zagrabionych ziem.Tymczasem zmarł książę Rusi Halickiej Bolesław Jerzy II, który przed śmiercią uczynił swym sukcesorem Kazimierza, co postawiło przed polską polityką zagraniczną nowe wyzwanie. Król musiał dokonać wyboru, gdyż Polska nie była wówczas na tyle silna, by podjąć się walki na dwóch frontach.Kazimierz Wielki uznał, że lepszym nabytkiem dla Korony byłoby uzyskanie terenów księstwa ruskiego, w związku z czym spór z zakonem należało załagodzić. W tych warunkach doszło w roku 1343 do zawarcia pokoju w Kaliszu, dzięki któremu zapewniony został rozejm, a Polska odzyskała Kujawy i ziemię dobrzyńską. Poza tym Kazimierz Wielki zachował tytuł władcy Pomorza Gdańskiego, co w przyszłości mogło stanowić podstawę do ewentualnych roszczeń ze strony polskiej[13].W 1397 na ziemiach zakonu powstała organizacja mająca bronić interesów lokalnego społeczeństwa przed uciskiem krzyżackim: Związek Jaszczurczy. Początkowo swoim zasięgiem obejmował jedynie ziemię chełmińską, z czasem jednak się rozrósł i stał się podstawą dla kolejnej struktury: Związku Pruskiego[14]. Kolejny kryzys we wzajemnych stosunkach nastąpił w 1401, tuż po zawarciu przez Królestwo Polskie i Wielkie Księstwo Litewskie unii wileńsko-radomskiej. Młodszy brat króla Władysława Jagiełły, Świdrygiełło, przeciwnik porozumienia polsko-litewskiego, stanął na czele buntu przeciw Witoldowi. Postanowił także poszukać wsparcia u Krzyżaków, którzy byli zainteresowani osłabieniem Litwy – jednak znów udało się zapobiec wojnie i w 1404 roku strony zawarły pokój w Raciążu, gdzie Witold przedstawił także polskie postulaty dotyczące kwestii utraconych ziem. Polska odkupiła ziemię dobrzyńską.Tymczasem powrócił problem Santoka i Drezdenka, gdy w 1402 roku zakon krzyżacki nabył Nową Marchię. Podporządkowanie sobie tych grodów przez państwo zakonne doprowadziło do utwardzenia stanowiska Polski w kwestiach krzyżacko-litewskich. Gdy wielkim mistrzem został zwolennik konfrontacyjnej polityki wobec Polski, Ulrich von Jungingen, wybuch wojny stał się już tylko kwestią czasu"
lvl = int(sys.argv[1])
list = get_ngram_list(lvl, sentence)
dict = markow_dict_from_list(list)
print generate_word(sys.argv[2], dict)