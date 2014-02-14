import sys, glob, os
sys.path.append('snpy')

from loadgenome import load23andme, loadgensnpy
from parsexml import loadxml, returnSNPs
import sn
from xml.etree.ElementTree import ParseError

#gendict = load23andme("sample genomes/sample.23andme.txt")
#xmlfile = loadxml("xml files/eye_color.xml")
#gensnpy = loadgensnpy("sample genomes/1117.23andme.txt")
#print gensnpy
#print gensnpy.next()

def get_filelist():
    filelist = []
    os.chdir("xml files")
    for f in glob.glob("*.xml"):
        filelist.append(f)
    return filelist
                
def get_subset(genome):
    '''
    Returns subset of genome containing information found in xml files
    '''
    genome_dict = {}
    snps_list = []
    
    #iterate through files to get all snps
    for f in get_filelist():
        try:
            #get all the SNPs in a file
            snps = returnSNPs(f)
        except ParseError:
            pass
        finally:
            if len(snps) >= 1:
                snps_list.extend(snps)
    
    #iterate through genome to find all relevant snps
    gensnpy = loadgensnpy(genome)
    for s in gensnpy:
        if s.name in snps_list:
            genome_dict[s.name]=s.genotype
            
    #print genome_dict
    return genome_dict

def punnet(genome1,genome2):
    '''cross two genomes (make a baby)'''
    pass
    
    
if  __name__ =='__main__':
    #flist = get_filelist()
    #print flist
    subset = get_subset("../sample genomes/1117.23andme.txt")
    #print subset
