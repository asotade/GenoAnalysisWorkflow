import subprocess
import os

files_dir = os.path.dirname(os.path.realpath(__file__))+"../media/"
samfile = "aligned.sam"
bamfile = "aligned.bam"
bamRGfile = "alignedRG.bam"
bamRGSORfile = "alignedRGSOR.bam"


def realfile(filename):
    return files_dir+filename


def align_to_sam(reff,forward,reverse):
    return subprocess.call("bwa mem '" + realfile(reff) + "' '" + realfile(forward) + "' '" + realfile(reverse) + "' > "+realfile(samfile),shell=True)


def align_to_bam(reff,forward,reverse):
    aligned_to_sam = align_to_sam(reff,forward,reverse):
    if aligned_to_sam == 0:
        return subprocess.call("samtools view -b " + realfile(samfile) + " > " + realfile(bamfile) ,shell=True)
    else:
        return aligned_to_sam


def readgroup(reff,forwar,reverse):
        aligned_to_bam = align_to_bam(reff,forward,reverse):
        if aligned_to_bam == 0:
            return subprocess.call("java -jar picard.jar  AddOrReplaceReadGroups I=" + realfile(bamfile) + "' O=" +  realfile(bamRGfile) + "' RGID=FLOWCELL1 RGLB=lib1 RGPL=illumina RGPU=unit1 RGSM=patient1",shell=True)
        else:
            return aligned_to_bam


def sortbam(reff,forwar,reverse):
        read_group = readgroup(reff,forward,reverse):
        if read_group == 0:
            return subprocess.call("java -jar picard.jar SortSam INPUT=" +  realfile(bamRGfile) + " OUTPUT=" +  realfile(bamRGSORfile) + " SORT_ORDER=coordinate ",shell=True)
        else:
            return read_group


def indexing(reff,forwar,reverse):
        sorted_bam = sortbam(reff,forward,reverse):
        if sorted_bam == 0:
            return subprocess.call("java -jar picard.jar BuildBamIndex INPUT=" +  realfile(bamRGSORfile) ,shell=True)
        else:
            return sorted_bam
