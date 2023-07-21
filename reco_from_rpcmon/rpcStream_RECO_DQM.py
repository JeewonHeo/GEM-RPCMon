import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run3_cff import Run3

process = cms.Process('RECO',Run3)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('RecoMuon.Configuration.RecoMuon_cff')
process.load("DQM.GEM.GEMDQM_cff")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        # 'file:/eos/user/j/jheo/367260/7ad6f18d-508a-4510-af6b-79efb5b12518.root',
        # 'file:/eos/user/j/jheo/367260/8c216ef1-5937-4001-b72f-d8e4db8b8719.root',
        # 'file:/eos/user/j/jheo/367260/0df11715-7d7e-40d0-8647-029d8b1c0b39.root',
        # 'file:/eos/user/j/jheo/367260/99f1bfe2-cc1f-45f5-a750-c004d49aa362.root',
        # 'file:/eos/user/j/jheo/367260/771246b2-7e26-4f33-a8bd-64f28b9e32de.root',
        # 'file:/eos/user/j/jheo/367260/5d6ca20c-d431-4a25-aebe-99c6a4124882.root',
        # 'file:/eos/user/j/jheo/367260/cd7ed057-bf9e-4425-b340-d21f380c78bc.root',
        # 'file:/eos/user/j/jheo/367260/43ce1b4e-6e33-4086-b9c1-c215ffb00dfc.root',
        # 'file:/eos/user/j/jheo/367260/8aa2b5f9-1cbc-41f7-874d-efd0d301950f.root',
        # 'file:/eos/user/j/jheo/367260/f41e4284-6212-464a-8571-bfe661a4322f.root',
        # 'file:/eos/user/j/jheo/367260/9b48c621-1133-41f9-9f2e-26d3db799aa3.root',
        # 'file:/eos/user/j/jheo/367260/7822b93b-6efe-4b25-97b5-964f6fa5fa48.root',
        # 'file:/eos/user/j/jheo/367260/c6e86ae8-b5a7-4b0e-8bbb-76f8e203bacb.root',
        # 'file:/eos/user/j/jheo/367260/d03c6273-a4df-48a8-b3f1-9b828163ee71.root',
        # 'file:/eos/user/j/jheo/367260/e9222918-f42a-4975-a313-a97e318bc60f.root',
        # 'file:/eos/user/j/jheo/367260/0b4384ac-f9ce-439d-a806-417256e17f40.root',
        # 'file:/eos/user/j/jheo/367260/72041e13-6699-407f-bd21-28a8bedc2edb.root',
        # 'file:/eos/user/j/jheo/367260/66f36fb6-6129-4009-9b64-4bb44ba42b6f.root',
        # 'file:/eos/user/j/jheo/367260/808a5558-ac9c-468a-88df-e44b6050ecdf.root',
        # 'file:/eos/user/j/jheo/367260/ad3dfaf4-6c32-48be-8537-9d940f912b49.root',
        # 'file:/eos/user/j/jheo/367260/4368573d-b137-4c12-b866-2b3655ea3e1f.root',
        # 'file:/eos/user/j/jheo/367260/832822ba-edf7-42d2-9f53-91cd3d3e357f.root',
        # 'file:/eos/user/j/jheo/367260/1c153f66-fc56-4c58-947d-753f4d0eb804.root',
        # 'file:/eos/cms/tier0/store/data/Run2023C/RPCMonitor/RAW/v1/000/367/619/00000/bf6e97ca-972b-4ae8-9954-64f9c19eb81f.root'
        'file:/afs/cern.ch/user/j/jheo/rpc-monitor/gemdigi_CMSSW/src/outputRPCMON.root'
        ),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(
    FailPath = cms.untracked.vstring(),
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    SkipEvent = cms.untracked.vstring(),
    accelerators = cms.untracked.vstring('*'),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    deleteNonConsumedUnscheduledModules = cms.untracked.bool(True),
    dumpOptions = cms.untracked.bool(False),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(
            allowAnyLabel_=cms.required.untracked.uint32
        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(0)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    holdsReferencesToDeleteEarly = cms.untracked.VPSet(),
    makeTriggerResults = cms.obsolete.untracked.bool,
    modulesToIgnoreForDeleteEarly = cms.untracked.vstring(),
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(0),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(1),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step3 nevts:1'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RECOoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('RECO'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('step3_RECO_DQM.root'),
    outputCommands = cms.untracked.vstring("drop *",
                                           "keep *_standAloneMuons_*_*",
                                           "keep *_muons1stStep_*_*",
                                           ),
    splitLevel = cms.untracked.int32(0)
)

process.DQMoutput = cms.OutputModule("DQMRootOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('DQMIO'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('step3_RECO_DQM_inDQM.root'),
    outputCommands = process.DQMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '130X_dataRun3_Prompt_v2', '')

from RecoVertex.BeamSpotProducer.BeamSpotFakeParameters_cfi import *
process.offlineBeamSpot = cms.EDProducer("BeamSpotProducer")
from RecoMuon.MuonIdentification.muons1stStep_cfi import muons1stStep
process.muons1stStep = muons1stStep.clone(
    inputCollectionTypes = ['outer tracks'],
    inputCollectionLabels = ['standAloneMuons:UpdatedAtVtx'],
    minP         = 3.0, # was 2.5
    minPt        = 2.0, # was 0.5
    minPCaloMuon = 3.0, # was 1.0
    fillCaloCompatibility = False,
    fillEnergy = False,
    fillGlobalTrackQuality = False,
    fillGlobalTrackRefits  = False,
    fillIsolation = False,
    fillTrackerKink = False,
    fillShowerDigis = False,
    storeCrossedHcalRecHits = False,
    fillMatching = False,
    writeIsoDeposits = False,
    arbitrateTrackerMuons = False,    
    selectHighPurity = False,
    TrackAssociatorParameters = dict(
	useHO   = False,
	useEcal = False,
	useHcal = False,
    CSCSegmentCollectionLabel = cms.InputTag("hltCscSegments"),
    DTRecSegment4DCollectionLabel = cms.InputTag("hltDt4DSegments")
    ),
    CaloExtractorPSet = dict(
    TrackAssociatorParameters = dict(
    CSCSegmentCollectionLabel = cms.InputTag("hltCscSegments"),
    DTRecSegment4DCollectionLabel = cms.InputTag("hltDt4DSegments")
    )
    ),
    JetExtractorPSet = dict(
    TrackAssociatorParameters = dict(
    CSCSegmentCollectionLabel = cms.InputTag("hltCscSegments"),
    DTRecSegment4DCollectionLabel = cms.InputTag("hltDt4DSegments")
    )
    )
)
process.muons1stStep.TimingFillerParameters.MatchParameters.CSCsegments = cms.InputTag("hltCscSegments")
process.muons1stStep.TimingFillerParameters.MatchParameters.DTsegments = cms.InputTag("hltDt4DSegments")
process.muons1stStep.TimingFillerParameters.MatchParameters.RPChits = cms.InputTag("hltRpcRecHits")
process.load("TrackingTools.TransientTrack.TransientTrackBuilder_cfi")

from RecoMuon.MuonIdentification.muons_cfi import muons
process.muons = muons.clone(
    FillPFMomentumAndAssociation = cms.bool(False),
    FillTimingInfo = cms.bool(False),
    FillDetectorBasedIsolation = cms.bool(False),
    FillPFIsolation = cms.bool(False),
    FillSelectorMaps = cms.bool(False),
    FillShoweringInfo = cms.bool(False),
    FillCosmicsIdMap = cms.bool(False),
    ComputeStandardSelectors = cms.bool(False),
)

process.standalonemuontrackingTask = cms.Task(process.standAloneMuons,process.muons1stStep,process.muons)
process.reconstruction_step = cms.Path(process.standalonemuontrackingTask)

from DQM.GEM.GEMRecHitSource_cfi import *
from DQM.GEM.GEMDAQStatusSource_cfi import *
from DQM.GEM.GEMDQMHarvester_cfi import *
from DQM.GEM.gemEfficiencyAnalyzer_cfi import *

process.gemDQMStaMuons = cms.EDFilter("MuonSelector",
    src = cms.InputTag("muons1stStep"),
    cut = cms.string("isStandAloneMuon"),
    filter = cms.bool(False)
)
process.standalonemuontrackingTask = cms.Task(process.offlineBeamSpot,process.ancientMuonSeed,process.standAloneMuons,process.muons1stStep,process.gemDQMStaMuons)

process.gemEfficiencyAnalyzerSta = gemEfficiencyAnalyzer.clone(
    muonTag = "gemDQMStaMuons",
    muonTrackType = "OuterTrack",
    startingStateType = "OutermostMeasurementState",
    folder = "GEM/Efficiency/muonSTA",
    muonName = "STA Muon",
    #propagationErrorRCut = 0.5, # cm
    #propagationErrorPhiCut = 0.2, # degree
    propagationErrorRCut = 5, # cm
    propagationErrorPhiCut = 2, # degree
    muonPtMinCutGE11 = cms.untracked.double(5),
    #maskChamberWithError = cms.untracked.bool(True)
)

# process.GEMDQM = cms.Sequence(GEMRecHitSource*GEMDAQStatusSource*process.gemEfficiencyAnalyzerSta+GEMDQMHarvester)
process.GEMDigiSource.runType = "offline"
process.GEMRecHitSource.runType = "offline"
process.GEMDAQStatusSource.runType = "offline"
process.GEMDQM = cms.Sequence(GEMRecHitSource*GEMDAQStatusSource*process.gemEfficiencyAnalyzerSta)
#process.GEMDQM = cms.Sequence(GEMRecHitSource*GEMDAQStatusSource+GEMDQMHarvester)

process.load("DQM.Integration.config.environment_cfi")
process.dqmEnv.subSystemFolder = "GEM"
process.dqmEnv.eventInfoFolder = "EventInfo"
process.dqmSaver.path = "/eos/user/j/jheo/"

process.end_path = cms.EndPath(process.dqmEnv+process.dqmSaver)

process.ancientMuonSeed.CSCRecSegmentLabel = cms.InputTag("hltCscSegments")
process.ancientMuonSeed.DTRecSegmentLabel = cms.InputTag("hltDt4DSegments")
process.standAloneMuons.STATrajBuilderParameters.BWFilterParameters.CSCRecSegmentLabel = cms.InputTag("hltCscSegments")
process.standAloneMuons.STATrajBuilderParameters.FilterParameters.CSCRecSegmentLabel = cms.InputTag("hltCscSegments")
process.standAloneMuons.STATrajBuilderParameters.BWFilterParameters.EnableGEMMeasurement = cms.bool(False)
process.standAloneMuons.STATrajBuilderParameters.FilterParameters.EnableGEMMeasurement = cms.bool(False)
process.standAloneMuons.STATrajBuilderParameters.BWFilterParameters.DTRecSegmentLabel = cms.InputTag("hltDt4DSegments")
process.standAloneMuons.STATrajBuilderParameters.FilterParameters.DTRecSegmentLabel = cms.InputTag("hltDt4DSegments")
process.standAloneMuons.STATrajBuilderParameters.BWFilterParameters.RPCRecSegmentLabel = cms.InputTag("hltRpcRecHits")
process.standAloneMuons.STATrajBuilderParameters.FilterParameters.RPCRecSegmentLabel = cms.InputTag("hltRpcRecHits")
#process.standAloneMuons.TrackLoaderParameters.VertexConstraint = cms.bool(False)


process.GEMRecHitSource.recHitsInputLabel = cms.InputTag("hltGemRecHits")
process.GEMDAQStatusSource.AMC13InputLabel = cms.InputTag("hltMuonGEMDigis","AMC13Status")
process.GEMDAQStatusSource.AMCInputLabel = cms.InputTag("hltMuonGEMDigis","AMCStatus")
process.GEMDAQStatusSource.OHInputLabel = cms.InputTag("hltMuonGEMDigis","OHStatus")
process.GEMDAQStatusSource.VFATInputLabel = cms.InputTag("hltMuonGEMDigis","VFATStatus")
process.gemEfficiencyAnalyzerSta.ServiceParameters.GEMLayers = cms.untracked.bool(False)
process.gemEfficiencyAnalyzerSta.ohStatusTag = cms.untracked.InputTag("hltMuonGEMDigis","OHStatus")
process.gemEfficiencyAnalyzerSta.recHitTag = cms.untracked.InputTag("hltGemRecHits")
process.gemEfficiencyAnalyzerSta.vfatStatusTag = cms.untracked.InputTag("hltMuonGEMDigis","VFATStatus")

#process.GEMDQM = cms.Sequence(GEMRecHitSource+GEMDAQStatusSource+GgemEfficiencyAnalyzerStaSeqEMDQMHarvester)
process.dqmoffline_step = cms.EndPath(process.GEMDQM)
process.RECOoutput_step = cms.EndPath(process.RECOoutput)
process.DQMoutput_step = cms.EndPath(process.DQMoutput)

# Schedule definition
#process.schedule = cms.Schedule(process.reconstruction_step,process.dqmoffline_step,process.RECOoutput_step,process.end_path)
process.schedule = cms.Schedule(process.reconstruction_step,process.dqmoffline_step,process.end_path)
# process.schedule = cms.Schedule(process.reconstruction_step,process.dqmoffline_step,process.DQMoutput_step)

process.MessageLogger.cerr.threshold = "DEBUG"
process.MessageLogger.debugModules = ["gemEfficiencyAnalyzerSta"]
#process.MessageLogger.cerr.FwkReport.reportEvery = 1000
# from pathlib import Path
# data_dir = Path("/eos/cms/tier0/store/data/Run2023C/RPCMonitor/RAW/v1/000/")
# path_iter = data_dir.glob("**/*.root")
# # input_files = ['file:' + str(next(path_iter))]
# input_files = ['file:' + str(path) for path in path_iter][:10]
# print(f'{input_files=}')
# process.source.fileNames = input_files

import FWCore.ParameterSet.VarParsing as VarParsing
options = VarParsing.VarParsing('analysis')
options.parseArguments()
# process.source.fileNames = cms.untracked.vstring('file:'+options.inputFiles[0])
process.DQMoutput.fileName = cms.untracked.string('file:'+options.outputFile)
# process.dqmSaver.tag = options.outputFile

