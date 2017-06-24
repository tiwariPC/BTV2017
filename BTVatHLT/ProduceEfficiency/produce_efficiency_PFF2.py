import sys
import math
import ROOT
import matplotlib.pyplot as plt

from ROOT import TH1F, TH2F
from matplotlib.pyplot import figure, show
from numpy import arange, sin, pi

# Performances of the PF online b-tagging sequence based on events triggered by PFHT800, and studying the CSV cut of the HLT_PFHT450_SixJet40_BTagCSV_p056

def main() :

    # Files
    f_ntuple            = ROOT.TFile("ntupleTest2017BTuned50000.root",    	 "READ")
    f_results           = ROOT.TFile("results2017B_PF.root",     	     "RECREATE")
    f_results.cd()

    # Functions
    makePlots(f_ntuple,  f_results)

def makePlots(f_ntuple, f_results) :

    t = f_ntuple.Get("tree")
    print "Tree extracted..."

    h_csvbeforefilter      = TH1F("h_csvbeforefilter",    "h_csvbeforefilter",     50,  0,  1)
    h_csvafterfilter       = TH1F("h_csvafterfilter",     "h_csvafterfilter",      50,  0,  1)
    h_csvbeforefilterlog   = TH1F("h_csvbeforefilterlog", "h_csvbeforefilterlog",  50,  0,  7)
    h_csvafterfilterlog    = TH1F("h_csvafterfilterlog",  "h_csvafterfilterlog",   50,  0,  7)
    h_csvratiolog          = TH1F("h_csvratiolog",        "h_csvratiolog",         50,  0,  7)

    i = 0

    for event in t:
        print "New event --------"
        
        #print
        #print "PF jets"
        #for i in range(0, event.pfJet_num) :
        #    print "i:       ", i
        #    print "pt:      ", event.pfJet_pt[i]
       	#    print "eta:     ", event.pfJet_eta[i]
        #    print "phi:     ", event.pfJet_phi[i]
        #    print "matched: ", event.pfJet_offmatch[i]

        #print
        #print "Offline jets"
        #for i in range(0, event.offJet_num) :
        #    print "i:       ", i
        #    print "pt:      ", event.offJet_pt[i]
        #    print "eta:     ", event.offJet_eta[i]
        #    print "phi:     ", event.offJet_phi[i]

	# FROM HLT_HT300PT30_QuadJet_75_60_45_40_TripeCSV_p07_v2

        if event.HLT_HT300PT30_QuadJet_75_60_45_40 :
		print "alright without b-tagging cut"
		
		for i in range(0,event.pfJet_num-1) :
			if event.pfJet_offmatch[i] >= 0 :
				print "event[", i, "]"
                       		print "event.pfJet_num:         ", event.pfJet_num
                         	print "event.pfJet_offmatch[i]: ", event.pfJet_offmatch[i]
                         	print "event.offJet_num:          ", event.offJet_num
                         	print "event.offJet_csv[matched]: ", event.offJet_csv[ event.pfJet_offmatch[i] ]
                         	print "event.offJet_pt[matched]:  ", event.offJet_pt[  event.pfJet_offmatch[i] ] 
                         	h_csvbeforefilter.Fill(                   event.offJet_csv[ event.pfJet_offmatch[i] ] )
                         	h_csvbeforefilterlog.Fill( -math.log( 1 - event.offJet_csv[ event.pfJet_offmatch[i] ] ) )
                         	if event.pfJet_hltBTagPFCSVp070Triple[i] :
                             		print "pass trigger"
                             		print "CSV:        ", event.offJet_csv[event.pfJet_offmatch[i]]
                             		print "online pT:  ", event.pfJet_pt[i]
                             		print "online eta: ", event.pfJet_eta[i]
                             		h_csvafterfilter.Fill(                   event.offJet_csv[ event.pfJet_offmatch[i] ] )
                             		h_csvafterfilterlog.Fill( -math.log( 1 - event.offJet_csv[ event.pfJet_offmatch[i] ] ) )

    h_csvratiolog = h_csvafterfilterlog.Clone()
    h_csvratiolog.Divide(h_csvbeforefilterlog)

    f_results.Write()

####################################

main()
