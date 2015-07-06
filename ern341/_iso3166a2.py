# ./_iso3166a2.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:94b35e5fa167f1cbc52c4ef67dd51e6e4ae4e5fc
# Generated 2015-07-06 09:45:08.298167 by PyXB version 1.2.4 using Python 2.7.6.final.0
# Namespace http://ddex.net/xml/20120404/iso3166a2 [xmlns:iso3166a2]

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:a29ac908-23c3-11e5-b0e6-080027960975')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://ddex.net/xml/20120404/iso3166a2', create_if_missing=True)
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


# Atomic simple type: {http://ddex.net/xml/20120404/iso3166a2}TerritoryCode
class TerritoryCode (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An ISO 3166-1 two-letter code representing a ddex:Territory."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TerritoryCode')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20120404/iso3166a2.xsd', 10, 3)
    _Documentation = 'An ISO 3166-1 two-letter code representing a ddex:Territory.'
TerritoryCode._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TerritoryCode, enum_prefix=None)
TerritoryCode.AF = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='AF', tag='AF')
TerritoryCode.AX = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='AX', tag='AX')
TerritoryCode.AL = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='AL', tag='AL')
TerritoryCode.DZ = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='DZ', tag='DZ')
TerritoryCode.AD = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='AD', tag='AD')
TerritoryCode.AO = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='AO', tag='AO')
TerritoryCode.AG = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='AG', tag='AG')
TerritoryCode.AR = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='AR', tag='AR')
TerritoryCode.AM = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='AM', tag='AM')
TerritoryCode.AU = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='AU', tag='AU')
TerritoryCode.AT = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='AT', tag='AT')
TerritoryCode.AZ = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='AZ', tag='AZ')
TerritoryCode.BS = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='BS', tag='BS')
TerritoryCode.BH = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='BH', tag='BH')
TerritoryCode.BD = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='BD', tag='BD')
TerritoryCode.BB = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='BB', tag='BB')
TerritoryCode.BY = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='BY', tag='BY')
TerritoryCode.BE = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='BE', tag='BE')
TerritoryCode.BZ = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='BZ', tag='BZ')
TerritoryCode.BJ = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='BJ', tag='BJ')
TerritoryCode.BT = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='BT', tag='BT')
TerritoryCode.BO = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='BO', tag='BO')
TerritoryCode.BA = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='BA', tag='BA')
TerritoryCode.BW = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='BW', tag='BW')
TerritoryCode.BR = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='BR', tag='BR')
TerritoryCode.BN = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='BN', tag='BN')
TerritoryCode.BG = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='BG', tag='BG')
TerritoryCode.BF = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='BF', tag='BF')
TerritoryCode.BI = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='BI', tag='BI')
TerritoryCode.KH = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='KH', tag='KH')
TerritoryCode.CM = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='CM', tag='CM')
TerritoryCode.CA = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='CA', tag='CA')
TerritoryCode.CV = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='CV', tag='CV')
TerritoryCode.CF = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='CF', tag='CF')
TerritoryCode.TD = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='TD', tag='TD')
TerritoryCode.CL = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='CL', tag='CL')
TerritoryCode.CN = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='CN', tag='CN')
TerritoryCode.CO = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='CO', tag='CO')
TerritoryCode.KM = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='KM', tag='KM')
TerritoryCode.CG = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='CG', tag='CG')
TerritoryCode.CD = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='CD', tag='CD')
TerritoryCode.CR = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='CR', tag='CR')
TerritoryCode.CI = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='CI', tag='CI')
TerritoryCode.HR = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='HR', tag='HR')
TerritoryCode.CU = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='CU', tag='CU')
TerritoryCode.CY = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='CY', tag='CY')
TerritoryCode.CZ = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='CZ', tag='CZ')
TerritoryCode.DK = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='DK', tag='DK')
TerritoryCode.DJ = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='DJ', tag='DJ')
TerritoryCode.DM = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='DM', tag='DM')
TerritoryCode.DO = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='DO', tag='DO')
TerritoryCode.TL = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='TL', tag='TL')
TerritoryCode.EC = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='EC', tag='EC')
TerritoryCode.EG = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='EG', tag='EG')
TerritoryCode.SV = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='SV', tag='SV')
TerritoryCode.GQ = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='GQ', tag='GQ')
TerritoryCode.ER = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='ER', tag='ER')
TerritoryCode.EE = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='EE', tag='EE')
TerritoryCode.ET = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='ET', tag='ET')
TerritoryCode.FJ = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='FJ', tag='FJ')
TerritoryCode.FI = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='FI', tag='FI')
TerritoryCode.FR = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='FR', tag='FR')
TerritoryCode.GA = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='GA', tag='GA')
TerritoryCode.GM = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='GM', tag='GM')
TerritoryCode.GE = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='GE', tag='GE')
TerritoryCode.DE = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='DE', tag='DE')
TerritoryCode.GH = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='GH', tag='GH')
TerritoryCode.GR = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='GR', tag='GR')
TerritoryCode.GD = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='GD', tag='GD')
TerritoryCode.GT = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='GT', tag='GT')
TerritoryCode.GG = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='GG', tag='GG')
TerritoryCode.GN = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='GN', tag='GN')
TerritoryCode.GW = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='GW', tag='GW')
TerritoryCode.GY = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='GY', tag='GY')
TerritoryCode.HT = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='HT', tag='HT')
TerritoryCode.VA = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='VA', tag='VA')
TerritoryCode.HN = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='HN', tag='HN')
TerritoryCode.HU = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='HU', tag='HU')
TerritoryCode.IS = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='IS', tag='IS')
TerritoryCode.IN = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='IN', tag='IN')
TerritoryCode.ID = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='ID', tag='ID')
TerritoryCode.IR = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='IR', tag='IR')
TerritoryCode.IQ = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='IQ', tag='IQ')
TerritoryCode.IE = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='IE', tag='IE')
TerritoryCode.IM = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='IM', tag='IM')
TerritoryCode.IL = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='IL', tag='IL')
TerritoryCode.IT = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='IT', tag='IT')
TerritoryCode.JM = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='JM', tag='JM')
TerritoryCode.JP = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='JP', tag='JP')
TerritoryCode.JE = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='JE', tag='JE')
TerritoryCode.JO = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='JO', tag='JO')
TerritoryCode.KZ = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='KZ', tag='KZ')
TerritoryCode.KE = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='KE', tag='KE')
TerritoryCode.KI = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='KI', tag='KI')
TerritoryCode.KP = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='KP', tag='KP')
TerritoryCode.KR = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='KR', tag='KR')
TerritoryCode.KW = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='KW', tag='KW')
TerritoryCode.KG = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='KG', tag='KG')
TerritoryCode.LA = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='LA', tag='LA')
TerritoryCode.LV = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='LV', tag='LV')
TerritoryCode.LB = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='LB', tag='LB')
TerritoryCode.LS = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='LS', tag='LS')
TerritoryCode.LR = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='LR', tag='LR')
TerritoryCode.LY = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='LY', tag='LY')
TerritoryCode.LI = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='LI', tag='LI')
TerritoryCode.LT = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='LT', tag='LT')
TerritoryCode.LU = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='LU', tag='LU')
TerritoryCode.MG = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='MG', tag='MG')
TerritoryCode.MW = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='MW', tag='MW')
TerritoryCode.MY = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='MY', tag='MY')
TerritoryCode.MV = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='MV', tag='MV')
TerritoryCode.ML = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='ML', tag='ML')
TerritoryCode.MT = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='MT', tag='MT')
TerritoryCode.MH = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='MH', tag='MH')
TerritoryCode.MR = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='MR', tag='MR')
TerritoryCode.MU = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='MU', tag='MU')
TerritoryCode.MX = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='MX', tag='MX')
TerritoryCode.FM = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='FM', tag='FM')
TerritoryCode.MD = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='MD', tag='MD')
TerritoryCode.MC = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='MC', tag='MC')
TerritoryCode.MN = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='MN', tag='MN')
TerritoryCode.ME = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='ME', tag='ME')
TerritoryCode.MA = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='MA', tag='MA')
TerritoryCode.MZ = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='MZ', tag='MZ')
TerritoryCode.MM = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='MM', tag='MM')
TerritoryCode.NA = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='NA', tag='NA')
TerritoryCode.NR = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='NR', tag='NR')
TerritoryCode.NP = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='NP', tag='NP')
TerritoryCode.NL = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='NL', tag='NL')
TerritoryCode.NZ = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='NZ', tag='NZ')
TerritoryCode.NI = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='NI', tag='NI')
TerritoryCode.NE = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='NE', tag='NE')
TerritoryCode.NG = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='NG', tag='NG')
TerritoryCode.NO = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='NO', tag='NO')
TerritoryCode.OM = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='OM', tag='OM')
TerritoryCode.PK = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='PK', tag='PK')
TerritoryCode.PW = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='PW', tag='PW')
TerritoryCode.PA = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='PA', tag='PA')
TerritoryCode.PG = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='PG', tag='PG')
TerritoryCode.PY = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='PY', tag='PY')
TerritoryCode.PE = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='PE', tag='PE')
TerritoryCode.PH = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='PH', tag='PH')
TerritoryCode.PL = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='PL', tag='PL')
TerritoryCode.PT = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='PT', tag='PT')
TerritoryCode.QA = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='QA', tag='QA')
TerritoryCode.RO = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='RO', tag='RO')
TerritoryCode.RU = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='RU', tag='RU')
TerritoryCode.RW = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='RW', tag='RW')
TerritoryCode.KN = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='KN', tag='KN')
TerritoryCode.LC = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='LC', tag='LC')
TerritoryCode.VC = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='VC', tag='VC')
TerritoryCode.WS = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='WS', tag='WS')
TerritoryCode.SM = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='SM', tag='SM')
TerritoryCode.ST = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='ST', tag='ST')
TerritoryCode.SA = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='SA', tag='SA')
TerritoryCode.SN = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='SN', tag='SN')
TerritoryCode.RS = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='RS', tag='RS')
TerritoryCode.SC = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='SC', tag='SC')
TerritoryCode.SL = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='SL', tag='SL')
TerritoryCode.SG = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='SG', tag='SG')
TerritoryCode.SK = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='SK', tag='SK')
TerritoryCode.SI = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='SI', tag='SI')
TerritoryCode.SB = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='SB', tag='SB')
TerritoryCode.SO = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='SO', tag='SO')
TerritoryCode.ZA = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='ZA', tag='ZA')
TerritoryCode.ES = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='ES', tag='ES')
TerritoryCode.LK = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='LK', tag='LK')
TerritoryCode.SD = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='SD', tag='SD')
TerritoryCode.SR = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='SR', tag='SR')
TerritoryCode.SZ = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='SZ', tag='SZ')
TerritoryCode.SE = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='SE', tag='SE')
TerritoryCode.CH = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='CH', tag='CH')
TerritoryCode.SY = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='SY', tag='SY')
TerritoryCode.TJ = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='TJ', tag='TJ')
TerritoryCode.TZ = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='TZ', tag='TZ')
TerritoryCode.TH = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='TH', tag='TH')
TerritoryCode.MK = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='MK', tag='MK')
TerritoryCode.TG = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='TG', tag='TG')
TerritoryCode.TO = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='TO', tag='TO')
TerritoryCode.TT = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='TT', tag='TT')
TerritoryCode.TN = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='TN', tag='TN')
TerritoryCode.TR = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='TR', tag='TR')
TerritoryCode.TM = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='TM', tag='TM')
TerritoryCode.TV = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='TV', tag='TV')
TerritoryCode.UG = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='UG', tag='UG')
TerritoryCode.UA = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='UA', tag='UA')
TerritoryCode.AE = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='AE', tag='AE')
TerritoryCode.GB = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='GB', tag='GB')
TerritoryCode.US = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='US', tag='US')
TerritoryCode.UY = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='UY', tag='UY')
TerritoryCode.UZ = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='UZ', tag='UZ')
TerritoryCode.VU = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='VU', tag='VU')
TerritoryCode.VE = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='VE', tag='VE')
TerritoryCode.VN = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='VN', tag='VN')
TerritoryCode.YE = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='YE', tag='YE')
TerritoryCode.ZM = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='ZM', tag='ZM')
TerritoryCode.ZW = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='ZW', tag='ZW')
TerritoryCode.AS = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='AS', tag='AS')
TerritoryCode.AI = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='AI', tag='AI')
TerritoryCode.AQ = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='AQ', tag='AQ')
TerritoryCode.AW = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='AW', tag='AW')
TerritoryCode.BM = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='BM', tag='BM')
TerritoryCode.BV = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='BV', tag='BV')
TerritoryCode.IO = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='IO', tag='IO')
TerritoryCode.KY = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='KY', tag='KY')
TerritoryCode.CX = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='CX', tag='CX')
TerritoryCode.CC = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='CC', tag='CC')
TerritoryCode.CK = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='CK', tag='CK')
TerritoryCode.FK = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='FK', tag='FK')
TerritoryCode.FO = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='FO', tag='FO')
TerritoryCode.GF = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='GF', tag='GF')
TerritoryCode.PF = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='PF', tag='PF')
TerritoryCode.TF = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='TF', tag='TF')
TerritoryCode.GI = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='GI', tag='GI')
TerritoryCode.GL = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='GL', tag='GL')
TerritoryCode.GP = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='GP', tag='GP')
TerritoryCode.GU = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='GU', tag='GU')
TerritoryCode.HM = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='HM', tag='HM')
TerritoryCode.HK = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='HK', tag='HK')
TerritoryCode.MO = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='MO', tag='MO')
TerritoryCode.MQ = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='MQ', tag='MQ')
TerritoryCode.YT = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='YT', tag='YT')
TerritoryCode.MS = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='MS', tag='MS')
TerritoryCode.AN = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='AN', tag='AN')
TerritoryCode.NC = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='NC', tag='NC')
TerritoryCode.NU = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='NU', tag='NU')
TerritoryCode.NF = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='NF', tag='NF')
TerritoryCode.MP = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='MP', tag='MP')
TerritoryCode.PS = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='PS', tag='PS')
TerritoryCode.PN = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='PN', tag='PN')
TerritoryCode.PR = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='PR', tag='PR')
TerritoryCode.RE = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='RE', tag='RE')
TerritoryCode.BL = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='BL', tag='BL')
TerritoryCode.SH = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='SH', tag='SH')
TerritoryCode.MF = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='MF', tag='MF')
TerritoryCode.PM = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='PM', tag='PM')
TerritoryCode.GS = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='GS', tag='GS')
TerritoryCode.SJ = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='SJ', tag='SJ')
TerritoryCode.TW = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='TW', tag='TW')
TerritoryCode.TK = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='TK', tag='TK')
TerritoryCode.TC = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='TC', tag='TC')
TerritoryCode.UM = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='UM', tag='UM')
TerritoryCode.VG = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='VG', tag='VG')
TerritoryCode.VI = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='VI', tag='VI')
TerritoryCode.WF = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='WF', tag='WF')
TerritoryCode.EH = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='EH', tag='EH')
TerritoryCode._InitializeFacetMap(TerritoryCode._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TerritoryCode', TerritoryCode)
