import xml.etree.ElementTree as ET

#Classes
class Report():
    '''
    Report on a study with user results
    '''
    #trait = 
    pass
    
class Phenotypes():
    '''
    Information about phenotypes
    '''
    
class Trait():
    '''
    Information about traits
    '''
    pass

class Genotype():
    #genotype = 
    #shortmeaning=
    #longmeaning = 
    pass


#Functions
def run(xmlfile):
    #root = loadxml(xmlfile)
    #gettrait(root)
    #getreports(root)
    returnSNPs(xmlfile)

def loadxml(xmlfile):
    tree = ET.parse(xmlfile)
    root = tree.getroot()
    if root.tag != 'data':
        print 'The root tag of the XML file must be an <data> tag.'
        return
    else:
        return root

def returnSNPs(xmlfile):
    '''
    Returns list of rsids of all the SNPs reported on in a file.
    '''
    root = loadxml(xmlfile)
    snps = []
    for o in root.findall("output"):
        for s in o.findall("SNP"):
            snps.append(s.find("rsid").text)
    #print snps
    return snps
    

def determineOutputType(xmlfile):
    #outdated code below. 
    #else:
        #try:
            #otype = root.attrib['type']
        #except KeyError:
            #print 'Output tags must have a \'type\' attribute'
            #return
        #finally:
            #if otype == 'phenotype':
                #print otype
                #phenotype(root)
            #elif otype == 'probability':
                #print otype
                #probability(root)
            #else:
                #print 'Currently the only allowed values for the type attribute are \'phenotype\' and \'probability\''

    pass
        
def gettrait(root):
    '''
    Gets information about the trait.
    This is standardized in both the probability.xml and phenotype.xml
    '''
    
    '''below are different ways of getting trait info'''
    
 
    #get child elements of trait tag

    trait = root.getiterator("trait")[0]

    traitdict = {}
    for child in trait:
        traitdict[child.tag] = child.text.strip()
    
    for key, value in traitdict.items():
        print "%s: %s\n" % (key,value)
    
    #another way- gets only tags specified in unstrucuredtags lists
    #list of tags of which there is only one in the file and describe the trait
    #create a dict of these and their values
    #no error handling here, beware.
    unstructtagdict = {}
    unstructuredtags = ["name", "wikipedialink", "supertrait", "subtrait"]
    for t in unstructuredtags:
        unstructtagdict[t] = gettext(root,t)
    #print unstructtagdict
    
    #alternatively these can be made into python variables
    name = gettext(root, "name")
    wlink = gettext(root,"wikipedialink")
    supertrait = gettext(root,"supertrait")
    subtrait = gettext(root,"subtrait")
    
    #the description may have subelements (likely citations) so the element
    #is returned here, instead of text.
    try:
        description = root.getiterator("description")[0]
    except:
        description = None
        
    return traitdict
    
def gettext(root, text):
    '''
    returns variable corresponding to text within a tag
    '''
    try:
        return root.getiterator(text)[0].text.strip()
    except IndexError:
        return None
        
def getreports(root):
    '''
    gets report from each output tag
    '''
    report_list = []
    for o in root.findall("output"):
        output_type = o.get("type")
        if output_type == "phenotype":
            report_list.append(reportify_phenotype(o))
        else:
            print "The output type \'%s\' is not currently supported" % output_type
    #print report_list
    return report_list


def reportify_phenotype(o_tag):
    '''
    Returns a list of tuples in the format (ethnicity_string, genotype_dict)
    '''
    
    try:
        gettrait(o_tag) #prints trait information specfic to report
    except:
        pass
        
    report = []
        
    snps = o_tag.findall('SNP')
    for s in snps:
        #each snp should have exactly one rsid
        rsid = "SNP RSID: %s" % s.find("rsid").text
        print rsid
        
        ethnicity = s.findall("ethnicity")
        for e in ethnicity:
            genotype_dict = getgenotypes(e)
            eth_name = e.attrib["value"]
            report.append((eth_name,genotype_dict))
    
    #print report
    return report

def getgenotypes(ethnicity):
    '''
    return dict of genotypes and meanings
    '''
    genotype_dict = {}
    genotypes = ethnicity.findall("genotype")
    for g in genotypes:
        genotype = g.get('value')
        meanings = {}
        for child in g:
            meanings[child.tag] = child.text.strip() 
        genotype_dict[genotype] = meanings
    return genotype_dict

        
def reportify_probability(root):
    '''
    Parses an output tag where a probability
    of the phenotype or disease described in the <outcome> tag.
    Sample XML file is in /xmlschemas/
    '''
    pass


if  __name__ =='__main__':

    #loadxml('xml schemas/phenotype.xml')
    #loadxml('xml schemas/probability.xml')
    returnSNPs("xml files/eye_color.xml")
    #loadxml("xml files/spherical_errors.xml")
    
    
