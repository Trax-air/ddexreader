# ./_iso4217a.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:aec0c517a0206685fc23268343ee13279d01e464
# Generated 2015-07-06 15:09:50.906340 by PyXB version 1.2.4 using Python 2.7.6.final.0
# Namespace http://ddex.net/xml/20100712/iso4217a [xmlns:iso4217a]

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:f7997896-23f0-11e5-bc58-080027960975')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://ddex.net/xml/20100712/iso4217a', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: {http://ddex.net/xml/20100712/iso4217a}CurrencyCode
class CurrencyCode (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An ISO4217 three-letter code representing a Currency."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CurrencyCode')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100712/iso4217a.xsd', 3, 4)
    _Documentation = 'An ISO4217 three-letter code representing a Currency.'
CurrencyCode._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CurrencyCode, enum_prefix=None)
CurrencyCode.ADP = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='ADP', tag='ADP')
CurrencyCode.AED = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='AED', tag='AED')
CurrencyCode.AFA = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='AFA', tag='AFA')
CurrencyCode.ALL = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='ALL', tag='ALL')
CurrencyCode.AMD = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='AMD', tag='AMD')
CurrencyCode.ANG = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='ANG', tag='ANG')
CurrencyCode.AOA = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='AOA', tag='AOA')
CurrencyCode.ARS = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='ARS', tag='ARS')
CurrencyCode.ATS = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='ATS', tag='ATS')
CurrencyCode.AUD = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='AUD', tag='AUD')
CurrencyCode.AWG = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='AWG', tag='AWG')
CurrencyCode.AZM = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='AZM', tag='AZM')
CurrencyCode.BAM = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='BAM', tag='BAM')
CurrencyCode.BBD = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='BBD', tag='BBD')
CurrencyCode.BDT = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='BDT', tag='BDT')
CurrencyCode.BEF = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='BEF', tag='BEF')
CurrencyCode.BGN = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='BGN', tag='BGN')
CurrencyCode.BHD = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='BHD', tag='BHD')
CurrencyCode.BIF = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='BIF', tag='BIF')
CurrencyCode.BMD = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='BMD', tag='BMD')
CurrencyCode.BND = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='BND', tag='BND')
CurrencyCode.BOB = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='BOB', tag='BOB')
CurrencyCode.BOV = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='BOV', tag='BOV')
CurrencyCode.BRL = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='BRL', tag='BRL')
CurrencyCode.BSD = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='BSD', tag='BSD')
CurrencyCode.BTN = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='BTN', tag='BTN')
CurrencyCode.BWP = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='BWP', tag='BWP')
CurrencyCode.BYR = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='BYR', tag='BYR')
CurrencyCode.BZD = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='BZD', tag='BZD')
CurrencyCode.CAD = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='CAD', tag='CAD')
CurrencyCode.CDF = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='CDF', tag='CDF')
CurrencyCode.CHF = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='CHF', tag='CHF')
CurrencyCode.CLP = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='CLP', tag='CLP')
CurrencyCode.CNY = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='CNY', tag='CNY')
CurrencyCode.COP = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='COP', tag='COP')
CurrencyCode.CRC = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='CRC', tag='CRC')
CurrencyCode.CUP = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='CUP', tag='CUP')
CurrencyCode.CVE = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='CVE', tag='CVE')
CurrencyCode.CYP = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='CYP', tag='CYP')
CurrencyCode.CZK = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='CZK', tag='CZK')
CurrencyCode.DEM = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='DEM', tag='DEM')
CurrencyCode.DJF = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='DJF', tag='DJF')
CurrencyCode.DKK = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='DKK', tag='DKK')
CurrencyCode.DOP = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='DOP', tag='DOP')
CurrencyCode.DZD = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='DZD', tag='DZD')
CurrencyCode.EEK = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='EEK', tag='EEK')
CurrencyCode.EGP = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='EGP', tag='EGP')
CurrencyCode.ERN = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='ERN', tag='ERN')
CurrencyCode.ESP = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='ESP', tag='ESP')
CurrencyCode.ETB = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='ETB', tag='ETB')
CurrencyCode.EUR = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='EUR', tag='EUR')
CurrencyCode.FIM = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='FIM', tag='FIM')
CurrencyCode.FJD = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='FJD', tag='FJD')
CurrencyCode.FKP = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='FKP', tag='FKP')
CurrencyCode.FRF = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='FRF', tag='FRF')
CurrencyCode.GBP = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='GBP', tag='GBP')
CurrencyCode.GEL = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='GEL', tag='GEL')
CurrencyCode.GHC = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='GHC', tag='GHC')
CurrencyCode.GIP = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='GIP', tag='GIP')
CurrencyCode.GMD = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='GMD', tag='GMD')
CurrencyCode.GNF = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='GNF', tag='GNF')
CurrencyCode.GRD = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='GRD', tag='GRD')
CurrencyCode.GTQ = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='GTQ', tag='GTQ')
CurrencyCode.GWP = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='GWP', tag='GWP')
CurrencyCode.GYD = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='GYD', tag='GYD')
CurrencyCode.HKD = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='HKD', tag='HKD')
CurrencyCode.HNL = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='HNL', tag='HNL')
CurrencyCode.HRK = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='HRK', tag='HRK')
CurrencyCode.HTG = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='HTG', tag='HTG')
CurrencyCode.HUF = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='HUF', tag='HUF')
CurrencyCode.IDR = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='IDR', tag='IDR')
CurrencyCode.IEP = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='IEP', tag='IEP')
CurrencyCode.ILS = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='ILS', tag='ILS')
CurrencyCode.INR = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='INR', tag='INR')
CurrencyCode.IQD = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='IQD', tag='IQD')
CurrencyCode.IRR = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='IRR', tag='IRR')
CurrencyCode.ISK = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='ISK', tag='ISK')
CurrencyCode.ITL = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='ITL', tag='ITL')
CurrencyCode.JMD = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='JMD', tag='JMD')
CurrencyCode.JOD = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='JOD', tag='JOD')
CurrencyCode.JPY = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='JPY', tag='JPY')
CurrencyCode.KES = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='KES', tag='KES')
CurrencyCode.KGS = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='KGS', tag='KGS')
CurrencyCode.KHR = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='KHR', tag='KHR')
CurrencyCode.KMF = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='KMF', tag='KMF')
CurrencyCode.KPW = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='KPW', tag='KPW')
CurrencyCode.KRW = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='KRW', tag='KRW')
CurrencyCode.KWD = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='KWD', tag='KWD')
CurrencyCode.KYD = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='KYD', tag='KYD')
CurrencyCode.KZT = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='KZT', tag='KZT')
CurrencyCode.LAK = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='LAK', tag='LAK')
CurrencyCode.LBP = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='LBP', tag='LBP')
CurrencyCode.LKR = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='LKR', tag='LKR')
CurrencyCode.LRD = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='LRD', tag='LRD')
CurrencyCode.LSL = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='LSL', tag='LSL')
CurrencyCode.LTL = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='LTL', tag='LTL')
CurrencyCode.LUF = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='LUF', tag='LUF')
CurrencyCode.LVL = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='LVL', tag='LVL')
CurrencyCode.LYD = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='LYD', tag='LYD')
CurrencyCode.MAD = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='MAD', tag='MAD')
CurrencyCode.MDL = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='MDL', tag='MDL')
CurrencyCode.MGF = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='MGF', tag='MGF')
CurrencyCode.MKD = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='MKD', tag='MKD')
CurrencyCode.MMK = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='MMK', tag='MMK')
CurrencyCode.MNT = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='MNT', tag='MNT')
CurrencyCode.MOP = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='MOP', tag='MOP')
CurrencyCode.MRO = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='MRO', tag='MRO')
CurrencyCode.MTL = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='MTL', tag='MTL')
CurrencyCode.MUR = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='MUR', tag='MUR')
CurrencyCode.MVR = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='MVR', tag='MVR')
CurrencyCode.MWK = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='MWK', tag='MWK')
CurrencyCode.MXN = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='MXN', tag='MXN')
CurrencyCode.MYR = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='MYR', tag='MYR')
CurrencyCode.MZM = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='MZM', tag='MZM')
CurrencyCode.NAD = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='NAD', tag='NAD')
CurrencyCode.NGN = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='NGN', tag='NGN')
CurrencyCode.NIO = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='NIO', tag='NIO')
CurrencyCode.NLG = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='NLG', tag='NLG')
CurrencyCode.NOK = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='NOK', tag='NOK')
CurrencyCode.NPR = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='NPR', tag='NPR')
CurrencyCode.NZD = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='NZD', tag='NZD')
CurrencyCode.OMR = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='OMR', tag='OMR')
CurrencyCode.PAB = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='PAB', tag='PAB')
CurrencyCode.PEN = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='PEN', tag='PEN')
CurrencyCode.PGK = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='PGK', tag='PGK')
CurrencyCode.PHP = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='PHP', tag='PHP')
CurrencyCode.PKR = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='PKR', tag='PKR')
CurrencyCode.PLN = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='PLN', tag='PLN')
CurrencyCode.PTE = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='PTE', tag='PTE')
CurrencyCode.PYG = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='PYG', tag='PYG')
CurrencyCode.QAR = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='QAR', tag='QAR')
CurrencyCode.ROL = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='ROL', tag='ROL')
CurrencyCode.RUB = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='RUB', tag='RUB')
CurrencyCode.RWF = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='RWF', tag='RWF')
CurrencyCode.SAR = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='SAR', tag='SAR')
CurrencyCode.SBD = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='SBD', tag='SBD')
CurrencyCode.SCR = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='SCR', tag='SCR')
CurrencyCode.SDD = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='SDD', tag='SDD')
CurrencyCode.SEK = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='SEK', tag='SEK')
CurrencyCode.SGD = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='SGD', tag='SGD')
CurrencyCode.SHP = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='SHP', tag='SHP')
CurrencyCode.SIT = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='SIT', tag='SIT')
CurrencyCode.SKK = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='SKK', tag='SKK')
CurrencyCode.SLL = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='SLL', tag='SLL')
CurrencyCode.SOS = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='SOS', tag='SOS')
CurrencyCode.SRD = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='SRD', tag='SRD')
CurrencyCode.STD = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='STD', tag='STD')
CurrencyCode.SVC = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='SVC', tag='SVC')
CurrencyCode.SYP = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='SYP', tag='SYP')
CurrencyCode.SZL = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='SZL', tag='SZL')
CurrencyCode.THB = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='THB', tag='THB')
CurrencyCode.TJS = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='TJS', tag='TJS')
CurrencyCode.TMM = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='TMM', tag='TMM')
CurrencyCode.TND = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='TND', tag='TND')
CurrencyCode.TOP = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='TOP', tag='TOP')
CurrencyCode.TPE = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='TPE', tag='TPE')
CurrencyCode.TRL = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='TRL', tag='TRL')
CurrencyCode.TTD = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='TTD', tag='TTD')
CurrencyCode.TWD = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='TWD', tag='TWD')
CurrencyCode.TZS = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='TZS', tag='TZS')
CurrencyCode.UAH = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='UAH', tag='UAH')
CurrencyCode.UGX = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='UGX', tag='UGX')
CurrencyCode.USD = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='USD', tag='USD')
CurrencyCode.UYU = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='UYU', tag='UYU')
CurrencyCode.UZS = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='UZS', tag='UZS')
CurrencyCode.VEB = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='VEB', tag='VEB')
CurrencyCode.VND = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='VND', tag='VND')
CurrencyCode.VUV = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='VUV', tag='VUV')
CurrencyCode.WST = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='WST', tag='WST')
CurrencyCode.XAF = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='XAF', tag='XAF')
CurrencyCode.XCD = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='XCD', tag='XCD')
CurrencyCode.XOF = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='XOF', tag='XOF')
CurrencyCode.XPF = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='XPF', tag='XPF')
CurrencyCode.YER = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='YER', tag='YER')
CurrencyCode.YUM = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='YUM', tag='YUM')
CurrencyCode.ZAR = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='ZAR', tag='ZAR')
CurrencyCode.ZMK = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='ZMK', tag='ZMK')
CurrencyCode.ZWD = CurrencyCode._CF_enumeration.addEnumeration(unicode_value='ZWD', tag='ZWD')
CurrencyCode._InitializeFacetMap(CurrencyCode._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CurrencyCode', CurrencyCode)
