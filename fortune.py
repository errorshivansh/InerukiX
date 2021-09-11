importcodecs
importrandom
importre
importsys
fromoptparseimportOptionParser

#---------------------------------------------------------------------------
#Exports
#---------------------------------------------------------------------------

__all__=["main","get_random_fortune"]

#Infoaboutthemodule
__version__="1.1.0"
__author__="BrianM.Clapper"
__email__="bmc@clapper.org"
__url__="http://software.clapper.org/fortune/"
__copyright__="2008-2019BrianM.Clapper"
__license__="BSD-stylelicense"

#---------------------------------------------------------------------------
#Functions
#---------------------------------------------------------------------------


def_random_int(start,end):
try:
#UseSystemRandom,ifit'savailable,sinceit'slikelytohave
#moreentropy.
r=random.SystemRandom()
exceptBaseException:
r=random

returnr.randint(start,end)


def_read_fortunes(fortune_file):
withcodecs.open(fortune_file,mode="r",encoding="utf-8")asf:
contents=f.read()

lines=[line.rstrip()forlineincontents.split("\n")]

delim=re.compile(r"^%$")

fortunes=[]
cur=[]

defsave_if_nonempty(buf):
fortune="\n".join(buf)
iffortune.strip():
fortunes.append(fortune)

forlineinlines:
ifdelim.match(line):
save_if_nonempty(cur)
cur=[]
continue

cur.append(line)

ifcur:
save_if_nonempty(cur)

returnfortunes


defget_random_fortune(fortune_file):
fortunes=list(_read_fortunes(fortune_file))
randomRecord=_random_int(0,len(fortunes)-1)
returnfortunes[randomRecord]


defmain():
usage="Usage:%prog[OPTIONS][fortune_file]"
arg_parser=OptionParser(usage=usage)
arg_parser.add_option(
"-V",
"--version",
action="store_true",
dest="show_version",
help="Showversionandexit.",
)
arg_parser.epilog=(
"Iffortune_fileisomitted,fortunelooksatthe"
"FORTUNE_FILEenvironmentvariableforthepath."
)

options,args=arg_parser.parse_args(sys.argv)
iflen(args)==2:
fortune_file=args[1]

else:
try:
fortune_file="notes.txt"
exceptKeyError:
print("Missingfortunefile.",file=sys.stderr)
print(usage,file=sys.stderr)
sys.exit(1)

try:
ifoptions.show_version:
print("fortune,version{}".format(__version__))
else:
print(get_random_fortune(fortune_file))
exceptValueErrorasmsg:
print(msg,file=sys.stderr)
sys.exit(1)


if__name__=="__main__":
main()
