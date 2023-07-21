# GEM-RPCMon

## Get HLT Configuration
```bash
scram project CMSSW CMSSW_13_0_5_patch1
cd CMSSW_13_0_5_patch1/src && cmsenv
hltInfo /eos/cms/store/data/Run2023C/EphemeralHLTPhysics0/RAW/v1/000/367/260/00000/0b4384ac-f9ce-439d-a806-417256e17f40.root
# Dumps the HLT configuration in to a python file
hltGetConfiguration run:367260 \
   --globaltag 130X_dataRun3_HLT_v2 \
   --data \
   --unprescale \
   --output all \
   --max-events 100 \
   --eras Run3 \
   --input file:/eos/cms/store/data/Run2023C/EphemeralHLTPhysics0/RAW/v1/000/367/260/00000/0b4384ac-f9ce-439d-a806-417256e17f40.root \
   > hltData.py
```
