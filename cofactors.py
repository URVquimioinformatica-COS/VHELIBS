# -*- coding: utf-8 -*-
#
#   Copyright 2011-2012 Adrià Cereto Massagué <adrian.cereto@.urv.cat>
#
#   Ligand blacklist
#

metals = {
'3CO': 'Cobalt'
, 'NAW': 'SODIUM ION'
, 'MO3': 'Magnesium Ion, 3 Waters coordinated'
, 'MO2': 'Magnesium Ion, 2 Waters coordinated'
, 'MO1': 'Magnesium Ion, 1 Water coordinated'
, 'MO6': 'Magnesium Ion, 6 Waters coordinated'
, 'MO5': 'Magnesium Ion, 5 Waters coordinated'
, 'MO4': 'Magnesium Ion, 4 Waters coordinated'
, 'PT': 'Platinum ion'
, 'PB': 'LEAD (II) ION'
, 'ZO3': 'Zinc'
, 'MH2': 'Manganese'
, 'MH3': 'Manganese'
, 'ZN': 'Zinc'
, 'K': 'POTASSIUM ION'
, 'MN6': 'Manganese'
, 'MG': 'MAGNESIUM ION'
, 'MN': 'Manganese'
, 'O4M': 'Manganese'
, 'FE': 'Fe(2+)'
, 'CD3': 'CADMIUM ION'
, 'CD5': 'CADMIUM ION'
, 'AU3': 'GOLD'
, 'CU': 'COPPER ION'
, 'CO': 'COBALT ION'
, 'CL': 'CHLORIDE ION'
, 'CA': 'Calcium'
, 'CE': 'CERIUM (III) ION'
, 'CD': 'CADMIUM ION'
, 'SE': 'Selenium'
, 'YB': 'Yterbium ion'
, 'CS': 'CESIUM ION'
, 'LI': 'LITHIUM ION'
, '3NI': 'NICKEL (III) ION'
, 'NH4': 'Ammonium Ion'
, 'IOD': 'IODIDE ION'
, '6MO': 'Molybdenum'
, 'RU': 'Rutenium ion'
, 'BR': 'BROMIDE ION'
, 'KO4': 'POTASSIUM ION, 4 WATERS COORDINATED'
, '4MO': 'Molybdenum'
, 'BA': 'Barium ion'
, 'ZNO': 'Zinc'
, 'NAO': 'SODIUM ION'
, 'V': 'Vanadium'
, 'HG': 'Mercury (II) Bound to Cys 206'
, 'NA2': 'SODIUM ION'
, 'ZN2': 'Zinc'
, 'NA6': 'SODIUM ION'
, 'NA5': 'SODIUM ION'
, 'CD1': 'CADMIUM ION'
, 'CR': 'CHROMIUM ION'
, 'ZN3': 'Zinc'
, 'CUA': 'DINUCLEAR COPPER ION'
, '1CU': 'COPPER ION, 1 WATER COORDINATED'
, 'MN3': 'Manganese'
, 'MN5': 'Manganese'
, 'MW3': 'Manganese'
, 'MW2': 'Manganese'
, 'MW1': 'Manganese'
, '2OF': 'FERROUS ION, 2 WATERS COORDINATED'
, 'NI': 'Nickel ion'
, 'NA': 'SODIUM ION'
, 'FE2': 'FE (II) ION'
, 'AG': 'SILVER ION'
, 'AL': 'ALUMINUM ION'
, 'AU': 'GOLD'
, 'W': 'Tungsten'
, 'EU': 'Europium ion'
, 'OS': 'Osmium ion'
, 'HO': 'Holmium ion'
, 'IR': 'Iridium(4+)'
, 'IR3': 'IRIDIUM (III) ION '
, 'U1': 'Uranium'
, 'SB': 'ANTIMONY (III) ION '
, 'PR': 'PRASEODYMIUM ION'
, 'GD': 'GADOLINIUM ATOM '
, 'SM': 'SAMARIUM (III) ION'
, 'LU': 'LUTETIUM (III) ION'
, 'TB': 'TERBIUM(III) ION'
, 'RB': 'RUBIDIUM ION'
, 'Y1': 'yttrium(+2) cation'
, 'TL': 'THALLIUM (I) ION'
, 'PD': 'PALLADIUM ION'
, 'SO3': 'SULFITE ION'
, 'SR': 'Strontium ion'
, 'C1O': 'CU- O LINKAGE'
, 'O': 'Oxygen atom'
, 'F': 'FLUORIDE'
}

ligand_blacklist = {
'': ''
, 'EOH': 'Ethanol'
, 'HEM': 'Protoprphyrin IX containing FE'
, 'SIN': 'Succinic acid'
, 'SPV': 'SULFOPYRUVATE'
, '543': 'CALCIUM ION, 6 WATERS PLUS ETHANOL COORDINATED'
, 'SF4': 'Iron Sulfur cluster'
, '7QM': 'MENAQUINONE- 7 (ALTERED)'
, 'MQ7': 'MENAQUINONE- 7'
, 'MQ9': 'MENAQUINONE 9'
, 'MQ8': 'MENAQUINONE 8'
, 'PQQ': 'PYRROLOQUINOLINE QUINONE'
, 'UQ1': 'UBIQUINONE-1'
, 'UQ2': 'UBIQUINONE-2'
, 'UQ7': 'UBIQUINONE-7'
, 'EGL': 'Ethylene Glycol'
, 'BEF': 'BERYLLIUM TRIFLUORIDE ION'
, 'DMS': 'Dimethyl Sulfoxide'
, 'NO2': 'NITRITE ION'
, 'NO3': 'NITRATE ION'
, 'CIT': 'Citric Acid'
, 'PI': 'HYDROGENPHOSPHATE ION'
, 'S': 'sulfur'
, 'MD': 'molybdopterin guanine dinucleotide'
, 'LCP': 'PERCHLORATE ION'
, 'MOO': 'MOLYBDATE ION'
, 'LCO': 'CHLORATE ION'
, 'COS': 'Coenzyme A persulfide'
, 'PEP': 'PHOSPHOENOLPYRUVATE'
, 'PER': 'PEROXIDE ION'
, 'COA': 'COENZYME A'
, 'SMM': 'S-ADENOSYLMETHIONINE METHYL ESTER'
, 'BCT': 'Bicarbonate'
, 'AUC': 'GOLD CYANIDE'
, 'FMN': 'FMN'
, 'HEA': 'HEM A'
, 'HEB': 'HEM B'
, 'HEC': 'HEM C'
, 'NDP': 'NADPH'
, 'HEO': 'Heme o'
, 'CO3': 'Carbonate Ion'
, 'PLP': 'PYRIDOXAL- 5- PHOSPHATE'
, 'ALF': 'TETRAFLUOROALUMINATE ION'
, 'EDO': '1,2-Ethanediol'
, 'FS1': 'IRON/SULFUR CLUSTER'
, 'FS3': 'Fe3-S4 Cluster'
, 'FS4': 'Iron/Sulfur Cluster'
, 'DPM': 'Dipyrromethane'
, 'SOH': 'HYDROGEN SULFATE'
, 'PPR': 'PHOSPHONOPYRUVATE'
, 'GAI': 'Guanidine'
, 'FAD': 'FAD'
, 'SO4': 'Sulfate Ion'
, 'NH2': 'Amino group'
, 'ARS': 'Arsenic'
, 'NAD': 'NAD'
, 'NAH': 'NAD'
, 'NAI': 'NADH'
, 'NAP': 'NADPH'
, 'GHA': 'MIO'
, 'THF': '5-HYDROXYMETHYLENE-6-HYDROFOLIC ACID'
, 'GSH': 'Glutathione'
, 'SAM': 'S-ADENOSYLMETHIONINE'
, 'BF4': 'BERYLLIUM TETRAFLUORIDE ION'
, 'TPQ': '5- (2-CARBOXY-2-AMINOETHYL)-2-HYDROXY-1,4-BENZOQUINONE'
, 'TPP': 'Thiamine diphosphate'
, 'LPA': 'LIPOIC ACID'
, 'OH': 'HYDROXIDE ION'
, 'PYR': 'Pyruvic acid'
, 'BO4': 'BORATE ION'
, 'FLC': 'CITRATE ANION'
, 'FUM': 'Fumaric acid'
, 'PDP': 'PYRIDOXAL- 5- DIPHOSPHATE'
, 'BME': 'Betamercaptoethanol'
, 'WO4': 'Tungstate ion'
, 'YT3': 'Yttrium ion'
, 'DHE': 'Heme d'
, 'OXY': 'Oxygen molecule'
, '2HP': 'DIHYDROGENPHOSPHATE ION'
, 'PO3': 'PHOSPHITE ION'
, 'OXL': 'OXALATE ION'
, 'TRS': '2- AMINO- 2- HYDROXYMETHYL- PROPANE- 1,3- DIOL'
, 'BTN': 'Biotin'
, 'ACE': 'Acetyl Group'
, 'SUL': 'Sulfate Anion'
, 'B12': 'Cobalamin'
, 'ATP': 'ADENOSINE- 5- TRIPHOSPHATE'
, 'ACT': 'Acetate Ion'
, 'U10': 'UBIQUINONE-10'
, 'ACY': 'Acetic Acid'
, 'ASC': 'ASCORBIC ACID'
, 'SEO': 'Beta-Mercaptoethanol 102LA4'
, 'ADP': 'ADENOSINE-5-DIPHOSPHATE'
, 'UNX': 'Unknown'
, 'CUZ': '(MU- 4- SULFIDO)- TETRA- NUCLEAR COPPER ION'
, 'XE': 'Xenon'
, 'GTP': 'Guaniosuine-5-triphosphate'
, 'GTT': 'Glutathione'
, 'FES': 'Fe2/S2 (Inorganic) Cluster'
, 'FRU': 'Fructose'
, 'GMP': 'Guanosine'
, 'H2S': 'HYDROSULFURIC ACID'
, 'AZI': 'AZIDE ION'
, 'BPV': 'Bromopyruvate'
, 'MSE': 'Selenmethionine'
, 'BIO': 'BIOPTERIN'
, 'CYN': 'CYANIDE ION'
, 'GOL': 'Glycerol'
, 'PO4': 'Phosphate Ion'
, 'MLI': 'MALONATE ION'
, 'MLT': 'MALATE ION'
, 'RBF': 'Riboflavin'
, 'SRM': 'Siroheme'
, 'UQ8': 'UBIQUINONE-8'
, 'HOH': 'Water'
, 'NAG': 'n-acetylglucosamine'
, 'EPE': 'Hepes'
, 'PEG': 'poly(ethylene glycol)'
, '0U': 'L-nucleotide'
, '6HT': 'L-nucleotide'
, '0C': 'L-nucleotide'
, '0G': 'L-nucleotide'
, '6HG': 'chemically modified oligonucleotide derivative'
, '6HA': 'chemically modified oligonucleotide derivative'
, '6HC': 'chemically modified oligonucleotide derivative'
, 'A44': 'chemically modified oligonucleotide derivative'
, 'C43': 'chemically modified oligonucleotide derivative'
, 'G48': 'chemically modified oligonucleotide derivative'
, 'U36': 'chemically modified oligonucleotide derivative'
, 'ZCY': 'RNA linking'
, 'ZGU': 'RNA linking'
, 'ZAD': 'RNA linking'
, 'ZTH': 'RNA linking'
, 'LCA': 'RNA linking'
, 'LCC': 'RNA linking'
, 'LCG': 'RNA linking'
, 'TLN': 'RNA linking'
, 'ZBC': 'RNA linking'
, 'ZBU': 'RNA linking'
, 'ZHP': 'RNA linking'
, 'AF2': 'DNA linking'
, 'GF2': 'DNA linking'
, 'XAD': 'DNA linking'
, 'XCT': 'DNA linking'
, 'XGU': 'DNA linking'
, 'XTH': 'DNA linking'

}

def update_lists(new_m = metals, new_lb = ligand_blacklist):
    global metals
    metals = new_m
    global ligand_blacklist
    ligand_blacklist = new_lb

def dump_lists(fname = 'notligands.ini'):
    file = open(fname, 'w')
    metalstring = ''
    metalhetids = metals.keys()
    metalhetids.sort()
    for hetid in metalhetids:
        if hetid:
            metalstring += hetid + ' : ' + metals[hetid] + '\n'
    lblstring = ''
    lblhetids = ligand_blacklist.keys()
    lblhetids.sort()
    for hetid in lblhetids:
        if hetid:
            lblstring += hetid + ' : ' + ligand_blacklist[hetid] + '\n'
    file.write('[Blacklist]\n')
    file.write(lblstring)
    file.write('\n[Non-propagating]\n')
    file.write(metalstring)
    file.close()
    return 0

def load_lists(fname):
    new_m = {}
    new_lb = {}
    file = open(fname, 'r')
    lines = file.readlines()
    file.close()
    d = None
    for line in lines:
        if line.lower().startswith('[blacklist]'):
            d = new_lb
            continue
        elif line.lower().startswith('[non-propagating]'):
            d = new_m
            continue
        if d != None:
            line = line.strip()
            if ':' in line and len(line) >= 3:
                dirty_hetid,  dirty_desc = line.split(':')
                d[dirty_hetid.strip()] = dirty_desc.strip()
    update_lists(new_m, new_lb)
    return 0


