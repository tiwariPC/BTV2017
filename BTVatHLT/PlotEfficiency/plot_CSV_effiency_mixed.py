
import ROOT as rt
import CMS_lumi, tdrstyle
import array

#set the tdr style
tdrstyle.setTDRStyle()

file = rt.TFile("results2017C_mixed_test.root","READ")

#change the CMS_lumi variables (see CMS_lumi.py)
CMS_lumi.lumi_7TeV = "4.8 fb^{-1}"
CMS_lumi.lumi_8TeV = "18.3 fb^{-1}"
CMS_lumi.writeExtraText = 1
CMS_lumi.extraText = "Preliminary"
CMS_lumi.lumi_sqrtS = "2017C (13 TeV)" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)

iPos = 11
if( iPos==0 ): CMS_lumi.relPosX = 0.12

H_ref = 600; 
W_ref = 800; 
W = W_ref
H  = H_ref

iPeriod = 0

# references for T, B, L, R
T = 0.08*H_ref
B = 0.12*H_ref 
L = 0.12*W_ref
R = 0.04*W_ref

canvas = rt.TCanvas("c2","c2",50,50,W,H)
canvas.SetFillColor(0)
canvas.SetBorderMode(0)
canvas.SetFrameFillStyle(0)
canvas.SetFrameBorderMode(0)
canvas.SetLeftMargin( L/W )
canvas.SetRightMargin( R/W )
canvas.SetTopMargin( T/H )
canvas.SetBottomMargin( B/H )
canvas.SetTickx(0)
canvas.SetTicky(0)
canvas.SetBatch()
canvas.SetGrid()

h =  rt.TH1F("h","h; offline CSVv2 discriminator; Efficiency",50,0,1)
# h =  rt.TH1F("h","h; -log(1-CSVv2 discriminator); Efficiency",50,0,7)

h.SetMaximum(1.4)

xAxis = h.GetXaxis()
xAxis.SetNdivisions(6,5,0)

yAxis = h.GetYaxis()
yAxis.SetNdivisions(6,5,0)
yAxis.SetTitleOffset(1)

h.Draw()


# data1 = file.Get("h_csv_inc_calo_log")
# data2 = file.Get("h_csv_inc_pf_log")
data1 = file.Get("eff_csv_inc_calo")
data2 = file.Get("eff_csv_inc_pf")

MC   = file.Get("h_csvafterfilterlog")

#MC.Draw("histsame")
data1.SetMarkerStyle(20)
data1.SetMarkerSize(0.9)
data1.SetMarkerColor(rt.kBlue)
#data.Draw("esamex0")
data1.Draw("same")

data2.SetMarkerStyle(20)
data2.SetMarkerSize(0.9)
data2.SetMarkerColor(rt.kRed)
data2.Draw("same")

#draw the lumi text on the canvas
CMS_lumi.CMS_lumi(canvas, iPeriod, iPos)

canvas.cd()
canvas.Update()
canvas.RedrawAxis()
frame = canvas.GetFrame()
frame.Draw()

leg = rt.TLegend(.65,.2,.9,.3)
leg.AddEntry(data1,'calo sequence','pe')
leg.AddEntry(data2,'PF sequence','pe')
leg.Draw('same')
canvas.Modified()
canvas.Update()


#update the canvas to draw the legend
canvas.Update()
canvas.SaveAs("EfficiencyJet.pdf")

# raw_input("Press Enter to end")
