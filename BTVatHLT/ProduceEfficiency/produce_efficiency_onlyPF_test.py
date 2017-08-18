import sys
import math
import ROOT
import matplotlib.pyplot as plt

from ROOT import TH1F, TH2F, TEfficiency
from matplotlib.pyplot import figure, show
from numpy import arange, sin, pi

# Performance of the PF online b-tagging sequence based on events triggered by HLT_PFHT430_SixPFJet40, and studying the CSV cut of the HLT_PFHT430_SixPFJet40_PFBTagCSV_1p5 (hltBTagPFCSVp080Single)

def main() :

    # Files
    f_ntuple            = ROOT.TFile("ntupleTest2017C_2017_08_17_50k_JetHT.root",    	 "READ")
    f_results           = ROOT.TFile("results2017C_onlyPF_test_JetHT.root", 	     "RECREATE")
    f_results.cd()

    # Functions
    makePlots(f_ntuple,  f_results)

def makePlots(f_ntuple, f_results) :

    t = f_ntuple.Get("tree")
    print "Tree extracted..."

    h_csv_inc_4PF      	= TH1F("h_csv_inc_4PF",    		"h_csv_inc_4PF",     	50,  0,  1)
    h_csv_inc_log_4PF   = TH1F("h_csv_inc_log_4PF",    		"h_csv_inc_log_4PF",     	50,  0,  7)
    h_csv_inc_pf       	= TH1F("h_csv_inc_pf",  	"h_csv_inc_pf",      	50,  0,  1)
    h_csv_inc_pf_log	= TH1F("h_csv_inc_pf_log",  	"h_csv_inc_pf_log",     50,  0,  7)

    eff_csv_inc_pf      = TEfficiency("eff_csv_inc_pf",    "eff_csv_inc_pf",      	50,  0,  1)
    eff_csv_inc_pf_log	  = TEfficiency("eff_csv_inc_pf_log",    "eff_csv_inc_pf_log",     50,  0,  7)


    i = 0

    for event in t:
        print
	print "New event --------"
	print
        
        if not event.HLT_PFHT430_SixPFJet40 : continue

	print "PF JET SECTION : # pf jet = ", event.pfJet_num
	for i in range(0, event.pfJet_num-1) :	
		if event.pfJet_offmatch[i] >= 0 :
			print "pf jet[", i, "]"
			print "event.pfJet_offmatch[i]: ", 	event.pfJet_offmatch[i], 	" event.offJet_num: ", 	event.offJet_num
			print "pf pt: ", 			event.pfJet_pt[i], 		" offline pt: ",	event.offJet_pt[  event.pfJet_offmatch[i] ]
			print "pf eta: ",			event.pfJet_eta[i],		" offline eta: ",	event.offJet_eta[ event.pfJet_offmatch[i] ]
			print "pf phi: ",			event.pfJet_phi[i],		" offline phi: ",	event.offJet_phi[ event.pfJet_offmatch[i] ]
			print "offline csv: ", 			event.offJet_csv[  event.pfJet_offmatch[i] ]

                        if event.offJet_pt[  event.pfJet_offmatch[i] ] < 30 : continue

                        passed = False

			h_csv_inc_4PF.Fill( 			event.offJet_csv[ event.pfJet_offmatch[i] ] )
                        if event.offJet_csv[ event.pfJet_offmatch[i] ] < 1. :
                            h_csv_inc_log_4PF.Fill( 		-math.log( 1 -	event.offJet_csv[ event.pfJet_offmatch[i] ] ) )

			if event.pfJet_hltBTagPFCSVp080Single[i] :# from HLT_PFHT430_SixPFJet40_PFBTagCSV_1p5
                                passed = True
				print "passes pf filter", event.offJet_csv[  event.pfJet_offmatch[i] ]
				h_csv_inc_pf.Fill(				event.offJet_csv[ event.pfJet_offmatch[i] ] )
                                if event.offJet_csv[ event.pfJet_offmatch[i] ] < 1. :
                                    h_csv_inc_pf_log.Fill(	-math.log( 1 -  event.offJet_csv[ event.pfJet_offmatch[i] ] ) )

                        eff_csv_inc_pf.Fill(passed, event.offJet_csv[ event.pfJet_offmatch[i] ] )
                        if event.offJet_csv[ event.pfJet_offmatch[i] ] < 1. : eff_csv_inc_pf_log.Fill(passed, -math.log( 1 -  event.offJet_csv[ event.pfJet_offmatch[i] ] ) )


    f_results.Write()

####################################

main()
