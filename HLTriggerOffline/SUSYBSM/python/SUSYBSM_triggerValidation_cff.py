import FWCore.ParameterSet.Config as cms
import HLTriggerOffline.SUSYBSM.mcSel_RA1_cff as mcSel_RA1
import HLTriggerOffline.SUSYBSM.mcSel_RA2_cff as mcSel_RA2
import HLTriggerOffline.SUSYBSM.mcSel_RA3_cff as mcSel_RA3
import HLTriggerOffline.SUSYBSM.mcSel_RA4_e_cff as mcSel_RA4_e
import HLTriggerOffline.SUSYBSM.mcSel_RA4_m_cff as mcSel_RA4_m
import HLTriggerOffline.SUSYBSM.mcSel_RA5RA6_1e1m_cff as mcSel_RA5RA6_1e1m
import HLTriggerOffline.SUSYBSM.mcSel_RA5RA6_2e_cff as mcSel_RA5RA6_2e
import HLTriggerOffline.SUSYBSM.mcSel_RA5RA6_2m_cff as mcSel_RA5RA6_2m
import HLTriggerOffline.SUSYBSM.mcSel_RA7_1e2m_cff as mcSel_RA7_1e2m
import HLTriggerOffline.SUSYBSM.mcSel_RA7_2e1m_cff as mcSel_RA7_2e1m
import HLTriggerOffline.SUSYBSM.mcSel_RA7_3e_cff as mcSel_RA7_3e
import HLTriggerOffline.SUSYBSM.mcSel_RA7_3m_cff as mcSel_RA7_3m

HLTSusyExoVal = cms.EDAnalyzer("TriggerValidator",
    TurnOnParams = cms.PSet(
        hlt1MuonIsoList = cms.vstring('hltSingleMuIsoLevel1Seed', 
            'hltSingleMuIsoL1Filtered', 
            'hltSingleMuIsoL2PreFiltered', 
            'hltSingleMuIsoL2IsoFiltered', 
            'hltSingleMuIsoL3PreFiltered', 
            'hltSingleMuIsoL3IsoFiltered'),
        hltMuonTracks = cms.string('hltL3MuonCandidates'),
        hlt1MuonNonIsoList = cms.vstring('hltSingleMuNoIsoLevel1Seed', 
            'hltSingleMuNoIsoL1Filtered', 
            'hltSingleMuNoIsoL2PreFiltered', 
            'hltSingleMuNoIsoL3PreFiltered'),
        genMother = cms.string('b'), ## it can be W, b, WtoJ, All

        recoMuons = cms.string('muons'),
        mcParticles = cms.string('genParticles')
        ),
    statFileName = cms.untracked.string('MonElements_LM1_IDEAL_30x_v1_300pre7.stat'),
    dirname = cms.untracked.string('HLT/SusyExo'),
    L1Label = cms.InputTag("hltL1GtObjectMap"),
    HltLabel = cms.InputTag("TriggerResults","","HLT"),
    reco_parametersets = cms.VPSet(
        cms.PSet(
            name = cms.string('Reco1'),
            reco_ptJet2Min = cms.double(30.0),
            jets = cms.string('iterativeCone5CaloJets'),
            reco_ptElecMin = cms.double(10.0),
            reco_ptJet1Min = cms.double(80.0),
            photonProducer = cms.string('photons'),
            reco_metMin = cms.double(100.0),
            photons = cms.string(''),
            muons = cms.string('muons'),
            reco_ptMuonMin = cms.double(10.0),
            reco_ptPhotMin = cms.double(0.0),
            calomet = cms.string('caloMet'),
            electrons = cms.string('gedGsfElectrons')
        )
    ),
                               
    # if mc_flag = false the McSelection folder will contain empty histograms
    mc_parametersets = cms.VPSet(
        cms.PSet(
            name = cms.string("RA1"),
            genMet = cms.string('genMetTrue'),
            genJets = cms.string('iterativeCone5GenJets'),
            mcparticles = cms.string('genParticles'),
            mc_nJet = mcSel_RA1.mc_nJet,
            mc_nPhot = mcSel_RA1.mc_nPhot,
            mc_nElec = mcSel_RA1.mc_nElec,
            mc_nMuon = mcSel_RA1.mc_nMuon,
            mc_ptElecMin = mcSel_RA1.mc_ptElecMin,
            mc_ptPhotMin = mcSel_RA1.mc_ptPhotMin,
            mc_ptJetMin = mcSel_RA1.mc_ptJetMin,
            mc_ptMuonMin = mcSel_RA1.mc_ptMuonMin,
            mc_metMin = mcSel_RA1.mc_metMin,
            mc_ptTauMin = mcSel_RA1.mc_ptTauMin,
            mc_ptJetForHtMin = mcSel_RA1.mc_ptJetForHtMin,
            mc_htMin = mcSel_RA1.mc_htMin,
            mc_nTau = mcSel_RA1.mc_nTau,
            mc_nMuonRule = mcSel_RA1.mc_nMuonRule,
            mc_nElecRule = mcSel_RA1.mc_nElecRule
        ),
        cms.PSet(
            name = cms.string("RA2"),
            genMet = cms.string('genMetTrue'),
            genJets = cms.string('iterativeCone5GenJets'),
            mcparticles = cms.string('genParticles'),
            mc_nJet = mcSel_RA2.mc_nJet,
            mc_nPhot = mcSel_RA2.mc_nPhot,
            mc_nElec = mcSel_RA2.mc_nElec,
            mc_nMuon = mcSel_RA2.mc_nMuon,
            mc_ptElecMin = mcSel_RA2.mc_ptElecMin,
            mc_ptPhotMin = mcSel_RA2.mc_ptPhotMin,
            mc_ptJetMin = mcSel_RA2.mc_ptJetMin,
            mc_ptMuonMin = mcSel_RA2.mc_ptMuonMin,
            mc_metMin = mcSel_RA2.mc_metMin,
            mc_ptTauMin = mcSel_RA2.mc_ptTauMin,
            mc_ptJetForHtMin = mcSel_RA2.mc_ptJetForHtMin,
            mc_htMin = mcSel_RA2.mc_htMin,
            mc_nTau = mcSel_RA2.mc_nTau,
            mc_nMuonRule = mcSel_RA2.mc_nMuonRule,
            mc_nElecRule = mcSel_RA2.mc_nElecRule
        ),
        cms.PSet(
            name = cms.string("RA3"),
            genMet = cms.string('genMetTrue'),
            genJets = cms.string('iterativeCone5GenJets'),
            mcparticles = cms.string('genParticles'),
            mc_nJet = mcSel_RA3.mc_nJet,
            mc_nPhot = mcSel_RA3.mc_nPhot,
            mc_nElec = mcSel_RA3.mc_nElec,
            mc_nMuon = mcSel_RA3.mc_nMuon,
            mc_ptElecMin = mcSel_RA3.mc_ptElecMin,
            mc_ptPhotMin = mcSel_RA3.mc_ptPhotMin,
            mc_ptJetMin = mcSel_RA3.mc_ptJetMin,
            mc_ptMuonMin = mcSel_RA3.mc_ptMuonMin,
            mc_metMin = mcSel_RA3.mc_metMin,
            mc_ptTauMin = mcSel_RA3.mc_ptTauMin,
            mc_ptJetForHtMin = mcSel_RA3.mc_ptJetForHtMin,
            mc_htMin = mcSel_RA3.mc_htMin,
            mc_nTau = mcSel_RA3.mc_nTau,
            mc_nMuonRule = mcSel_RA3.mc_nMuonRule,
            mc_nElecRule = mcSel_RA3.mc_nElecRule
        ),
        cms.PSet(
            name = cms.string("RA4_e"),
            genMet = cms.string('genMetTrue'),
            genJets = cms.string('iterativeCone5GenJets'),
            mcparticles = cms.string('genParticles'),
            mc_nJet = mcSel_RA4_e.mc_nJet,
            mc_nPhot = mcSel_RA4_e.mc_nPhot,
            mc_nElec = mcSel_RA4_e.mc_nElec,
            mc_nMuon = mcSel_RA4_e.mc_nMuon,
            mc_ptElecMin = mcSel_RA4_e.mc_ptElecMin,
            mc_ptPhotMin = mcSel_RA4_e.mc_ptPhotMin,
            mc_ptJetMin = mcSel_RA4_e.mc_ptJetMin,
            mc_ptMuonMin = mcSel_RA4_e.mc_ptMuonMin,
            mc_metMin = mcSel_RA4_e.mc_metMin,
            mc_ptTauMin = mcSel_RA4_e.mc_ptTauMin,
            mc_ptJetForHtMin = mcSel_RA4_e.mc_ptJetForHtMin,
            mc_htMin = mcSel_RA4_e.mc_htMin,
            mc_nTau = mcSel_RA4_e.mc_nTau,
            mc_nMuonRule = mcSel_RA4_e.mc_nMuonRule,
            mc_nElecRule = mcSel_RA4_e.mc_nElecRule
        ),
        cms.PSet(
            name = cms.string("RA4_m"),
            genMet = cms.string('genMetTrue'),
            genJets = cms.string('iterativeCone5GenJets'),
            mcparticles = cms.string('genParticles'),
            mc_nJet = mcSel_RA4_m.mc_nJet,
            mc_nPhot = mcSel_RA4_m.mc_nPhot,
            mc_nElec = mcSel_RA4_m.mc_nElec,
            mc_nMuon = mcSel_RA4_m.mc_nMuon,
            mc_ptElecMin = mcSel_RA4_m.mc_ptElecMin,
            mc_ptPhotMin = mcSel_RA4_m.mc_ptPhotMin,
            mc_ptJetMin = mcSel_RA4_m.mc_ptJetMin,
            mc_ptMuonMin = mcSel_RA4_m.mc_ptMuonMin,
            mc_metMin = mcSel_RA4_m.mc_metMin,
            mc_ptTauMin = mcSel_RA4_m.mc_ptTauMin,
            mc_ptJetForHtMin = mcSel_RA4_m.mc_ptJetForHtMin,
            mc_htMin = mcSel_RA4_m.mc_htMin,
            mc_nTau = mcSel_RA4_m.mc_nTau,
            mc_nMuonRule = mcSel_RA4_m.mc_nMuonRule,
            mc_nElecRule = mcSel_RA4_m.mc_nElecRule
        ),
        cms.PSet(
            name = cms.string("RA5RA6_1e1m"),
            genMet = cms.string('genMetTrue'),
            genJets = cms.string('iterativeCone5GenJets'),
            mcparticles = cms.string('genParticles'),
            mc_nJet = mcSel_RA5RA6_1e1m.mc_nJet,
            mc_nPhot = mcSel_RA5RA6_1e1m.mc_nPhot,
            mc_nElec = mcSel_RA5RA6_1e1m.mc_nElec,
            mc_nMuon = mcSel_RA5RA6_1e1m.mc_nMuon,
            mc_ptElecMin = mcSel_RA5RA6_1e1m.mc_ptElecMin,
            mc_ptPhotMin = mcSel_RA5RA6_1e1m.mc_ptPhotMin,
            mc_ptJetMin = mcSel_RA5RA6_1e1m.mc_ptJetMin,
            mc_ptMuonMin = mcSel_RA5RA6_1e1m.mc_ptMuonMin,
            mc_metMin = mcSel_RA5RA6_1e1m.mc_metMin,
            mc_ptTauMin = mcSel_RA5RA6_1e1m.mc_ptTauMin,
            mc_ptJetForHtMin = mcSel_RA5RA6_1e1m.mc_ptJetForHtMin,
            mc_htMin = mcSel_RA5RA6_1e1m.mc_htMin,
            mc_nTau = mcSel_RA5RA6_1e1m.mc_nTau,
            mc_nMuonRule = mcSel_RA5RA6_1e1m.mc_nMuonRule,
            mc_nElecRule = mcSel_RA5RA6_1e1m.mc_nElecRule
        ),
        cms.PSet(
            name = cms.string("RA5RA6_2e"),
            genMet = cms.string('genMetTrue'),
            genJets = cms.string('iterativeCone5GenJets'),
            mcparticles = cms.string('genParticles'),
            mc_nJet = mcSel_RA5RA6_2e.mc_nJet,
            mc_nPhot = mcSel_RA5RA6_2e.mc_nPhot,
            mc_nElec = mcSel_RA5RA6_2e.mc_nElec,
            mc_nMuon = mcSel_RA5RA6_2e.mc_nMuon,
            mc_ptElecMin = mcSel_RA5RA6_2e.mc_ptElecMin,
            mc_ptPhotMin = mcSel_RA5RA6_2e.mc_ptPhotMin,
            mc_ptJetMin = mcSel_RA5RA6_2e.mc_ptJetMin,
            mc_ptMuonMin = mcSel_RA5RA6_2e.mc_ptMuonMin,
            mc_metMin = mcSel_RA5RA6_2e.mc_metMin,
            mc_ptTauMin = mcSel_RA5RA6_2e.mc_ptTauMin,
            mc_ptJetForHtMin = mcSel_RA5RA6_2e.mc_ptJetForHtMin,
            mc_htMin = mcSel_RA5RA6_2e.mc_htMin,
            mc_nTau = mcSel_RA5RA6_2e.mc_nTau,
            mc_nMuonRule = mcSel_RA5RA6_2e.mc_nMuonRule,
            mc_nElecRule = mcSel_RA5RA6_2e.mc_nElecRule
        ),                       
        cms.PSet(
            name = cms.string("RA5RA6_2m"),
            genMet = cms.string('genMetTrue'),
            genJets = cms.string('iterativeCone5GenJets'),
            mcparticles = cms.string('genParticles'),
            mc_nJet = mcSel_RA5RA6_2m.mc_nJet,
            mc_nPhot = mcSel_RA5RA6_2m.mc_nPhot,
            mc_nElec = mcSel_RA5RA6_2m.mc_nElec,
            mc_nMuon = mcSel_RA5RA6_2m.mc_nMuon,
            mc_ptElecMin = mcSel_RA5RA6_2m.mc_ptElecMin,
            mc_ptPhotMin = mcSel_RA5RA6_2m.mc_ptPhotMin,
            mc_ptJetMin = mcSel_RA5RA6_2m.mc_ptJetMin,
            mc_ptMuonMin = mcSel_RA5RA6_2m.mc_ptMuonMin,
            mc_metMin = mcSel_RA5RA6_2m.mc_metMin,
            mc_ptTauMin = mcSel_RA5RA6_2m.mc_ptTauMin,
            mc_ptJetForHtMin = mcSel_RA5RA6_2m.mc_ptJetForHtMin,
            mc_htMin = mcSel_RA5RA6_2m.mc_htMin,
            mc_nTau = mcSel_RA5RA6_2m.mc_nTau,
            mc_nMuonRule = mcSel_RA5RA6_2m.mc_nMuonRule,
            mc_nElecRule = mcSel_RA5RA6_2m.mc_nElecRule
        ),
        cms.PSet(
            name = cms.string("RA7_1e2m"),
            genMet = cms.string('genMetTrue'),
            genJets = cms.string('iterativeCone5GenJets'),
            mcparticles = cms.string('genParticles'),
            mc_nJet = mcSel_RA7_1e2m.mc_nJet,
            mc_nPhot = mcSel_RA7_1e2m.mc_nPhot,
            mc_nElec = mcSel_RA7_1e2m.mc_nElec,
            mc_nMuon = mcSel_RA7_1e2m.mc_nMuon,
            mc_ptElecMin = mcSel_RA7_1e2m.mc_ptElecMin,
            mc_ptPhotMin = mcSel_RA7_1e2m.mc_ptPhotMin,
            mc_ptJetMin = mcSel_RA7_1e2m.mc_ptJetMin,
            mc_ptMuonMin = mcSel_RA7_1e2m.mc_ptMuonMin,
            mc_metMin = mcSel_RA7_1e2m.mc_metMin,
            mc_ptTauMin = mcSel_RA7_1e2m.mc_ptTauMin,
            mc_ptJetForHtMin = mcSel_RA7_1e2m.mc_ptJetForHtMin,
            mc_htMin = mcSel_RA7_1e2m.mc_htMin,
            mc_nTau = mcSel_RA7_1e2m.mc_nTau,
            mc_nMuonRule = mcSel_RA7_1e2m.mc_nMuonRule,
            mc_nElecRule = mcSel_RA7_1e2m.mc_nElecRule
        ),
        cms.PSet(
            name = cms.string("RA7_2e1m"),
            genMet = cms.string('genMetTrue'),
            genJets = cms.string('iterativeCone5GenJets'),
            mcparticles = cms.string('genParticles'),
            mc_nJet = mcSel_RA7_2e1m.mc_nJet,
            mc_nPhot = mcSel_RA7_2e1m.mc_nPhot,
            mc_nElec = mcSel_RA7_2e1m.mc_nElec,
            mc_nMuon = mcSel_RA7_2e1m.mc_nMuon,
            mc_ptElecMin = mcSel_RA7_2e1m.mc_ptElecMin,
            mc_ptPhotMin = mcSel_RA7_2e1m.mc_ptPhotMin,
            mc_ptJetMin = mcSel_RA7_2e1m.mc_ptJetMin,
            mc_ptMuonMin = mcSel_RA7_2e1m.mc_ptMuonMin,
            mc_metMin = mcSel_RA7_2e1m.mc_metMin,
            mc_ptTauMin = mcSel_RA7_2e1m.mc_ptTauMin,
            mc_ptJetForHtMin = mcSel_RA7_2e1m.mc_ptJetForHtMin,
            mc_htMin = mcSel_RA7_2e1m.mc_htMin,
            mc_nTau = mcSel_RA7_2e1m.mc_nTau,
            mc_nMuonRule = mcSel_RA7_2e1m.mc_nMuonRule,
            mc_nElecRule = mcSel_RA7_2e1m.mc_nElecRule
        ),
        cms.PSet(
            name = cms.string("RA7_3e"),
            genMet = cms.string('genMetTrue'),
            genJets = cms.string('iterativeCone5GenJets'),
            mcparticles = cms.string('genParticles'),
            mc_nJet = mcSel_RA7_3e.mc_nJet,
            mc_nPhot = mcSel_RA7_3e.mc_nPhot,
            mc_nElec = mcSel_RA7_3e.mc_nElec,
            mc_nMuon = mcSel_RA7_3e.mc_nMuon,
            mc_ptElecMin = mcSel_RA7_3e.mc_ptElecMin,
            mc_ptPhotMin = mcSel_RA7_3e.mc_ptPhotMin,
            mc_ptJetMin = mcSel_RA7_3e.mc_ptJetMin,
            mc_ptMuonMin = mcSel_RA7_3e.mc_ptMuonMin,
            mc_metMin = mcSel_RA7_3e.mc_metMin,
            mc_ptTauMin = mcSel_RA7_3e.mc_ptTauMin,
            mc_ptJetForHtMin = mcSel_RA7_3e.mc_ptJetForHtMin,
            mc_htMin = mcSel_RA7_3e.mc_htMin,
            mc_nTau = mcSel_RA7_3e.mc_nTau,
            mc_nMuonRule = mcSel_RA7_3e.mc_nMuonRule,
            mc_nElecRule = mcSel_RA7_3e.mc_nElecRule
        ),
        cms.PSet(
            name = cms.string("RA7_3m"),
            genMet = cms.string('genMetTrue'),
            genJets = cms.string('iterativeCone5GenJets'),
            mcparticles = cms.string('genParticles'),
            mc_nJet = mcSel_RA7_3m.mc_nJet,
            mc_nPhot = mcSel_RA7_3m.mc_nPhot,
            mc_nElec = mcSel_RA7_3m.mc_nElec,
            mc_nMuon = mcSel_RA7_3m.mc_nMuon,
            mc_ptElecMin = mcSel_RA7_3m.mc_ptElecMin,
            mc_ptPhotMin = mcSel_RA7_3m.mc_ptPhotMin,
            mc_ptJetMin = mcSel_RA7_3m.mc_ptJetMin,
            mc_ptMuonMin = mcSel_RA7_3m.mc_ptMuonMin,
            mc_metMin = mcSel_RA7_3m.mc_metMin,
            mc_ptTauMin = mcSel_RA7_3m.mc_ptTauMin,
            mc_ptJetForHtMin = mcSel_RA7_3m.mc_ptJetForHtMin,
            mc_htMin = mcSel_RA7_3m.mc_htMin,
            mc_nTau = mcSel_RA7_3m.mc_nTau,
            mc_nMuonRule = mcSel_RA7_3m.mc_nMuonRule,
            mc_nElecRule = mcSel_RA7_3m.mc_nElecRule
        )
    ),

    mc_flag = cms.untracked.bool(True), ## put mc_flag = false if you don't want to use the mc information.
    l1_flag = cms.untracked.bool(False), ## put l1_flag = false if you don't want the plots for the L1 objects. 
                                         ## Put false for usage in the DQM framework (reduce the number of bins).
    triggerTag = cms.InputTag("hltTriggerSummaryAOD"),
    hltConfigName = cms.string("HLT"),
    hltPathsToCheck = cms.vstring(
      "HLT_PFHT900_v",
      "HLT_PFHT350_PFMET120_NoiseCleaned_v",
      "HLT_PFMET170_NoiseCleaned_v",
      "HLT_PFMET120_NoiseCleaned_BTagCSV07_v"
    ),
    muonTag = cms.InputTag('muons'),
    histoFileName = cms.untracked.string('MonElements_LM1_IDEAL_30x_v1_300pre7.root'),
    PlotMakerL1Input = cms.PSet(
        l1extramc = cms.string('hltL1extraParticles')
    ),
    PlotMakerRecoInput = cms.PSet(
        def_electronPtMin = cms.double(10.0),
        def_muonPtMin = cms.double(7.0),
        def_photonPtMin = cms.double(30.0),
        calomet = cms.string('caloMet'),
        electrons = cms.string('gedGsfElectrons'),
        jets = cms.string('iterativeCone5CaloJets'),
        muons = cms.string('muons'),
        def_jetPtMin = cms.double(30.0),
        photons = cms.string(''),
        photonProducer = cms.string('photons'),
        BinFactor = cms.int32(1) #put a number >1 to have a larger number of bins for eta and phi distributions. Put 1 for DQM.
    )
)
