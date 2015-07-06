# ./_iso3166a2.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:8f43b5925a7b83449fab36a12e55aa96cbbe17e9
# Generated 2015-07-06 15:56:21.644583 by PyXB version 1.2.4 using Python 2.7.6.final.0
# Namespace http://ddex.net/xml/20121219/iso3166a2 [xmlns:iso3166a2]

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:74f1c0fe-23f7-11e5-bdf6-080027960975')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://ddex.net/xml/20121219/iso3166a2', create_if_missing=True)
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


# Atomic simple type: {http://ddex.net/xml/20121219/iso3166a2}TerritoryCode
class TerritoryCode (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An ISO 3166-1 two-letter code representing a ddex:Territory."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TerritoryCode')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20121219/iso3166a2.xsd', 9, 3)
    _Documentation = 'An ISO 3166-1 two-letter code representing a ddex:Territory.'
TerritoryCode._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TerritoryCode, enum_prefix=None)
TerritoryCode.AD = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='AD', tag='AD')
TerritoryCode.AE = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='AE', tag='AE')
TerritoryCode.AF = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='AF', tag='AF')
TerritoryCode.AG = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='AG', tag='AG')
TerritoryCode.AI = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='AI', tag='AI')
TerritoryCode.AL = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='AL', tag='AL')
TerritoryCode.AM = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='AM', tag='AM')
TerritoryCode.AN = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='AN', tag='AN')
TerritoryCode.AO = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='AO', tag='AO')
TerritoryCode.AQ = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='AQ', tag='AQ')
TerritoryCode.AR = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='AR', tag='AR')
TerritoryCode.AS = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='AS', tag='AS')
TerritoryCode.AT = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='AT', tag='AT')
TerritoryCode.AU = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='AU', tag='AU')
TerritoryCode.AW = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='AW', tag='AW')
TerritoryCode.AX = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='AX', tag='AX')
TerritoryCode.AZ = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='AZ', tag='AZ')
TerritoryCode.BA = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='BA', tag='BA')
TerritoryCode.BB = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='BB', tag='BB')
TerritoryCode.BD = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='BD', tag='BD')
TerritoryCode.BE = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='BE', tag='BE')
TerritoryCode.BF = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='BF', tag='BF')
TerritoryCode.BG = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='BG', tag='BG')
TerritoryCode.BH = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='BH', tag='BH')
TerritoryCode.BI = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='BI', tag='BI')
TerritoryCode.BJ = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='BJ', tag='BJ')
TerritoryCode.BL = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='BL', tag='BL')
TerritoryCode.BM = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='BM', tag='BM')
TerritoryCode.BN = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='BN', tag='BN')
TerritoryCode.BO = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='BO', tag='BO')
TerritoryCode.BQ = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='BQ', tag='BQ')
TerritoryCode.BR = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='BR', tag='BR')
TerritoryCode.BS = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='BS', tag='BS')
TerritoryCode.BT = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='BT', tag='BT')
TerritoryCode.BV = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='BV', tag='BV')
TerritoryCode.BW = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='BW', tag='BW')
TerritoryCode.BY = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='BY', tag='BY')
TerritoryCode.BZ = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='BZ', tag='BZ')
TerritoryCode.CA = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='CA', tag='CA')
TerritoryCode.CC = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='CC', tag='CC')
TerritoryCode.CD = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='CD', tag='CD')
TerritoryCode.CF = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='CF', tag='CF')
TerritoryCode.CG = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='CG', tag='CG')
TerritoryCode.CH = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='CH', tag='CH')
TerritoryCode.CI = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='CI', tag='CI')
TerritoryCode.CK = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='CK', tag='CK')
TerritoryCode.CL = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='CL', tag='CL')
TerritoryCode.CM = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='CM', tag='CM')
TerritoryCode.CN = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='CN', tag='CN')
TerritoryCode.CO = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='CO', tag='CO')
TerritoryCode.CR = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='CR', tag='CR')
TerritoryCode.CS = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='CS', tag='CS')
TerritoryCode.CU = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='CU', tag='CU')
TerritoryCode.CV = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='CV', tag='CV')
TerritoryCode.CW = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='CW', tag='CW')
TerritoryCode.CX = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='CX', tag='CX')
TerritoryCode.CY = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='CY', tag='CY')
TerritoryCode.CZ = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='CZ', tag='CZ')
TerritoryCode.DE = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='DE', tag='DE')
TerritoryCode.DJ = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='DJ', tag='DJ')
TerritoryCode.DK = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='DK', tag='DK')
TerritoryCode.DM = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='DM', tag='DM')
TerritoryCode.DO = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='DO', tag='DO')
TerritoryCode.DZ = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='DZ', tag='DZ')
TerritoryCode.EC = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='EC', tag='EC')
TerritoryCode.EE = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='EE', tag='EE')
TerritoryCode.EG = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='EG', tag='EG')
TerritoryCode.EH = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='EH', tag='EH')
TerritoryCode.ER = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='ER', tag='ER')
TerritoryCode.ES = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='ES', tag='ES')
TerritoryCode.ET = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='ET', tag='ET')
TerritoryCode.FI = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='FI', tag='FI')
TerritoryCode.FJ = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='FJ', tag='FJ')
TerritoryCode.FK = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='FK', tag='FK')
TerritoryCode.FM = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='FM', tag='FM')
TerritoryCode.FO = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='FO', tag='FO')
TerritoryCode.FR = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='FR', tag='FR')
TerritoryCode.GA = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='GA', tag='GA')
TerritoryCode.GB = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='GB', tag='GB')
TerritoryCode.GD = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='GD', tag='GD')
TerritoryCode.GE = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='GE', tag='GE')
TerritoryCode.GF = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='GF', tag='GF')
TerritoryCode.GG = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='GG', tag='GG')
TerritoryCode.GH = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='GH', tag='GH')
TerritoryCode.GI = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='GI', tag='GI')
TerritoryCode.GL = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='GL', tag='GL')
TerritoryCode.GM = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='GM', tag='GM')
TerritoryCode.GN = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='GN', tag='GN')
TerritoryCode.GP = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='GP', tag='GP')
TerritoryCode.GQ = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='GQ', tag='GQ')
TerritoryCode.GR = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='GR', tag='GR')
TerritoryCode.GS = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='GS', tag='GS')
TerritoryCode.GT = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='GT', tag='GT')
TerritoryCode.GU = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='GU', tag='GU')
TerritoryCode.GW = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='GW', tag='GW')
TerritoryCode.GY = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='GY', tag='GY')
TerritoryCode.HK = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='HK', tag='HK')
TerritoryCode.HM = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='HM', tag='HM')
TerritoryCode.HN = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='HN', tag='HN')
TerritoryCode.HR = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='HR', tag='HR')
TerritoryCode.HT = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='HT', tag='HT')
TerritoryCode.HU = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='HU', tag='HU')
TerritoryCode.ID = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='ID', tag='ID')
TerritoryCode.IE = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='IE', tag='IE')
TerritoryCode.IL = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='IL', tag='IL')
TerritoryCode.IM = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='IM', tag='IM')
TerritoryCode.IN = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='IN', tag='IN')
TerritoryCode.IO = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='IO', tag='IO')
TerritoryCode.IQ = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='IQ', tag='IQ')
TerritoryCode.IR = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='IR', tag='IR')
TerritoryCode.IS = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='IS', tag='IS')
TerritoryCode.IT = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='IT', tag='IT')
TerritoryCode.JE = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='JE', tag='JE')
TerritoryCode.JM = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='JM', tag='JM')
TerritoryCode.JO = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='JO', tag='JO')
TerritoryCode.JP = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='JP', tag='JP')
TerritoryCode.KE = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='KE', tag='KE')
TerritoryCode.KG = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='KG', tag='KG')
TerritoryCode.KH = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='KH', tag='KH')
TerritoryCode.KI = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='KI', tag='KI')
TerritoryCode.KM = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='KM', tag='KM')
TerritoryCode.KN = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='KN', tag='KN')
TerritoryCode.KP = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='KP', tag='KP')
TerritoryCode.KR = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='KR', tag='KR')
TerritoryCode.KW = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='KW', tag='KW')
TerritoryCode.KY = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='KY', tag='KY')
TerritoryCode.KZ = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='KZ', tag='KZ')
TerritoryCode.LA = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='LA', tag='LA')
TerritoryCode.LB = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='LB', tag='LB')
TerritoryCode.LC = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='LC', tag='LC')
TerritoryCode.LI = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='LI', tag='LI')
TerritoryCode.LK = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='LK', tag='LK')
TerritoryCode.LR = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='LR', tag='LR')
TerritoryCode.LS = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='LS', tag='LS')
TerritoryCode.LT = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='LT', tag='LT')
TerritoryCode.LU = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='LU', tag='LU')
TerritoryCode.LV = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='LV', tag='LV')
TerritoryCode.LY = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='LY', tag='LY')
TerritoryCode.MA = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='MA', tag='MA')
TerritoryCode.MC = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='MC', tag='MC')
TerritoryCode.MD = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='MD', tag='MD')
TerritoryCode.ME = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='ME', tag='ME')
TerritoryCode.MF = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='MF', tag='MF')
TerritoryCode.MG = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='MG', tag='MG')
TerritoryCode.MH = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='MH', tag='MH')
TerritoryCode.MK = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='MK', tag='MK')
TerritoryCode.ML = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='ML', tag='ML')
TerritoryCode.MM = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='MM', tag='MM')
TerritoryCode.MN = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='MN', tag='MN')
TerritoryCode.MO = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='MO', tag='MO')
TerritoryCode.MP = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='MP', tag='MP')
TerritoryCode.MQ = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='MQ', tag='MQ')
TerritoryCode.MR = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='MR', tag='MR')
TerritoryCode.MS = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='MS', tag='MS')
TerritoryCode.MT = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='MT', tag='MT')
TerritoryCode.MU = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='MU', tag='MU')
TerritoryCode.MV = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='MV', tag='MV')
TerritoryCode.MW = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='MW', tag='MW')
TerritoryCode.MX = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='MX', tag='MX')
TerritoryCode.MY = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='MY', tag='MY')
TerritoryCode.MZ = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='MZ', tag='MZ')
TerritoryCode.NA = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='NA', tag='NA')
TerritoryCode.NC = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='NC', tag='NC')
TerritoryCode.NE = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='NE', tag='NE')
TerritoryCode.NF = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='NF', tag='NF')
TerritoryCode.NG = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='NG', tag='NG')
TerritoryCode.NI = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='NI', tag='NI')
TerritoryCode.NL = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='NL', tag='NL')
TerritoryCode.NO = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='NO', tag='NO')
TerritoryCode.NP = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='NP', tag='NP')
TerritoryCode.NR = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='NR', tag='NR')
TerritoryCode.NU = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='NU', tag='NU')
TerritoryCode.NZ = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='NZ', tag='NZ')
TerritoryCode.OM = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='OM', tag='OM')
TerritoryCode.PA = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='PA', tag='PA')
TerritoryCode.PE = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='PE', tag='PE')
TerritoryCode.PF = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='PF', tag='PF')
TerritoryCode.PG = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='PG', tag='PG')
TerritoryCode.PH = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='PH', tag='PH')
TerritoryCode.PK = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='PK', tag='PK')
TerritoryCode.PL = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='PL', tag='PL')
TerritoryCode.PM = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='PM', tag='PM')
TerritoryCode.PN = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='PN', tag='PN')
TerritoryCode.PR = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='PR', tag='PR')
TerritoryCode.PS = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='PS', tag='PS')
TerritoryCode.PT = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='PT', tag='PT')
TerritoryCode.PW = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='PW', tag='PW')
TerritoryCode.PY = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='PY', tag='PY')
TerritoryCode.QA = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='QA', tag='QA')
TerritoryCode.RE = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='RE', tag='RE')
TerritoryCode.RO = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='RO', tag='RO')
TerritoryCode.RS = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='RS', tag='RS')
TerritoryCode.RU = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='RU', tag='RU')
TerritoryCode.RW = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='RW', tag='RW')
TerritoryCode.SA = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='SA', tag='SA')
TerritoryCode.SB = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='SB', tag='SB')
TerritoryCode.SC = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='SC', tag='SC')
TerritoryCode.SD = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='SD', tag='SD')
TerritoryCode.SE = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='SE', tag='SE')
TerritoryCode.SG = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='SG', tag='SG')
TerritoryCode.SH = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='SH', tag='SH')
TerritoryCode.SI = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='SI', tag='SI')
TerritoryCode.SJ = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='SJ', tag='SJ')
TerritoryCode.SK = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='SK', tag='SK')
TerritoryCode.SL = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='SL', tag='SL')
TerritoryCode.SM = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='SM', tag='SM')
TerritoryCode.SN = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='SN', tag='SN')
TerritoryCode.SO = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='SO', tag='SO')
TerritoryCode.SR = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='SR', tag='SR')
TerritoryCode.SS = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='SS', tag='SS')
TerritoryCode.ST = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='ST', tag='ST')
TerritoryCode.SV = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='SV', tag='SV')
TerritoryCode.SX = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='SX', tag='SX')
TerritoryCode.SY = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='SY', tag='SY')
TerritoryCode.SZ = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='SZ', tag='SZ')
TerritoryCode.TC = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='TC', tag='TC')
TerritoryCode.TD = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='TD', tag='TD')
TerritoryCode.TF = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='TF', tag='TF')
TerritoryCode.TG = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='TG', tag='TG')
TerritoryCode.TH = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='TH', tag='TH')
TerritoryCode.TJ = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='TJ', tag='TJ')
TerritoryCode.TK = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='TK', tag='TK')
TerritoryCode.TL = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='TL', tag='TL')
TerritoryCode.TM = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='TM', tag='TM')
TerritoryCode.TN = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='TN', tag='TN')
TerritoryCode.TO = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='TO', tag='TO')
TerritoryCode.TR = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='TR', tag='TR')
TerritoryCode.TT = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='TT', tag='TT')
TerritoryCode.TV = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='TV', tag='TV')
TerritoryCode.TW = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='TW', tag='TW')
TerritoryCode.TZ = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='TZ', tag='TZ')
TerritoryCode.UA = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='UA', tag='UA')
TerritoryCode.UG = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='UG', tag='UG')
TerritoryCode.UM = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='UM', tag='UM')
TerritoryCode.US = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='US', tag='US')
TerritoryCode.UY = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='UY', tag='UY')
TerritoryCode.UZ = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='UZ', tag='UZ')
TerritoryCode.VA = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='VA', tag='VA')
TerritoryCode.VC = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='VC', tag='VC')
TerritoryCode.VE = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='VE', tag='VE')
TerritoryCode.VG = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='VG', tag='VG')
TerritoryCode.VI = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='VI', tag='VI')
TerritoryCode.VN = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='VN', tag='VN')
TerritoryCode.VU = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='VU', tag='VU')
TerritoryCode.WF = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='WF', tag='WF')
TerritoryCode.WS = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='WS', tag='WS')
TerritoryCode.YE = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='YE', tag='YE')
TerritoryCode.YT = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='YT', tag='YT')
TerritoryCode.ZA = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='ZA', tag='ZA')
TerritoryCode.ZM = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='ZM', tag='ZM')
TerritoryCode.ZW = TerritoryCode._CF_enumeration.addEnumeration(unicode_value='ZW', tag='ZW')
TerritoryCode._InitializeFacetMap(TerritoryCode._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TerritoryCode', TerritoryCode)
