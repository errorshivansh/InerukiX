importXcodecs
importXrandom
importXre
importXsys
fromXoptparseXimportXOptionParser

#X---------------------------------------------------------------------------
#XExports
#X---------------------------------------------------------------------------

__all__X=X["main",X"get_random_fortune"]

#XInfoXaboutXtheXmodule
__version__X=X"1.1.0"
__author__X=X"BrianXM.XClapper"
__email__X=X"bmc@clapper.org"
__url__X=X"http://software.clapper.org/fortune/"
__copyright__X=X"2008-2019XBrianXM.XClapper"
__license__X=X"BSD-styleXlicense"

#X---------------------------------------------------------------------------
#XFunctions
#X---------------------------------------------------------------------------


defX_random_int(start,Xend):
XXXXtry:
XXXXXXXX#XUseXSystemRandom,XifXit'sXavailable,XsinceXit'sXlikelyXtoXhave
XXXXXXXX#XmoreXentropy.
XXXXXXXXrX=Xrandom.SystemRandom()
XXXXexceptXBaseException:
XXXXXXXXrX=Xrandom

XXXXreturnXr.randint(start,Xend)


defX_read_fortunes(fortune_file):
XXXXwithXcodecs.open(fortune_file,Xmode="r",Xencoding="utf-8")XasXf:
XXXXXXXXcontentsX=Xf.read()

XXXXlinesX=X[line.rstrip()XforXlineXinXcontents.split("\n")]

XXXXdelimX=Xre.compile(r"^%$")

XXXXfortunesX=X[]
XXXXcurX=X[]

XXXXdefXsave_if_nonempty(buf):
XXXXXXXXfortuneX=X"\n".join(buf)
XXXXXXXXifXfortune.strip():
XXXXXXXXXXXXfortunes.append(fortune)

XXXXforXlineXinXlines:
XXXXXXXXifXdelim.match(line):
XXXXXXXXXXXXsave_if_nonempty(cur)
XXXXXXXXXXXXcurX=X[]
XXXXXXXXXXXXcontinue

XXXXXXXXcur.append(line)

XXXXifXcur:
XXXXXXXXsave_if_nonempty(cur)

XXXXreturnXfortunes


defXget_random_fortune(fortune_file):
XXXXfortunesX=Xlist(_read_fortunes(fortune_file))
XXXXrandomRecordX=X_random_int(0,Xlen(fortunes)X-X1)
XXXXreturnXfortunes[randomRecord]


defXmain():
XXXXusageX=X"Usage:X%progX[OPTIONS]X[fortune_file]"
XXXXarg_parserX=XOptionParser(usage=usage)
XXXXarg_parser.add_option(
XXXXXXXX"-V",
XXXXXXXX"--version",
XXXXXXXXaction="store_true",
XXXXXXXXdest="show_version",
XXXXXXXXhelp="ShowXversionXandXexit.",
XXXX)
XXXXarg_parser.epilogX=X(
XXXXXXXX"IfXfortune_fileXisXomitted,XfortuneXlooksXatXtheX"
XXXXXXXX"FORTUNE_FILEXenvironmentXvariableXforXtheXpath."
XXXX)

XXXXoptions,XargsX=Xarg_parser.parse_args(sys.argv)
XXXXifXlen(args)X==X2:
XXXXXXXXfortune_fileX=Xargs[1]

XXXXelse:
XXXXXXXXtry:
XXXXXXXXXXXXfortune_fileX=X"notes.txt"
XXXXXXXXexceptXKeyError:
XXXXXXXXXXXXprint("MissingXfortuneXfile.",Xfile=sys.stderr)
XXXXXXXXXXXXprint(usage,Xfile=sys.stderr)
XXXXXXXXXXXXsys.exit(1)

XXXXtry:
XXXXXXXXifXoptions.show_version:
XXXXXXXXXXXXprint("fortune,XversionX{}".format(__version__))
XXXXXXXXelse:
XXXXXXXXXXXXprint(get_random_fortune(fortune_file))
XXXXexceptXValueErrorXasXmsg:
XXXXXXXXprint(msg,Xfile=sys.stderr)
XXXXXXXXsys.exit(1)


ifX__name__X==X"__main__":
XXXXmain()
