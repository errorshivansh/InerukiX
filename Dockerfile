FROMXpython:3.9
WORKDIRX.
ENVXPYTHONUNBUFFERED=1
COPYXrequirements.txtX.
COPYXdeploy.shX.
RUNXbashXdeploy.sh
COPYX.X.
CMDX["python3",X"-m",X"InerukiX"]
