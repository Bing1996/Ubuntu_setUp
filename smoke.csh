clear

echo "processing SMOKE"
setenv SMK_HOME /home/bing/SMOKE

cd $SMK_HOME/subsys/smoke/assigns
source ASSIGNS.nctox.cmaq.cb05_soa.us12-nc

cd
cd $SMK_HOME/subsys/smoke/scripts/run
./smk_area_nctox.csh
cd
 
