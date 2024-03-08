API_URL_DATA = ".renoweb.dk/Legacy/JService.asmx/GetAffaldsplanMateriel_mitAffald"
API_URL_SEARCH = ".renoweb.dk/Legacy/JService.asmx/Adresse_SearchByString"

NON_SUPPORTED_ITEMS = [
    "Asbest",
    "Beholderservice",
    "Bestillerordning",
    "Henteordning for grene",
]

SUPPORTED_ITEMS = {
    "restaffaldmadaffald": [
        "Restaffald-Madaffald",
        "Rest/mad",
        "Restaffald",
        "Rest - Mad",
        "Rest-/Madaffald",
        "Mad- og restaffald",
        "Mad/rest",
        "Rest-/madaffald",
        "Mad/Rest",
        "Mad og restaffald",
        "Mad-/ og restaffald",
        "Rest / Mad",
        "Rest Mad",
        "Energispand - Obligatorisk min. 1 spand",
        "Rest/madaffald",
        "Energibeholder (mad/rest)",
        "Rest- og Madaffald",
    ],
    "dagrenovation": ["Dagrenovation"],
    "glas": ["Industri Genbrugeligt"],
    "metalglas": ["Glas og metal", "Metal-Glas", "Glas/Metal", "Metal og Glas"],
    "pappi": [
        "Plast MDK og papir",
        "PAPPI",
        "Plast/MD-karton/PP",
        "Plast/Papir",
        "Papir/Plast og kartoner",
        "Plast og Mad- & drikkekartoner/Papir",
        "Plast, Metal, MDK",
    ],
    "farligtaffald": [
        "Farligt affald",
        "Miljøkasser",
        "Farligt Affald, Rød boks",
        "Genbrugsbilen",
    ],
    "farligtaffaldmiljoboks": ["Farligt affald/Miljøboks", "Papir og glas/dåser"],
    "flis": ["Flis", "Flishugning"],
    "genbrug": [
        "Tekstiler",
        "Genbrug",
        "Genbrugsøer",
        "Genanvendeligt",
        "Genbrug 240 L",
    ],
    "jern": ["Jern"],
    "papir": ["Papir", "Papir 660 L"],
    "papirmetal": ["Papir & Metal", "Papir/metal", "Metal/papir", "Papir og Metal"],
    "pap": ["Pap"],
    "plastmetal": [
        "Plast & Metal",
        "Plast, metal & MDK 660L",
        "Plast/ Metal",
        "Plast/MDK/Metal",
        "Plast-metal",
        "Plast/Metal",
    ],
    "storskrald": [
        "Storskrald",
        "Stort elektronik",
        "Storskrald og genbrug",
        "Pap og Storskrald",
    ],
    "storskraldogtekstilaffald": ["Storskrald og tekstilaffald"],
    "haveaffald": [
        "Haveaffald, flishugning",
        "Haveaffald",
        "Trærødder og stammer",
        "Haveaffald - Frivilligt",
        "Haveaffald 140 L",
    ],
    "papirglas": ["Papir og pap/Glas", "Glas-papir", "Papir, Pap/Glas"],
    "plastmadkarton": [
        "Plast/MDK",
        "Plast & mad- og drikkekartoner",
        "Plast/ Mad- og drikkekartoner",
        "Plast og MDK",
    ],
    "pappapirglasmetal": [
        "Pap, papir, tekstil & metal og glas",
        "4delt beholder",
        "Ressourcebeholder (pap/papir og glas/metal)",
    ],
    "plastmetalmadmdk": ["Plast/Metal/Mad- & drikkekartoner"],
    "pappapir": ["Pap/Papir", "Papir/Pap", "Papir og Pap"],
    "tekstil": ["Standplads", "Tekstilaffald", "Miljøkasse/tekstiler", "Tekstil"],
    "glasplast": ["Glas/Plast og MDK"],
    "plastmetalpapir": [
        "Plast/Metal/Papir ",
        "Genbrugsspand - Obligatorisk min. 1 spand",
    ],
    "plast": ["Plast - Obligatorisk min. 1 spand", "Plast"],
}

MATERIAL_LIST = {
    "restaffaldmadaffald": "Restaffald-Madaffald",
    "dagrenovation": "Dagrenovation",
    "glas": "Glas",
    "metalglas": ["Glas/metal (1 stk.)",],
    "pappi": ["Plast/papir (1 stk.)",],
    "farligtaffald": "Farligt affald",
    "farligtaffaldmiljoboks": "Farligt affald & Miljøboks",
    "flis": "Flis",
    "genbrug": "Genbrug",
    "jern": "Jern",
    "papir": "Papir",
    "papirmetal": "Papir-Metal",
    "pap": ["Pap 240 L (villa) (1 stk.)",],
    "plastmetal": "Plast-Metal",
    "storskrald": "Storskrald",
    "storskraldogtekstilaffald": "Storskrald & Tekstilaffald",
    "haveaffald": "Haveaffald",
    "papirglas": "Papir-Glas",
    "plastmadkarton": "Plast-Madkarton",
    "pappapirglasmetal": "Papir-Pap-Glas-Metal",
    "plastmetalmadmdk": "Plast-Metal-Madkarton",
    "pappapir": "Pap-Papir",
    "tekstil": "Tekstilaffald",
    "glasplast": "Glas-Plast",
    "plastmetalpapir": "Plast-Metal-Papir",
    "plast": "Plast",
}

ICON_LIST = {
    "restaffaldmadaffald": "mdi:trash-can",
    "dagrenovation": "mdi:trash-can",
    "glas": "liquor",
    "metalglas": "mdi:glass-fragile",
    "pappi": "mdi:recycle",
    "farligtaffald": "mdi:biohazard",
    "farligtaffaldmiljoboks": "mdi:biohazard",
    "flis": "mdi:tree",
    "genbrug": "mdi:recycle",
    "jern": "mdi:bucket",
    "papir": "mdi:file",
    "papirmetal": "mdi:delete-empty",
    "pap": "mdi:note",
    "plastmetal": "mdi:trash-can-outline",
    "storskrald": "mdi:table-furniture",
    "storskraldogtekstilaffald": "mdi:table-furniture",
    "haveaffald": "mdi:leaf",
    "papirglas": "mdi:greenhouse",
    "plastmadkarton": "mdi:trash-can",
    "pappapirglasmetal": "mdi:trash-can",
    "plastmetalmadmdk": "mdi:trash-can",
    "pappapir": "mdi:file",
    "tekstil": "mdi:recycle",
    "glasplast": "mdi:trash-can",
    "plastmetalpapir": "mdi:trash-can",
    "plast": "mdi:trash-can",
}

NAME_LIST = {
    "restaffaldmadaffald": "Rest & Madaffald",
    "dagrenovation": "Dagrenovation",
    "glas": "Glas",
    "metalglas": "Metal & Glas",
    "pappi": "Papir & Plast",
    "farligtaffald": "Farligt affald",
    "farligtaffaldmiljoboks": "Farligt affald & Miljøboks",
    "flis": "Flis",
    "genbrug": "Genbrug",
    "jern": "Jern",
    "papir": "Papir",
    "papirmetal": "Papir & Metal",
    "pap": "Pap",
    "plastmetal": "Plast & Metal",
    "storskrald": "Storskrald",
    "storskraldogtekstilaffald": "Storskrald & Tekstilaffald",
    "haveaffald": "Haveaffald",
    "papirglas": "Papir, Pap & Glas",
    "plastmadkarton": "Plast & Madkarton",
    "pappapirglasmetal": "Pap, Papir, Glas & Metal",
    "plastmetalmadmdk": "Plast, Metal, Mad & Drikkekartoner",
    "pappapir": "Pap & Papir",
    "tekstil": "Tekstilaffald",
    "glasplast": "Glas, Plast & Madkartoner",
    "plastmetalpapir": "Plast, Metal & Papir",
    "plast": "Plast",
}
NAME_ARRAY = list(NAME_LIST.keys())

SPECIAL_MUNICIPALITIES_LIST = [
    "allerod",
    "egedal",
    "randers",
    "rudersdal",
]

MUNICIPALITIES_LIST = {
    "Aabenraa": "aabenraa",
    "Aalborg": "aalborg",
    "Albertslund": "albertslund",
    "Allerød": "allerod",
    "Brøndby": "brondby",
    "Brønderslev": "bronderslev",
    "Dragør": "dragoer",
    "Egedal": "egedal",
    "Esbjerg": "esbjerg",
    "Faxe": "faxe",
    "Fredensborg": "fredensborg",
    "Frederiksberg": "frederiksberg",
    "Frederikssund": "frederikssund",
    "Furesø": "furesoe",
    "Gentofte": "gentofte",
    "Gladsaxe": "gladsaxe",
    "Glostrup": "glostrup",
    "Greve": "greve",
    "Gribskov": "gribskov",
    "Halsnæs": "halsnaes",
    "Hedensted": "hedensted",
    "Helsingør": "helsingor",
    "Herlev": "herlev",
    "Hillerød": "hillerod",
    "Hjørring": "hjoerring",
    "Horsens": "horsens",
    "Hvidovre": "hvidovre",
    "Høje-Taastrup": "htk",
    "Hørsholm": "hoersholm",
    "Jammerbugt": "jammerbugt",
    "Kerteminde": "kerteminde",
    "Køge": "koege",
    "Lyngby-Taarbæk": "ltf",
    "Mariagerfjord": "mariagerfjord",
    "Næstved": "naestved",
    "Odsherred": "odsherred",
    "Randers": "randers",
    "Rebild": "rebild",
    "Ringkøbing-Skjern": "rksk",
    "Ringsted": "ringsted",
    "Roskilde": "roskilde",
    "Rudersdal": "rudersdal",
    "Rødovre": "rk",
    "Samsø": "samsoe",
    "Slagelse": "slagelse",
    "Solrød": "solrod",
    "Sorø": "soroe",
    "Stevns": "stevns",
    "Svendborg": "svendborg",
    "Sønderborg": "sonderborg",
    "Tårnby": "taarnby",
    "Varde": "varde",
    "Vejen": "vejen",
    "Vordingborg": "vordingborg",
}

MUNICIPALITIES_ARRAY = list(MUNICIPALITIES_LIST.keys())

WEEKDAYS = ["Mandag", "Tirsdag", "Onsdag", "Torsdag", "Fredag", "Lørdag", "Søndag"]
