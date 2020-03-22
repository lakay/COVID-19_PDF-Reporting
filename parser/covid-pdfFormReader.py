# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from collections import OrderedDict
from PyPDF2 import PdfFileWriter, PdfFileReader
from os import listdir
from os.path import isfile, join
from pprint import pprint
import pandas as pd

def _getFields(obj, tree=None, retval=None, fileobj=None):
    """
    Extracts field data if this PDF contains interactive form fields.
    The *tree* and *retval* parameters are for recursive use.

    :param fileobj: A file object (usually a text file) to write
        a report to on all interactive form fields found.
    :return: A dictionary where each key is a field name, and each
        value is a :class:`Field<PyPDF2.generic.Field>` object. By
        default, the mapping name is used for keys.
    :rtype: dict, or ``None`` if form data could not be located.
    """
    fieldAttributes = {'/FT': 'Field Type', '/Parent': 'Parent', '/T': 'Field Name', '/TU': 'Alternate Field Name',
                       '/TM': 'Mapping Name', '/Ff': 'Field Flags', '/V': 'Value', '/DV': 'Default Value'}
    if retval is None:
        retval = OrderedDict()
        catalog = obj.trailer["/Root"]
        # get the AcroForm tree
        if "/AcroForm" in catalog:
            tree = catalog["/AcroForm"]
        else:
            return None
    if tree is None:
        return retval

    obj._checkKids(tree, retval, fileobj)
    for attr in fieldAttributes:
        if attr in tree:
            # Tree is a field
            obj._buildField(tree, retval, fileobj, fieldAttributes)
            break

    if "/Fields" in tree:
        fields = tree["/Fields"]
        for f in fields:
            field = f.getObject()
            obj._buildField(field, retval, fileobj, fieldAttributes)

    return retval


def get_form_fields(infile):
    infile = PdfFileReader(open(infile, 'rb'))
    fields = _getFields(infile)
    return OrderedDict((k, v.get('/V', '')) for k, v in fields.items())


# %%
def cleanAndReorderDict(oDict:OrderedDict) -> OrderedDict:
    for key,value in oDict.items():
        #if('/True' in value):
        #    value=True
        #if('/False' in value):
        #    value=False
        print(key,value)


# %%

def getAllForms(mypath):
    allForms = []
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

    for currentFile in onlyfiles:
        if '.pdf' in currentFile:
            allForms.append(mypath + currentFile)
    return allForms

# %%
def run_all():
    labPath= '../test-forms/labor_covid19/'
    formsLabList = getAllForms(labPath)
    for labForm in formsLabList:
        labDict=get_form_fields(labForm)


    meldungPath='../test-forms/covid19/'
    formsMeldungList = getAllForms(meldungPath)
    meldungDictList=[]
    for meldForm in formsMeldungList:
        meldDict=get_form_fields(meldForm)
        meldungDictList.append(meldDict)

    cleanAndReorderDict(meldDict)

    df=pd.DataFrame(meldungDictList)
    df.head()

    meldungenCsv='covid19.csv'
    df.to_csv(meldungPath + 'csv/' + meldungenCsv,sep=';')


# %%
import argparse

if __name__ == "__main__":
    parser=argparse.ArgumentParser(
        description='''This Script reads a given set of PDF Forms for COVID19 Reporting from a folder and reads all Form Data and writes it to a csv file. ''',
        epilog='''Please report problems and enhancements at https://github.com/lakay/COVID-19_PDF-Reporting. '''
    )
    parser.add_argument('-type','-ft','--ft', type=str, metavar='form type',default='am', help='am for Arzt Meldung, lm for Labor Meldung, tm for Todes Meldung')
    parser.add_argument('-o','--o','-out', type=str,metavar='Output',default='../test-forms/covid19/csv/covid19.csv', help='Path and Filename for the output csv')
    parser.add_argument('path', nargs=1, type=str, metavar='path', default='../test-forms/covid19/', help='pfad zu den PDF Formularen')
    args=parser.parse_args()
    
    run_all()



# %%
