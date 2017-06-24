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
    JSONlist={"273158": [[1, 1279]],
 "273302": [[1, 459]],
 "273402": [[100, 292]],
 "273403": [[1, 53]],
 "273404": [[1, 18]],
 "273405": [[2, 25]],
 "273406": [[1, 112]],
 "273408": [[1, 6]],
 "273409": [[1, 309]],
 "273410": [[1, 90]],
 "273411": [[1, 29]],
 "273425": [[62, 352], [354, 733]],
 "273446": [[1, 33]],
 "273447": [[1, 113], [115, 412]],
 "273448": [[1, 391]],
 "273449": [[1, 214]],
 "273450": [[1, 214], [219, 647]],
 "273492": [[71, 71], [73, 282], [284, 325], [327, 338]],
 "273493": [[1, 233]],
 "273494": [[1, 192]],
 "273502": [[73, 256], [258, 318], [320, 813], [815, 1064]],
 "273503": [[1, 598]],
 "273554": [[77, 437]],
 "273555": [[1, 173]],
 "273725": [[83, 252], [254, 2545]],
 "273728": [[1, 100]],
 "273730": [[1, 1814], [1820, 2126]],
 "274094": [[108, 332]],
 "274146": [[1, 67]],
 "274159": [[1, 43]],
 "274160": [[1, 207]],
 "274161": [[1, 516]],
 "274172": [[31, 95]],
 "274198": [[81, 191]],
 "274199": [[1, 623]],
 "274200": [[1, 678]],
 "274240": [[1, 40], [42, 82]],
 "274241": [[1, 1152], [1161, 1176]],
 "274244": [[1, 607]],
 "274250": [[1, 701]],
 "274251": [[1, 546]],
 "274283": [[2, 19]],
 "274284": [[1, 210]],
 "274286": [[1, 154]],
 "274314": [[97, 97], [99, 158]],
 "274315": [[1, 424]],
 "274316": [[1, 959]],
 "274317": [[1, 3]],
 "274319": [[1, 225]],
 "274335": [[60, 1003]],
 "274336": [[1, 14]],
 "274337": [[3, 17]],
 "274338": [[1, 698]],
 "274339": [[1, 29], [31, 31], [33, 33], [35, 93]],
 "274344": [[1, 632]],
 "274345": [[1, 170]],
 "274382": [[94, 144]],
 "274387": [[88, 439]],
 "274388": [[1, 1820]],
 "274420": [[94, 268]],
 "274421": [[1, 342]],
 "274422": [[1, 2207]],
 "274440": [[92, 493]],
 "274441": [[1, 431]],
 "274442": [[1, 752]],
 "274954": [[37, 37], [39, 57]],
 "274955": [[1, 91]],
 "274968": [[1, 1192]],
 "274969": [[1, 1003]],
 "274970": [[1, 47]],
 "274971": [[1, 905]],
 "274998": [[64, 782]],
 "274999": [[1, 1241]],
 "275000": [[1, 136]],
 "275001": [[1, 1781], [1786, 2061]],
 "275059": [[78, 81], [105, 137]],
 "275066": [[1, 96]],
 "275067": [[1, 392]],
 "275068": [[1, 915]],
 "275073": [[1, 517]],
 "275074": [[1, 442], [444, 647]],
 "275124": [[106, 106], [108, 431]],
 "275125": [[1, 989]],
 "275282": [[91, 180]],
 "275283": [[1, 132]],
 "275284": [[1, 74]],
 "275290": [[96, 143]],
 "275291": [[1, 347]],
 "275292": [[1, 121]],
 "275293": [[1, 142], [144, 201]],
 "275309": [[55, 617]],
 "275310": [[1, 1929]],
 "275311": [[1, 1253]],
 "275319": [[141, 282]],
 "275337": [[1, 427]],
 "275338": [[1, 520]],
 "275344": [[76, 356]],
 "275345": [[1, 353]],
 "275370": [[81, 365]],
 "275371": [[1, 22], [28, 569]],
 "275375": [[127, 1449]],
 "275376": [[1, 2667], [2669, 3096]],
 "275657": [[1, 105]],
 "275658": [[1, 337]],
 "275659": [[1, 17]],
 "275761": [[1, 9]],
 "275767": [[1, 4]],
 "275772": [[1, 56]],
 "275773": [[1, 7]],
 "275774": [[1, 311], [315, 315]],
 "275776": [[1, 140]],
 "275777": [[1, 300]],
 "275778": [[1, 305]],
 "275782": [[1, 131], [133, 762]],
 "275832": [[1, 367]],
 "275833": [[1, 53], [56, 115], [117, 251]],
 "275834": [[1, 297]],
 "275835": [[1, 13]],
 "275836": [[1, 429], [431, 1163], [1166, 1170], [1184, 1293]],
 "275837": [[1, 186], [198, 726]],
 "275847": [[1, 2263]],
 "275886": [[73, 109]],
 "275890": [[1, 1393]],
 "275911": [[62, 298], [300, 354], [356, 440]],
 "275912": [[1, 289]],
 "275913": [[1, 475]],
 "275918": [[1, 318], [348, 361]],
 "275920": [[5, 463]],
 "275921": [[1, 2], [4, 5], [17, 20]],
 "275923": [[3, 53], [63, 64], [66, 126]],
 "275931": [[1, 14], [19, 89]],
 "275963": [[82, 139], [141, 172]],
 "276092": [[74, 149]],
 "276097": [[1, 507]],
 "276242": [[1, 7], [18, 61], [72, 1664]],
 "276243": [[1, 15], [18, 480], [482, 611]],
 "276244": [[3, 1202]],
 "276282": [[75, 534], [537, 1142]],
 "276283": [[3, 1087]],
 "276315": [[40, 175], [178, 217]],
 "276317": [[3, 138]],
 "276318": [[3, 103], [106, 570]],
 "276355": [[1, 33]],
 "276361": [[1, 161], [169, 208], [210, 800], [802, 833]],
 "276363": [[1, 140], [142, 238], [242, 1482]],
 "276384": [[2, 1117]]}

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
    'hltBTagCaloCSVp05Double', # from HLT_HT300PT30_QuadJet_75_60_45_40_TripeCSV_p07
    'hltBTagCaloCSVp44Single', # HLT_PFHT380_SixJet32_DoubleBTagCSV_p075
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
    'hltBTagPFCSVp070Triple', # from HLT_HT300PT30_QuadJet_75_60_45_40_TripeCSV_p07
    'hltBTagPFCSVp075Double', # from HLT_PFHT380_SixJet32_DoubleBTagCSV_p075_v1
    'hltBTagPFCSVp080Single', # from HLT_PFHT430_SixJet40_BTagCSV_p080_v1
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
    HLTprocess = "HLT"
    if len(filesInput)>0 and ('reHLT' in filesInput[0]):
        HLTprocess = "HLT2"
    print "HLTprocess=",HLTprocess
    
    btags, btagLabel = Handle("edm::AssociationVector<edm::RefToBaseProd<reco::Jet>,vector<float>,edm::RefToBase<reco::Jet>,unsigned int,edm::helper::AssociationIdenticalKeyReference>"), ("pfCombinedInclusiveSecondaryVertexV2BJetTags") #("pfCombinedSecondaryVertexBJetTags")
    
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
                for j in range(0,btags.product().size()):
                    jetB = btags.product().key(j).get()
                    dR = deltaR(jetB.eta(),jetB.phi(),jet.eta(),jet.phi())
                    if dR<0.3:
                        offlineCSV = max(0.,btags.product().value(j))
                        break
                
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
        for key in collectionKeys:
            caloJet = trigObjColl[key]
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
        for key in collectionKeys:
            pfJet = trigObjColl[key]
            if pfJet.pt()<20: continue
            if i<maxJets:
                pfJet_pt[i] = pfJet.pt()
                pfJet_eta[i] = pfJet.eta()
                pfJet_phi[i] = pfJet.phi()
                pfJet_mass[i] = pfJet.mass()
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
