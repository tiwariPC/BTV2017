from launchNtupleFromAOD2017 import launchNtupleFromAOD2017

maxevents=50000
fileOutput = 'ntupleTest2017BTuned_2017_07_11_50k.root'
filesInput=['root://cms-xrd-global.cern.ch//store/data/Run2017B/BTagCSV/AOD/PromptReco-v1/000/297/722/00000/008316A9-CF5E-E711-8B52-02163E0145AA.root',
            'root://cms-xrd-global.cern.ch//store/data/Run2017B/BTagCSV/AOD/PromptReco-v1/000/297/722/00000/70C23A78-C85E-E711-99F5-02163E01A3F0.root',
            'root://cms-xrd-global.cern.ch//store/data/Run2017B/BTagCSV/AOD/PromptReco-v1/000/297/722/00000/8CC1BE7D-CE5E-E711-A921-02163E019E5B.root',
            'root://cms-xrd-global.cern.ch//store/data/Run2017B/BTagCSV/AOD/PromptReco-v1/000/297/722/00000/90BE6EB2-E85E-E711-8106-02163E01341F.root',
            'root://cms-xrd-global.cern.ch//store/data/Run2017B/BTagCSV/AOD/PromptReco-v1/000/297/722/00000/C0B0508F-E95E-E711-BCB9-02163E01A50C.root',
            'root://cms-xrd-global.cern.ch//store/data/Run2017B/BTagCSV/AOD/PromptReco-v1/000/297/722/00000/D8DE0484-CD5E-E711-9D16-02163E01A3DB.root'
            # 'root://cms-xrd-global.cern.ch//store/data/Run2017B/BTagCSV/AOD/PromptReco-v1/000/297/675/00000/348070F8-725E-E711-9FEA-02163E019BBD.root',
            # 'root://cms-xrd-global.cern.ch//store/data/Run2017B/BTagCSV/AOD/PromptReco-v1/000/297/675/00000/4A40BA34-765E-E711-ABCF-02163E0144BE.root',
            # 'root://cms-xrd-global.cern.ch//store/data/Run2017B/BTagCSV/AOD/PromptReco-v1/000/297/675/00000/C00B86D3-795E-E711-86C9-02163E011F67.root',
            # 'root://cms-xrd-global.cern.ch//store/data/Run2017B/BTagCSV/AOD/PromptReco-v1/000/297/675/00000/D0A77440-6D5E-E711-9317-02163E013586.root',
            # 'root://cms-xrd-global.cern.ch//store/data/Run2017B/BTagCSV/AOD/PromptReco-v1/000/297/675/00000/DAE21877-705E-E711-9222-02163E019BB6.root'
            # 'root://cms-xrd-global.cern.ch//store/data/Run2017B/BTagCSV/AOD/PromptReco-v1/000/297/670/00000/30AF14CB-305E-E711-B92F-02163E01A508.root',
            # 'root://cms-xrd-global.cern.ch//store/data/Run2017B/BTagCSV/AOD/PromptReco-v1/000/297/671/00000/486738DA-4B5E-E711-8536-02163E01376B.root',
            # 'root://cms-xrd-global.cern.ch//store/data/Run2017B/BTagCSV/AOD/PromptReco-v1/000/297/672/00000/2AC6C182-2E5E-E711-8D48-02163E01A618.root',
            # 'root://cms-xrd-global.cern.ch//store/data/Run2017B/BTagCSV/AOD/PromptReco-v1/000/297/674/00000/72F1F8F5-4C5E-E711-A10F-02163E01186A.root',
            # 'root://cms-xrd-global.cern.ch//store/data/Run2017B/BTagCSV/AOD/PromptReco-v1/000/297/674/00000/849798EF-555E-E711-A1E4-02163E0144F6.root',
            # 'root://cms-xrd-global.cern.ch//store/data/Run2017B/BTagCSV/AOD/PromptReco-v1/000/297/674/00000/E29372C9-515E-E711-9262-02163E01A43C.root',
            # 'root://cms-xrd-global.cern.ch//store/data/Run2017B/BTagCSV/AOD/PromptReco-v1/000/297/678/00000/522A0201-5C5E-E711-8F5C-02163E0146E5.root',
            # 'root://cms-xrd-global.cern.ch//store/data/Run2017B/BTagCSV/AOD/PromptReco-v1/000/297/722/00000/008316A9-CF5E-E711-8B52-02163E0145AA.root',
            # 'root://cms-xrd-global.cern.ch//store/data/Run2017B/BTagCSV/AOD/PromptReco-v1/000/297/722/00000/70C23A78-C85E-E711-99F5-02163E01A3F0.root',
            # 'root://cms-xrd-global.cern.ch//store/data/Run2017B/BTagCSV/AOD/PromptReco-v1/000/297/722/00000/8CC1BE7D-CE5E-E711-A921-02163E019E5B.root',
            # 'root://cms-xrd-global.cern.ch//store/data/Run2017B/BTagCSV/AOD/PromptReco-v1/000/297/722/00000/90BE6EB2-E85E-E711-8106-02163E01341F.root',
            # 'root://cms-xrd-global.cern.ch//store/data/Run2017B/BTagCSV/AOD/PromptReco-v1/000/297/722/00000/C0B0508F-E95E-E711-BCB9-02163E01A50C.root',
            # 'root://cms-xrd-global.cern.ch//store/data/Run2017B/BTagCSV/AOD/PromptReco-v1/000/297/722/00000/D8DE0484-CD5E-E711-9D16-02163E01A3DB.root',
            # 'root://cms-xrd-global.cern.ch//store/data/Run2017B/BTagCSV/AOD/PromptReco-v1/000/297/723/00000/944D89B8-DF5E-E711-9CB8-02163E01A5B3.root',
            # 'root://cms-xrd-global.cern.ch//store/data/Run2017B/BTagCSV/AOD/PromptReco-v1/000/297/723/00000/A477788E-DB5E-E711-9385-02163E01A6C1.root',
            # 'root://cms-xrd-global.cern.ch//store/data/Run2017B/BTagCSV/AOD/PromptReco-v1/000/297/723/00000/F6E1C2F4-D25E-E711-B0AC-02163E0144D9.root'
            ]
launchNtupleFromAOD2017(fileOutput,filesInput,maxevents)

	# "root://cms-xrd-global.cern.ch//store/data/Run2017B/BTagCSV/AOD/PromptReco-v1/000/297/046/00000/32BCD2B2-1556-E711-ADCE-02163E013911.root",
	# "root://cms-xrd-global.cern.ch//store/data/Run2017B/BTagCSV/AOD/PromptReco-v1/000/297/047/00000/FE61AABA-1456-E711-98E8-02163E0142FC.root",
	# "root://cms-xrd-global.cern.ch//store/data/Run2017B/BTagCSV/AOD/PromptReco-v1/000/297/050/00000/188898A2-5356-E711-8FE8-02163E01A252.root",
	# "root://cms-xrd-global.cern.ch//store/data/Run2017B/BTagCSV/AOD/PromptReco-v1/000/297/050/00000/1A1F6A4A-6E56-E711-9163-02163E0145AA.root",
	# "root://cms-xrd-global.cern.ch//store/data/Run2017B/BTagCSV/AOD/PromptReco-v1/000/297/050/00000/287994E2-5C56-E711-B16F-02163E0135DE.root",
	# "root://cms-xrd-global.cern.ch//store/data/Run2017B/BTagCSV/AOD/PromptReco-v1/000/297/050/00000/F228C479-5856-E711-B248-02163E0137FA.root"
