import sys
sys.path.append('snpy')

from loadgenome import load23andme, loadgensnpy
from parsexml import loadxml, returnSNPs, get_trait_obj, get_xml_filelist
import sn
from xml.etree.ElementTree import ParseError

#This file primarily provides functions that intersect report xml data and genome data
                
def get_subset(genome):
    '''
    Returns subset of genome containing SNPs relevant xml files
    '''
    genome_dict = {}
    snps_list = []
    
    #iterate through files to get all snps
    for f in get_xml_filelist():
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

def get_summary(genome_dict):
    '''
    Gets a summary of all the traits and the short meaning of the phenotype
    '''
    genome_dict = get_subset(genome)
    filelist = get_xml_filelist()
    
    for f in filelist:
        pass
    
def punnet(genome1,genome2):
    '''cross two genomes (make a baby)'''
    pass


if  __name__ =='__main__':

    subset = get_subset("../sample genomes/1117.23andme.txt")
    
