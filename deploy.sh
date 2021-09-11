
echo"
***********STARTINGDEPLOY***********

INERUKIv2-BaseAiogram
(C)2020-2021by@errorshivansh
SupportChatis@INERUKISUPPORT_OFFICIAL.

***************************************
"
update_and_install_packages(){
apt-qqupdate-y
apt-qqinstall-y--no-install-recommends\
git\
ffmpeg\
mediainfo\
unzip\
wget\
gifsicle
}

install_helper_packages(){
wgethttps://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb&&apt-fqqyinstall./google-chrome-stable_current_amd64.deb&&rmgoogle-chrome-stable_current_amd64.deb
wgethttps://chromedriver.storage.googleapis.com/88.0.4324.96/chromedriver_linux64.zip&&unzipchromedriver_linux64.zip&&chmod+xchromedriver&&mv-fchromedriver/usr/bin/&&rmchromedriver_linux64.zip
wget-Oopencv.ziphttps://github.com/opencv/opencv/archive/master.zip&&unzipopencv.zip&&mv-fopencv-master/usr/bin/&&rmopencv.zip
wgethttps://people.eecs.berkeley.edu/~rich.zhang/projects/2016_colorization/files/demo_v2/colorization_release_v2.caffemodel-P./bot_utils_files/ai_helpers/
}

ech_final(){
echo"

=++---------------------------------------------++=
INERUKI.DeployedSuccessfully

***************************

───────────────────────────────────────────────────────────────────────────────────────────────────────────────
─██████████─██████──────────██████─██████████████─████████████████───██████──██████─██████──████████─██████████
─██▒▒▒▒▒▒██─██▒▒██████████──██▒▒██─██▒▒▒▒▒▒▒▒▒▒██─██▒▒▒▒▒▒▒▒▒▒▒▒██───██▒▒██──██▒▒██─██▒▒██──██▒▒▒▒██─██▒▒▒▒▒▒██
─████▒▒████─██▒▒▒▒▒▒▒▒▒▒██──██▒▒██─██▒▒██████████─██▒▒████████▒▒██───██▒▒██──██▒▒██─██▒▒██──██▒▒████─████▒▒████
───██▒▒██───██▒▒██████▒▒██──██▒▒██─██▒▒██─────────██▒▒██────██▒▒██───██▒▒██──██▒▒██─██▒▒██──██▒▒██─────██▒▒██──
───██▒▒██───██▒▒██──██▒▒██──██▒▒██─██▒▒██████████─██▒▒████████▒▒██───██▒▒██──██▒▒██─██▒▒██████▒▒██─────██▒▒██──
───██▒▒██───██▒▒██──██▒▒██──██▒▒██─██▒▒▒▒▒▒▒▒▒▒██─██▒▒▒▒▒▒▒▒▒▒▒▒██───██▒▒██──██▒▒██─██▒▒▒▒▒▒▒▒▒▒██─────██▒▒██──
───██▒▒██───██▒▒██──██▒▒██──██▒▒██─██▒▒██████████─██▒▒██████▒▒████───██▒▒██──██▒▒██─██▒▒██████▒▒██─────██▒▒██──
───██▒▒██───██▒▒██──██▒▒██████▒▒██─██▒▒██─────────██▒▒██──██▒▒██─────██▒▒██──██▒▒██─██▒▒██──██▒▒██─────██▒▒██──
─████▒▒████─██▒▒██──██▒▒▒▒▒▒▒▒▒▒██─██▒▒██████████─██▒▒██──██▒▒██████─██▒▒██████▒▒██─██▒▒██──██▒▒████─████▒▒████
─██▒▒▒▒▒▒██─██▒▒██──██████████▒▒██─██▒▒▒▒▒▒▒▒▒▒██─██▒▒██──██▒▒▒▒▒▒██─██▒▒▒▒▒▒▒▒▒▒██─██▒▒██──██▒▒▒▒██─██▒▒▒▒▒▒██
─██████████─██████──────────██████─██████████████─██████──██████████─██████████████─██████──████████─██████████
───────────────────────────────────────────────────────────────────────────────────────────────────────────────

*******************v0.0.1**

ThanksfordeployingIneruki
(C)2020-2021by@errorshivansh
SupportChatis@INERUKISUPPORT_OFFICIAL.
=++---------------------------------------------++=
Greetingsfromdevteam:)
"
}

_run_all(){
UPDATE
install_helper_packages
pip3install–upgradepip
pip3install--no-cache-dir-rrequirements.txt
ech_final
}

_run_all
