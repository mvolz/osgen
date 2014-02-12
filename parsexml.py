import xml.etree.ElementTree as ET

def loadxml(xmlfile):
    tree = ET.parse(xmlfile)
    root = tree.getroot()
    if root.tag != 'data':
        print 'The root tag of the XML file must be an <data> tag.'
        return
    else:
        #gettrait(root)
        getgenotypes(root)


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
    print traitdict
    
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
    
def gettext(root, text):
    '''
    returns variable corresponding to text within a tag
    '''
    try:
        return root.getiterator(text)[0].text.strip()
    except IndexError:
        return None
        
def getgenotypes(root):
    '''
    return a dict of dicts in the format {'genotype':{'shortmeaning':'meaninghere', 'longmeaning':'meaninghere'}}
    '''
    gendict = {}
    for tag in root.findall("output"):
        print "here"
        print tag
        print tag.text
    
    #find all output tags and put them to determine output type
    print gendict
    return gendict
    
def calcor(root, user_genome, ethnicity):
    '''Calculates odds ratio of having a given phenotype given the users genome,
    their ethnicity (self reported) and the risk alleles reported here'''
    
    
def phenotype(root):
    '''
    Parses an XML file in which a genotype corresponds to one or 
    multiple phenotypes.
    Sample XML file is in /xmlschemas/
    '''
    getgenotypes(root)
    gettrait(root)

def probability(root):
    '''
    Parses an XML file in which output is a probability
    of the phenotype or disease described in the <outcome> tag.
    Sample XML file is in /xmlschemas/
    '''
    gettrait(root)
    
    

if  __name__ =='__main__':

    determineOutputType('xml schemas/phenotype.xml')
    determineOutputType('xml schemas/probability.xml')
    
    
