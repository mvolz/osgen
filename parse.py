import xml.etree.ElementTree as ET

def determineOutputType(xmlfile):
    tree = ET.parse(xmlfile)
    root = tree.getroot()
    if root.tag != 'output':
        print 'The root tag of the XML file must be an <output> tag.'
        return
    else:
        try:
            otype = root.attrib['type']
        except KeyError:
            print 'Output tags must have a \'type\' attribute'
            return
        finally:
            if otype == 'phenotype':
                print otype
                phenotype(root)
            elif otype == 'probability':
                print otype
                probability(root)
            else:
                print 'Currently the only allowed values for the type attribute are \'phenotype\' and \'probability\''

        

def phenotype(root):
    '''
    Parses an XML file in which a trait corresponds to multiple phenotypes.
    Sample XML file is in /xmlschemas/
    
    For the time being, the output of phenotype files will be a phenotype
    corresponding to one SNP.
    '''
    pass
    
def probability(root):
    '''
    Parses an XML file in which a trait corresponds to a multiple SNPs.
    Sample XML file is in /xmlschemas/
    
    For the time being, the output of a multipleSNP files will be a probability
    of the phenotype or disease described in the <outcome> tag.
    '''
    pass
    
    

if  __name__ =='__main__':

    determineOutputType('xml schemas/phenotype.xml')
    determineOutputType('xml schemas/probability.xml')
    
    
