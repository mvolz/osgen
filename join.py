import sys
sys.path.append('snpy')

from loadgenome import load23andme, loadgensnpy
from parsexml import loadxml
import sn


#gendict = load23andme("sample genomes/sample.23andme.txt")
xmlfile = loadxml("xml files/eye_color.xml")
#gensnpy = loadgensnpy("sample genomes/1117.23andme.txt")
#print gensnpy
#print gensnpy.next()

