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

def get_summary(genome):
    '''
    Gets a summary of all the traits and the short meaning of the phenotype
    '''
    filelist = get_xml_filelist()
    #print filelist
    
    genome_dict = get_subset(genome)
    #print genome_dict
    
    for f in filelist:
        trait = get_trait_obj(f)
        print trait.name

    
def punnett(genome1,genome2):
    '''cross two genomes (make a baby)'''
    pass


if  __name__ =='__main__':

    subset = get_summary("sample genomes/sample.23andme.txt")
    
