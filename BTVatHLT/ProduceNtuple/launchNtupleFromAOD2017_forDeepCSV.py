from math import sqrt, pi, log10, log, exp

def isGoodMuonCut( me0muon, MaxPullX, MaxDiffX, MaxPullY, MaxDiffY, MaxDiffPhiDir ):
    thisSegment = me0muon.me0segment()
    r3FinalReco = me0muon.localTrackPosAtSurface()
    C = me0muon.localTrackCov()
    thisPosition = LocalPoint(thisSegment.localPosition())
    sigmax = sqrt(C[3][3]+thisSegment.localPositionError().xx() )
    sigmay = sqrt(C[4][4]+thisSegment.localPositionError().yy() )
    X_MatchFound = False, Y_MatchFound = False, Dir_MatchFound = False
    if ( (abs(thisPosition.x()-r3FinalReco.x())/sigmax ) < MaxPullX ) or (abs(thisPosition.x()-r3FinalReco.x()) < MaxDiffX ) : X_MatchFound = True
    if ( (abs(thisPosition.y()-r3FinalReco.y())/sigmay ) < MaxPullY ) or (abs(thisPosition.y()-r3FinalReco.y()) < MaxDiffY ) : Y_MatchFound = True
    if abs(reco.deltaPhi(me0muon.localTrackMomAtSurface().barePhi(),thisSegment.localDirection().barePhi())) < MaxDiffPhiDir : Dir_MatchFound = True
    return (X_MatchFound and Y_MatchFound and Dir_MatchFound)

def isGoodMuon(me0muon, type):
    if type=="All":
        return True
    elif type=="VeryLoose":
        return isGoodMuonCut(me0muon,3,4,20,20,3.14)
    elif type=="Loose":
        return isGoodMuonCut(me0muon,3,2,3,2,0.5)
    elif type=="Tight":
        return isGoodMuonCut(me0muon,3,2,3,2,0.15)
    else:
        return False

def isLooseMuon(muon):
 return muon.isPFMuon() and ( muon.isGlobalMuon() or muon.isTrackerMuon());

def printLabelFilters(triggerEv):
    print "Filters:"
    for i in range(triggerEv.sizeFilters()):
        print "\t",triggerEv.filterLabel(i)
    print

def printLabelCollections(triggerEv):
    print "Collection:"
    for i in range(triggerEv.sizeCollections()):
        print "\t",triggerEv.collectionTagEncoded(i)
    print

def getSizeFilter(triggerEv,inputTag):
    filterIndex = triggerEv.filterIndex(inputTag)
    if filterIndex >= triggerEv.sizeFilters():
        return -1
    else:
        return len(triggerEv.filterKeys(filterIndex))

def goodEvent(run,lumi): #https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions15/13TeV/Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON.txt
# https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/DCSOnly/json_DCSONLY.txt

# 2017
# https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions17/13TeV/

    JSONlist={"297050": [[1, 137], [193, 195], [197, 371], [374, 599], [602, 604], [607, 665], [668, 776]], "297056": [[12, 26], [28, 101], [104, 187], [189, 203]], "297057": [[1, 4], [14, 83], [85, 105], [112, 183], [185, 360], [362, 377], [385, 410], [413, 418], [424, 509], [516, 554], [556, 629], [632, 906]], "297099": [[40, 62]], "297100": [[1, 15], [21, 220], [222, 369], [375, 381]], "297101": [[1, 349], [351, 547], [550, 585], [587, 665], [667, 668], [673, 697], [700, 856], [862, 920]], "297113": [[1, 15], [27, 149], [151, 204], [211, 252]], "297114": [[1, 36], [38, 99], [106, 132], [135, 159]], "297175": [[1, 22], [24, 85]], "297176": [[1, 120], [125, 214]], "297215": [[1, 27], [29, 47]], "297218": [[1, 27]], "297219": [[1, 11], [14, 80], [85, 147], [149, 281], [288, 331], [333, 579], [585, 625], [627, 730], [732, 916], [921, 972], [974, 1071], [1073, 1093], [1095, 1210], [1212, 1363], [1365, 1429], [1436, 1479], [1481, 1712], [1714, 2004], [2010, 2057], [2059, 2111], [2114, 2431], [2433, 2565], [2567, 2572], [2574, 2638]], "297224": [[1, 19], [24, 81], [83, 138]], "297225": [[1, 21], [24, 32]], "297227": [[1, 59], [62, 192]], "297292": [[1, 54], [56, 125], [130, 131], [136, 320], [323, 342], [344, 509], [512, 667], [675, 750], [753, 753]], "297293": [[1, 12], [14, 77], [79, 121], [127, 150]], "297296": [[1, 87], [90, 133], [136, 213], [215, 230], [232, 236], [240, 304], [306, 401], [406, 418], [425, 497]], "297308": [[8, 44]], "297359": [[51, 56], [60, 70], [164, 180]], "297411": [[32, 69], [71, 190], [192, 297], [299, 479], [481, 694], [696, 737], [740, 776], [779, 800], [807, 947], [950, 950]], "297424": [[32, 149]], "297425": [[1, 107], [112, 137], [140, 157]], "297426": [[1, 28], [34, 84], [90, 111]], "297429": [[1, 72]], "297430": [[1, 32], [34, 66], [69, 190], [192, 199]], "297431": [[1, 49], [55, 64], [71, 142], [144, 188]], "297432": [[1, 19], [21, 30], [32, 112]], "297433": [[1, 127], [130, 159]], "297434": [[1, 161]], "297435": [[1, 14], [16, 94]], "297467": [[50, 80], [82, 127], [129, 138]], "297468": [[1, 74]], "297469": [[1, 4], [9, 70]], "297483": [[37, 68], [71, 201], [206, 214]], "297484": [[1, 20], [23, 47], [53, 98], [100, 208], [214, 214]], "297485": [[2, 16], [23, 55], [57, 253], [258, 299], [302, 314], [321, 411], [414, 420]], "297486": [[1, 74], [79, 140], [142, 598], [603, 604], [607, 625]], "297487": [[1, 147], [150, 338], [340, 433], [439, 491], [495, 603], [609, 613]], "297488": [[1, 73], [80, 424]], "297503": [[1, 59], [61, 193], [195, 275], [282, 559], [566, 606], [612, 635], [642, 772], [777, 779]], "297504": [[1, 27], [29, 33], [36, 41], [125, 136]], "297505": [[1, 61], [63, 394]], "297557": [[8, 113], [119, 167], [173, 174], [180, 394]], "297558": [[1, 124], [126, 164], [167, 225], [227, 266]], "297562": [[1, 3], [5, 92], [94, 369]], "297563": [[1, 69], [71, 77], [79, 254], [260, 262]], "297599": [[1, 156], [158, 169], [211, 225], [230, 312], [319, 385], [395, 407]], "297603": [[1, 104], [107, 289], [291, 420]], "297604": [[1, 91], [94, 126], [131, 161], [163, 179], [181, 272], [279, 359], [361, 375], [381, 402], [404, 407]], "297605": [[1, 6], [13, 20], [24, 89], [95, 104], [106, 179], [182, 219], [221, 407]], "297606": [[1, 29], [31, 94], [99, 231]], "297620": [[32, 98], [101, 127], [129, 318]], "297656": [[64, 116], [123, 135], [140, 230], [269, 307], [313, 330], [341, 376], [378, 388], [393, 433]], "297665": [[1, 153], [159, 209], [214, 265], [268, 279]], "297666": [[1, 11], [17, 72], [74, 81], [86, 94], [97, 97], [100, 121]], "297670": [[1, 34]], "297674": [[1, 102], [108, 188]], "297675": [[1, 123], [129, 149], [151, 163], [165, 175], [178, 186], [189, 199], [202, 239], [244, 328], [334, 467], [470, 471]], "297722": [[55, 160], [165, 289], [292, 310], [313, 344], [346, 350], [352, 353]], "297723": [[1, 222]], "298996": [[33, 216]], "298997": [[1, 47]], "299000": [[1, 16], [18, 77]], "299042": [[33, 55]], "299061": [[38, 194], [197, 280], [282, 343], [345, 355]], "299062": [[1, 81], [83, 163], [166, 183], [186, 303]], "299064": [[1, 85]], "299065": [[13, 248], [251, 342]], "299067": [[1, 58], [60, 110], [112, 190], [193, 248], [250, 268], [270, 303], [305, 327], [329, 459]], "299096": [[1, 3], [5, 55], [57, 97]], "299149": [[29, 87], [89, 198], [200, 216], [218, 263], [266, 266], [268, 272], [274, 282], [284, 288], [290, 470]], "299178": [[37, 56], [58, 111]], "299180": [[1, 98]], "299184": [[1, 130], [132, 164], [166, 326], [328, 359], [361, 416], [419, 456], [458, 480], [482, 561]], "299185": [[1, 107], [109, 120]], "299327": [[1, 72]], "299329": [[1, 6], [8, 151], [153, 172]], "299368": [[37, 54], [56, 61], [63, 175]], "299369": [[1, 21], [24, 44], [46, 289], [291, 303]], "299370": [[1, 72], [74, 149], [151, 174], [176, 411], [413, 457], [460, 523], [525, 529], [531, 610], [612, 698], [701, 705]], "299380": [[32, 36], [39, 83], [86, 170], [172, 227]], "299381": [[1, 45]], "299394": [[1, 33]], "299395": [[1, 58], [60, 64], [66, 127], [130, 187]], "299396": [[1, 34], [37, 52], [54, 81]], "299420": [[1, 50]], "299443": [[145, 164]], "299450": [[39, 88]], "299477": [[34, 42], [82, 87]], "299478": [[1, 16], [19, 81], [83, 140], [143, 175]], "299479": [[1, 67], [69, 123]], "299480": [[1, 7], [9, 244], [247, 330], [332, 346], [348, 359], [361, 451], [454, 460], [463, 463], [466, 502], [504, 646], [649, 713]], "299481": [[1, 66], [68, 177], [179, 196], [199, 236], [260, 263], [266, 323], [326, 424], [426, 433], [435, 452], [454, 479], [487, 521], [523, 602], [604, 644], [646, 655], [657, 747], [750, 868], [871, 940], [943, 997], [1000, 1030], [1033, 1037], [1061, 1145], [1147, 1205], [1207, 1257]], "299593": [[95, 103], [106, 157], [159, 177], [179, 201], [204, 419], [421, 437], [439, 508], [511, 513], [515, 515], [518, 575], [577, 591], [593, 678], [680, 747], [750, 896]], "299594": [[1, 27], [29, 115], [117, 221], [224, 249], [251, 317]], "299595": [[1, 33], [35, 112], [114, 134], [138, 138]], "299597": [[1, 8], [11, 62], [65, 91], [93, 209], [212, 228], [230, 258], [260, 445], [447, 534], [536, 540]], "299649": [[151, 228], [230, 332]], "300087": [[36, 59], [61, 126], [128, 137], [140, 208], [210, 210], [213, 216], [218, 239]], "300105": [[1, 21]], "300106": [[1, 12], [14, 74]], "300107": [[1, 28], [30, 47]], "300117": [[35, 67]], "300122": [[44, 85], [88, 100], [102, 127], [129, 186], [188, 235], [237, 303], [306, 453], [456, 527], [530, 560], [563, 609], [611, 617], [619, 627], [629, 657], [660, 691], [693, 697], [699, 730], [735, 809], [811, 924], [927, 1026], [1028, 1051], [1053, 1082], [1084, 1172], [1175, 1286], [1289, 1295]], "300123": [[1, 91], [93, 93], [96, 158], [160, 177], [180, 381], [383, 384], [387, 487], [490, 612]], "300155": [[35, 62], [64, 357], [359, 411], [413, 527], [529, 539], [542, 630], [632, 736], [738, 840], [842, 950], [953, 982], [984, 1176], [1178, 1229]], "300156": [[1, 29], [31, 53], [56, 63], [65, 70], [72, 72]], "300157": [[1, 28], [30, 133], [135, 152], [154, 225], [228, 296], [298, 460], [462, 484], [486, 535], [538, 680], [682, 738], [740, 785], [788, 802], [805, 876], [879, 890], [892, 908], [911, 996], [998, 1027], [1030, 1075], [1077, 1107]], "300226": [[43, 72], [74, 162], [164, 192], [195, 258], [260, 314], [316, 358], [360, 408], [410, 448]], "300233": [[43, 69], [72, 151], [154, 162]], "300234": [[1, 59]], "300235": [[1, 153], [155, 182], [184, 187]], "300236": [[1, 95], [97, 124], [126, 187]], "300237": [[1, 59], [61, 61], [63, 98], [101, 112], [114, 147], [150, 315], [317, 354], [356, 379], [381, 388], [390, 428], [430, 458], [461, 471], [474, 546], [548, 629], [631, 713], [716, 717]], "300238": [[1, 58], [62, 86], [89, 273], [275, 329]], "300239": [[1, 7], [9, 22], [25, 67], [70, 78], [80, 128], [130, 145], [148, 158], [161, 167], [171, 213]], "300240": [[1, 7], [11, 46], [51, 79], [81, 210], [212, 221], [224, 340], [342, 362]], "300281": [[3, 8]], "300282": [[1, 9], [13, 59], [73, 92], [97, 114], [142, 151], [156, 172], [174, 186]], "300283": [[1, 13], [15, 34]], "300284": [[1, 2], [5, 22], [38, 47], [50, 63], [65, 82], [90, 98], [108, 130], [133, 152], [156, 245], [248, 250], [260, 293], [295, 414], [420, 561], [568, 585], [590, 680], [691, 711], [713, 751]], "300364": [[24, 46]], "300365": [[3, 20]], "300367": [[1, 20]], "300368": [[1, 10], [12, 20]], "300370": [[1, 1], [3, 20]], "300372": [[1, 8]], "300373": [[1, 21]], "300374": [[1, 21]], "300375": [[1, 47], [50, 93]], "300389": [[1, 1], [4, 5], [8, 8], [11, 20], [23, 39], [60, 149]], "300391": [[1, 21]], "300392": [[1, 21]], "300393": [[1, 20]], "300394": [[1, 21]], "300395": [[1, 2], [5, 20]], "300397": [[1, 20]], "300398": [[1, 5], [8, 20]], "300399": [[1, 20]], "300400": [[1, 59], [61, 288], [291, 342], [344, 372], [374, 391], [393, 395], [398, 561], [563, 582], [584, 596], [598, 643], [645, 677]], "300461": [[1, 31], [34, 98]], "300462": [[1, 97]], "300463": [[1, 67], [69, 124]], "300466": [[1, 34], [36, 56], [59, 79], [82, 223], [225, 303], [305, 326], [328, 336], [338, 385], [388, 455], [457, 578], [580, 593], [596, 614], [617, 650]], "300467": [[1, 50], [52, 70], [73, 91], [93, 228], [230, 342], [344, 434], [436, 484], [486, 489], [492, 563]], "300497": [[26, 28], [31, 125], [127, 149], [151, 175]], "300514": [[38, 43], [46, 78], [80, 150]], "300516": [[1, 78], [80, 111]], "300517": [[1, 8], [103, 179], [181, 391], [394, 409], [411, 479], [482, 587], [589, 623]], "300558": [[1, 37], [39, 104], [106, 167], [169, 194], [196, 287], [289, 342], [344, 548]], "300575": [[1, 82]]}

    if str(run) in JSONlist.keys():
        for rg in JSONlist[str(run)]:
            if len(rg) ==2:
                if lumi>=rg[0] and lumi<=rg[1]:
                    return True
    
    return False

def checkTriggerIndex(name,index, names):
    if not 'firstTriggerError' in globals():
        global firstTriggerError
        firstTriggerError = True
    if index>=names.size():
        if firstTriggerError:
            for tr in names: print tr
            print
            print name," not found!"
            print
            firstTriggerError = False
            return False
        else:
            return False
    else:
        return True

def deltaPhi(phi1, phi2):
  PHI = abs(phi1-phi2)
  if PHI<=pi:
      return PHI
  else:
      return 2*pi-PHI

def deltaR(eta1, phi1, eta2, phi2):
  deta = eta1-eta2
  dphi = deltaPhi(phi1,phi2)
  return sqrt(deta*deta + dphi*dphi)

def matching(eta,phi,offJet_eta,offJet_phi,offJet_num):
    dRMin = 99.
    index = -1
    for i in range(0,offJet_num):
        dR = deltaR(eta,phi,offJet_eta[i],offJet_phi[i])
        if dR < 0.5 and dR < dRMin:
            dRMin = dR
            index = i
    
    return index

def getCollectionKeys(triggerEvent,inputTag):
    collectionKeys = []
    collectionIndex = triggerEvent.collectionIndex(inputTag)
    if collectionIndex<triggerEvent.sizeCollections():
        start = 0
        if collectionIndex>0: start = triggerEvent.collectionKey(collectionIndex-1)
        stop = triggerEvent.collectionKey(collectionIndex)
        collectionKeys = range(start, stop)
        del start
        del stop
    
    del collectionIndex
    return collectionKeys

def getMET(triggerEvent,inputTag):
    collectionKeys = getCollectionKeys(triggerEvent,inputTag)
    trigObjColl = triggerEvent.getObjects()
    if len(collectionKeys)>0:
        met = trigObjColl[collectionKeys[0]]
        return met.pt(), met.phi()
    else:
        return 0,0
    del trigObjColl
    del collectionKeys


def getFilterKeys(triggerEvent,inputTag):
    filterKeys = []
    filterIndex = triggerEvent.filterIndex(inputTag)
    if filterIndex<triggerEvent.sizeFilters():
        filterKeys = triggerEvent.filterKeys(filterIndex)
    
    del filterIndex
    return filterKeys

def launchNtupleFromAOD2017(fileOutput,filesInput,maxevents):

    print "fileOutput=",fileOutput
    print
    print "filesInput=",filesInput
    print
    print "maxevents=",maxevents
    print

    import ROOT
    import itertools
    import resource
    from array import array
    from math import sqrt, pi, log10, log, exp
    # load FWlite python libraries
    from DataFormats.FWLite import Handle, Events

    pt_min=20
    eta_max=2.4
    NHFmax=0.9
    NEMFmax=0.99
    CHFmin=0.
    MUFmax=0.8
    CEMFmax=0.99
    NumConstMin=1
    CHMmin=0

    f = ROOT.TFile(fileOutput,"recreate")
    tree = ROOT.TTree("tree","tree")
    
    maxJets = 50
    
    calobjets = [
    'hltBTagCaloDeepCSVp44Single'# HLT_PFHT380_SixJet32_DoubleBTageepSV_p075
    #'hltBTagCaloCSVp44Single', # HLT_PFHT380_SixJet32_DoubleBTagCSV_p075
	]
    
#    calobjetsMC = [
#    'hltBLifetimeL3FilterCSVsusy',
#    'hltCSV0p7L3',
#    'hltCSVL30p6',
#    'hltTripleCSV0p5',
#    'hltDoubleCSV0p5',
#    'hltBLifetimeL3FilterCSVLoose0p41',
#    'hltCSV0p5L3',
#    ]
    
    pfbjets = [
    'hltBTagPFDeepCSVp075Double', # HLT_PFHT380_SixJet32_DoubleBTageepSV_p075 
    'hltBTagPFDeepCSVp059Single',
    'hltBTagPFCSVp080Single'
    #'hltBTagPFCSVp075Double', # from HLT_PFHT380_SixJet32_DoubleBTagCSV_p075_v1
    ]
    
#    pfbjetsMC = [
#    'hltCSVFilterSingleTop',
#    'hltDoubleCSVPF0p4',
#    'hltCSVPF0p7',
#    'hltCSV0p5FilterSingleMu10',
#    'hltCSV0p5FilterSingleEle10',
#    'hltCSVFilterPF0p7',
#    'hlt2CSVFilterPF0p7',
#    ]
    
#    filtersMC = [
#    'hltL1sTripleVBF',
#    'hltPreQuadPFJetDoubleBTagCSVVBFMqq200',
#    'hltPreQuadPFJetSingleBTagCSVVBFMqq460',
#    'hltPreQuadPFJetDoubleBTagCSVVBFMqq240',
#    'hltPreQuadPFJetSingleBTagCSVVBFMqq500',
#    'hltQuadJet15',
#    'hltTripleJet50',
#    'hltDoubleJet65',
#    'hltSingleJet80',
#    'hltVBFCaloJetEtaSortedMqq150Deta1p5',
#    'hltCSVL30p6',
#    'hltPFQuadJetLooseID15',
#    'hltPFTripleJetLooseID64',
#    'hltPFDoubleJetLooseID76',
#    'hltPFSingleJetLooseID92',
#    'hltSelector6PFJets',
#    'hltDoubleCSVPF0p4',
#    'hltCSVPF0p7',
#    'hltVBFPFJetCSVSortedMqq200Detaqq1p2',
#    'hltVBFPFJetCSVSortedMqq460Detaqq4p1',
#    'hltVBFPFJetCSVSortedMqq240Detaqq2p0',
#    'hltVBFPFJetCSVSortedMqq500Detaqq4p6',
#    ]
    
    filters = [
    #TO BE UPDATED
    'hltMHTNoPU90',
    'hltBTagCaloCSVp067Single',
    ]

    MC = False
    if len(filesInput)>0 and ('AODSIM' in filesInput[0]):
        MC = True
    HLTprocess = "reHLT"
    if len(filesInput)>0 and ('reHLT' in filesInput[0]):
        HLTprocess = "HLT2"
    print "HLTprocess=",HLTprocess
    
    btags, btagLabel = Handle("edm::AssociationVector<edm::RefToBaseProd<reco::Jet>,vector<float>,edm::RefToBase<reco::Jet>,unsigned int,edm::helper::AssociationIdenticalKeyReference>"),("pfCombinedInclusiveSecondaryVertexV2BJetTags") #("pfCombinedSecondaryVertexBJetTags")
    
    btags_b, btagLabel_b = Handle("edm::AssociationVector<edm::RefToBaseProd<reco::Jet>,vector<float>,edm::RefToBase<reco::Jet>,unsigned int,edm::helper::AssociationIdenticalKeyReference>"),("pfDeepCSVJetTags:probb")#("pfCombinedInclusiveSecondaryVertexV2BJetTags") #("pfCombinedSecondaryVertexBJetTags")
    btags_bb, btagLabel_bb = Handle("edm::AssociationVector<edm::RefToBaseProd<reco::Jet>,vector<float>,edm::RefToBase<reco::Jet>,unsigned int,edm::helper::AssociationIdenticalKeyReference>"),("pfDeepCSVJetTags:probbb")#("pfCombinedInclusiveSecondaryVertexV2BJetTags")
    
    btagsCSVOnline, btagLabelCSVOnline, processname = Handle('edm::AssociationVector<edm::RefToBaseProd<reco::Jet>,vector<float>,edm::RefToBase<reco::Jet>,unsigned int,edm::helper::AssociationIdenticalKeyReference>'), ("hltCombinedSecondaryVertexBJetTagsPF"),(HLTprocess)
    btagsDCSVOnline, btagLabelDCSVOnline, processname = Handle('edm::AssociationVector<edm::RefToBaseProd<reco::Jet>,vector<float>,edm::RefToBase<reco::Jet>,unsigned int,edm::helper::AssociationIdenticalKeyReference>'), ("hltDeepCombinedSecondaryVertexBJetTagsPF:probb"),(HLTprocess)
    
    if MC:
#        btagLabel = ("combinedInclusiveSecondaryVertexV2BJetTags")
#        calobjets = calobjetsMC
#        pfbjets = pfbjetsMC
	pass    
    ncalobjets = len(calobjets)
    npfbjets = len(pfbjets)

    ##python array types: http://docs.python.it/html/lib/module-array.html
    ##ROOT branch types: https://root.cern.ch/doc/master/classTTree.html
    nVertices = array( 'i', [ 0 ] )
    tree.Branch( 'nVertices', nVertices, 'nVertices/I' )
    run = array( 'L', [ 0 ] )
    tree.Branch( 'run', run, 'run/i' )
    lumi = array( 'L', [ 0 ] )
    tree.Branch( 'lumi', lumi, 'lumi/i' )
    eventNumber = array( 'L', [ 0 ] )
    tree.Branch( 'event', eventNumber, 'event/i' )
    bx = array( 'L', [ 0 ] )
    tree.Branch( 'bx', bx, 'bx/i' )
    JSON = array( 'i', [ 0 ] )
    tree.Branch( 'JSON', JSON, 'JSON/I' )
    instLumi = array( 'f', [ 0 ] )
    tree.Branch( 'instLumi', instLumi, 'instLumi/F' )
    
    caloMet = array( 'f', [ 0 ] )
    tree.Branch( 'caloMet', caloMet, 'caloMet/F' )
    caloMet_phi = array( 'f', [ 0 ] )
    tree.Branch( 'caloMet_phi', caloMet_phi, 'caloMet_phi/F' )
    
    pfMet = array( 'f', [ 0 ] )
    tree.Branch( 'pfMet', pfMet, 'pfMet/F' )
    pfMet_phi = array( 'f', [ 0 ] )
    tree.Branch( 'pfMet_phi', pfMet_phi, 'pfMet_phi/F' )
    
    caloMht = array( 'f', [ 0 ] )
    tree.Branch( 'caloMht', caloMht, 'caloMht/F' )
    caloMht_phi = array( 'f', [ 0 ] )
    tree.Branch( 'caloMht_phi', caloMht_phi, 'caloMht_phi/F' )
    
    pfMht = array( 'f', [ 0 ] )
    tree.Branch( 'pfMht', pfMht, 'pfMht/F' )
    pfMht_phi = array( 'f', [ 0 ] )
    tree.Branch( 'pfMht_phi', pfMht_phi, 'pfMht_phi/F' )
    
    caloNoPuMht = array( 'f', [ 0 ] )
    tree.Branch( 'caloNoPuMht', caloNoPuMht, 'caloNoPuMht/F' )
    caloNoPuMht_phi = array( 'f', [ 0 ] )
    tree.Branch( 'caloNoPuMht_phi', caloNoPuMht_phi, 'caloNoPuMht_phi/F' )
    
    l1MET2 = array( 'f', [ 0 ] )
    tree.Branch( 'l1MET2', l1MET2, 'l1MET2/F' )
    l1MET2_phi = array( 'f', [ 0 ] )
    tree.Branch( 'l1MET2_phi', l1MET2_phi, 'l1MET2_phi/F' )
    
    l1MET = array( 'f', [ 0 ] )
    tree.Branch( 'l1MET', l1MET, 'l1MET/F' )
    l1MET_phi = array( 'f', [ 0 ] )
    tree.Branch( 'l1MET_phi', l1MET_phi, 'l1MET_phi/F' )
    l1ET = array( 'f', [ 0 ] )
    tree.Branch( 'l1ET', l1ET, 'l1ET/F' )
    
    l1MHT = array( 'f', [ 0 ] )
    tree.Branch( 'l1MHT', l1MHT, 'l1MHT/F' )
    l1MHT_phi = array( 'f', [ 0 ] )
    tree.Branch( 'l1MHT_phi', l1MHT_phi, 'l1MHT_phi/F' )
    l1HT = array( 'f', [ 0 ] )
    tree.Branch( 'l1HT', l1HT, 'l1HT/F' )
    
    l1Jet_num = array( 'i', [ 0 ] )
    tree.Branch( 'l1Jet_num', l1Jet_num, 'l1Jet_num/I' )
    l1Jet_pt = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'l1Jet_pt', l1Jet_pt, 'l1Jet_pt[l1Jet_num]/F' )
    l1Jet_eta = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'l1Jet_eta', l1Jet_eta, 'l1Jet_eta[l1Jet_num]/F' )
    l1Jet_phi = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'l1Jet_phi', l1Jet_phi, 'l1Jet_phi[l1Jet_num]/F' )
    l1Jet_mass = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'l1Jet_mass', l1Jet_mass, 'l1Jet_mass[l1Jet_num]/F' )
    l1Jet_offmatch = array( 'i', maxJets*[ 0 ] )
    tree.Branch( 'l1Jet_offmatch', l1Jet_offmatch, 'l1Jet_offmatch[l1Jet_num]/I' )
    
    l1Tau_num = array( 'i', [ 0 ] )
    tree.Branch( 'l1Tau_num', l1Tau_num, 'l1Tau_num/I' )
    l1Tau_pt = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'l1Tau_pt', l1Tau_pt, 'l1Tau_pt[l1Tau_num]/F' )
    l1Tau_eta = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'l1Tau_eta', l1Tau_eta, 'l1Tau_eta[l1Tau_num]/F' )
    l1Tau_phi = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'l1Tau_phi', l1Tau_phi, 'l1Tau_phi[l1Tau_num]/F' )
    l1Tau_mass = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'l1Tau_mass', l1Tau_mass, 'l1Tau_mass[l1Tau_num]/F' )
    l1Tau_offmatch = array( 'i', maxJets*[ 0 ] )
    tree.Branch( 'l1Tau_offmatch', l1Tau_offmatch, 'l1Tau_offmatch[l1Tau_num]/I' )
    
    l1EGamma_num = array( 'i', [ 0 ] )
    tree.Branch( 'l1EGamma_num', l1EGamma_num, 'l1EGamma_num/I' )
    l1EGamma_pt = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'l1EGamma_pt', l1EGamma_pt, 'l1EGamma_pt[l1EGamma_num]/F' )
    l1EGamma_eta = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'l1EGamma_eta', l1EGamma_eta, 'l1EGamma_eta[l1EGamma_num]/F' )
    l1EGamma_phi = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'l1EGamma_phi', l1EGamma_phi, 'l1EGamma_phi[l1EGamma_num]/F' )
    l1EGamma_mass = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'l1EGamma_mass', l1EGamma_mass, 'l1EGamma_mass[l1EGamma_num]/F' )
    l1EGamma_iso = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'l1EGamma_iso', l1EGamma_iso, 'l1EGamma_iso[l1EGamma_num]/F' )
    l1EGamma_offmatch = array( 'i', maxJets*[ 0 ] )
    tree.Branch( 'l1EGamma_offmatch', l1EGamma_offmatch, 'l1EGamma_offmatch[l1EGamma_num]/I' )
    
    l1Muon_num = array( 'i', [ 0 ] )
    tree.Branch( 'l1Muon_num', l1Muon_num, 'l1Muon_num/I' )
    l1Muon_pt = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'l1Muon_pt', l1Muon_pt, 'l1Muon_pt[l1Muon_num]/F' )
    l1Muon_eta = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'l1Muon_eta', l1Muon_eta, 'l1Muon_eta[l1Muon_num]/F' )
    l1Muon_phi = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'l1Muon_phi', l1Muon_phi, 'l1Muon_phi[l1Muon_num]/F' )
    l1Muon_iso = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'l1Muon_iso', l1Muon_iso, 'l1Muon_iso[l1Muon_num]/F' )
    l1Muon_offmatch = array( 'i', maxJets*[ 0 ] )
    tree.Branch( 'l1Muon_offmatch', l1Muon_offmatch, 'l1Muon_offmatch[l1Muon_num]/I' )
    
    offMet = array( 'f', [ 0 ] )
    tree.Branch( 'offMet', offMet, 'offMet/F' )
    offMet_phi = array( 'f', [ 0 ] )
    tree.Branch( 'offMet_phi', offMet_phi, 'offMet_phi/F' )
    offMet_sig = array( 'f', [ 0 ] )
    tree.Branch( 'offMet_sig', offMet_sig, 'offMet_sig/F' )
    offMet_sumet = array( 'f', [ 0 ] )
    tree.Branch( 'offMet_sumet', offMet_sumet, 'offMet_sumet/F' )
    
    offMht = array( 'f', [ 0 ] )
    tree.Branch( 'offMht', offMht, 'offMht/F' )
    offMht_phi = array( 'f', [ 0 ] )
    tree.Branch( 'offMht_phi', offMht_phi, 'offMht_phi/F' )
    offMht_sumet = array( 'f', [ 0 ] )
    tree.Branch( 'offMht_sumet', offMht_sumet, 'offMht_sumet/F' )
    
    offPUPPIMht = array( 'f', [ 0 ] )
    tree.Branch( 'offPUPPIMht', offPUPPIMht, 'offPUPPIMht/F' )
    offPUPPIMht_phi = array( 'f', [ 0 ] )
    tree.Branch( 'offPUPPIMht_phi', offPUPPIMht_phi, 'offPUPPIMht_phi/F' )
    offPUPPIMht_sumet = array( 'f', [ 0 ] )
    tree.Branch( 'offPUPPIMht_sumet', offPUPPIMht_sumet, 'offPUPPIMht_sumet/F' )
    
    caloJet_num = array( 'i', [ 0 ] )
    tree.Branch( 'caloJet_num', caloJet_num, 'caloJet_num/I' )
    caloJet_pt = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'caloJet_pt', caloJet_pt, 'caloJet_pt[caloJet_num]/F' )
    caloJet_eta = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'caloJet_eta', caloJet_eta, 'caloJet_eta[caloJet_num]/F' )
    caloJet_phi = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'caloJet_phi', caloJet_phi, 'caloJet_phi[caloJet_num]/F' )
    caloJet_mass = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'caloJet_mass', caloJet_mass, 'caloJet_mass[caloJet_num]/F' )
    caloJet_offmatch = array( 'i', maxJets*[ 0 ] )
    tree.Branch( 'caloJet_offmatch', caloJet_offmatch, 'caloJet_offmatch[caloJet_num]/I' )
    caloJet_btagged ={}
    for calobjet in calobjets:
        caloJet_btagged[calobjet] = array( 'f', maxJets*[ 0 ] )
        tree.Branch( 'caloJet_'+calobjet, caloJet_btagged[calobjet], 'caloJet_'+calobjet+'[caloJet_num]/F' )
    
    pfJet_num = array( 'i', [ 0 ] )
    tree.Branch( 'pfJet_num', pfJet_num, 'pfJet_num/I' )
    pfJet_pt = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'pfJet_pt', pfJet_pt, 'pfJet_pt[pfJet_num]/F' )
    pfJet_eta = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'pfJet_eta', pfJet_eta, 'pfJet_eta[pfJet_num]/F' )
    pfJet_phi = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'pfJet_phi', pfJet_phi, 'pfJet_phi[pfJet_num]/F' )
    pfJet_mass = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'pfJet_mass', pfJet_mass, 'pfJet_mass[pfJet_num]/F' )
    onPFJet_csv = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'onPFJet_csv', onPFJet_csv, 'onPFJet_csv[pfJet_num]/F' )
    onPFJet_deepcsv = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'onPFJet_deepcsv', onPFJet_deepcsv, 'onPFJet_deepcsv[pfJet_num]/F' )
    pfJet_offmatch = array( 'i', maxJets*[ 0 ] )
    tree.Branch( 'pfJet_offmatch', pfJet_offmatch, 'pfJet_offmatch[pfJet_num]/I' )
    pfJet_btagged ={}
    for pfbjet in pfbjets:
        pfJet_btagged[pfbjet] = array( 'f', maxJets*[ 0 ] )
        tree.Branch( 'pfJet_'+pfbjet, pfJet_btagged[pfbjet], 'pfJet_'+pfbjet+'[pfJet_num]/F' )
    
    offJet_num = array( 'i', [ 0 ] )
    tree.Branch( 'offJet_num', offJet_num, 'offJet_num/I' )
    offJet_pt = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'offJet_pt', offJet_pt, 'offJet_pt[offJet_num]/F' )
    offJet_eta = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'offJet_eta', offJet_eta, 'offJet_eta[offJet_num]/F' )
    offJet_phi = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'offJet_phi', offJet_phi, 'offJet_phi[offJet_num]/F' )
    offJet_mass = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'offJet_mass', offJet_mass, 'offJet_mass[offJet_num]/F' )
    offJet_csv = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'offJet_csv', offJet_csv, 'offJet_csv[offJet_num]/F' )
    offJet_deepcsv = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'offJet_deepcsv', offJet_deepcsv, 'offJet_deepcsv[offJet_num]/F' )
    offJet_pfmatch = array( 'i', maxJets*[ 0 ] )
    tree.Branch( 'offJet_pfmatch', offJet_pfmatch, 'offJet_pfmatch[offJet_num]/I' )
    offJet_calomatch = array( 'i', maxJets*[ 0 ] )
    tree.Branch( 'offJet_calomatch', offJet_calomatch, 'offJet_calomatch[offJet_num]/I' )
    offJet_l1match = array( 'i', maxJets*[ 0 ] )
    tree.Branch( 'offJet_l1match', offJet_l1match, 'offJet_l1match[offJet_num]/I' )

    
    offElectron_num = array( 'i', [ 0 ] )
    tree.Branch( 'offElectron_num', offElectron_num, 'offElectron_num/I' )
    offElectron_pt = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'offElectron_pt', offElectron_pt, 'offElectron_pt[offElectron_num]/F' )
    offElectron_eta = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'offElectron_eta', offElectron_eta, 'offElectron_eta[offElectron_num]/F' )
    offElectron_phi = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'offElectron_phi', offElectron_phi, 'offElectron_phi[offElectron_num]/F' )
    offElectron_iso = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'offElectron_iso', offElectron_iso, 'offElectron_iso[offElectron_num]/F' )
    
    offMuon_num = array( 'i', [ 0 ] )
    tree.Branch( 'offMuon_num', offMuon_num, 'offMuon_num/I' )
    offMuon_pt = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'offMuon_pt', offMuon_pt, 'offMuon_pt[offMuon_num]/F' )
    offMuon_eta = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'offMuon_eta', offMuon_eta, 'offMuon_eta[offMuon_num]/F' )
    offMuon_phi = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'offMuon_phi', offMuon_phi, 'offMuon_phi[offMuon_num]/F' )
    offMuon_iso = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'offMuon_iso', offMuon_iso, 'offMuon_iso[offMuon_num]/F' )
    
    offPhoton_num = array( 'i', [ 0 ] )
    tree.Branch( 'offPhoton_num', offPhoton_num, 'offPhoton_num/I' )
    offPhoton_pt = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'offPhoton_pt', offPhoton_pt, 'offPhoton_pt[offPhoton_num]/F' )
    offPhoton_eta = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'offPhoton_eta', offPhoton_eta, 'offPhoton_eta[offPhoton_num]/F' )
    offPhoton_phi = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'offPhoton_phi', offPhoton_phi, 'offPhoton_phi[offPhoton_num]/F' )
    offPhoton_iso = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'offPhoton_iso', offPhoton_iso, 'offPhoton_iso[offPhoton_num]/F' )
    
    
    offPUPPIMet = array( 'f', [ 0 ] )
    tree.Branch( 'offPUPPIMet', offPUPPIMet, 'offPUPPIMet/F' )
    offPUPPIMet_phi = array( 'f', [ 0 ] )
    tree.Branch( 'offPUPPIMet_phi', offPUPPIMet_phi, 'offPUPPIMet_phi/F' )
    offPUPPIMet_sig = array( 'f', [ 0 ] )
    tree.Branch( 'offPUPPIMet_sig', offPUPPIMet_sig, 'offPUPPIMet_sig/F' )
    offPUPPIMet_sumet = array( 'f', [ 0 ] )
    tree.Branch( 'offPUPPIMet_sumet', offPUPPIMet_sumet, 'offPUPPIMet_sumet/F' )
    
    offPUPPIJet_num = array( 'i', [ 0 ] )
    tree.Branch( 'offPUPPIJet_num', offPUPPIJet_num, 'offPUPPIJet_num/I' )
    offPUPPIJet_pt = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'offPUPPIJet_pt', offPUPPIJet_pt, 'offPUPPIJet_pt[offPUPPIJet_num]/F' )
    offPUPPIJet_eta = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'offPUPPIJet_eta', offPUPPIJet_eta, 'offPUPPIJet_eta[offPUPPIJet_num]/F' )
    offPUPPIJet_phi = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'offPUPPIJet_phi', offPUPPIJet_phi, 'offPUPPIJet_phi[offPUPPIJet_num]/F' )
    offPUPPIJet_mass = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'offPUPPIJet_mass', offPUPPIJet_mass, 'offPUPPIJet_mass[offPUPPIJet_num]/F' )
    offPUPPIJet_csv = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'offPUPPIJet_csv', offPUPPIJet_csv, 'offPUPPIJet_csv[offPUPPIJet_num]/F' )
    
    triggerBits, triggerBitLabel = Handle("edm::TriggerResults"), ("TriggerResults::%s"%HLTprocess)
    triggerObjects, triggerObjectLabel  = Handle("std::vector<pat::TriggerObjectStandAlone>"), "selectedPatTrigger"
    triggerPrescales, triggerPrescaleLabel  = Handle("pat::PackedTriggerPrescales"), "patTrigger"
    
    lumiscaler, lumiscalerLabel = Handle("vector<LumiScalers>"), ("scalersRawToDigi")

    patJets, patJetLabel = Handle("vector<reco::PFJet>"), ("ak4PFJets") #AOD

    l1Jets, l1JetLabel = Handle("BXVector<l1t::Jet>"), ("caloStage2Digis:Jet") #AOD
    l1Taus, l1TauLabel = Handle("BXVector<l1t::Tau>"), ("caloStage2Digis:Tau") #AOD
    l1EGammas, l1EGammaLabel = Handle("BXVector<l1t::EGamma>"), ("caloStage2Digis:EGamma") #AOD
    l1EtSums, l1EtSumLabel = Handle("BXVector<l1t::EtSum>"), ("caloStage2Digis:EtSum") #AOD
    l1Muons, l1MuonLabel = Handle("BXVector<l1t::Muon>"), ("gmtStage2Digis:Muon") #AOD

    patMets, patMetLabel = Handle("vector<reco::PFMET>"), ("pfMet") #AOD
    recoVertexs, recoVertexLabel = Handle("vector<reco::Vertex>"), ("offlinePrimaryVertices") #AOD
    patElectrons, patElectronLabel = Handle("vector<reco::GsfElectron>"), ("gedGsfElectrons") #AOD
    patMuons, patMuonLabel = Handle("vector<reco::Muon>"), ("muons") #AOD
    patPhotons, patPhotonLabel = Handle("vector<reco::Photon>"), ("photons") #AOD
    
    ##load file
    if len(filesInput)==0: return
    events = Events (filesInput)

    ##get triggerNames from the first event
    events.to(0)
    for event in events: break
    triggerEvent, triggerEventLabel = Handle("trigger::TriggerEvent"), ("hltTriggerSummaryAOD::%s"%HLTprocess)
    event.getByLabel(triggerBitLabel, triggerBits)
    triggerBits.product()
    names = event.object().triggerNames(triggerBits.product())
    triggerNames = names.triggerNames()
    for name in triggerNames: name = name.split("_v")[0]
    nTriggers = len(triggerNames)

#    ##get filters from the first event
#    event.getByLabel(triggerEventLabel, triggerEvent) ## AOD
#    for i in range(triggerEvent.product().sizeFilters()): filters.append(triggerEvent.product().filterLabel(i))
    
    ##
    triggerVars = {}
    for trigger in triggerNames:
        triggerVars[trigger]=array( 'i', [ 0 ] )
        tree.Branch( trigger[:-3], triggerVars[trigger], trigger[:-3]+'/O' )

    filterVars = {}
    for filter_ in filters:
        filterVars[filter_]=array( 'i', [ 0 ] )
        tree.Branch( filter_, filterVars[filter_], filter_+'/I' )
    
    skipL1 = False
    memOld = 0
    ##event loop
    for iev,event in enumerate(events):
        if iev%1000==0:
            print "iev=",iev
            memNew = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
            print 'Memory usage: %s (MB)'% (memNew/1000)
            print 'Diff', (memNew-memOld)/1000
            memOld = memNew
        if iev>maxevents: break
        event.getByLabel(triggerBitLabel, triggerBits)
            
#        event.getByLabel(triggerObjectLabel, triggerObjects)
#        event.getByLabel(triggerPrescaleLabel, triggerPrescales)
        event.getByLabel(triggerEventLabel, triggerEvent) ## AOD
        event.getByLabel(patJetLabel, patJets)
        event.getByLabel(patMetLabel, patMets)
        event.getByLabel(recoVertexLabel, recoVertexs)
        event.getByLabel(patElectronLabel, patElectrons)
        event.getByLabel(patMuonLabel, patMuons)
        event.getByLabel(patPhotonLabel, patPhotons)
        event.getByLabel(lumiscalerLabel, lumiscaler)        
        ## AOD
        event.getByLabel(btagLabel, btags)
        event.getByLabel(btagLabel_b, btags_b)
        event.getByLabel(btagLabel_bb, btags_bb)
        ##RAW
        event.getByLabel(processname, btagLabelCSVOnline, btagsCSVOnline)
        event.getByLabel(processname, btagLabelDCSVOnline, btagsDCSVOnline)

        nVertices[0] = recoVertexs.product().size()
        run[0] = event.eventAuxiliary().run()
        lumi[0] = event.eventAuxiliary().luminosityBlock()
        eventNumber[0] = event.eventAuxiliary().event()
        if not MC: 
            bx[0] = event.eventAuxiliary().bunchCrossing()
            instLumi[0] = lumiscaler.product().begin().instantLumi()
            JSON[0] = goodEvent(event.eventAuxiliary().run(),event.eventAuxiliary().luminosityBlock())
        
        i=0
        offJet_num[0] = 0
        for jet in patJets.product():
            if jet.pt()<20: continue
            if i<maxJets:                
                offJet_pt[i] = jet.pt()
                offJet_eta[i] = jet.eta()
                offJet_phi[i] = jet.phi()
                offJet_mass[i] = jet.mass()
                ## AOD
                offlineCSV = -1.
                offlineDeepCSV = -1.
                offlineDeepCSV_b = -1.
                offlineDeepCSV_bb = -1.
                for j in range(0,btags.product().size()):
                    jetB = btags.product().key(j).get()
                    dR = deltaR(jetB.eta(),jetB.phi(),jet.eta(),jet.phi())
                    if dR<0.3:
                        offlineCSV = max(0.,btags.product().value(j))
                        break
                for j in range(0,btags_b.product().size()):
                    jetB = btags_b.product().key(j).get()
                    dR = deltaR(jetB.eta(),jetB.phi(),jet.eta(),jet.phi())
                    if dR<0.3:
                        offlineDeepCSV_b = max(0.,btags_b.product().value(j))
                        break
                for j in range(0,btags_bb.product().size()):
                    jetB = btags_bb.product().key(j).get()
                    dR = deltaR(jetB.eta(),jetB.phi(),jet.eta(),jet.phi())
                    if dR<0.3:
                        offlineDeepCSV_bb = max(0.,btags_bb.product().value(j))
                        break
                offlineDeepCSV = offlineDeepCSV_b + offlineDeepCSV_bb
                offJet_deepcsv[i] = offlineDeepCSV
                offJet_csv[i] = offlineCSV
                offJet_num[0] = i + 1
                i+=1
        i=0
        offMuon_num[0] = 0
        for muon in patMuons.product():
            if muon.pt()<10: continue
            if i<maxJets:
                offMuon_pt[i] = muon.pt()
                offMuon_eta[i] = muon.eta()
                offMuon_phi[i] = muon.phi()
#                print muon.pfIsolationR03()
                if isLooseMuon(muon):
                    offMuon_iso[i] = 1
                else:
                    offMuon_iso[i] = 0
#                pfIsolationR04()
                offMuon_num[0] = i + 1
                i+=1
        
        i=0
        offElectron_num[0] = 0
        for electron in patElectrons.product():
            if electron.pt()<10: continue
            if i<maxJets:
                offElectron_pt[i] = electron.pt()
                offElectron_eta[i] = electron.eta()
                offElectron_phi[i] = electron.phi()
                offElectron_iso[i] = electron.mva_Isolated() 
                offElectron_num[0] = i + 1
                i+=1

        i=0
        offPhoton_num[0] = 0
        for photon in patPhotons.product():
            if photon.pt()<10: continue
            if i<maxJets:
                offPhoton_pt[i] = photon.pt()
                offPhoton_eta[i] = photon.eta()
                offPhoton_phi[i] = photon.phi()
                offPhoton_iso[i] = photon.photonIso()
                offPhoton_num[0] = i + 1
                i+=1
                
        offMet[0] = patMets.product().begin().pt()
        offMet_phi[0] = patMets.product().begin().phi()
        offMet_sumet[0] = patMets.product().begin().sumEt()
        offMet_sig[0] = patMets.product().begin().significance()
        
        MHT2D = ROOT.TVector2()
        jet2D = ROOT.TVector2()
        offMht_sumet[0]=0
        for jet in patJets.product():
            if jet.pt()>pt_min and abs(jet.eta())<eta_max \
            and jet.neutralHadronEnergyFraction()<NHFmax \
            and jet.neutralEmEnergyFraction()<NEMFmax \
            and jet.chargedHadronEnergyFraction()>CHFmin \
            and jet.muonEnergyFraction()<MUFmax \
            and jet.chargedEmEnergyFraction()<CEMFmax \
            and jet.chargedMultiplicity()+jet.neutralMultiplicity()>NumConstMin \
            and jet.chargedMultiplicity()>CHMmin :
                jet2D.SetMagPhi(jet.pt(),jet.phi())
                MHT2D = MHT2D - jet2D
                offMht_sumet[0]+=jet.pt()
        
        offMht[0] = MHT2D.Mod()
        offMht_phi[0] = MHT2D.Phi()
        
        calojetCollection = "hltAK4CaloJetsCorrectedIDPassed"
        calojetCollectionForBtag = "hltSelector8CentralJetsL1FastJet"
        trigObjColl = triggerEvent.product().getObjects()
        collectionKeys = getCollectionKeys(triggerEvent.product(),ROOT.edm.InputTag(calojetCollection,"",HLTprocess))
        collectionKeysForBtag = getCollectionKeys(triggerEvent.product(),ROOT.edm.InputTag(calojetCollectionForBtag,"",HLTprocess))
        i=0
        caloJet_num[0] = 0
        for keys in collectionKeys:
            caloJet = trigObjColl[keys]
            if caloJet.pt()<20: continue
            if i<maxJets:
                caloJet_pt[i] = caloJet.pt()
                caloJet_eta[i] = caloJet.eta()
                caloJet_phi[i] = caloJet.phi()
                caloJet_mass[i] = caloJet.mass()
                caloJet_offmatch[i] = matching(caloJet.eta(),caloJet.phi(),offJet_eta,offJet_phi,offJet_num[0])
                caloJet_num[0] = i+1 
                for calobjet in calobjets:
                    caloJet_btagged[calobjet][i] = -1
                    filterIndex = triggerEvent.product().filterIndex(ROOT.edm.InputTag(calobjet,"",HLTprocess))
                    if filterIndex < triggerEvent.product().sizeFilters():
                        for key3 in collectionKeysForBtag:
                            jetForBtag = trigObjColl[key3];
                            dR = deltaR(jetForBtag.eta(),jetForBtag.phi(),caloJet.eta(),caloJet.phi())
                            if dR<0.3:
                                caloJet_btagged[calobjet][i] = 0
                                break
                        filterKeys = triggerEvent.product().filterKeys(filterIndex)
                        for key2 in filterKeys:
                            bjet = trigObjColl[key2];
                            dR = deltaR(bjet.eta(),bjet.phi(),caloJet.eta(),caloJet.phi())
                            if dR<0.3:
                                caloJet_btagged[calobjet][i] = 1
                                break
            i+=1
        pfjetCollection = "hltAK4PFJetsCorrected"
        pfjetCollectionForBtag = "hltPFJetForBtag"
        trigObjColl = triggerEvent.product().getObjects()
        collectionKeys = getCollectionKeys(triggerEvent.product(),ROOT.edm.InputTag(pfjetCollection,"",HLTprocess))
        collectionKeysForBtag = getCollectionKeys(triggerEvent.product(),ROOT.edm.InputTag(pfjetCollectionForBtag,"",HLTprocess))
        i=0
        pfJet_num[0] = 0
        for keys in collectionKeys:
            pfJet = trigObjColl[keys]
            if pfJet.pt()<20: continue
            if i<maxJets:
                pfJet_pt[i] = pfJet.pt()
                pfJet_eta[i] = pfJet.eta()
                pfJet_phi[i] = pfJet.phi()
                pfJet_mass[i] = pfJet.mass()
                onlineCSV = -1.
                onlineDeepCSV = -1.
                for j in range(0,btagsCSVOnline.product().size()):
                    jetB = btagsCSVOnline.product().key(j).get()
                    dR = deltaR(jetB.eta(),jetB.phi(),jet.eta(),jet.phi())
                    if dR<0.3:
                        onineCSV = max(0.,btagsCSVOnline.product().value(j))
                        break
                for j in range(0,btagsDCSVOnline.product().size()):
                    jetB = btagsDCSVOnline.product().key(j).get()
                    dR = deltaR(jetB.eta(),jetB.phi(),jet.eta(),jet.phi())
                    if dR<0.3:
                        onineDeepCSV = max(0.,btagsDCSVOnline.product().value(j))
                        break
                onPFJet_csv[i] = onlineCSV
                onPFJet_deepcsv[i] = onlineDeepCSV
                pfJet_offmatch[i] = matching(pfJet.eta(),pfJet.phi(),offJet_eta,offJet_phi,offJet_num[0])
                pfJet_num[0] = i+1
                for pfbjet in pfbjets:
                    pfJet_btagged[pfbjet][i] = -1
                    filterIndex = triggerEvent.product().filterIndex(ROOT.edm.InputTag(pfbjet,"",HLTprocess))
                    if filterIndex < triggerEvent.product().sizeFilters():
                        for key3 in collectionKeysForBtag:
                            jetForBtag = trigObjColl[key3];
                            dR = deltaR(jetForBtag.eta(),jetForBtag.phi(),pfJet.eta(),pfJet.phi())
                            if dR<0.3:
                                pfJet_btagged[pfbjet][i] = 0
                                break
                        filterKeys = triggerEvent.product().filterKeys(filterIndex)
                        for key2 in filterKeys:
                            bjet = trigObjColl[key2];
                            dR = deltaR(bjet.eta(),bjet.phi(),pfJet.eta(),pfJet.phi())
                            if dR<0.3:
                                pfJet_btagged[pfbjet][i] = 1
                                break
            i+=1
        
        for i in range(offJet_num[0]):
            offJet_pfmatch[i] = matching(offJet_eta[i],offJet_phi[i],pfJet_eta,pfJet_phi,pfJet_num[0])
            offJet_calomatch[i] = matching(offJet_eta[i],offJet_phi[i],caloJet_eta,caloJet_phi,caloJet_num[0])
        
        caloMETCollection = "hltMet"
        caloMet[0],caloMet_phi[0] = getMET(triggerEvent.product(),ROOT.edm.InputTag(caloMETCollection,"",HLTprocess))
        
        caloMHTCollection = "hltHtMht"
        caloMht[0],caloMht_phi[0] = getMET(triggerEvent.product(),ROOT.edm.InputTag(caloMHTCollection,"",HLTprocess))

        caloNoPuMHTCollection = "hltMHTNoPU"
        caloNoPuMht[0],caloNoPuMht_phi[0] = getMET(triggerEvent.product(),ROOT.edm.InputTag(caloNoPuMHTCollection,"",HLTprocess))

        pfMETCollection = "hltPFMETProducer"
        pfMet[0],pfMet_phi[0] = getMET(triggerEvent.product(),ROOT.edm.InputTag(pfMETCollection,"",HLTprocess))
        
        pfMHTCollection = "hltPFMHTTightID"
        pfMht[0],pfMht_phi[0] = getMET(triggerEvent.product(),ROOT.edm.InputTag(pfMHTCollection,"",HLTprocess))

	if not skipL1:
	 try:
          event.getByLabel(l1JetLabel, l1Jets)
          i=0
          l1Jet_num[0] = 0
          for i in range(l1Jets.product().size(0)):
            l1Jet = l1Jets.product().at(0,i)
            l1Jet_pt[i] = l1Jet.pt()
            l1Jet_eta[i] = l1Jet.eta()
            l1Jet_phi[i] = l1Jet.phi()
            l1Jet_mass[i] = l1Jet.mass()
            l1Jet_offmatch[i] = matching(l1Jet.eta(),l1Jet.phi(),offJet_eta,offJet_phi,offJet_num[0])
            l1Jet_num[0] = i+1
            i+=1

          event.getByLabel(l1TauLabel, l1Taus)
          i=0
          l1Tau_num[0] = 0
          for i in range(l1Taus.product().size(0)):
            l1Tau = l1Taus.product().at(0,i)
            l1Tau_pt[i] = l1Tau.pt()
            l1Tau_eta[i] = l1Tau.eta()
            l1Tau_phi[i] = l1Tau.phi()
            l1Tau_mass[i] = l1Tau.mass()
            l1Tau_offmatch[i] = matching(l1Tau.eta(),l1Tau.phi(),offJet_eta,offJet_phi,offJet_num[0])
            l1Tau_num[0] = i+1
            i+=1

          event.getByLabel(l1MuonLabel, l1Muons)
          i=0
          l1Muon_num[0] = 0
          for i in range(l1Muons.product().size(0)):
            l1Muon = l1Muons.product().at(0,i)
            l1Muon_pt[i] = l1Muon.pt()
            l1Muon_eta[i] = l1Muon.eta()
            l1Muon_phi[i] = l1Muon.phi()
            l1Muon_iso[i] = l1Muon.hwIsoSum()
            l1Muon_offmatch[i] = matching(l1Muon.eta(),l1Muon.phi(),offJet_eta,offJet_phi,offJet_num[0])
            l1Muon_num[0] = i+1
            i+=1

          event.getByLabel(l1EGammaLabel, l1EGammas)
          i=0
          l1EGamma_num[0] = 0
          for i in range(l1EGammas.product().size(0)):
            l1EGamma = l1EGammas.product().at(0,i)
            l1EGamma_pt[i] = l1EGamma.pt()
            l1EGamma_eta[i] = l1EGamma.eta()
            l1EGamma_phi[i] = l1EGamma.phi()
            l1EGamma_mass[i] = l1EGamma.mass()
            l1EGamma_iso[i] = l1EGamma.isoEt()
            l1EGamma_offmatch[i] = matching(l1EGamma.eta(),l1EGamma.phi(),offJet_eta,offJet_phi,offJet_num[0])
            l1EGamma_num[0] = i+1
            i+=1

          event.getByLabel(l1EtSumLabel, l1EtSums)
          MET2,MET,ET,MHT,HT = 0,0,0,0,0
          for i in range(l1EtSums.product().size(0)):
            l1Obj = l1EtSums.product().at(0,i)
            l1ObjType = l1Obj.getType()
            if l1ObjType == l1Obj.kMissingEt2:
                MET2 = l1Obj
            elif l1ObjType == l1Obj.kMissingEt:
                MET = l1Obj
            elif l1ObjType == l1Obj.kMissingHt:
                MHT = l1Obj
            elif l1ObjType == l1Obj.kTotalEt:
                ET = l1Obj
            elif l1ObjType == l1Obj.kTotalHt:
                HT = l1Obj

          if MET2:
            l1MET2[0] = MET2.pt()
            l1MET2_phi[0] = MET2.phi()
          if MET:
            l1MET[0] = MET.pt()
            l1MET_phi[0] = MET.phi()
          if ET:
            l1ET[0] = ET.pt()
          if MHT:
            l1MHT[0] = MHT.pt()
            l1MHT_phi[0] = MHT.phi()
          if HT:
            l1HT[0] = HT.pt()
	 except:
	  skipL1=True

        names = event.object().triggerNames(triggerBits.product())
        for i,triggerName in enumerate(triggerNames):
            index = names.triggerIndex(triggerName)
            if checkTriggerIndex(triggerName,index,names.triggerNames()):
                triggerVars[triggerName][0] = triggerBits.product().accept(index)
            else:
                triggerVars[triggerName][0] = 0
        
        for filter_ in filters:
            filterVars[filter_][0] = getSizeFilter(triggerEvent.product(),ROOT.edm.InputTag(filter_,"",HLTprocess))
        
#        if triggerVars["HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDLoose_v1"][0]:
#        if triggerVars['HLT_QuadPFJet_SingleBTagCSV_VBF_Mqq500_v2'][0]:
#            printLabelCollections(triggerEvent.product())
#            printLabelFilters(triggerEvent.product())

        tree.Fill()
    
    
    f.Write()
    f.Close()

#maxevents=200
#fileOutput = 'tree.root'
#filesInput=[
#]
#launchNtupleFromAOD(fileOutput,filesInput,maxevents)
