BTV at HLT
==========

Tools to study performances of the BTV sequences at HLT

Producing ntuples
---

```
# Setup release (so far in 9_2_3)
cmsrel CMSSW_9_2_3_patch2
cd CMSSW_9_2_3_patch2/src
cmsenv

# Clone this repo
git clone https://github.com/XavierAtCERN/BTV2017.git

# Move of production of ntuples
cd BTV2017/BTVatHLT/ProduceNtuple/

# Run the production
python ntupleRun2017B.py
```

Producing efficiencies
---

```
# Move to production of efficiencies
cd ../ProduceEfficiency

# Move ntuples
mv ../ProduceNtuple/*.root .

# Modify the name of the input file in the python code

# Run the efficiency
python produce_efficiency_mixedcaloPF.py
```

Will produce efficiency plot by dividing the number of jets of offline CSV passing a filter associated to online b-tagging by the total number of jets


Ongoing work and next steps
----------

- Make the ntuple production compatible with using crab (should be done soon)

- Look at the content of the different data format to find informations useful for monitoring and performances

- Look at the way to rerun the HLT on the data with the relevant parameters
  - cmsDriver [options]

- Update the offline DQM




