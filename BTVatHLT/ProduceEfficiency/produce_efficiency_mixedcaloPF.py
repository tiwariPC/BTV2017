import sys
import math
import ROOT
import matplotlib.pyplot as plt

from ROOT import TH1F, TH2F, TEfficiency
from matplotlib.pyplot import figure, show
from numpy import arange, sin, pi

# Performances of the PF online b-tagging sequence based on events triggered by HLT_PFHT300PT30_QuadPFJet_75_60_45_40, and studying the CSV cut of the HLT_PFHT300PT30_QuadPFJet_75_60_45_40_TriplePFBTagCSV_3p0

def main() :

    # Files
    f_ntuple            = ROOT.TFile("ntupleTest2017C_2017_08_17_50k.root",    	 "READ")
    f_results           = ROOT.TFile("results2017C_mixed_test.root", 	     "RECREATE")
    f_results.cd()

    # Functions
    makePlots(f_ntuple,  f_results)

def makePlots(f_ntuple, f_results) :

    t = f_ntuple.Get("tree")
    print "Tree extracted..."

    h_csv_inc_4Calo     = TH1F("h_csv_inc_4Calo",    		"h_csv_inc_4Calo",     	50,  0,  1)
    h_csv_inc_4PF      	= TH1F("h_csv_inc_4PF",    		"h_csv_inc_4PF",     	50,  0,  1)
    # h_csv_inc      	= TH1F("h_csv_inc",    		"h_csv_inc",     	50,  0,  1)
    h_csv_afcalo       	= TH1F("h_csv_afcalo",  	"h_csv_afcalo",      	50,  0,  1)
    h_csv_afpf		= TH1F("h_csv_afpf",		"h_csv_afpf",		50,  0,  1)

    h_csv_inc_log_4Calo     = TH1F("h_csv_inc_log_4Calo",    		"h_csv_inc_log_4Calo",     	50,  0,  7)
    h_csv_inc_log_4PF       = TH1F("h_csv_inc_log_4PF",    		"h_csv_inc_log_4PF",     	50,  0,  7)
    # h_csv_inc_log      	= TH1F("h_csv_inc_log",    	"h_csv_inc_log",     	50,  0,  7)
    h_csv_afcalo_log	= TH1F("h_csv_afcalo_log",  	"h_csv_afcalo_log",	50,  0,  7)
    h_csv_afpf_log	= TH1F("h_csv_afpf_log",	"h_csv_afpf_log",	50,  0,  7)

    h_csv_inc_calo      = TH1F("h_csv_inc_calo",   	"h_csv_inc_calo",     	50,  0,  1)
    h_csv_inc_pf       	= TH1F("h_csv_inc_pf",  	"h_csv_inc_pf",      	50,  0,  1)
    h_csv_calo_pf	= TH1F("h_csv_calo_pf",		"h_csv_calo_pf",	50,  0,  1)

    h_csv_inc_calo_log	= TH1F("h_csv_inc_calo_log",    "h_csv_inc_calo_log",   50,  0,  7)
    h_csv_inc_pf_log	= TH1F("h_csv_inc_pf_log",  	"h_csv_inc_pf_log",     50,  0,  7)
    h_csv_calo_pf_log	= TH1F("h_csv_calo_pf_log",	"h_csv_calog_pf_log",	50,  0,  7)


    eff_csv_inc_calo    = TEfficiency("eff_csv_inc_calo", "eff_csv_inc_calo",     	50,  0,  1)
    eff_csv_inc_pf      = TEfficiency("eff_csv_inc_pf",    "eff_csv_inc_pf",      	50,  0,  1)
    eff_csv_calo_pf	= TEfficiency("eff_csv_calo_pf",   "eff_csv_calo_pf",          50,  0,  1)

    eff_csv_inc_calo_log  = TEfficiency("eff_csv_inc_calo_log",  "eff_csv_inc_calo_log",   50,  0,  7)
    eff_csv_inc_pf_log	  = TEfficiency("eff_csv_inc_pf_log",    "eff_csv_inc_pf_log",     50,  0,  7)
    eff_csv_calo_pf_log	  = TEfficiency("eff_csv_calo_pf_log",	  "eff_csv_calog_pf_log",   50,  0,  7)


    i = 0

    for event in t:
        print
	print "New event --------"
	print
        
        if not event.HLT_PFHT300PT30_QuadPFJet_75_60_45_40 : continue
        # if not event.HLT_PFHT890_ : continue

	print "CALO JET SECTION : # calo jet = ", event.caloJet_num
	for i in range(0, event.caloJet_num-1) :	
		if event.caloJet_offmatch[i] >= 0 :
			print "calo jet[", i, "]"
			print "event.caloJet_offmatch[i]: ", 	event.caloJet_offmatch[i], 	" event.offJet_num: ", 	event.offJet_num
			print "calo pt: ", 			event.caloJet_pt[i], 		" offline pt: ",	event.offJet_pt[  event.caloJet_offmatch[i] ]
			print "calo eta: ",			event.caloJet_eta[i],		" offline eta: ",	event.offJet_eta[ event.caloJet_offmatch[i] ]
			print "calo phi: ",			event.caloJet_phi[i],		" offline phi: ",	event.offJet_phi[ event.caloJet_offmatch[i] ]
			print "offline csv: ", 			event.offJet_csv[  event.caloJet_offmatch[i] ]

                        if event.offJet_pt[  event.caloJet_offmatch[i] ] < 30 : continue

                        passed = False

			h_csv_inc_4Calo.Fill( 			event.offJet_csv[ event.caloJet_offmatch[i] ] )
                        if event.offJet_csv[ event.caloJet_offmatch[i] ] < 1. :
                            h_csv_inc_log_4Calo.Fill( 		-math.log( 1 -	event.offJet_csv[ event.caloJet_offmatch[i] ] ) )
			if event.caloJet_hltBTagCaloCSVp05Double[i] :
                                passed = True
				print "passes calo filter", event.offJet_csv[  event.caloJet_offmatch[i] ]
				h_csv_afcalo.Fill(			event.offJet_csv[ event.caloJet_offmatch[i] ] )
                                h_csv_inc_calo.Fill(                    event.offJet_csv[ event.caloJet_offmatch[i] ] )
                                if event.offJet_csv[ event.caloJet_offmatch[i] ] != 1. :
                                    h_csv_afcalo_log.Fill( 	-math.log( 1 - 	event.offJet_csv[ event.caloJet_offmatch[i] ] ) )	
                                    h_csv_inc_calo_log.Fill( -math.log( 1 -   event.offJet_csv[ event.caloJet_offmatch[i] ] ) )

                        eff_csv_inc_calo.Fill(passed, event.offJet_csv[ event.caloJet_offmatch[i] ] )

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
			if event.pfJet_hltBTagPFCSVp070Triple[i] :
                                passed = True
				print "passes pf filter", event.offJet_csv[  event.pfJet_offmatch[i] ]
				h_csv_afpf.Fill(				event.offJet_csv[ event.pfJet_offmatch[i] ] )
				h_csv_inc_pf.Fill(				event.offJet_csv[ event.pfJet_offmatch[i] ] )
				h_csv_calo_pf.Fill(				event.offJet_csv[ event.pfJet_offmatch[i] ] )
                                if event.offJet_csv[ event.pfJet_offmatch[i] ] < 1. :
                                    h_csv_afpf_log.Fill( 	-math.log( 1 - 	event.offJet_csv[ event.pfJet_offmatch[i] ] ) )
                                    h_csv_inc_pf_log.Fill(	-math.log( 1 -  event.offJet_csv[ event.pfJet_offmatch[i] ] ) )
                                    h_csv_calo_pf_log.Fill(	-math.log( 1 -  event.offJet_csv[ event.pfJet_offmatch[i] ] ) )	

                        eff_csv_inc_pf.Fill(passed, event.offJet_csv[ event.pfJet_offmatch[i] ] )

    # h_csv_inc_calo_log.Divide(	h_csv_inc_log_4Calo		)
    # h_csv_inc_pf_log.Divide(	h_csv_inc_log_4PF		)
    # h_csv_calo_pf_log.Divide(	h_csv_afcalo_log	)

    # h_csv_inc_calo.Divide(	h_csv_inc_4Calo		)
    # h_csv_inc_pf.Divide(	h_csv_inc_4PF		)
    # h_csv_calo_pf.Divide(	h_csv_afcalo	)

    # eff_csv_inc_calo_log = h_csv_inc_calo_log.Clone()
    # eff_csv_inc_pf_log = h_csv_inc_pf_log.Clone()
    # eff_csv_calo_pf_log = h_csv_calo_pf_log.Clone()
    # eff_csv_inc_calo = h_csv_inc_calo.Clone()
    # eff_csv_inc_pf = h_csv_inc_pf.Clone()
    # eff_csv_calo_pf = h_csv_calo_pf.Clone()


    # eff_csv_inc_calo_log.Divide ( h_csv_inc_calo_log, h_csv_inc_log_4Calo, 1.,1.,'B' )
    # eff_csv_inc_pf_log.Divide   ( h_csv_inc_pf_log, h_csv_inc_log_4PF, 1.,1.,'B'     )
    # eff_csv_calo_pf_log.Divide  ( h_csv_calo_pf_log, h_csv_afcalo_log, 1.,1.,'B'     )

    # eff_csv_inc_calo.Divide     ( h_csv_inc_calo, h_csv_inc_4Calo, 1.,1.,'B'         )
    # eff_csv_inc_pf.Divide       ( h_csv_inc_pf, h_csv_inc_4PF, 1.,1.,'B'             )
    # eff_csv_calo_pf.Divide      ( h_csv_calo_pf, h_csv_afcalo, 1.,1.,'B'             )


    f_results.Write()

####################################

main()
