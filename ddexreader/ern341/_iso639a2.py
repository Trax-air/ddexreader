# ./_iso639a2.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:97aceb0400e81c93c87e874f323d78167ad65fdc
# Generated 2015-07-06 09:45:08.294553 by PyXB version 1.2.4 using Python 2.7.6.final.0
# Namespace http://ddex.net/xml/20120404/iso639a2 [xmlns:iso639a2]

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
Namespace = pyxb.namespace.NamespaceForURI('http://ddex.net/xml/20120404/iso639a2', create_if_missing=True)
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


# Atomic simple type: {http://ddex.net/xml/20120404/iso639a2}LanguageCode
class LanguageCode (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An ISO639-1 two-letter code representing a ddex:Language."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LanguageCode')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20120404/iso639a2.xsd', 10, 3)
    _Documentation = 'An ISO639-1 two-letter code representing a ddex:Language.'
LanguageCode._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=LanguageCode, enum_prefix=None)
LanguageCode.aa = LanguageCode._CF_enumeration.addEnumeration(unicode_value='aa', tag='aa')
LanguageCode.ab = LanguageCode._CF_enumeration.addEnumeration(unicode_value='ab', tag='ab')
LanguageCode.af = LanguageCode._CF_enumeration.addEnumeration(unicode_value='af', tag='af')
LanguageCode.ak = LanguageCode._CF_enumeration.addEnumeration(unicode_value='ak', tag='ak')
LanguageCode.sq = LanguageCode._CF_enumeration.addEnumeration(unicode_value='sq', tag='sq')
LanguageCode.am = LanguageCode._CF_enumeration.addEnumeration(unicode_value='am', tag='am')
LanguageCode.ar = LanguageCode._CF_enumeration.addEnumeration(unicode_value='ar', tag='ar')
LanguageCode.an = LanguageCode._CF_enumeration.addEnumeration(unicode_value='an', tag='an')
LanguageCode.hy = LanguageCode._CF_enumeration.addEnumeration(unicode_value='hy', tag='hy')
LanguageCode.as_ = LanguageCode._CF_enumeration.addEnumeration(unicode_value='as', tag='as_')
LanguageCode.av = LanguageCode._CF_enumeration.addEnumeration(unicode_value='av', tag='av')
LanguageCode.ae = LanguageCode._CF_enumeration.addEnumeration(unicode_value='ae', tag='ae')
LanguageCode.ay = LanguageCode._CF_enumeration.addEnumeration(unicode_value='ay', tag='ay')
LanguageCode.az = LanguageCode._CF_enumeration.addEnumeration(unicode_value='az', tag='az')
LanguageCode.ba = LanguageCode._CF_enumeration.addEnumeration(unicode_value='ba', tag='ba')
LanguageCode.bm = LanguageCode._CF_enumeration.addEnumeration(unicode_value='bm', tag='bm')
LanguageCode.eu = LanguageCode._CF_enumeration.addEnumeration(unicode_value='eu', tag='eu')
LanguageCode.be = LanguageCode._CF_enumeration.addEnumeration(unicode_value='be', tag='be')
LanguageCode.bn = LanguageCode._CF_enumeration.addEnumeration(unicode_value='bn', tag='bn')
LanguageCode.bh = LanguageCode._CF_enumeration.addEnumeration(unicode_value='bh', tag='bh')
LanguageCode.bi = LanguageCode._CF_enumeration.addEnumeration(unicode_value='bi', tag='bi')
LanguageCode.bo = LanguageCode._CF_enumeration.addEnumeration(unicode_value='bo', tag='bo')
LanguageCode.bs = LanguageCode._CF_enumeration.addEnumeration(unicode_value='bs', tag='bs')
LanguageCode.br = LanguageCode._CF_enumeration.addEnumeration(unicode_value='br', tag='br')
LanguageCode.bg = LanguageCode._CF_enumeration.addEnumeration(unicode_value='bg', tag='bg')
LanguageCode.my = LanguageCode._CF_enumeration.addEnumeration(unicode_value='my', tag='my')
LanguageCode.ca = LanguageCode._CF_enumeration.addEnumeration(unicode_value='ca', tag='ca')
LanguageCode.cs = LanguageCode._CF_enumeration.addEnumeration(unicode_value='cs', tag='cs')
LanguageCode.ch = LanguageCode._CF_enumeration.addEnumeration(unicode_value='ch', tag='ch')
LanguageCode.ce = LanguageCode._CF_enumeration.addEnumeration(unicode_value='ce', tag='ce')
LanguageCode.zh = LanguageCode._CF_enumeration.addEnumeration(unicode_value='zh', tag='zh')
LanguageCode.cu = LanguageCode._CF_enumeration.addEnumeration(unicode_value='cu', tag='cu')
LanguageCode.cv = LanguageCode._CF_enumeration.addEnumeration(unicode_value='cv', tag='cv')
LanguageCode.kw = LanguageCode._CF_enumeration.addEnumeration(unicode_value='kw', tag='kw')
LanguageCode.co = LanguageCode._CF_enumeration.addEnumeration(unicode_value='co', tag='co')
LanguageCode.cr = LanguageCode._CF_enumeration.addEnumeration(unicode_value='cr', tag='cr')
LanguageCode.cy = LanguageCode._CF_enumeration.addEnumeration(unicode_value='cy', tag='cy')
LanguageCode.da = LanguageCode._CF_enumeration.addEnumeration(unicode_value='da', tag='da')
LanguageCode.de = LanguageCode._CF_enumeration.addEnumeration(unicode_value='de', tag='de')
LanguageCode.dv = LanguageCode._CF_enumeration.addEnumeration(unicode_value='dv', tag='dv')
LanguageCode.nl = LanguageCode._CF_enumeration.addEnumeration(unicode_value='nl', tag='nl')
LanguageCode.dz = LanguageCode._CF_enumeration.addEnumeration(unicode_value='dz', tag='dz')
LanguageCode.el = LanguageCode._CF_enumeration.addEnumeration(unicode_value='el', tag='el')
LanguageCode.en = LanguageCode._CF_enumeration.addEnumeration(unicode_value='en', tag='en')
LanguageCode.eo = LanguageCode._CF_enumeration.addEnumeration(unicode_value='eo', tag='eo')
LanguageCode.et = LanguageCode._CF_enumeration.addEnumeration(unicode_value='et', tag='et')
LanguageCode.ee = LanguageCode._CF_enumeration.addEnumeration(unicode_value='ee', tag='ee')
LanguageCode.fo = LanguageCode._CF_enumeration.addEnumeration(unicode_value='fo', tag='fo')
LanguageCode.fa = LanguageCode._CF_enumeration.addEnumeration(unicode_value='fa', tag='fa')
LanguageCode.fj = LanguageCode._CF_enumeration.addEnumeration(unicode_value='fj', tag='fj')
LanguageCode.fi = LanguageCode._CF_enumeration.addEnumeration(unicode_value='fi', tag='fi')
LanguageCode.fr = LanguageCode._CF_enumeration.addEnumeration(unicode_value='fr', tag='fr')
LanguageCode.fy = LanguageCode._CF_enumeration.addEnumeration(unicode_value='fy', tag='fy')
LanguageCode.ff = LanguageCode._CF_enumeration.addEnumeration(unicode_value='ff', tag='ff')
LanguageCode.ka = LanguageCode._CF_enumeration.addEnumeration(unicode_value='ka', tag='ka')
LanguageCode.gd = LanguageCode._CF_enumeration.addEnumeration(unicode_value='gd', tag='gd')
LanguageCode.ga = LanguageCode._CF_enumeration.addEnumeration(unicode_value='ga', tag='ga')
LanguageCode.gl = LanguageCode._CF_enumeration.addEnumeration(unicode_value='gl', tag='gl')
LanguageCode.gv = LanguageCode._CF_enumeration.addEnumeration(unicode_value='gv', tag='gv')
LanguageCode.gn = LanguageCode._CF_enumeration.addEnumeration(unicode_value='gn', tag='gn')
LanguageCode.gu = LanguageCode._CF_enumeration.addEnumeration(unicode_value='gu', tag='gu')
LanguageCode.ht = LanguageCode._CF_enumeration.addEnumeration(unicode_value='ht', tag='ht')
LanguageCode.ha = LanguageCode._CF_enumeration.addEnumeration(unicode_value='ha', tag='ha')
LanguageCode.he = LanguageCode._CF_enumeration.addEnumeration(unicode_value='he', tag='he')
LanguageCode.hz = LanguageCode._CF_enumeration.addEnumeration(unicode_value='hz', tag='hz')
LanguageCode.hi = LanguageCode._CF_enumeration.addEnumeration(unicode_value='hi', tag='hi')
LanguageCode.ho = LanguageCode._CF_enumeration.addEnumeration(unicode_value='ho', tag='ho')
LanguageCode.hr = LanguageCode._CF_enumeration.addEnumeration(unicode_value='hr', tag='hr')
LanguageCode.hu = LanguageCode._CF_enumeration.addEnumeration(unicode_value='hu', tag='hu')
LanguageCode.ig = LanguageCode._CF_enumeration.addEnumeration(unicode_value='ig', tag='ig')
LanguageCode.is_ = LanguageCode._CF_enumeration.addEnumeration(unicode_value='is', tag='is_')
LanguageCode.io = LanguageCode._CF_enumeration.addEnumeration(unicode_value='io', tag='io')
LanguageCode.ii = LanguageCode._CF_enumeration.addEnumeration(unicode_value='ii', tag='ii')
LanguageCode.iu = LanguageCode._CF_enumeration.addEnumeration(unicode_value='iu', tag='iu')
LanguageCode.ie = LanguageCode._CF_enumeration.addEnumeration(unicode_value='ie', tag='ie')
LanguageCode.ia = LanguageCode._CF_enumeration.addEnumeration(unicode_value='ia', tag='ia')
LanguageCode.id = LanguageCode._CF_enumeration.addEnumeration(unicode_value='id', tag='id')
LanguageCode.ik = LanguageCode._CF_enumeration.addEnumeration(unicode_value='ik', tag='ik')
LanguageCode.it = LanguageCode._CF_enumeration.addEnumeration(unicode_value='it', tag='it')
LanguageCode.jv = LanguageCode._CF_enumeration.addEnumeration(unicode_value='jv', tag='jv')
LanguageCode.ja = LanguageCode._CF_enumeration.addEnumeration(unicode_value='ja', tag='ja')
LanguageCode.kl = LanguageCode._CF_enumeration.addEnumeration(unicode_value='kl', tag='kl')
LanguageCode.kn = LanguageCode._CF_enumeration.addEnumeration(unicode_value='kn', tag='kn')
LanguageCode.ks = LanguageCode._CF_enumeration.addEnumeration(unicode_value='ks', tag='ks')
LanguageCode.kr = LanguageCode._CF_enumeration.addEnumeration(unicode_value='kr', tag='kr')
LanguageCode.kk = LanguageCode._CF_enumeration.addEnumeration(unicode_value='kk', tag='kk')
LanguageCode.km = LanguageCode._CF_enumeration.addEnumeration(unicode_value='km', tag='km')
LanguageCode.ki = LanguageCode._CF_enumeration.addEnumeration(unicode_value='ki', tag='ki')
LanguageCode.rw = LanguageCode._CF_enumeration.addEnumeration(unicode_value='rw', tag='rw')
LanguageCode.ky = LanguageCode._CF_enumeration.addEnumeration(unicode_value='ky', tag='ky')
LanguageCode.kv = LanguageCode._CF_enumeration.addEnumeration(unicode_value='kv', tag='kv')
LanguageCode.kg = LanguageCode._CF_enumeration.addEnumeration(unicode_value='kg', tag='kg')
LanguageCode.ko = LanguageCode._CF_enumeration.addEnumeration(unicode_value='ko', tag='ko')
LanguageCode.kj = LanguageCode._CF_enumeration.addEnumeration(unicode_value='kj', tag='kj')
LanguageCode.ku = LanguageCode._CF_enumeration.addEnumeration(unicode_value='ku', tag='ku')
LanguageCode.lo = LanguageCode._CF_enumeration.addEnumeration(unicode_value='lo', tag='lo')
LanguageCode.la = LanguageCode._CF_enumeration.addEnumeration(unicode_value='la', tag='la')
LanguageCode.lv = LanguageCode._CF_enumeration.addEnumeration(unicode_value='lv', tag='lv')
LanguageCode.li = LanguageCode._CF_enumeration.addEnumeration(unicode_value='li', tag='li')
LanguageCode.ln = LanguageCode._CF_enumeration.addEnumeration(unicode_value='ln', tag='ln')
LanguageCode.lt = LanguageCode._CF_enumeration.addEnumeration(unicode_value='lt', tag='lt')
LanguageCode.lb = LanguageCode._CF_enumeration.addEnumeration(unicode_value='lb', tag='lb')
LanguageCode.lu = LanguageCode._CF_enumeration.addEnumeration(unicode_value='lu', tag='lu')
LanguageCode.lg = LanguageCode._CF_enumeration.addEnumeration(unicode_value='lg', tag='lg')
LanguageCode.mk = LanguageCode._CF_enumeration.addEnumeration(unicode_value='mk', tag='mk')
LanguageCode.mh = LanguageCode._CF_enumeration.addEnumeration(unicode_value='mh', tag='mh')
LanguageCode.ml = LanguageCode._CF_enumeration.addEnumeration(unicode_value='ml', tag='ml')
LanguageCode.mi = LanguageCode._CF_enumeration.addEnumeration(unicode_value='mi', tag='mi')
LanguageCode.mr = LanguageCode._CF_enumeration.addEnumeration(unicode_value='mr', tag='mr')
LanguageCode.ms = LanguageCode._CF_enumeration.addEnumeration(unicode_value='ms', tag='ms')
LanguageCode.mg = LanguageCode._CF_enumeration.addEnumeration(unicode_value='mg', tag='mg')
LanguageCode.mt = LanguageCode._CF_enumeration.addEnumeration(unicode_value='mt', tag='mt')
LanguageCode.mo = LanguageCode._CF_enumeration.addEnumeration(unicode_value='mo', tag='mo')
LanguageCode.mn = LanguageCode._CF_enumeration.addEnumeration(unicode_value='mn', tag='mn')
LanguageCode.na = LanguageCode._CF_enumeration.addEnumeration(unicode_value='na', tag='na')
LanguageCode.nv = LanguageCode._CF_enumeration.addEnumeration(unicode_value='nv', tag='nv')
LanguageCode.nr = LanguageCode._CF_enumeration.addEnumeration(unicode_value='nr', tag='nr')
LanguageCode.nd = LanguageCode._CF_enumeration.addEnumeration(unicode_value='nd', tag='nd')
LanguageCode.ng = LanguageCode._CF_enumeration.addEnumeration(unicode_value='ng', tag='ng')
LanguageCode.ne = LanguageCode._CF_enumeration.addEnumeration(unicode_value='ne', tag='ne')
LanguageCode.nn = LanguageCode._CF_enumeration.addEnumeration(unicode_value='nn', tag='nn')
LanguageCode.nb = LanguageCode._CF_enumeration.addEnumeration(unicode_value='nb', tag='nb')
LanguageCode.no = LanguageCode._CF_enumeration.addEnumeration(unicode_value='no', tag='no')
LanguageCode.ny = LanguageCode._CF_enumeration.addEnumeration(unicode_value='ny', tag='ny')
LanguageCode.oc = LanguageCode._CF_enumeration.addEnumeration(unicode_value='oc', tag='oc')
LanguageCode.oj = LanguageCode._CF_enumeration.addEnumeration(unicode_value='oj', tag='oj')
LanguageCode.or_ = LanguageCode._CF_enumeration.addEnumeration(unicode_value='or', tag='or_')
LanguageCode.om = LanguageCode._CF_enumeration.addEnumeration(unicode_value='om', tag='om')
LanguageCode.os = LanguageCode._CF_enumeration.addEnumeration(unicode_value='os', tag='os')
LanguageCode.pa = LanguageCode._CF_enumeration.addEnumeration(unicode_value='pa', tag='pa')
LanguageCode.pi = LanguageCode._CF_enumeration.addEnumeration(unicode_value='pi', tag='pi')
LanguageCode.pl = LanguageCode._CF_enumeration.addEnumeration(unicode_value='pl', tag='pl')
LanguageCode.pt = LanguageCode._CF_enumeration.addEnumeration(unicode_value='pt', tag='pt')
LanguageCode.ps = LanguageCode._CF_enumeration.addEnumeration(unicode_value='ps', tag='ps')
LanguageCode.qu = LanguageCode._CF_enumeration.addEnumeration(unicode_value='qu', tag='qu')
LanguageCode.rm = LanguageCode._CF_enumeration.addEnumeration(unicode_value='rm', tag='rm')
LanguageCode.ro = LanguageCode._CF_enumeration.addEnumeration(unicode_value='ro', tag='ro')
LanguageCode.rn = LanguageCode._CF_enumeration.addEnumeration(unicode_value='rn', tag='rn')
LanguageCode.ru = LanguageCode._CF_enumeration.addEnumeration(unicode_value='ru', tag='ru')
LanguageCode.sg = LanguageCode._CF_enumeration.addEnumeration(unicode_value='sg', tag='sg')
LanguageCode.sa = LanguageCode._CF_enumeration.addEnumeration(unicode_value='sa', tag='sa')
LanguageCode.sr = LanguageCode._CF_enumeration.addEnumeration(unicode_value='sr', tag='sr')
LanguageCode.si = LanguageCode._CF_enumeration.addEnumeration(unicode_value='si', tag='si')
LanguageCode.sk = LanguageCode._CF_enumeration.addEnumeration(unicode_value='sk', tag='sk')
LanguageCode.sl = LanguageCode._CF_enumeration.addEnumeration(unicode_value='sl', tag='sl')
LanguageCode.se = LanguageCode._CF_enumeration.addEnumeration(unicode_value='se', tag='se')
LanguageCode.sm = LanguageCode._CF_enumeration.addEnumeration(unicode_value='sm', tag='sm')
LanguageCode.sn = LanguageCode._CF_enumeration.addEnumeration(unicode_value='sn', tag='sn')
LanguageCode.sd = LanguageCode._CF_enumeration.addEnumeration(unicode_value='sd', tag='sd')
LanguageCode.so = LanguageCode._CF_enumeration.addEnumeration(unicode_value='so', tag='so')
LanguageCode.st = LanguageCode._CF_enumeration.addEnumeration(unicode_value='st', tag='st')
LanguageCode.es = LanguageCode._CF_enumeration.addEnumeration(unicode_value='es', tag='es')
LanguageCode.sc = LanguageCode._CF_enumeration.addEnumeration(unicode_value='sc', tag='sc')
LanguageCode.ss = LanguageCode._CF_enumeration.addEnumeration(unicode_value='ss', tag='ss')
LanguageCode.su = LanguageCode._CF_enumeration.addEnumeration(unicode_value='su', tag='su')
LanguageCode.sw = LanguageCode._CF_enumeration.addEnumeration(unicode_value='sw', tag='sw')
LanguageCode.sv = LanguageCode._CF_enumeration.addEnumeration(unicode_value='sv', tag='sv')
LanguageCode.ty = LanguageCode._CF_enumeration.addEnumeration(unicode_value='ty', tag='ty')
LanguageCode.ta = LanguageCode._CF_enumeration.addEnumeration(unicode_value='ta', tag='ta')
LanguageCode.tt = LanguageCode._CF_enumeration.addEnumeration(unicode_value='tt', tag='tt')
LanguageCode.te = LanguageCode._CF_enumeration.addEnumeration(unicode_value='te', tag='te')
LanguageCode.tg = LanguageCode._CF_enumeration.addEnumeration(unicode_value='tg', tag='tg')
LanguageCode.tl = LanguageCode._CF_enumeration.addEnumeration(unicode_value='tl', tag='tl')
LanguageCode.th = LanguageCode._CF_enumeration.addEnumeration(unicode_value='th', tag='th')
LanguageCode.ti = LanguageCode._CF_enumeration.addEnumeration(unicode_value='ti', tag='ti')
LanguageCode.to = LanguageCode._CF_enumeration.addEnumeration(unicode_value='to', tag='to')
LanguageCode.tn = LanguageCode._CF_enumeration.addEnumeration(unicode_value='tn', tag='tn')
LanguageCode.ts = LanguageCode._CF_enumeration.addEnumeration(unicode_value='ts', tag='ts')
LanguageCode.tk = LanguageCode._CF_enumeration.addEnumeration(unicode_value='tk', tag='tk')
LanguageCode.tr = LanguageCode._CF_enumeration.addEnumeration(unicode_value='tr', tag='tr')
LanguageCode.tw = LanguageCode._CF_enumeration.addEnumeration(unicode_value='tw', tag='tw')
LanguageCode.ug = LanguageCode._CF_enumeration.addEnumeration(unicode_value='ug', tag='ug')
LanguageCode.uk = LanguageCode._CF_enumeration.addEnumeration(unicode_value='uk', tag='uk')
LanguageCode.ur = LanguageCode._CF_enumeration.addEnumeration(unicode_value='ur', tag='ur')
LanguageCode.uz = LanguageCode._CF_enumeration.addEnumeration(unicode_value='uz', tag='uz')
LanguageCode.ve = LanguageCode._CF_enumeration.addEnumeration(unicode_value='ve', tag='ve')
LanguageCode.vi = LanguageCode._CF_enumeration.addEnumeration(unicode_value='vi', tag='vi')
LanguageCode.vo = LanguageCode._CF_enumeration.addEnumeration(unicode_value='vo', tag='vo')
LanguageCode.wa = LanguageCode._CF_enumeration.addEnumeration(unicode_value='wa', tag='wa')
LanguageCode.wo = LanguageCode._CF_enumeration.addEnumeration(unicode_value='wo', tag='wo')
LanguageCode.xh = LanguageCode._CF_enumeration.addEnumeration(unicode_value='xh', tag='xh')
LanguageCode.yi = LanguageCode._CF_enumeration.addEnumeration(unicode_value='yi', tag='yi')
LanguageCode.yo = LanguageCode._CF_enumeration.addEnumeration(unicode_value='yo', tag='yo')
LanguageCode.za = LanguageCode._CF_enumeration.addEnumeration(unicode_value='za', tag='za')
LanguageCode.zu = LanguageCode._CF_enumeration.addEnumeration(unicode_value='zu', tag='zu')
LanguageCode._InitializeFacetMap(LanguageCode._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'LanguageCode', LanguageCode)
