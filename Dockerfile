FROMpython:3.9
WORKDIR.
ENVPYTHONUNBUFFERED=1
COPYrequirements.txt.
COPYdeploy.sh.
RUNbashdeploy.sh
COPY..
CMD["python3","-m","Ineruki"]
