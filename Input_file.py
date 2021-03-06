
#************************************************************************

TestCaseSheet = "C:\\ROBOTSERVER_FILES\\OUPUT_FILE\\Polycom.xls"
LogFileLoc = "C:\\logs\\"
ReportPath = "C:\\logs\\"
LogForBug = "C:\\Logforbug\\logforbug.txt"
#**************************************************************************
SPEEDLIST="128"
CALLTYPE="H323"
DUT1="10.75.15.108"
DUT2="10.75.15.109"
#DUT3="172.21.128.83"
#DUT4="172.20.177.40"
DUT5="10.14.12.58"
BRIDGENO="10.234.104.173##76904071"
TELNET_PORT_NUMBER="24"
CALLER_ID2=""
CALL_TYPE2=""
DUT1_PROMPT_VALUE=""
DUT2_PROMPT_VALUE=""
CALLTYPE2="SIP"
DUT1GATEKEEPER_IP="10.223.80.30"
DUT2GATEKEEPER_IP="10.223.80.30"
CALL1="0"
TXRATE1="128"
KVALUE1="K"
RXRATE1="128"
PKTLOSS1="0"
PERCENTPKTLOSS1="0.0 %"
TVP1="H.264-HP"
RVP1="H.264-HP"
TVF1="768x448"
RVF1="1024x576"
TAP1="SirenLPR"
RAP1="SirenLPR"
TCP1="H.323"
RCP1="H.323"
FIRSTSITE="0"
SECONDSITE="1"

SIPTCP1="sip"
SIPRCP1="sip"
SIP_NETSTATS="tcp:sip rcp:sip"
H323_NETSTATS="tcp:H.323 rcp:H.323"
SOURCE_IS_CONNECTED="YES"
CONTENT="3"


tc1="H323P2P_NoGK"
tc3="TelnetBasicH323P2PNoGKMarsToMars"
tc2="TelnetBasicH323P2PNoGKSaturntoMars"
tc4="P2PSIPCALL"
tc5="SIPP2P_NoServerNoIp"