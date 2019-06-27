# cmssw_config_hgcal

To set Up CRAB environment
```
cmsenv
source /cvmfs/cms.cern.ch/cmsset_default.sh
source /cvmfs/cms.cern.ch/crab3/crab.sh
voms-proxy-init --rfc --voms cms
```
Note: if you have problem with grid certificate, visit [here](https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookStartingGrid)

Useful commands are listed.
* `crab submit -c <CRAB_CONFIG.py>`
* `crab status -d <PROJECT/DIR>`
* `crab kill -d <PROJECT/DIR>`
* `crab checkusername` 
* `crab checkwrite --site=T3_US_FNALLPC` 
