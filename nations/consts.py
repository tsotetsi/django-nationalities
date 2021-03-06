from django.utils.translation import ugettext_lazy as _

# source(s):
#   - http://29lt.com/api/settings/home
#   - https://www.englishclub.com/vocabulary/world-countries-nationality.htm
#   - https://en.wikipedia.org/wiki/ISO_3166-1

COUNTRIES = (
    ("AF", _("Afghanistan")),
    ("AL", _("Albania")),
    ("DZ", _("Algeria")),
    ("AS", _("American Samoa")),
    ("AD", _("Andorra")),
    ("AO", _("Angola")),
    ("AI", _("Anguilla")),
    ("AQ", _("Antarctica")),
    ("AG", _("Antigua And Barbuda")),
    ("AR", _("Argentina")),
    ("AM", _("Armenia")),
    ("AW", _("Aruba")),
    ("AU", _("Australia")),
    ("AT", _("Austria")),
    ("AZ", _("Azerbaijan")),
    ("BS", _("Bahamas")),
    ("BH", _("Bahrain")),
    ("BD", _("Bangladesh")),
    ("BB", _("Barbados")),
    ("BY", _("Belarus")),
    ("BE", _("Belgium")),
    ("BZ", _("Belize")),
    ("BJ", _("Benin")),
    ("BM", _("Bermuda")),
    ("BT", _("Bhutan")),
    ("BO", _("Bolivia")),
    ("BA", _("Bosnia And Herzegovina")),
    ("BW", _("Botswana")),
    ("BV", _("Bouvet Island")),
    ("BR", _("Brazil")),
    ("IO", _("British Indian Ocean Territory")),
    ("BN", _("Brunei Darussalam")),
    ("BG", _("Bulgaria")),
    ("BF", _("Burkina Faso")),
    ("BI", _("Burundi")),
    ("KH", _("Cambodia")),
    ("CM", _("Cameroon")),
    ("CA", _("Canada")),
    ("CV", _("Cape Verde")),
    ("KY", _("Cayman Islands")),
    ("CF", _("Central African Republic")),
    ("TD", _("Chad")),
    ("CL", _("Chile")),
    ("CN", _("China")),
    ("CX", _("Christmas Island")),
    ("CC", _("Cocos (keeling) Islands")),
    ("CO", _("Colombia")),
    ("KM", _("Comoros")),
    ("CG", _("Congo")),
    ("CD", _("Congo (Democratic Republic of the Congo)")),
    ("CK", _("Cook Islands")),
    ("CR", _("Costa Rica")),
    ("CI", _("Cote D'ivoire")),
    ("HR", _("Croatia")),
    ("CU", _("Cuba")),
    ("CY", _("Cyprus")),
    ("CZ", _("Czech Republic")),
    ("DK", _("Denmark")),
    ("DJ", _("Djibouti")),
    ("DM", _("Dominica")),
    ("DO", _("Dominican Republic")),
    ("EC", _("Ecuador")),
    ("EG", _("Egypt")),
    ("SV", _("El Salvador")),
    ("GQ", _("Equatorial Guinea")),
    ("ER", _("Eritrea")),
    ("EE", _("Estonia")),
    ("ET", _("Ethiopia")),
    ("FK", _("Falkland Islands (malvinas)")),
    ("FO", _("Faroe Islands")),
    ("FJ", _("Fiji")),
    ("FI", _("Finland")),
    ("FR", _("France")),
    ("GF", _("French Guiana")),
    ("PF", _("French Polynesia")),
    ("TF", _("French Southern Territories")),
    ("GA", _("Gabon")),
    ("GM", _("Gambia")),
    ("GE", _("Georgia")),
    ("DE", _("Germany")),
    ("GH", _("Ghana")),
    ("GI", _("Gibraltar")),
    ("GR", _("Greece")),
    ("GL", _("Greenland")),
    ("GD", _("Grenada")),
    ("GP", _("Guadeloupe")),
    ("GU", _("Guam")),
    ("GT", _("Guatemala")),
    ("GN", _("Guinea")),
    ("GW", _("Guinea-bissau")),
    ("GY", _("Guyana")),
    ("HT", _("Haiti")),
    ("HM", _("Heard Island And Mcdonald Islands")),
    ("VA", _("Holy See (Vatican City State)")),
    ("HN", _("Honduras")),
    ("HK", _("Hong Kong")),
    ("HU", _("Hungary")),
    ("IS", _("Iceland")),
    ("IN", _("India")),
    ("ID", _("Indonesia")),
    ("IR", _("Iran, Islamic Republic of Iran")),
    ("IQ", _("Iraq")),
    ("IE", _("Ireland")),
    ("IM", _("Isle of Man")),
    ("IL", _("Israel")),
    ("IT", _("Italy")),
    ("JM", _("Jamaica")),
    ("JP", _("Japan")),
    ("JE", _("Jersey")),
    ("JO", _("Jordan")),
    ("KZ", _("Kazakstan")),
    ("KE", _("Kenya")),
    ("KI", _("Kiribati")),
    ("KV", _("Kosovo")),
    ("KW", _("Kuwait")),
    ("KG", _("Kyrgyzstan")),
    ("LA", _("Lao People's Democratic Republic")),
    ("LV", _("Latvia")),
    ("LB", _("Lebanon")),
    ("LS", _("Lesotho")),
    ("LR", _("Liberia")),
    ("LY", _("Libyan Arab Jamahiriya")),
    ("LI", _("Liechtenstein")),
    ("LT", _("Lithuania")),
    ("LU", _("Luxembourg")),
    ("MO", _("Macau")),
    ("MK", _("Republic of Macedonia")),
    ("MG", _("Madagascar")),
    ("MW", _("Malawi")),
    ("MY", _("Malaysia")),
    ("MV", _("Maldives")),
    ("ML", _("Mali")),
    ("MT", _("Malta")),
    ("MH", _("Marshall Islands")),
    ("MQ", _("Martinique")),
    ("MR", _("Mauritania")),
    ("MU", _("Mauritius")),
    ("YT", _("Mayotte")),
    ("MX", _("Mexico")),
    ("FM", _("Micronesia (Federated States of Micronesia)")),
    ("MD", _("Moldova (Republic of Moldova)")),
    ("MC", _("Monaco")),
    ("MN", _("Mongolia")),
    ("ME", _("Montenegro")),
    ("MS", _("Montserrat")),
    ("MA", _("Morocco")),
    ("MZ", _("Mozambique")),
    ("MM", _("Republic of the Union of Myanmar (Burma)")),
    ("NA", _("Namibia")),
    ("NR", _("Nauru")),
    ("NP", _("Nepal")),
    ("NL", _("Netherlands")),
    ("NC", _("New Caledonia")),
    ("NZ", _("New Zealand")),
    ("NI", _("Nicaragua")),
    ("NE", _("Niger")),
    ("NG", _("Nigeria")),
    ("NU", _("Niue")),
    ("NF", _("Norfolk Island")),
    ("KP", _("North Korea (Democratic People's Republic of Korea)")),
    ("MP", _("Northern Mariana Islands")),
    ("NO", _("Norway")),
    ("OM", _("Oman")),
    ("PK", _("Pakistan")),
    ("PW", _("Palau")),
    ("PS", _("Palestine")),
    ("PA", _("Panama")),
    ("PG", _("Papua New Guinea")),
    ("PY", _("Paraguay")),
    ("PE", _("Peru")),
    ("PH", _("Philippines")),
    ("PN", _("Pitcairn")),
    ("PL", _("Poland")),
    ("PT", _("Portugal")),
    ("PR", _("Puerto Rico")),
    ("QA", _("Qatar")),
    ("RE", _("Reunion")),
    ("RO", _("Romania")),
    ("RU", _("Russian Federation")),
    ("RW", _("Rwanda")),
    ("BL", _("Saint Barthelemy")),
    ("SH", _("Saint Helena")),
    ("KN", _("Saint Kitts And Nevis")),
    ("LC", _("Saint Lucia")),
    ("MF", _("Saint Martin")),
    ("PM", _("Saint Pierre And Miquelon")),
    ("VC", _("Saint Vincent And The Grenadines")),
    ("WS", _("Samoa")),
    ("SM", _("San Marino")),
    ("ST", _("Sao Tome And Principe")),
    ("SA", _("Saudi Arabia")),
    ("SN", _("Senegal")),
    ("RS", _("Serbia")),
    ("SC", _("Seychelles")),
    ("SL", _("Sierra Leone")),
    ("SG", _("Singapore")),
    ("SK", _("Slovakia")),
    ("SI", _("Slovenia")),
    ("SB", _("Solomon Islands")),
    ("SO", _("Somalia")),
    ("ZA", _("South Africa")),
    ("GS", _("South Georgia And The South Sandwich Islands")),
    ("KR", _("South Korea (Republic of Korea)")),
    ("SS", _("South Sudan")),
    ("ES", _("Spain")),
    ("LK", _("Sri Lanka")),
    ("PM", _("St. Pierre and Miquelon")),
    ("SD", _("Sudan")),
    ("SR", _("Suriname")),
    ("SJ", _("Svalbard And Jan Mayen Island")),
    ("SZ", _("Swaziland")),
    ("SE", _("Sweden")),
    ("CH", _("Switzerland")),
    ("SY", _("Syrian Arab Republic")),
    ("TW", _("Taiwan, Province Of China")),
    ("TJ", _("Tajikistan")),
    ("TZ", _("United Republic of Tanzania")),
    ("TH", _("Thailand")),
    ("TL", _("Timor-Leste")),
    ("TG", _("Togo")),
    ("TK", _("Tokelau")),
    ("TO", _("Tonga")),
    ("TT", _("Trinidad And Tobago")),
    ("TN", _("Tunisia")),
    ("TR", _("Turkey")),
    ("TM", _("Turkmenistan")),
    ("TC", _("Turks And Caicos Islands")),
    ("TV", _("Tuvalu")),
    ("UG", _("Uganda")),
    ("UA", _("Ukraine")),
    ("AE", _("United Arab Emirates")),
    ("GB", _("United Kingdom")),
    ("UM", _("United States Minor Outlying Islands")),
    ("US", _("United States of America")),
    ("UY", _("Uruguay")),
    ("UZ", _("Uzbekistan")),
    ("VU", _("Vanuatu")),
    ("VE", _("Venezuela")),
    ("VN", _("Viet Nam")),
    ("VG", _("Virgin Islands, British")),
    ("VI", _("Virgin Islands, U.S")),
    ("WF", _("Wallis And Futuna")),
    ("EH", _("Western Sahara")),
    ("YE", _("Yemen")),
    ("ZM", _("Zambia")),
    ("ZW", _("Zimbabwe")),
)

NATIONALITIES = (
    ("AF", _("Afghan")),
    ("AL", _("Albanian")),
    ("DZ", _("Algerian")),
    ("AS", _("American Samoa")),
    ("AD", _("Andorran")),
    ("AO", _("Angolan")),
    ("AI", _("Anguillian")),
    ("AQ", _("None")),
    ("AG", _("Antiguan or Barbudan")),
    ("AR", _("Argentinian")),
    ("AM", _("Armenian")),
    ("AW", _("Dutch")),
    ("AU", _("Australian")),
    ("AT", _("Austrian")),
    ("AZ", _("Azerbaijani")),
    ("BS", _("Bahamian")),
    ("BH", _("Bahraini")),
    ("BD", _("Bangladeshi")),
    ("BB", _("Barbadian")),
    ("BY", _("Belarusian or Belarusan")),
    ("BE", _("Belgian")),
    ("BZ", _("Belizean")),
    ("BJ", _("Beninese")),
    ("BM", _("Bermudian")),
    ("BT", _("Bhutanese")),
    ("BO", _("Bolivian")),
    ("BA", _("Bosnian")),
    ("BW", _("Botswanan")),
    ("BV", _("None")),
    ("BR", _("Brazilian")),
    ("IO", _("None")),
    ("BN", _("Bruneian")),
    ("BG", _("Bulgarian")),
    ("BF", _("Burkinabe")),
    ("BI", _("Burundian")),
    ("KH", _("Cambodian")),
    ("CM", _("Cameroonian")),
    ("CA", _("Canadian")),
    ("CV", _("Cape Verdean")),
    ("KY", _("Caymanian")),
    ("CF", _("Central African")),
    ("TD", _("Chadian")),
    ("CL", _("Chilean")),
    ("CN", _("Chinese")),
    ("CX", _("Christmas Islande")),
    ("CC", _("Cocos Islander")),
    ("CO", _("Colombian")),
    ("KM", _("Comorian")),
    ("CG", _("Congolese")),
    ("CD", _("Congolese")),
    ("CK", _("Cook Islander")),
    ("CR", _("Costa Rican")),
    ("CI", _("Ivorian")),
    ("HR", _("Croatian")),
    ("CU", _("Cuban")),
    ("CY", _("Cypriot")),
    ("CZ", _("Czech")),
    ("DK", _("Danish")),
    ("DJ", _("Djiboutian")),
    ("DM", _("Dominican")),
    ("DO", _("Dominican")),
    ("EC", _("Ecuadorean")),
    ("EG", _("Egyptian")),
    ("SV", _("Salvadorean")),
    ("GQ", _("Equatorial Guinean")),
    ("ER", _("Eritrean")),
    ("EE", _("Estonian")),
    ("ET", _("Ethiopian")),
    ("FK", _("Falkland Islander")),
    ("FO", _("Faroese")),
    ("FJ", _("Fijian")),
    ("FI", _("Finnish")),
    ("FR", _("French")),
    ("GF", _("French Guianese")),
    ("PF", _("French Polynesian")),
    ("TF", _("French")),
    ("GA", _("Gabonese")),
    ("GM", _("Gambian")),
    ("GE", _("Georgian")),
    ("DE", _("German")),
    ("GH", _("Ghanaian")),
    ("GI", _("Gibralterian")),
    ("GR", _("Greek")),
    ("GL", _("Greenlander")),
    ("GD", _("Grenadian")),
    ("GP", _("Guadeloupean")),
    ("GU", _("Guamanian")),
    ("GT", _("Guatemalan")),
    ("GN", _("Guinean")),
    ("GW", _("Guinean")),
    ("GY", _("Guyanese")),
    ("HT", _("Haitian")),
    ("HM", _("Heard and McDonald Islands")),
    ("VA", _(" Vatican")),
    ("HN", _("Honduran")),
    ("HK", _("Hong Konger")),
    ("HU", _("Hungarian")),
    ("IS", _("Icelander")),
    ("IN", _("Indian")),
    ("ID", _("Indonesian")),
    ("IR", _("Iranian")),
    ("IQ", _("Iraqi")),
    ("IE", _("Irish")),
    ("IM", _("Manx")),
    ("IL", _("Israeli")),
    ("IT", _("Italian")),
    ("JM", _("Jamaican")),
    ("JP", _("Japanese")),
    ("JE", _("Jersey")),
    ("JO", _("Jordanian")),
    ("KZ", _("Kazakhstani")),
    ("KE", _("Kenyan")),
    ("KI", _("I-Kiribati")),
    ("KV", _("Kosovan")),
    ("KW", _("Kuwaiti")),
    ("KG", _("Kyrgyzstani")),
    ("LA", _("Laotian")),
    ("LV", _("Latvian")),
    ("LB", _("Lebanese")),
    ("LS", _("Mosotho")),
    ("LR", _("Liberian")),
    ("LY", _("Libyan")),
    ("LI", _("Liechtensteiner")),
    ("LT", _("Lithunian")),
    ("LU", _("Luxembourger")),
    ("MO", _("Macanese")),
    ("MK", _("Macedonian")),
    ("MG", _("Malagasy")),
    ("MW", _("Malawian")),
    ("MY", _("Malaysian")),
    ("MV", _("Maldivan")),
    ("ML", _("Malian")),
    ("MT", _("Maltese")),
    ("MH", _("Marshallese")),
    ("MQ", _("Martinican")),
    ("MR", _("Mauritanian")),
    ("MU", _("Mauritian")),
    ("YT", _("Mahoran")),
    ("MX", _("Mexican")),
    ("FM", _("Micronesian")),
    ("MD", _("Moldovan")),
    ("MC", _("Monacan")),
    ("MN", _("Mongolian")),
    ("ME", _("Montenegrin")),
    ("MS", _("Montserratian")),
    ("MA", _("Moroccan")),
    ("MZ", _("Mozambican")),
    ("MM", _("Myanmarese")),
    ("NA", _("Namibian")),
    ("NR", _("Nauruan")),
    ("NP", _("Nepalese")),
    ("NL", _("Dutch")),
    ("NC", _("New Caledonian")),
    ("NZ", _("New Zealander")),
    ("NI", _("Nicaraguan")),
    ("NE", _("Nigerien")),
    ("NG", _("Nigerian")),
    ("NU", _("Niuean")),
    ("NF", _("Norfolk Islander")),
    ("KP", _("North Korean")),
    ("MP", _("")),
    ("NO", _("Norwegian")),
    ("OM", _("Omani")),
    ("PK", _("Pakistani")),
    ("PW", _("Palauan")),
    ("PS", _("Palestinian")),
    ("PA", _("Panamanian")),
    ("PG", _("Papua New Guinean")),
    ("PY", _("Paraguayan")),
    ("PE", _("Peruvian")),
    ("PH", _("Filipino")),
    ("PN", _("Pitcairn Islande")),
    ("PL", _("Polish")),
    ("PT", _("Portuguese")),
    ("PR", _("Puerto Rica")),
    ("QA", _("Qatari")),
    ("RE", _("Reunion")),
    ("RO", _("Romanian")),
    ("RU", _("Russian")),
    ("RW", _("Rwandan")),
    ("BL", _("Barthelemois")),
    ("SH", _("Saint Helenian")),
    ("KN", _("Kittian")),
    ("LC", _("Saint Lucian")),
    ("MF", _("French")),
    ("PM", _("French")),
    ("VC", _("Saint Vincentian")),
    ("WS", _("Samoan")),
    ("SM", _("Sanmarinese")),
    ("ST", _("Sao Tomean")),
    ("SA", _("Saudi Arabian")),
    ("SN", _("Senegalese")),
    ("RS", _("Serbian")),
    ("SC", _("Seychellois")),
    ("SL", _("Sierra Leonean")),
    ("SG", _("Singaporean")),
    ("SK", _("Slovakian")),
    ("SI", _("Slovenian")),
    ("SB", _("Solomon Islander")),
    ("SO", _("Somali")),
    ("ZA", _("South African")),
    ("GS", _("South Georgia and the South Sandwich Islands")),
    ("KR", _("South Korean")),
    ("SS", _("South Sudanese")),
    ("ES", _("Spanish")),
    ("LK", _("Sri Lankan")),
    ("PM", _("Saint-Pierrais")),
    ("SD", _("Sudanese")),
    ("SR", _("Surinamese")),
    ("SJ", _("Svalbard and Jan Mayen Islands")),
    ("SZ", _("Swazi")),
    ("SE", _("Swedish")),
    ("CH", _("Swiss")),
    ("SY", _("Syrian")),
    ("TW", _("Taiwanese")),
    ("TJ", _("Tajikistani")),
    ("TZ", _("Tanzanian")),
    ("TH", _("Thai")),
    ("TL", _("Timorese")),
    ("TG", _("Togolese")),
    ("TK", _("Tokelauan")),
    ("TO", _("Tongan")),
    ("TT", _("Trinidadian")),
    ("TN", _("Tunisian")),
    ("TR", _("Turkish")),
    ("TM", _("Turkmen")),
    ("TC", _("Turks and Caicos Islander")),
    ("TV", _("Tuvaluan")),
    ("UG", _("Ugandan")),
    ("UA", _("Ukrainian")),
    ("AE", _("Emirian")),
    ("GB", _("British")),
    ("UM", _("American")),
    ("US", _("American")),
    ("UY", _("Uruguayan")),
    ("UZ", _("Uzbekistani")),
    ("VU", _("Ni-Vanuatu")),
    ("VE", _("Venezuelan")),
    ("VN", _("Vietnamese")),
    ("VG", _("British Virgin Islander")),
    ("VI", _("None")),
    ("WF", _("Wallisian")),
    ("EH", _("Western Saharan")),
    ("YE", _("Yemeni")),
    ("ZM", _("Zambian")),
    ("ZW", _("Zimbabwean")),
)
