# COVID-19_PDF-Reporting

Adapted PDF Forms of the Swiss BAG to fully function for Input Case Data on the Computer.  
Acompanied ny Parsing Tools for automatic Bulk Form readout, resulting in CSV/XLSX Output to easily Import loads of Forms into Databases.

## The Forms

The PDF Forms of the Swiss BAG which are provided under [BAG COVID-19 Meldeformulare](https://www.bag.admin.ch/bag/de/home/krankheiten/infektionskrankheiten-bekaempfen/meldesysteme-infektionskrankheiten/meldepflichtige-ik/meldeformulare.html) are currently incomplete and have a lot artefacts due to automatic Generation from a Visio Document.

In the forms folder we provide corrected PDF Forms, which:

* have Form Fields for every necessary Input
* have a fixed Tabular Navigation, so that keyboard based filling is easy to be done
  * Tab Navigation is ordered by content groups
* have for every Formfield a unique and meaningful identifier, so that they can be considered easily machine readable
* have a usefull Field Grouping to reduce Data Cluttering on XML Output or Bulk Parsing
  * also enabling easy Selection Toggling of single valid Options
* have a Validation of Inputs
* have additional information to support easy submition of the digital forms by email
  * simply click the BAG Email Link and your favorit Email Client opens
* has all Hyperlinks clickable, for easy and fast access to external Resources

You can find the overhauled Forms in the forms Folder.  

## The Parser

The Parser for the Forms is python based and requires the PyPDF2 Module. A requirements.txt is provided for easy installation of the necessary Python Modules.

Current State is only a Proof of Concept. We are still working mainly on the Forms and Form Data Representation.

## Participation

If you have free time and want to help, we have need for Testing and Feedback on the functionality of the PDF Forms.
What you can Test:

* is the Navigation via tabs in the right order
* is the Text Formatting of the fields okay, and do these work if they would be printed out
  * does the Field Content behave correctly if more Data is typed in  
* currently all Forms are optimized to be used with Acrobat Reader, we are interested in Issues with other readers

Your help is much appreciated, please feel free to create Issues for any Problem or Change Request for improvements.

To test our Code we are in dire need of a bulk of filled forms, so if you Test the inputs, please save them and send them to us:

* <covid19_forms@wellenleiter.com>
