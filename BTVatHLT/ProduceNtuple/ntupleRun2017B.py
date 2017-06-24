from launchNtupleFromAOD2017 import launchNtupleFromAOD2017

maxevents=2000
fileOutput = 'ntupleTest2017BTuned2000.root'
filesInput=[
	"root://cms-xrd-global.cern.ch//store/data/Run2017B/BTagCSV/AOD/PromptReco-v1/000/297/046/00000/32BCD2B2-1556-E711-ADCE-02163E013911.root",
	"root://cms-xrd-global.cern.ch//store/data/Run2017B/BTagCSV/AOD/PromptReco-v1/000/297/047/00000/FE61AABA-1456-E711-98E8-02163E0142FC.root",
	"root://cms-xrd-global.cern.ch//store/data/Run2017B/BTagCSV/AOD/PromptReco-v1/000/297/050/00000/188898A2-5356-E711-8FE8-02163E01A252.root",
	"root://cms-xrd-global.cern.ch//store/data/Run2017B/BTagCSV/AOD/PromptReco-v1/000/297/050/00000/1A1F6A4A-6E56-E711-9163-02163E0145AA.root",
	"root://cms-xrd-global.cern.ch//store/data/Run2017B/BTagCSV/AOD/PromptReco-v1/000/297/050/00000/287994E2-5C56-E711-B16F-02163E0135DE.root",
	"root://cms-xrd-global.cern.ch//store/data/Run2017B/BTagCSV/AOD/PromptReco-v1/000/297/050/00000/F228C479-5856-E711-B248-02163E0137FA.root"
]
launchNtupleFromAOD2017(fileOutput,filesInput,maxevents)
