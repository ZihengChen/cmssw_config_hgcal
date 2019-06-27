# cmssw_config_hgcal

The cmsRun config files are based on `CMSSW_11_0_0_pre2`. To set Up CRAB environment, do the following command. If you have problem with grid certificate, visit [here](https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookStartingGrid)
```
cmsenv
source /cvmfs/cms.cern.ch/cmsset_default.sh
source /cvmfs/cms.cern.ch/crab3/crab.sh
voms-proxy-init --rfc --voms cms
```

Useful crab commands are listed.
* `crab submit -c <CRAB_CONFIG.py>`
* `crab status -d <PROJECT/DIR>`
* `crab kill -d <PROJECT/DIR>`
* `crab checkusername` 
* `crab checkwrite --site=T3_US_FNALLPC` 
