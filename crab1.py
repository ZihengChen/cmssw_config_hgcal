from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'muons_step1'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'step1.py'

config.Data.outputPrimaryDataset = 'muons'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 100
NJOBS = 100  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputDatasetTag = 'muons_step1'

config.Site.whitelist = ["T2_US*"]
config.Site.storageSite = 'T3_US_FNALLPC'
