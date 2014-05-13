# Sample platypus document
# From the FAQ at reportlab.org/oss/rl-toolkit/faq/#1.1

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch

from loadgenome import load23andme, loadgensnpy
from parsexml import loadxml, returnSNPs, get_xml_filelist
from join import get_subset, get_summary

#This file makes pdf reports of the data

PAGE_HEIGHT=defaultPageSize[1]
PAGE_WIDTH=defaultPageSize[0]
styles = getSampleStyleSheet()

pageinfo = "OSGEN report"
Title = "OSGEN report"

def myFirstPage(canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Bold',16)
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-108, Title)
    canvas.setFont('Times-Roman',9)
    canvas.drawString(inch, 0.75 * inch,"First Page / %s" % pageinfo)
    canvas.restoreState()
    
def myLaterPages(canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Roman', 9)
    canvas.drawString(inch, 0.75 * inch,"Page %d %s" % (doc.page, pageinfo))
    canvas.restoreState()

def gen_report(genome_file_name):
    subset = get_subset(genome_file_name)
    summmary = get_summary(subset)
    
def go(genome_file_name, output_file):
    global Title
    Title = "Report on genome file %s" % genome_file_name
    doc = SimpleDocTemplate(str(output_file) + ".pdf")
    Story = [Spacer(1,2*inch)]
    style = styles["Normal"]

    report_list = []

    for i in range(1,24):
        if i <=22:
            bogustext = ("Chromosome %s is cool. " % i) *22
        else:
            bogustext = ("The X chromosome is cooler than the y chromosome. ") *23
        report_list.append(bogustext)

    for r in report_list:
        p = Paragraph(r, style)
        Story.append(p)
        Story.append(Spacer(1,0.2*inch))

    doc.build(Story, onFirstPage=myFirstPage, onLaterPages=myLaterPages)
    print "Results generated in file %s.pdf" % output_file

    
if __name__ == "__main__":
    go("../sample genomes/1117.23andme.txt", "sample_results")
