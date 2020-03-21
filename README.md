# COVID-19_PDF-Reporting
Adapted PDF Forms of the Swiss BAG and Parsing Tools for automatic Form parsing

## The Forms
The PDF Forms of the Swiss BAG which are provided under [BAG COVID-19 Meldeformulare](https://www.bag.admin.ch/bag/de/home/krankheiten/infektionskrankheiten-bekaempfen/meldesysteme-infektionskrankheiten/meldepflichtige-ik/meldeformulare.html) are currently incomplete and have a lot artefacts due to automatic Generation from a Visio Document.

In the forms folder we provide corrected PDF Forms, which:

   * have Form Fields for every necessary Input
   * have for every Formfield a unique and meaningful identifier, so that they can be considered easily machine readable
   * have a fixed Tabular Navigation, so that keyboard based filling is easy to be done
   * have additional information to support easy submition of the digital form by email
   
## The Parser
The Parser for the Forms is python based and requires the PyPDF2 Module. A requirements.txt is provided for easy installation of the necessary Python Modules
