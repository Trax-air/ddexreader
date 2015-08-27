# .\_ddex.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:b5844111f7d00f7f21023c2d6379a665aaee8844
# Generated 2015-08-12 15:54:17.333000 by PyXB version 1.2.4 using Python 2.7.0.final.0
# Namespace http://ddex.net/xml/20100121/ddex [xmlns:ddex]

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:9d0dcd70-40f9-11e5-9eef-b870f477ffbe')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://ddex.net/xml/20100121/ddex', create_if_missing=True)
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


# Atomic simple type: {http://ddex.net/xml/20100121/ddex}AdministratingRecordCompanyRole
class AdministratingRecordCompanyRole (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A role played by a Party responsible for administering Rights in a Resource or a Release."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AdministratingRecordCompanyRole')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 9, 4)
    _Documentation = 'A role played by a Party responsible for administering Rights in a Resource or a Release.'
AdministratingRecordCompanyRole._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=AdministratingRecordCompanyRole, enum_prefix=None)
AdministratingRecordCompanyRole.DesignatedDsrMessageRecipient = AdministratingRecordCompanyRole._CF_enumeration.addEnumeration(unicode_value='DesignatedDsrMessageRecipient', tag='DesignatedDsrMessageRecipient')
AdministratingRecordCompanyRole.RightsAdministrator = AdministratingRecordCompanyRole._CF_enumeration.addEnumeration(unicode_value='RightsAdministrator', tag='RightsAdministrator')
AdministratingRecordCompanyRole.RoyaltyAdministrator = AdministratingRecordCompanyRole._CF_enumeration.addEnumeration(unicode_value='RoyaltyAdministrator', tag='RoyaltyAdministrator')
AdministratingRecordCompanyRole.Unknown = AdministratingRecordCompanyRole._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
AdministratingRecordCompanyRole._InitializeFacetMap(AdministratingRecordCompanyRole._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'AdministratingRecordCompanyRole', AdministratingRecordCompanyRole)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}ArtistRole
class ArtistRole (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A role of a principal Contributor in relation to a Performance or a Fixation."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ArtistRole')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 20, 4)
    _Documentation = 'A role of a principal Contributor in relation to a Performance or a Fixation.'
ArtistRole._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ArtistRole, enum_prefix=None)
ArtistRole.Actor = ArtistRole._CF_enumeration.addEnumeration(unicode_value='Actor', tag='Actor')
ArtistRole.Adapter = ArtistRole._CF_enumeration.addEnumeration(unicode_value='Adapter', tag='Adapter')
ArtistRole.Architect = ArtistRole._CF_enumeration.addEnumeration(unicode_value='Architect', tag='Architect')
ArtistRole.Arranger = ArtistRole._CF_enumeration.addEnumeration(unicode_value='Arranger', tag='Arranger')
ArtistRole.Artist = ArtistRole._CF_enumeration.addEnumeration(unicode_value='Artist', tag='Artist')
ArtistRole.AssociatedPerformer = ArtistRole._CF_enumeration.addEnumeration(unicode_value='AssociatedPerformer', tag='AssociatedPerformer')
ArtistRole.Author = ArtistRole._CF_enumeration.addEnumeration(unicode_value='Author', tag='Author')
ArtistRole.Band = ArtistRole._CF_enumeration.addEnumeration(unicode_value='Band', tag='Band')
ArtistRole.Cartoonist = ArtistRole._CF_enumeration.addEnumeration(unicode_value='Cartoonist', tag='Cartoonist')
ArtistRole.Choir = ArtistRole._CF_enumeration.addEnumeration(unicode_value='Choir', tag='Choir')
ArtistRole.Choreographer = ArtistRole._CF_enumeration.addEnumeration(unicode_value='Choreographer', tag='Choreographer')
ArtistRole.Composer = ArtistRole._CF_enumeration.addEnumeration(unicode_value='Composer', tag='Composer')
ArtistRole.ComposerLyricist = ArtistRole._CF_enumeration.addEnumeration(unicode_value='ComposerLyricist', tag='ComposerLyricist')
ArtistRole.ComputerGraphicCreator = ArtistRole._CF_enumeration.addEnumeration(unicode_value='ComputerGraphicCreator', tag='ComputerGraphicCreator')
ArtistRole.Conductor = ArtistRole._CF_enumeration.addEnumeration(unicode_value='Conductor', tag='Conductor')
ArtistRole.Contributor = ArtistRole._CF_enumeration.addEnumeration(unicode_value='Contributor', tag='Contributor')
ArtistRole.Designer = ArtistRole._CF_enumeration.addEnumeration(unicode_value='Designer', tag='Designer')
ArtistRole.Director = ArtistRole._CF_enumeration.addEnumeration(unicode_value='Director', tag='Director')
ArtistRole.Ensemble = ArtistRole._CF_enumeration.addEnumeration(unicode_value='Ensemble', tag='Ensemble')
ArtistRole.FeaturedArtist = ArtistRole._CF_enumeration.addEnumeration(unicode_value='FeaturedArtist', tag='FeaturedArtist')
ArtistRole.FilmDirector = ArtistRole._CF_enumeration.addEnumeration(unicode_value='FilmDirector', tag='FilmDirector')
ArtistRole.GraphicArtist = ArtistRole._CF_enumeration.addEnumeration(unicode_value='GraphicArtist', tag='GraphicArtist')
ArtistRole.GraphicDesigner = ArtistRole._CF_enumeration.addEnumeration(unicode_value='GraphicDesigner', tag='GraphicDesigner')
ArtistRole.Journalist = ArtistRole._CF_enumeration.addEnumeration(unicode_value='Journalist', tag='Journalist')
ArtistRole.Librettist = ArtistRole._CF_enumeration.addEnumeration(unicode_value='Librettist', tag='Librettist')
ArtistRole.Lyricist = ArtistRole._CF_enumeration.addEnumeration(unicode_value='Lyricist', tag='Lyricist')
ArtistRole.MainArtist = ArtistRole._CF_enumeration.addEnumeration(unicode_value='MainArtist', tag='MainArtist')
ArtistRole.MusicPublisher = ArtistRole._CF_enumeration.addEnumeration(unicode_value='MusicPublisher', tag='MusicPublisher')
ArtistRole.NonLyricAuthor = ArtistRole._CF_enumeration.addEnumeration(unicode_value='NonLyricAuthor', tag='NonLyricAuthor')
ArtistRole.Orchestra = ArtistRole._CF_enumeration.addEnumeration(unicode_value='Orchestra', tag='Orchestra')
ArtistRole.OriginalPublisher = ArtistRole._CF_enumeration.addEnumeration(unicode_value='OriginalPublisher', tag='OriginalPublisher')
ArtistRole.Painter = ArtistRole._CF_enumeration.addEnumeration(unicode_value='Painter', tag='Painter')
ArtistRole.Photographer = ArtistRole._CF_enumeration.addEnumeration(unicode_value='Photographer', tag='Photographer')
ArtistRole.PhotographyDirector = ArtistRole._CF_enumeration.addEnumeration(unicode_value='PhotographyDirector', tag='PhotographyDirector')
ArtistRole.Playwright = ArtistRole._CF_enumeration.addEnumeration(unicode_value='Playwright', tag='Playwright')
ArtistRole.PrimaryMusician = ArtistRole._CF_enumeration.addEnumeration(unicode_value='PrimaryMusician', tag='PrimaryMusician')
ArtistRole.Producer = ArtistRole._CF_enumeration.addEnumeration(unicode_value='Producer', tag='Producer')
ArtistRole.Programmer = ArtistRole._CF_enumeration.addEnumeration(unicode_value='Programmer', tag='Programmer')
ArtistRole.ScreenplayAuthor = ArtistRole._CF_enumeration.addEnumeration(unicode_value='ScreenplayAuthor', tag='ScreenplayAuthor')
ArtistRole.Soloist = ArtistRole._CF_enumeration.addEnumeration(unicode_value='Soloist', tag='Soloist')
ArtistRole.StudioPersonnel = ArtistRole._CF_enumeration.addEnumeration(unicode_value='StudioPersonnel', tag='StudioPersonnel')
ArtistRole.SubArranger = ArtistRole._CF_enumeration.addEnumeration(unicode_value='SubArranger', tag='SubArranger')
ArtistRole.SubPublisher = ArtistRole._CF_enumeration.addEnumeration(unicode_value='SubPublisher', tag='SubPublisher')
ArtistRole.SubstitutedPublisher = ArtistRole._CF_enumeration.addEnumeration(unicode_value='SubstitutedPublisher', tag='SubstitutedPublisher')
ArtistRole.Translator = ArtistRole._CF_enumeration.addEnumeration(unicode_value='Translator', tag='Translator')
ArtistRole.Unknown = ArtistRole._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
ArtistRole.UserDefined = ArtistRole._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
ArtistRole._InitializeFacetMap(ArtistRole._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ArtistRole', ArtistRole)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}AudioCodecType
class AudioCodecType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of AudioCodec."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AudioCodecType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 74, 4)
    _Documentation = 'A Type of AudioCodec.'
AudioCodecType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=AudioCodecType, enum_prefix=None)
AudioCodecType.AAC = AudioCodecType._CF_enumeration.addEnumeration(unicode_value='AAC', tag='AAC')
AudioCodecType.ADPCM = AudioCodecType._CF_enumeration.addEnumeration(unicode_value='ADPCM', tag='ADPCM')
AudioCodecType.MP2 = AudioCodecType._CF_enumeration.addEnumeration(unicode_value='MP2', tag='MP2')
AudioCodecType.MP3 = AudioCodecType._CF_enumeration.addEnumeration(unicode_value='MP3', tag='MP3')
AudioCodecType.PCM = AudioCodecType._CF_enumeration.addEnumeration(unicode_value='PCM', tag='PCM')
AudioCodecType.RealAudio = AudioCodecType._CF_enumeration.addEnumeration(unicode_value='RealAudio', tag='RealAudio')
AudioCodecType.Unknown = AudioCodecType._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
AudioCodecType.UserDefined = AudioCodecType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
AudioCodecType.Vorbis = AudioCodecType._CF_enumeration.addEnumeration(unicode_value='Vorbis', tag='Vorbis')
AudioCodecType.WMA = AudioCodecType._CF_enumeration.addEnumeration(unicode_value='WMA', tag='WMA')
AudioCodecType._InitializeFacetMap(AudioCodecType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'AudioCodecType', AudioCodecType)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}CalculationType
class CalculationType (pyxb.binding.datatypes.string):

    """A Type of Calculation used to determine an actual Amount paid."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CalculationType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 91, 4)
    _Documentation = 'A Type of Calculation used to determine an actual Amount paid.'
CalculationType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'CalculationType', CalculationType)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}CarrierType
class CarrierType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Carrier used for a Fixation."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CarrierType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 97, 4)
    _Documentation = 'A Type of Carrier used for a Fixation.'
CarrierType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CarrierType, enum_prefix=None)
CarrierType.n12InchDiscoSingleRemix = CarrierType._CF_enumeration.addEnumeration(unicode_value='12InchDiscoSingleRemix', tag='n12InchDiscoSingleRemix')
CarrierType.n33rpm10InchLP = CarrierType._CF_enumeration.addEnumeration(unicode_value='33rpm10InchLP', tag='n33rpm10InchLP')
CarrierType.n33rpm10InchSingle = CarrierType._CF_enumeration.addEnumeration(unicode_value='33rpm10InchSingle', tag='n33rpm10InchSingle')
CarrierType.n33rpm12InchLP = CarrierType._CF_enumeration.addEnumeration(unicode_value='33rpm12InchLP', tag='n33rpm12InchLP')
CarrierType.n33rpm12InchLp20Tracks = CarrierType._CF_enumeration.addEnumeration(unicode_value='33rpm12InchLp20Tracks', tag='n33rpm12InchLp20Tracks')
CarrierType.n33rpm12InchMaxiSingle = CarrierType._CF_enumeration.addEnumeration(unicode_value='33rpm12InchMaxiSingle', tag='n33rpm12InchMaxiSingle')
CarrierType.n33rpm12InchSingle = CarrierType._CF_enumeration.addEnumeration(unicode_value='33rpm12InchSingle', tag='n33rpm12InchSingle')
CarrierType.n33rpm7InchLP = CarrierType._CF_enumeration.addEnumeration(unicode_value='33rpm7InchLP', tag='n33rpm7InchLP')
CarrierType.n33rpm7InchSingle = CarrierType._CF_enumeration.addEnumeration(unicode_value='33rpm7InchSingle', tag='n33rpm7InchSingle')
CarrierType.n45rpm10InchLP = CarrierType._CF_enumeration.addEnumeration(unicode_value='45rpm10InchLP', tag='n45rpm10InchLP')
CarrierType.n45rpm10InchMaxiSingle = CarrierType._CF_enumeration.addEnumeration(unicode_value='45rpm10InchMaxiSingle', tag='n45rpm10InchMaxiSingle')
CarrierType.n45rpm10InchSingle = CarrierType._CF_enumeration.addEnumeration(unicode_value='45rpm10InchSingle', tag='n45rpm10InchSingle')
CarrierType.n45rpm12InchLP = CarrierType._CF_enumeration.addEnumeration(unicode_value='45rpm12InchLP', tag='n45rpm12InchLP')
CarrierType.n45rpm12InchMaxiSingle = CarrierType._CF_enumeration.addEnumeration(unicode_value='45rpm12InchMaxiSingle', tag='n45rpm12InchMaxiSingle')
CarrierType.n45rpm12InchSingle = CarrierType._CF_enumeration.addEnumeration(unicode_value='45rpm12InchSingle', tag='n45rpm12InchSingle')
CarrierType.n45rpm7InchEP = CarrierType._CF_enumeration.addEnumeration(unicode_value='45rpm7InchEP', tag='n45rpm7InchEP')
CarrierType.n45rpm7InchSingle = CarrierType._CF_enumeration.addEnumeration(unicode_value='45rpm7InchSingle', tag='n45rpm7InchSingle')
CarrierType.n7InchMaxiSingleRemix = CarrierType._CF_enumeration.addEnumeration(unicode_value='7InchMaxiSingleRemix', tag='n7InchMaxiSingleRemix')
CarrierType.BluRay = CarrierType._CF_enumeration.addEnumeration(unicode_value='BluRay', tag='BluRay')
CarrierType.CD = CarrierType._CF_enumeration.addEnumeration(unicode_value='CD', tag='CD')
CarrierType.CdCompilation = CarrierType._CF_enumeration.addEnumeration(unicode_value='CdCompilation', tag='CdCompilation')
CarrierType.CdEp = CarrierType._CF_enumeration.addEnumeration(unicode_value='CdEp', tag='CdEp')
CarrierType.CdEpEnhanced = CarrierType._CF_enumeration.addEnumeration(unicode_value='CdEpEnhanced', tag='CdEpEnhanced')
CarrierType.CdExtraCompilation = CarrierType._CF_enumeration.addEnumeration(unicode_value='CdExtraCompilation', tag='CdExtraCompilation')
CarrierType.CdExtraEP = CarrierType._CF_enumeration.addEnumeration(unicode_value='CdExtraEP', tag='CdExtraEP')
CarrierType.CdExtraLP = CarrierType._CF_enumeration.addEnumeration(unicode_value='CdExtraLP', tag='CdExtraLP')
CarrierType.CdExtraMaxiRemix = CarrierType._CF_enumeration.addEnumeration(unicode_value='CdExtraMaxiRemix', tag='CdExtraMaxiRemix')
CarrierType.CdExtraMaxiSingle = CarrierType._CF_enumeration.addEnumeration(unicode_value='CdExtraMaxiSingle', tag='CdExtraMaxiSingle')
CarrierType.CdExtraSingle = CarrierType._CF_enumeration.addEnumeration(unicode_value='CdExtraSingle', tag='CdExtraSingle')
CarrierType.CdExtraSingle2Tracks = CarrierType._CF_enumeration.addEnumeration(unicode_value='CdExtraSingle2Tracks', tag='CdExtraSingle2Tracks')
CarrierType.CdLp = CarrierType._CF_enumeration.addEnumeration(unicode_value='CdLp', tag='CdLp')
CarrierType.CdLp5Inch = CarrierType._CF_enumeration.addEnumeration(unicode_value='CdLp5Inch', tag='CdLp5Inch')
CarrierType.CdLpEnhanced = CarrierType._CF_enumeration.addEnumeration(unicode_value='CdLpEnhanced', tag='CdLpEnhanced')
CarrierType.CdLpPlusCdVideo = CarrierType._CF_enumeration.addEnumeration(unicode_value='CdLpPlusCdVideo', tag='CdLpPlusCdVideo')
CarrierType.CdLpPlusDvdAudio = CarrierType._CF_enumeration.addEnumeration(unicode_value='CdLpPlusDvdAudio', tag='CdLpPlusDvdAudio')
CarrierType.CdLpPlusDvdVideo = CarrierType._CF_enumeration.addEnumeration(unicode_value='CdLpPlusDvdVideo', tag='CdLpPlusDvdVideo')
CarrierType.CdLpPlusWeb = CarrierType._CF_enumeration.addEnumeration(unicode_value='CdLpPlusWeb', tag='CdLpPlusWeb')
CarrierType.CdMaxiSingle = CarrierType._CF_enumeration.addEnumeration(unicode_value='CdMaxiSingle', tag='CdMaxiSingle')
CarrierType.CdMaxiSingle3Inch = CarrierType._CF_enumeration.addEnumeration(unicode_value='CdMaxiSingle3Inch', tag='CdMaxiSingle3Inch')
CarrierType.CdMaxiSingleEnhanced = CarrierType._CF_enumeration.addEnumeration(unicode_value='CdMaxiSingleEnhanced', tag='CdMaxiSingleEnhanced')
CarrierType.CdMaxiSingleRemix = CarrierType._CF_enumeration.addEnumeration(unicode_value='CdMaxiSingleRemix', tag='CdMaxiSingleRemix')
CarrierType.CdPlusCdBonus = CarrierType._CF_enumeration.addEnumeration(unicode_value='CdPlusCdBonus', tag='CdPlusCdBonus')
CarrierType.CdPlusDvdBonus = CarrierType._CF_enumeration.addEnumeration(unicode_value='CdPlusDvdBonus', tag='CdPlusDvdBonus')
CarrierType.CdRom = CarrierType._CF_enumeration.addEnumeration(unicode_value='CdRom', tag='CdRom')
CarrierType.CdSingle = CarrierType._CF_enumeration.addEnumeration(unicode_value='CdSingle', tag='CdSingle')
CarrierType.CdSingle3Inch = CarrierType._CF_enumeration.addEnumeration(unicode_value='CdSingle3Inch', tag='CdSingle3Inch')
CarrierType.CdSingle5Inch = CarrierType._CF_enumeration.addEnumeration(unicode_value='CdSingle5Inch', tag='CdSingle5Inch')
CarrierType.CdVideo5LpNTSC = CarrierType._CF_enumeration.addEnumeration(unicode_value='CdVideo5LpNTSC', tag='CdVideo5LpNTSC')
CarrierType.CdVideo5LpPAL = CarrierType._CF_enumeration.addEnumeration(unicode_value='CdVideo5LpPAL', tag='CdVideo5LpPAL')
CarrierType.CdVideoAudioCompatible = CarrierType._CF_enumeration.addEnumeration(unicode_value='CdVideoAudioCompatible', tag='CdVideoAudioCompatible')
CarrierType.CombiPack = CarrierType._CF_enumeration.addEnumeration(unicode_value='CombiPack', tag='CombiPack')
CarrierType.DCC = CarrierType._CF_enumeration.addEnumeration(unicode_value='DCC', tag='DCC')
CarrierType.DccCompilation = CarrierType._CF_enumeration.addEnumeration(unicode_value='DccCompilation', tag='DccCompilation')
CarrierType.DualDisc = CarrierType._CF_enumeration.addEnumeration(unicode_value='DualDisc', tag='DualDisc')
CarrierType.DVD = CarrierType._CF_enumeration.addEnumeration(unicode_value='DVD', tag='DVD')
CarrierType.DvdAudio = CarrierType._CF_enumeration.addEnumeration(unicode_value='DvdAudio', tag='DvdAudio')
CarrierType.DvdAudio5MaxiSingle = CarrierType._CF_enumeration.addEnumeration(unicode_value='DvdAudio5MaxiSingle', tag='DvdAudio5MaxiSingle')
CarrierType.DvdAudioLP = CarrierType._CF_enumeration.addEnumeration(unicode_value='DvdAudioLP', tag='DvdAudioLP')
CarrierType.DvdAudioSingle = CarrierType._CF_enumeration.addEnumeration(unicode_value='DvdAudioSingle', tag='DvdAudioSingle')
CarrierType.DvdRom = CarrierType._CF_enumeration.addEnumeration(unicode_value='DvdRom', tag='DvdRom')
CarrierType.DvdSingle = CarrierType._CF_enumeration.addEnumeration(unicode_value='DvdSingle', tag='DvdSingle')
CarrierType.DvdVideo = CarrierType._CF_enumeration.addEnumeration(unicode_value='DvdVideo', tag='DvdVideo')
CarrierType.DvdVideo5MaxiSingleNTSC = CarrierType._CF_enumeration.addEnumeration(unicode_value='DvdVideo5MaxiSingleNTSC', tag='DvdVideo5MaxiSingleNTSC')
CarrierType.DvdVideo5MaxiSinglePAL = CarrierType._CF_enumeration.addEnumeration(unicode_value='DvdVideo5MaxiSinglePAL', tag='DvdVideo5MaxiSinglePAL')
CarrierType.DvdVideo5SingleNTSC = CarrierType._CF_enumeration.addEnumeration(unicode_value='DvdVideo5SingleNTSC', tag='DvdVideo5SingleNTSC')
CarrierType.DvdVideo5SinglePAL = CarrierType._CF_enumeration.addEnumeration(unicode_value='DvdVideo5SinglePAL', tag='DvdVideo5SinglePAL')
CarrierType.DvdVideoLpNTSC = CarrierType._CF_enumeration.addEnumeration(unicode_value='DvdVideoLpNTSC', tag='DvdVideoLpNTSC')
CarrierType.DvdVideoLpPAL = CarrierType._CF_enumeration.addEnumeration(unicode_value='DvdVideoLpPAL', tag='DvdVideoLpPAL')
CarrierType.DvdVideoLpPlusCdLpOrCdSingle = CarrierType._CF_enumeration.addEnumeration(unicode_value='DvdVideoLpPlusCdLpOrCdSingle', tag='DvdVideoLpPlusCdLpOrCdSingle')
CarrierType.FanPack = CarrierType._CF_enumeration.addEnumeration(unicode_value='FanPack', tag='FanPack')
CarrierType.HdDvdVideoLp = CarrierType._CF_enumeration.addEnumeration(unicode_value='HdDvdVideoLp', tag='HdDvdVideoLp')
CarrierType.LaserDiscLp12InchNTSC = CarrierType._CF_enumeration.addEnumeration(unicode_value='LaserDiscLp12InchNTSC', tag='LaserDiscLp12InchNTSC')
CarrierType.LpCompIdenticalToCdComp = CarrierType._CF_enumeration.addEnumeration(unicode_value='LpCompIdenticalToCdComp', tag='LpCompIdenticalToCdComp')
CarrierType.LpCompilation = CarrierType._CF_enumeration.addEnumeration(unicode_value='LpCompilation', tag='LpCompilation')
CarrierType.LpIdenticalToCD = CarrierType._CF_enumeration.addEnumeration(unicode_value='LpIdenticalToCD', tag='LpIdenticalToCD')
CarrierType.MC = CarrierType._CF_enumeration.addEnumeration(unicode_value='MC', tag='MC')
CarrierType.McCompIdenticalToCdComp = CarrierType._CF_enumeration.addEnumeration(unicode_value='McCompIdenticalToCdComp', tag='McCompIdenticalToCdComp')
CarrierType.McCompilation = CarrierType._CF_enumeration.addEnumeration(unicode_value='McCompilation', tag='McCompilation')
CarrierType.McDoubleLP = CarrierType._CF_enumeration.addEnumeration(unicode_value='McDoubleLP', tag='McDoubleLP')
CarrierType.McEP = CarrierType._CF_enumeration.addEnumeration(unicode_value='McEP', tag='McEP')
CarrierType.McIdenticalToCD = CarrierType._CF_enumeration.addEnumeration(unicode_value='McIdenticalToCD', tag='McIdenticalToCD')
CarrierType.McLP = CarrierType._CF_enumeration.addEnumeration(unicode_value='McLP', tag='McLP')
CarrierType.McMaxiSingle = CarrierType._CF_enumeration.addEnumeration(unicode_value='McMaxiSingle', tag='McMaxiSingle')
CarrierType.McRemix = CarrierType._CF_enumeration.addEnumeration(unicode_value='McRemix', tag='McRemix')
CarrierType.McSingle = CarrierType._CF_enumeration.addEnumeration(unicode_value='McSingle', tag='McSingle')
CarrierType.McSingleIdenticalToCDS = CarrierType._CF_enumeration.addEnumeration(unicode_value='McSingleIdenticalToCDS', tag='McSingleIdenticalToCDS')
CarrierType.MemoryDeviceAudioLP = CarrierType._CF_enumeration.addEnumeration(unicode_value='MemoryDeviceAudioLP', tag='MemoryDeviceAudioLP')
CarrierType.MemoryDeviceMixLP = CarrierType._CF_enumeration.addEnumeration(unicode_value='MemoryDeviceMixLP', tag='MemoryDeviceMixLP')
CarrierType.MemoryDeviceVideoLP = CarrierType._CF_enumeration.addEnumeration(unicode_value='MemoryDeviceVideoLP', tag='MemoryDeviceVideoLP')
CarrierType.Merchandise = CarrierType._CF_enumeration.addEnumeration(unicode_value='Merchandise', tag='Merchandise')
CarrierType.MiniDisc = CarrierType._CF_enumeration.addEnumeration(unicode_value='MiniDisc', tag='MiniDisc')
CarrierType.MiniDiscCompilation = CarrierType._CF_enumeration.addEnumeration(unicode_value='MiniDiscCompilation', tag='MiniDiscCompilation')
CarrierType.MiniDiscEP = CarrierType._CF_enumeration.addEnumeration(unicode_value='MiniDiscEP', tag='MiniDiscEP')
CarrierType.MiniDiscMaxiRemix = CarrierType._CF_enumeration.addEnumeration(unicode_value='MiniDiscMaxiRemix', tag='MiniDiscMaxiRemix')
CarrierType.MiniDiscSingleMaxiSingle = CarrierType._CF_enumeration.addEnumeration(unicode_value='MiniDiscSingleMaxiSingle', tag='MiniDiscSingleMaxiSingle')
CarrierType.PrePaidCard = CarrierType._CF_enumeration.addEnumeration(unicode_value='PrePaidCard', tag='PrePaidCard')
CarrierType.SACD = CarrierType._CF_enumeration.addEnumeration(unicode_value='SACD', tag='SACD')
CarrierType.SacdCompilation = CarrierType._CF_enumeration.addEnumeration(unicode_value='SacdCompilation', tag='SacdCompilation')
CarrierType.SacdLpStereo = CarrierType._CF_enumeration.addEnumeration(unicode_value='SacdLpStereo', tag='SacdLpStereo')
CarrierType.SacdLpStereoCdAudio = CarrierType._CF_enumeration.addEnumeration(unicode_value='SacdLpStereoCdAudio', tag='SacdLpStereoCdAudio')
CarrierType.SacdLpStereoSurround = CarrierType._CF_enumeration.addEnumeration(unicode_value='SacdLpStereoSurround', tag='SacdLpStereoSurround')
CarrierType.SacdLpStereoSurroundCdAudio = CarrierType._CF_enumeration.addEnumeration(unicode_value='SacdLpStereoSurroundCdAudio', tag='SacdLpStereoSurroundCdAudio')
CarrierType.SacdLpSurroundCdAudio = CarrierType._CF_enumeration.addEnumeration(unicode_value='SacdLpSurroundCdAudio', tag='SacdLpSurroundCdAudio')
CarrierType.SacdPlusDvdVideo = CarrierType._CF_enumeration.addEnumeration(unicode_value='SacdPlusDvdVideo', tag='SacdPlusDvdVideo')
CarrierType.VhsNTSC = CarrierType._CF_enumeration.addEnumeration(unicode_value='VhsNTSC', tag='VhsNTSC')
CarrierType.VhsPAL = CarrierType._CF_enumeration.addEnumeration(unicode_value='VhsPAL', tag='VhsPAL')
CarrierType.VhsPlusCdLp = CarrierType._CF_enumeration.addEnumeration(unicode_value='VhsPlusCdLp', tag='VhsPlusCdLp')
CarrierType.VhsSECAM = CarrierType._CF_enumeration.addEnumeration(unicode_value='VhsSECAM', tag='VhsSECAM')
CarrierType._InitializeFacetMap(CarrierType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CarrierType', CarrierType)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}CodingType
class CodingType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of coding used to encode a Resource."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CodingType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 212, 4)
    _Documentation = 'A Type of coding used to encode a Resource.'
CodingType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CodingType, enum_prefix=None)
CodingType.Lossless = CodingType._CF_enumeration.addEnumeration(unicode_value='Lossless', tag='Lossless')
CodingType.Lossy = CodingType._CF_enumeration.addEnumeration(unicode_value='Lossy', tag='Lossy')
CodingType._InitializeFacetMap(CodingType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CodingType', CodingType)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}CollectionCollectionReference
class CollectionCollectionReference (pyxb.binding.datatypes.IDREF):

    """A Reference to a Collection which is contained within a specific Collection."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CollectionCollectionReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 221, 4)
    _Documentation = 'A Reference to a Collection which is contained within a specific Collection.'
CollectionCollectionReference._CF_pattern = pyxb.binding.facets.CF_pattern()
CollectionCollectionReference._CF_pattern.addPattern(pattern='X[\\d\\-_a-zA-Z]+')
CollectionCollectionReference._InitializeFacetMap(CollectionCollectionReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'CollectionCollectionReference', CollectionCollectionReference)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}CollectionReference
class CollectionReference (pyxb.binding.datatypes.ID):

    """A Reference to a Collection."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CollectionReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 229, 4)
    _Documentation = 'A Reference to a Collection.'
CollectionReference._CF_pattern = pyxb.binding.facets.CF_pattern()
CollectionReference._CF_pattern.addPattern(pattern='X[\\d\\-_a-zA-Z]+')
CollectionReference._InitializeFacetMap(CollectionReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'CollectionReference', CollectionReference)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}CollectionResourceReference
class CollectionResourceReference (pyxb.binding.datatypes.IDREF):

    """A Reference to a Resource which is contained within a specific Collection."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CollectionResourceReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 237, 4)
    _Documentation = 'A Reference to a Resource which is contained within a specific Collection.'
CollectionResourceReference._CF_pattern = pyxb.binding.facets.CF_pattern()
CollectionResourceReference._CF_pattern.addPattern(pattern='A[\\d\\-_a-zA-Z]+')
CollectionResourceReference._InitializeFacetMap(CollectionResourceReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'CollectionResourceReference', CollectionResourceReference)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}CollectionType
class CollectionType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Collection."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CollectionType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 245, 4)
    _Documentation = 'A Type of Collection.'
CollectionType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CollectionType, enum_prefix=None)
CollectionType.AudioChapter = CollectionType._CF_enumeration.addEnumeration(unicode_value='AudioChapter', tag='AudioChapter')
CollectionType.Episode = CollectionType._CF_enumeration.addEnumeration(unicode_value='Episode', tag='Episode')
CollectionType.Season = CollectionType._CF_enumeration.addEnumeration(unicode_value='Season', tag='Season')
CollectionType.Series = CollectionType._CF_enumeration.addEnumeration(unicode_value='Series', tag='Series')
CollectionType.VideoChapter = CollectionType._CF_enumeration.addEnumeration(unicode_value='VideoChapter', tag='VideoChapter')
CollectionType._InitializeFacetMap(CollectionType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CollectionType', CollectionType)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}CommercialModelType
class CommercialModelType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of CommercialModel (e.g. SubscriptionModel and PayAsYouGoModel). The CommercialModelType indicates how a Consumer pays for a Service or Release."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CommercialModelType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 257, 4)
    _Documentation = 'A Type of CommercialModel (e.g. SubscriptionModel and PayAsYouGoModel). The CommercialModelType indicates how a Consumer pays for a Service or Release.'
CommercialModelType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CommercialModelType, enum_prefix=None)
CommercialModelType.AdvertisementSupportedModel = CommercialModelType._CF_enumeration.addEnumeration(unicode_value='AdvertisementSupportedModel', tag='AdvertisementSupportedModel')
CommercialModelType.AsPerContract = CommercialModelType._CF_enumeration.addEnumeration(unicode_value='AsPerContract', tag='AsPerContract')
CommercialModelType.FreeOfChargeModel = CommercialModelType._CF_enumeration.addEnumeration(unicode_value='FreeOfChargeModel', tag='FreeOfChargeModel')
CommercialModelType.PayAsYouGoModel = CommercialModelType._CF_enumeration.addEnumeration(unicode_value='PayAsYouGoModel', tag='PayAsYouGoModel')
CommercialModelType.SubscriptionModel = CommercialModelType._CF_enumeration.addEnumeration(unicode_value='SubscriptionModel', tag='SubscriptionModel')
CommercialModelType.Unknown = CommercialModelType._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
CommercialModelType.UserDefined = CommercialModelType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
CommercialModelType._InitializeFacetMap(CommercialModelType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CommercialModelType', CommercialModelType)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}CreationType
class CreationType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Creation."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CreationType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 271, 4)
    _Documentation = 'A Type of Creation.'
CreationType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CreationType, enum_prefix=None)
CreationType.MusicalWork = CreationType._CF_enumeration.addEnumeration(unicode_value='MusicalWork', tag='MusicalWork')
CreationType.Release = CreationType._CF_enumeration.addEnumeration(unicode_value='Release', tag='Release')
CreationType.Resource = CreationType._CF_enumeration.addEnumeration(unicode_value='Resource', tag='Resource')
CreationType._InitializeFacetMap(CreationType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CreationType', CreationType)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}CueOrigin
class CueOrigin (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Cue according to its origin."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CueOrigin')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 281, 4)
    _Documentation = 'A Type of Cue according to its origin.'
CueOrigin._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CueOrigin, enum_prefix=None)
CueOrigin.LibraryMusic = CueOrigin._CF_enumeration.addEnumeration(unicode_value='LibraryMusic', tag='LibraryMusic')
CueOrigin.PreexistingMusic = CueOrigin._CF_enumeration.addEnumeration(unicode_value='PreexistingMusic', tag='PreexistingMusic')
CueOrigin.SpeciallyCommissionedMusic = CueOrigin._CF_enumeration.addEnumeration(unicode_value='SpeciallyCommissionedMusic', tag='SpeciallyCommissionedMusic')
CueOrigin.Unknown = CueOrigin._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
CueOrigin.UserDefined = CueOrigin._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
CueOrigin._InitializeFacetMap(CueOrigin._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CueOrigin', CueOrigin)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}CueResourceReference
class CueResourceReference (pyxb.binding.datatypes.IDREF):

    """A Reference to a Resource which is contained within a specific Cue."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CueResourceReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 293, 4)
    _Documentation = 'A Reference to a Resource which is contained within a specific Cue.'
CueResourceReference._CF_pattern = pyxb.binding.facets.CF_pattern()
CueResourceReference._CF_pattern.addPattern(pattern='A[\\d\\-_a-zA-Z]+')
CueResourceReference._InitializeFacetMap(CueResourceReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'CueResourceReference', CueResourceReference)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}CueSheetReference
class CueSheetReference (pyxb.binding.datatypes.ID):

    """A Reference to a CueSheet."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CueSheetReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 301, 4)
    _Documentation = 'A Reference to a CueSheet.'
CueSheetReference._CF_pattern = pyxb.binding.facets.CF_pattern()
CueSheetReference._CF_pattern.addPattern(pattern='Q[\\d\\-_a-zA-Z]+')
CueSheetReference._InitializeFacetMap(CueSheetReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'CueSheetReference', CueSheetReference)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}CueSheetType
class CueSheetType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of CueSheet."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CueSheetType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 309, 4)
    _Documentation = 'A Type of CueSheet.'
CueSheetType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CueSheetType, enum_prefix=None)
CueSheetType.AverageCueSheet = CueSheetType._CF_enumeration.addEnumeration(unicode_value='AverageCueSheet', tag='AverageCueSheet')
CueSheetType.CompositeCueSheet = CueSheetType._CF_enumeration.addEnumeration(unicode_value='CompositeCueSheet', tag='CompositeCueSheet')
CueSheetType.StandardCueSheet = CueSheetType._CF_enumeration.addEnumeration(unicode_value='StandardCueSheet', tag='StandardCueSheet')
CueSheetType.SummarisedCueSheet = CueSheetType._CF_enumeration.addEnumeration(unicode_value='SummarisedCueSheet', tag='SummarisedCueSheet')
CueSheetType.SurrogateCueSheet = CueSheetType._CF_enumeration.addEnumeration(unicode_value='SurrogateCueSheet', tag='SurrogateCueSheet')
CueSheetType._InitializeFacetMap(CueSheetType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CueSheetType', CueSheetType)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}CueUseType
class CueUseType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of use of a Cue."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CueUseType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 321, 4)
    _Documentation = 'A Type of use of a Cue.'
CueUseType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CueUseType, enum_prefix=None)
CueUseType.AudioLogo = CueUseType._CF_enumeration.addEnumeration(unicode_value='AudioLogo', tag='AudioLogo')
CueUseType.Background = CueUseType._CF_enumeration.addEnumeration(unicode_value='Background', tag='Background')
CueUseType.Bumper = CueUseType._CF_enumeration.addEnumeration(unicode_value='Bumper', tag='Bumper')
CueUseType.EssentialPart = CueUseType._CF_enumeration.addEnumeration(unicode_value='EssentialPart', tag='EssentialPart')
CueUseType.FilmTheme = CueUseType._CF_enumeration.addEnumeration(unicode_value='FilmTheme', tag='FilmTheme')
CueUseType.IndistinguishableBackground = CueUseType._CF_enumeration.addEnumeration(unicode_value='IndistinguishableBackground', tag='IndistinguishableBackground')
CueUseType.OnScreenMusic = CueUseType._CF_enumeration.addEnumeration(unicode_value='OnScreenMusic', tag='OnScreenMusic')
CueUseType.RolledUpCue = CueUseType._CF_enumeration.addEnumeration(unicode_value='RolledUpCue', tag='RolledUpCue')
CueUseType.Theme = CueUseType._CF_enumeration.addEnumeration(unicode_value='Theme', tag='Theme')
CueUseType.UserDefined = CueUseType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
CueUseType._InitializeFacetMap(CueUseType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CueUseType', CueUseType)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}CueWorkReference
class CueWorkReference (pyxb.binding.datatypes.IDREF):

    """A Reference to a Work which is contained within a specific Cue."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CueWorkReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 338, 4)
    _Documentation = 'A Reference to a Work which is contained within a specific Cue.'
CueWorkReference._CF_pattern = pyxb.binding.facets.CF_pattern()
CueWorkReference._CF_pattern.addPattern(pattern='W[\\d\\-_a-zA-Z]+')
CueWorkReference._InitializeFacetMap(CueWorkReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'CueWorkReference', CueWorkReference)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}DataMismatchResponseType
class DataMismatchResponseType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of action that is a response to a DataMismatch."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DataMismatchResponseType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 346, 4)
    _Documentation = 'A Type of action that is a response to a DataMismatch.'
DataMismatchResponseType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DataMismatchResponseType, enum_prefix=None)
DataMismatchResponseType.AdditionalInformationOnly = DataMismatchResponseType._CF_enumeration.addEnumeration(unicode_value='AdditionalInformationOnly', tag='AdditionalInformationOnly')
DataMismatchResponseType.DataMismatchConfirmation = DataMismatchResponseType._CF_enumeration.addEnumeration(unicode_value='DataMismatchConfirmation', tag='DataMismatchConfirmation')
DataMismatchResponseType.DataMismatchOutOfScope = DataMismatchResponseType._CF_enumeration.addEnumeration(unicode_value='DataMismatchOutOfScope', tag='DataMismatchOutOfScope')
DataMismatchResponseType.DataMismatchRaisedCommercialDispute = DataMismatchResponseType._CF_enumeration.addEnumeration(unicode_value='DataMismatchRaisedCommercialDispute', tag='DataMismatchRaisedCommercialDispute')
DataMismatchResponseType.NoReaction = DataMismatchResponseType._CF_enumeration.addEnumeration(unicode_value='NoReaction', tag='NoReaction')
DataMismatchResponseType.UserDefined = DataMismatchResponseType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
DataMismatchResponseType._InitializeFacetMap(DataMismatchResponseType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DataMismatchResponseType', DataMismatchResponseType)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}DataMismatchStatus
class DataMismatchStatus (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A status of a DataMismatch."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DataMismatchStatus')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 359, 4)
    _Documentation = 'A status of a DataMismatch.'
DataMismatchStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DataMismatchStatus, enum_prefix=None)
DataMismatchStatus.AdditionalInformationOnly = DataMismatchStatus._CF_enumeration.addEnumeration(unicode_value='AdditionalInformationOnly', tag='AdditionalInformationOnly')
DataMismatchStatus.Corrected = DataMismatchStatus._CF_enumeration.addEnumeration(unicode_value='Corrected', tag='Corrected')
DataMismatchStatus.Fatal = DataMismatchStatus._CF_enumeration.addEnumeration(unicode_value='Fatal', tag='Fatal')
DataMismatchStatus.NotCorrected = DataMismatchStatus._CF_enumeration.addEnumeration(unicode_value='NotCorrected', tag='NotCorrected')
DataMismatchStatus.UserDefined = DataMismatchStatus._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
DataMismatchStatus._InitializeFacetMap(DataMismatchStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DataMismatchStatus', DataMismatchStatus)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}DataMismatchType
class DataMismatchType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of DataMismatch."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DataMismatchType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 371, 4)
    _Documentation = 'A Type of DataMismatch.'
DataMismatchType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DataMismatchType, enum_prefix=None)
DataMismatchType.AdditionalInformationOnly = DataMismatchType._CF_enumeration.addEnumeration(unicode_value='AdditionalInformationOnly', tag='AdditionalInformationOnly')
DataMismatchType.ChoreographyConflict = DataMismatchType._CF_enumeration.addEnumeration(unicode_value='ChoreographyConflict', tag='ChoreographyConflict')
DataMismatchType.ContradictoryData = DataMismatchType._CF_enumeration.addEnumeration(unicode_value='ContradictoryData', tag='ContradictoryData')
DataMismatchType.DuplicatedData = DataMismatchType._CF_enumeration.addEnumeration(unicode_value='DuplicatedData', tag='DuplicatedData')
DataMismatchType.IdentifierSyntaxMismatch = DataMismatchType._CF_enumeration.addEnumeration(unicode_value='IdentifierSyntaxMismatch', tag='IdentifierSyntaxMismatch')
DataMismatchType.MathematicalInconsistency = DataMismatchType._CF_enumeration.addEnumeration(unicode_value='MathematicalInconsistency', tag='MathematicalInconsistency')
DataMismatchType.MissingContractuallyMandatoryInformation = DataMismatchType._CF_enumeration.addEnumeration(unicode_value='MissingContractuallyMandatoryInformation', tag='MissingContractuallyMandatoryInformation')
DataMismatchType.MissingMandatoryInformation = DataMismatchType._CF_enumeration.addEnumeration(unicode_value='MissingMandatoryInformation', tag='MissingMandatoryInformation')
DataMismatchType.MissingReferencedMusicalWorkInformation = DataMismatchType._CF_enumeration.addEnumeration(unicode_value='MissingReferencedMusicalWorkInformation', tag='MissingReferencedMusicalWorkInformation')
DataMismatchType.MissingReferencedReleaseInformation = DataMismatchType._CF_enumeration.addEnumeration(unicode_value='MissingReferencedReleaseInformation', tag='MissingReferencedReleaseInformation')
DataMismatchType.MissingReferencedResourceInformation = DataMismatchType._CF_enumeration.addEnumeration(unicode_value='MissingReferencedResourceInformation', tag='MissingReferencedResourceInformation')
DataMismatchType.MissingReferencedTechnicalResourceDetailInformation = DataMismatchType._CF_enumeration.addEnumeration(unicode_value='MissingReferencedTechnicalResourceDetailInformation', tag='MissingReferencedTechnicalResourceDetailInformation')
DataMismatchType.MissingResourceFile = DataMismatchType._CF_enumeration.addEnumeration(unicode_value='MissingResourceFile', tag='MissingResourceFile')
DataMismatchType.TypographicMismatch = DataMismatchType._CF_enumeration.addEnumeration(unicode_value='TypographicMismatch', tag='TypographicMismatch')
DataMismatchType.UnexpectedAllowedValue = DataMismatchType._CF_enumeration.addEnumeration(unicode_value='UnexpectedAllowedValue', tag='UnexpectedAllowedValue')
DataMismatchType.UnexpectedMessageIntermediary = DataMismatchType._CF_enumeration.addEnumeration(unicode_value='UnexpectedMessageIntermediary', tag='UnexpectedMessageIntermediary')
DataMismatchType.UnexpectedMessageRecipient = DataMismatchType._CF_enumeration.addEnumeration(unicode_value='UnexpectedMessageRecipient', tag='UnexpectedMessageRecipient')
DataMismatchType.UnexpectedMessageSender = DataMismatchType._CF_enumeration.addEnumeration(unicode_value='UnexpectedMessageSender', tag='UnexpectedMessageSender')
DataMismatchType.UserDefined = DataMismatchType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
DataMismatchType.XmlFormatError = DataMismatchType._CF_enumeration.addEnumeration(unicode_value='XmlFormatError', tag='XmlFormatError')
DataMismatchType.XmlRangeError = DataMismatchType._CF_enumeration.addEnumeration(unicode_value='XmlRangeError', tag='XmlRangeError')
DataMismatchType._InitializeFacetMap(DataMismatchType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DataMismatchType', DataMismatchType)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}DdexPartyId
class DdexPartyId (pyxb.binding.datatypes.string):

    """An Identifier of a Party according to the DdexPartyId standard DDEX-DPID."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DdexPartyId')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 399, 4)
    _Documentation = 'An Identifier of a Party according to the DdexPartyId standard DDEX-DPID.'
DdexPartyId._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'DdexPartyId', DdexPartyId)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}DealReleaseReference
class DealReleaseReference (pyxb.binding.datatypes.IDREF):

    """A Reference to a Release which is included in a specific Deal."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DealReleaseReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 405, 4)
    _Documentation = 'A Reference to a Release which is included in a specific Deal.'
DealReleaseReference._CF_pattern = pyxb.binding.facets.CF_pattern()
DealReleaseReference._CF_pattern.addPattern(pattern='R[\\d\\-_a-zA-Z]+')
DealReleaseReference._InitializeFacetMap(DealReleaseReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'DealReleaseReference', DealReleaseReference)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}DealResourceReference
class DealResourceReference (pyxb.binding.datatypes.IDREF):

    """A Reference to a Resource which is contained within a specific Deal."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DealResourceReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 413, 4)
    _Documentation = 'A Reference to a Resource which is contained within a specific Deal.'
DealResourceReference._CF_pattern = pyxb.binding.facets.CF_pattern()
DealResourceReference._CF_pattern.addPattern(pattern='A[\\d\\-_a-zA-Z]+')
DealResourceReference._InitializeFacetMap(DealResourceReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'DealResourceReference', DealResourceReference)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}DealTechnicalResourceDetailsReference
class DealTechnicalResourceDetailsReference (pyxb.binding.datatypes.IDREF):

    """A Reference to a Resource which is contained within a specific Deal."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DealTechnicalResourceDetailsReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 421, 4)
    _Documentation = 'A Reference to a Resource which is contained within a specific Deal.'
DealTechnicalResourceDetailsReference._CF_pattern = pyxb.binding.facets.CF_pattern()
DealTechnicalResourceDetailsReference._CF_pattern.addPattern(pattern='T[\\d\\-_a-zA-Z]+')
DealTechnicalResourceDetailsReference._InitializeFacetMap(DealTechnicalResourceDetailsReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'DealTechnicalResourceDetailsReference', DealTechnicalResourceDetailsReference)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}DeclinationConditionReference
class DeclinationConditionReference (pyxb.binding.datatypes.IDREF):

    """A Reference to a LicenseOrClaimCondition which is contained within a specific declination."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DeclinationConditionReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 429, 4)
    _Documentation = 'A Reference to a LicenseOrClaimCondition which is contained within a specific declination.'
DeclinationConditionReference._CF_pattern = pyxb.binding.facets.CF_pattern()
DeclinationConditionReference._CF_pattern.addPattern(pattern='E[\\d\\-_a-zA-Z]+')
DeclinationConditionReference._InitializeFacetMap(DeclinationConditionReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'DeclinationConditionReference', DeclinationConditionReference)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}DeclinationReleaseReference
class DeclinationReleaseReference (pyxb.binding.datatypes.IDREF):

    """A Reference to a Release which is contained within a specific declination."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DeclinationReleaseReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 437, 4)
    _Documentation = 'A Reference to a Release which is contained within a specific declination.'
DeclinationReleaseReference._CF_pattern = pyxb.binding.facets.CF_pattern()
DeclinationReleaseReference._CF_pattern.addPattern(pattern='A[\\d\\-_a-zA-Z]+')
DeclinationReleaseReference._InitializeFacetMap(DeclinationReleaseReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'DeclinationReleaseReference', DeclinationReleaseReference)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}DeclinationResourceReference
class DeclinationResourceReference (pyxb.binding.datatypes.IDREF):

    """A Reference to a Resource which is contained within a specific declination."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DeclinationResourceReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 445, 4)
    _Documentation = 'A Reference to a Resource which is contained within a specific declination.'
DeclinationResourceReference._CF_pattern = pyxb.binding.facets.CF_pattern()
DeclinationResourceReference._CF_pattern.addPattern(pattern='A[\\d\\-_a-zA-Z]+')
DeclinationResourceReference._InitializeFacetMap(DeclinationResourceReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'DeclinationResourceReference', DeclinationResourceReference)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}DeclinationRightShareReference
class DeclinationRightShareReference (pyxb.binding.datatypes.IDREF):

    """A Reference to a RightShare which is contained within a specific declination."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DeclinationRightShareReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 453, 4)
    _Documentation = 'A Reference to a RightShare which is contained within a specific declination.'
DeclinationRightShareReference._CF_pattern = pyxb.binding.facets.CF_pattern()
DeclinationRightShareReference._CF_pattern.addPattern(pattern='S[\\d\\-_a-zA-Z]+')
DeclinationRightShareReference._InitializeFacetMap(DeclinationRightShareReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'DeclinationRightShareReference', DeclinationRightShareReference)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}DeclinationWorkReference
class DeclinationWorkReference (pyxb.binding.datatypes.IDREF):

    """A Reference to a Work which is contained within a specific declination."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DeclinationWorkReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 461, 4)
    _Documentation = 'A Reference to a Work which is contained within a specific declination.'
DeclinationWorkReference._CF_pattern = pyxb.binding.facets.CF_pattern()
DeclinationWorkReference._CF_pattern.addPattern(pattern='W[\\d\\-_a-zA-Z]+')
DeclinationWorkReference._InitializeFacetMap(DeclinationWorkReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'DeclinationWorkReference', DeclinationWorkReference)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}DeductionRateType
class DeductionRateType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of DeductionRate."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DeductionRateType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 469, 4)
    _Documentation = 'A Type of DeductionRate.'
DeductionRateType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DeductionRateType, enum_prefix=None)
DeductionRateType.PennyRate = DeductionRateType._CF_enumeration.addEnumeration(unicode_value='PennyRate', tag='PennyRate')
DeductionRateType.PercentageRate = DeductionRateType._CF_enumeration.addEnumeration(unicode_value='PercentageRate', tag='PercentageRate')
DeductionRateType.UserDefined = DeductionRateType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
DeductionRateType._InitializeFacetMap(DeductionRateType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DeductionRateType', DeductionRateType)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}DescriptorSyntax
class DescriptorSyntax (pyxb.binding.datatypes.string):

    """A Type of a Descriptor according to how it is defined syntactically."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DescriptorSyntax')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 479, 4)
    _Documentation = 'A Type of a Descriptor according to how it is defined syntactically.'
DescriptorSyntax._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'DescriptorSyntax', DescriptorSyntax)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}DistributionChannelType
class DistributionChannelType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of DistributionChannel used to disseminate a Service or Release to a Consumer."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DistributionChannelType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 485, 4)
    _Documentation = 'A Type of DistributionChannel used to disseminate a Service or Release to a Consumer.'
DistributionChannelType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DistributionChannelType, enum_prefix=None)
DistributionChannelType.AsPerContract = DistributionChannelType._CF_enumeration.addEnumeration(unicode_value='AsPerContract', tag='AsPerContract')
DistributionChannelType.Cable = DistributionChannelType._CF_enumeration.addEnumeration(unicode_value='Cable', tag='Cable')
DistributionChannelType.Internet = DistributionChannelType._CF_enumeration.addEnumeration(unicode_value='Internet', tag='Internet')
DistributionChannelType.InternetAndMobile = DistributionChannelType._CF_enumeration.addEnumeration(unicode_value='InternetAndMobile', tag='InternetAndMobile')
DistributionChannelType.IPTV = DistributionChannelType._CF_enumeration.addEnumeration(unicode_value='IPTV', tag='IPTV')
DistributionChannelType.MobileTelephone = DistributionChannelType._CF_enumeration.addEnumeration(unicode_value='MobileTelephone', tag='MobileTelephone')
DistributionChannelType.OnDemandStream = DistributionChannelType._CF_enumeration.addEnumeration(unicode_value='OnDemandStream', tag='OnDemandStream')
DistributionChannelType.PeerToPeer = DistributionChannelType._CF_enumeration.addEnumeration(unicode_value='PeerToPeer', tag='PeerToPeer')
DistributionChannelType.Physical = DistributionChannelType._CF_enumeration.addEnumeration(unicode_value='Physical', tag='Physical')
DistributionChannelType.Satellite = DistributionChannelType._CF_enumeration.addEnumeration(unicode_value='Satellite', tag='Satellite')
DistributionChannelType.Unknown = DistributionChannelType._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
DistributionChannelType.UserDefined = DistributionChannelType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
DistributionChannelType._InitializeFacetMap(DistributionChannelType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DistributionChannelType', DistributionChannelType)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}DrmEnforcementType
class DrmEnforcementType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of DRM enforcement."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DrmEnforcementType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 504, 4)
    _Documentation = 'A Type of DRM enforcement.'
DrmEnforcementType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DrmEnforcementType, enum_prefix=None)
DrmEnforcementType.DrmEnforced = DrmEnforcementType._CF_enumeration.addEnumeration(unicode_value='DrmEnforced', tag='DrmEnforced')
DrmEnforcementType.NotDrmEnforced = DrmEnforcementType._CF_enumeration.addEnumeration(unicode_value='NotDrmEnforced', tag='NotDrmEnforced')
DrmEnforcementType._InitializeFacetMap(DrmEnforcementType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DrmEnforcementType', DrmEnforcementType)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}DrmPlatformType
class DrmPlatformType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of DrmPlatform."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DrmPlatformType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 513, 4)
    _Documentation = 'A Type of DrmPlatform.'
DrmPlatformType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DrmPlatformType, enum_prefix=None)
DrmPlatformType.n3Day = DrmPlatformType._CF_enumeration.addEnumeration(unicode_value='3Day', tag='n3Day')
DrmPlatformType.Fairplay = DrmPlatformType._CF_enumeration.addEnumeration(unicode_value='Fairplay', tag='Fairplay')
DrmPlatformType.OMA = DrmPlatformType._CF_enumeration.addEnumeration(unicode_value='OMA', tag='OMA')
DrmPlatformType.Unknown = DrmPlatformType._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
DrmPlatformType.UserDefined = DrmPlatformType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
DrmPlatformType.WindowsMediaDRM = DrmPlatformType._CF_enumeration.addEnumeration(unicode_value='WindowsMediaDRM', tag='WindowsMediaDRM')
DrmPlatformType._InitializeFacetMap(DrmPlatformType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DrmPlatformType', DrmPlatformType)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}ExpressionType
class ExpressionType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of expression indicating how it should be perceived."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ExpressionType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 526, 4)
    _Documentation = 'A Type of expression indicating how it should be perceived.'
ExpressionType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ExpressionType, enum_prefix=None)
ExpressionType.Informative = ExpressionType._CF_enumeration.addEnumeration(unicode_value='Informative', tag='Informative')
ExpressionType.Instructive = ExpressionType._CF_enumeration.addEnumeration(unicode_value='Instructive', tag='Instructive')
ExpressionType._InitializeFacetMap(ExpressionType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ExpressionType', ExpressionType)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}ExternallyLinkedResourceType
class ExternallyLinkedResourceType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Resource pointed to by an ExternalLink."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ExternallyLinkedResourceType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 535, 4)
    _Documentation = 'A Type of Resource pointed to by an ExternalLink.'
ExternallyLinkedResourceType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ExternallyLinkedResourceType, enum_prefix=None)
ExternallyLinkedResourceType.AdditionalMetadata = ExternallyLinkedResourceType._CF_enumeration.addEnumeration(unicode_value='AdditionalMetadata', tag='AdditionalMetadata')
ExternallyLinkedResourceType.Logo = ExternallyLinkedResourceType._CF_enumeration.addEnumeration(unicode_value='Logo', tag='Logo')
ExternallyLinkedResourceType.PromotionalImage = ExternallyLinkedResourceType._CF_enumeration.addEnumeration(unicode_value='PromotionalImage', tag='PromotionalImage')
ExternallyLinkedResourceType.PromotionalInformation = ExternallyLinkedResourceType._CF_enumeration.addEnumeration(unicode_value='PromotionalInformation', tag='PromotionalInformation')
ExternallyLinkedResourceType.PromotionalItem = ExternallyLinkedResourceType._CF_enumeration.addEnumeration(unicode_value='PromotionalItem', tag='PromotionalItem')
ExternallyLinkedResourceType.Unknown = ExternallyLinkedResourceType._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
ExternallyLinkedResourceType.UserDefined = ExternallyLinkedResourceType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
ExternallyLinkedResourceType._InitializeFacetMap(ExternallyLinkedResourceType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ExternallyLinkedResourceType', ExternallyLinkedResourceType)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}FileStatus
class FileStatus (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A status of a File in terms of its validity."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FileStatus')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 549, 4)
    _Documentation = 'A status of a File in terms of its validity.'
FileStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=FileStatus, enum_prefix=None)
FileStatus.FileMissing = FileStatus._CF_enumeration.addEnumeration(unicode_value='FileMissing', tag='FileMissing')
FileStatus.FileOK = FileStatus._CF_enumeration.addEnumeration(unicode_value='FileOK', tag='FileOK')
FileStatus.HashSumWrong = FileStatus._CF_enumeration.addEnumeration(unicode_value='HashSumWrong', tag='HashSumWrong')
FileStatus.SignatureWrong = FileStatus._CF_enumeration.addEnumeration(unicode_value='SignatureWrong', tag='SignatureWrong')
FileStatus._InitializeFacetMap(FileStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'FileStatus', FileStatus)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}HashSum
class HashSum (pyxb.binding.datatypes.string):

    """A value calculated from digital data that serves to distinguish it from other digital data."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'HashSum')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 560, 4)
    _Documentation = 'A value calculated from digital data that serves to distinguish it from other digital data.'
HashSum._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'HashSum', HashSum)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}HashSumAlgorithmType
class HashSumAlgorithmType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of HashSumAlgorithm."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'HashSumAlgorithmType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 566, 4)
    _Documentation = 'A Type of HashSumAlgorithm.'
HashSumAlgorithmType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=HashSumAlgorithmType, enum_prefix=None)
HashSumAlgorithmType.MD4 = HashSumAlgorithmType._CF_enumeration.addEnumeration(unicode_value='MD4', tag='MD4')
HashSumAlgorithmType.MD5 = HashSumAlgorithmType._CF_enumeration.addEnumeration(unicode_value='MD5', tag='MD5')
HashSumAlgorithmType.SHA = HashSumAlgorithmType._CF_enumeration.addEnumeration(unicode_value='SHA', tag='SHA')
HashSumAlgorithmType.SHA1 = HashSumAlgorithmType._CF_enumeration.addEnumeration(unicode_value='SHA1', tag='SHA1')
HashSumAlgorithmType.UserDefined = HashSumAlgorithmType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
HashSumAlgorithmType._InitializeFacetMap(HashSumAlgorithmType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'HashSumAlgorithmType', HashSumAlgorithmType)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}ImageCodecType
class ImageCodecType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of ImageCodec."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ImageCodecType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 578, 4)
    _Documentation = 'A Type of ImageCodec.'
ImageCodecType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ImageCodecType, enum_prefix=None)
ImageCodecType.GIF = ImageCodecType._CF_enumeration.addEnumeration(unicode_value='GIF', tag='GIF')
ImageCodecType.JPEG = ImageCodecType._CF_enumeration.addEnumeration(unicode_value='JPEG', tag='JPEG')
ImageCodecType.JPEG2000 = ImageCodecType._CF_enumeration.addEnumeration(unicode_value='JPEG2000', tag='JPEG2000')
ImageCodecType.PNG = ImageCodecType._CF_enumeration.addEnumeration(unicode_value='PNG', tag='PNG')
ImageCodecType.TIFF = ImageCodecType._CF_enumeration.addEnumeration(unicode_value='TIFF', tag='TIFF')
ImageCodecType.Unknown = ImageCodecType._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
ImageCodecType.UserDefined = ImageCodecType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
ImageCodecType._InitializeFacetMap(ImageCodecType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ImageCodecType', ImageCodecType)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}ImageType
class ImageType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Image."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ImageType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 592, 4)
    _Documentation = 'A Type of Image.'
ImageType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ImageType, enum_prefix=None)
ImageType.BackCoverImage = ImageType._CF_enumeration.addEnumeration(unicode_value='BackCoverImage', tag='BackCoverImage')
ImageType.BookletBackImage = ImageType._CF_enumeration.addEnumeration(unicode_value='BookletBackImage', tag='BookletBackImage')
ImageType.BookletFrontImage = ImageType._CF_enumeration.addEnumeration(unicode_value='BookletFrontImage', tag='BookletFrontImage')
ImageType.DocumentImage = ImageType._CF_enumeration.addEnumeration(unicode_value='DocumentImage', tag='DocumentImage')
ImageType.FrontCoverImage = ImageType._CF_enumeration.addEnumeration(unicode_value='FrontCoverImage', tag='FrontCoverImage')
ImageType.Icon = ImageType._CF_enumeration.addEnumeration(unicode_value='Icon', tag='Icon')
ImageType.Logo = ImageType._CF_enumeration.addEnumeration(unicode_value='Logo', tag='Logo')
ImageType.Photograph = ImageType._CF_enumeration.addEnumeration(unicode_value='Photograph', tag='Photograph')
ImageType.Poster = ImageType._CF_enumeration.addEnumeration(unicode_value='Poster', tag='Poster')
ImageType.TrayImage = ImageType._CF_enumeration.addEnumeration(unicode_value='TrayImage', tag='TrayImage')
ImageType.Unknown = ImageType._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
ImageType.UserDefined = ImageType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
ImageType.VideoScreenCapture = ImageType._CF_enumeration.addEnumeration(unicode_value='VideoScreenCapture', tag='VideoScreenCapture')
ImageType.Wallpaper = ImageType._CF_enumeration.addEnumeration(unicode_value='Wallpaper', tag='Wallpaper')
ImageType._InitializeFacetMap(ImageType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ImageType', ImageType)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}InvoiceSupportInformationLicenseOrClaimReference
class InvoiceSupportInformationLicenseOrClaimReference (pyxb.binding.datatypes.IDREF):

    """A Reference to a License or Claim which is contained within a specific InvoiceSupportInformation."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InvoiceSupportInformationLicenseOrClaimReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 613, 4)
    _Documentation = 'A Reference to a License or Claim which is contained within a specific InvoiceSupportInformation.'
InvoiceSupportInformationLicenseOrClaimReference._CF_pattern = pyxb.binding.facets.CF_pattern()
InvoiceSupportInformationLicenseOrClaimReference._CF_pattern.addPattern(pattern='L[\\d\\-_a-zA-Z]+')
InvoiceSupportInformationLicenseOrClaimReference._InitializeFacetMap(InvoiceSupportInformationLicenseOrClaimReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'InvoiceSupportInformationLicenseOrClaimReference', InvoiceSupportInformationLicenseOrClaimReference)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}LicenseOrClaimConditionReference
class LicenseOrClaimConditionReference (pyxb.binding.datatypes.ID):

    """A Reference to a LicenseOrClaimCondition."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LicenseOrClaimConditionReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 621, 4)
    _Documentation = 'A Reference to a LicenseOrClaimCondition.'
LicenseOrClaimConditionReference._CF_pattern = pyxb.binding.facets.CF_pattern()
LicenseOrClaimConditionReference._CF_pattern.addPattern(pattern='E[\\d\\-_a-zA-Z]+')
LicenseOrClaimConditionReference._InitializeFacetMap(LicenseOrClaimConditionReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'LicenseOrClaimConditionReference', LicenseOrClaimConditionReference)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}LicenseOrClaimReference
class LicenseOrClaimReference (pyxb.binding.datatypes.ID):

    """A Reference to a LicenseOrClaim."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LicenseOrClaimReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 629, 4)
    _Documentation = 'A Reference to a LicenseOrClaim.'
LicenseOrClaimReference._CF_pattern = pyxb.binding.facets.CF_pattern()
LicenseOrClaimReference._CF_pattern.addPattern(pattern='L[\\d\\-_a-zA-Z]+')
LicenseOrClaimReference._InitializeFacetMap(LicenseOrClaimReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'LicenseOrClaimReference', LicenseOrClaimReference)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}LicenseOrClaimReferenceToLicenseOrClaimCondition
class LicenseOrClaimReferenceToLicenseOrClaimCondition (pyxb.binding.datatypes.IDREF):

    """A Reference to a LicenseOrClaimCondition which is contained within a specific License or Claim."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LicenseOrClaimReferenceToLicenseOrClaimCondition')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 637, 4)
    _Documentation = 'A Reference to a LicenseOrClaimCondition which is contained within a specific License or Claim.'
LicenseOrClaimReferenceToLicenseOrClaimCondition._CF_pattern = pyxb.binding.facets.CF_pattern()
LicenseOrClaimReferenceToLicenseOrClaimCondition._CF_pattern.addPattern(pattern='E[\\d\\-_a-zA-Z]+')
LicenseOrClaimReferenceToLicenseOrClaimCondition._InitializeFacetMap(LicenseOrClaimReferenceToLicenseOrClaimCondition._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'LicenseOrClaimReferenceToLicenseOrClaimCondition', LicenseOrClaimReferenceToLicenseOrClaimCondition)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}LicenseOrClaimRefusalReason
class LicenseOrClaimRefusalReason (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of reason for a refusing a License or Claim."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LicenseOrClaimRefusalReason')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 645, 4)
    _Documentation = 'A Type of reason for a refusing a License or Claim.'
LicenseOrClaimRefusalReason._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=LicenseOrClaimRefusalReason, enum_prefix=None)
LicenseOrClaimRefusalReason.AgreementOfAdditionalProvisionsRequired = LicenseOrClaimRefusalReason._CF_enumeration.addEnumeration(unicode_value='AgreementOfAdditionalProvisionsRequired', tag='AgreementOfAdditionalProvisionsRequired')
LicenseOrClaimRefusalReason.CorrectionOfAdvancePaymentRequired = LicenseOrClaimRefusalReason._CF_enumeration.addEnumeration(unicode_value='CorrectionOfAdvancePaymentRequired', tag='CorrectionOfAdvancePaymentRequired')
LicenseOrClaimRefusalReason.CorrectionOfGuaranteeRequired = LicenseOrClaimRefusalReason._CF_enumeration.addEnumeration(unicode_value='CorrectionOfGuaranteeRequired', tag='CorrectionOfGuaranteeRequired')
LicenseOrClaimRefusalReason.CorrectionOfLicenseeRequired = LicenseOrClaimRefusalReason._CF_enumeration.addEnumeration(unicode_value='CorrectionOfLicenseeRequired', tag='CorrectionOfLicenseeRequired')
LicenseOrClaimRefusalReason.CorrectionOfMostFavoredNationClauseRequired = LicenseOrClaimRefusalReason._CF_enumeration.addEnumeration(unicode_value='CorrectionOfMostFavoredNationClauseRequired', tag='CorrectionOfMostFavoredNationClauseRequired')
LicenseOrClaimRefusalReason.CorrectionOfNumberOfResourcesRequired = LicenseOrClaimRefusalReason._CF_enumeration.addEnumeration(unicode_value='CorrectionOfNumberOfResourcesRequired', tag='CorrectionOfNumberOfResourcesRequired')
LicenseOrClaimRefusalReason.CorrectionOfPlayingTimeRequired = LicenseOrClaimRefusalReason._CF_enumeration.addEnumeration(unicode_value='CorrectionOfPlayingTimeRequired', tag='CorrectionOfPlayingTimeRequired')
LicenseOrClaimRefusalReason.CorrectionOfPublisherInformationRequired = LicenseOrClaimRefusalReason._CF_enumeration.addEnumeration(unicode_value='CorrectionOfPublisherInformationRequired', tag='CorrectionOfPublisherInformationRequired')
LicenseOrClaimRefusalReason.CorrectionOfPublisherPercentageRequired = LicenseOrClaimRefusalReason._CF_enumeration.addEnumeration(unicode_value='CorrectionOfPublisherPercentageRequired', tag='CorrectionOfPublisherPercentageRequired')
LicenseOrClaimRefusalReason.CorrectionOfRateRequired = LicenseOrClaimRefusalReason._CF_enumeration.addEnumeration(unicode_value='CorrectionOfRateRequired', tag='CorrectionOfRateRequired')
LicenseOrClaimRefusalReason.CorrectionOfReleaseCreatorInformationRequired = LicenseOrClaimRefusalReason._CF_enumeration.addEnumeration(unicode_value='CorrectionOfReleaseCreatorInformationRequired', tag='CorrectionOfReleaseCreatorInformationRequired')
LicenseOrClaimRefusalReason.CorrectionOfReleaseDateRequired = LicenseOrClaimRefusalReason._CF_enumeration.addEnumeration(unicode_value='CorrectionOfReleaseDateRequired', tag='CorrectionOfReleaseDateRequired')
LicenseOrClaimRefusalReason.CorrectionOfReleaseTitleRequired = LicenseOrClaimRefusalReason._CF_enumeration.addEnumeration(unicode_value='CorrectionOfReleaseTitleRequired', tag='CorrectionOfReleaseTitleRequired')
LicenseOrClaimRefusalReason.CorrectionOfWorkContributorRequired = LicenseOrClaimRefusalReason._CF_enumeration.addEnumeration(unicode_value='CorrectionOfWorkContributorRequired', tag='CorrectionOfWorkContributorRequired')
LicenseOrClaimRefusalReason.CorrectionOfWorkTitleRequired = LicenseOrClaimRefusalReason._CF_enumeration.addEnumeration(unicode_value='CorrectionOfWorkTitleRequired', tag='CorrectionOfWorkTitleRequired')
LicenseOrClaimRefusalReason.DealExpired = LicenseOrClaimRefusalReason._CF_enumeration.addEnumeration(unicode_value='DealExpired', tag='DealExpired')
LicenseOrClaimRefusalReason.DifferentWork = LicenseOrClaimRefusalReason._CF_enumeration.addEnumeration(unicode_value='DifferentWork', tag='DifferentWork')
LicenseOrClaimRefusalReason.DirectLicense = LicenseOrClaimRefusalReason._CF_enumeration.addEnumeration(unicode_value='DirectLicense', tag='DirectLicense')
LicenseOrClaimRefusalReason.DuplicateLicense = LicenseOrClaimRefusalReason._CF_enumeration.addEnumeration(unicode_value='DuplicateLicense', tag='DuplicateLicense')
LicenseOrClaimRefusalReason.DuplicateRequest = LicenseOrClaimRefusalReason._CF_enumeration.addEnumeration(unicode_value='DuplicateRequest', tag='DuplicateRequest')
LicenseOrClaimRefusalReason.InsufficientInformation = LicenseOrClaimRefusalReason._CF_enumeration.addEnumeration(unicode_value='InsufficientInformation', tag='InsufficientInformation')
LicenseOrClaimRefusalReason.MedleyRequest = LicenseOrClaimRefusalReason._CF_enumeration.addEnumeration(unicode_value='MedleyRequest', tag='MedleyRequest')
LicenseOrClaimRefusalReason.NoOptIn = LicenseOrClaimRefusalReason._CF_enumeration.addEnumeration(unicode_value='NoOptIn', tag='NoOptIn')
LicenseOrClaimRefusalReason.NoPublisherClaim = LicenseOrClaimRefusalReason._CF_enumeration.addEnumeration(unicode_value='NoPublisherClaim', tag='NoPublisherClaim')
LicenseOrClaimRefusalReason.PublisherNotRepresented = LicenseOrClaimRefusalReason._CF_enumeration.addEnumeration(unicode_value='PublisherNotRepresented', tag='PublisherNotRepresented')
LicenseOrClaimRefusalReason.ReleaseWithdrawn = LicenseOrClaimRefusalReason._CF_enumeration.addEnumeration(unicode_value='ReleaseWithdrawn', tag='ReleaseWithdrawn')
LicenseOrClaimRefusalReason.RelinquishedClaim = LicenseOrClaimRefusalReason._CF_enumeration.addEnumeration(unicode_value='RelinquishedClaim', tag='RelinquishedClaim')
LicenseOrClaimRefusalReason.UserDefined = LicenseOrClaimRefusalReason._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
LicenseOrClaimRefusalReason.WorkDeletedFromRelease = LicenseOrClaimRefusalReason._CF_enumeration.addEnumeration(unicode_value='WorkDeletedFromRelease', tag='WorkDeletedFromRelease')
LicenseOrClaimRefusalReason.WorkInPublicDomain = LicenseOrClaimRefusalReason._CF_enumeration.addEnumeration(unicode_value='WorkInPublicDomain', tag='WorkInPublicDomain')
LicenseOrClaimRefusalReason.WorkNotUsed = LicenseOrClaimRefusalReason._CF_enumeration.addEnumeration(unicode_value='WorkNotUsed', tag='WorkNotUsed')
LicenseOrClaimRefusalReason._InitializeFacetMap(LicenseOrClaimRefusalReason._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'LicenseOrClaimRefusalReason', LicenseOrClaimRefusalReason)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}LicenseOrClaimReleaseReference
class LicenseOrClaimReleaseReference (pyxb.binding.datatypes.IDREF):

    """A Reference to a Release which is contained within a specific License or Claim."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LicenseOrClaimReleaseReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 683, 4)
    _Documentation = 'A Reference to a Release which is contained within a specific License or Claim.'
LicenseOrClaimReleaseReference._CF_pattern = pyxb.binding.facets.CF_pattern()
LicenseOrClaimReleaseReference._CF_pattern.addPattern(pattern='R[\\d\\-_a-zA-Z]+')
LicenseOrClaimReleaseReference._InitializeFacetMap(LicenseOrClaimReleaseReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'LicenseOrClaimReleaseReference', LicenseOrClaimReleaseReference)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}LicenseOrClaimResourceReference
class LicenseOrClaimResourceReference (pyxb.binding.datatypes.IDREF):

    """A Reference to a Resource which is contained within a specific License or Claim."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LicenseOrClaimResourceReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 691, 4)
    _Documentation = 'A Reference to a Resource which is contained within a specific License or Claim.'
LicenseOrClaimResourceReference._CF_pattern = pyxb.binding.facets.CF_pattern()
LicenseOrClaimResourceReference._CF_pattern.addPattern(pattern='A[\\d\\-_a-zA-Z]+')
LicenseOrClaimResourceReference._InitializeFacetMap(LicenseOrClaimResourceReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'LicenseOrClaimResourceReference', LicenseOrClaimResourceReference)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}LicenseOrClaimRightShareReference
class LicenseOrClaimRightShareReference (pyxb.binding.datatypes.IDREF):

    """A Reference to a RightShare which is contained within a specific License or Claim."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LicenseOrClaimRightShareReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 699, 4)
    _Documentation = 'A Reference to a RightShare which is contained within a specific License or Claim.'
LicenseOrClaimRightShareReference._CF_pattern = pyxb.binding.facets.CF_pattern()
LicenseOrClaimRightShareReference._CF_pattern.addPattern(pattern='S[\\d\\-_a-zA-Z]+')
LicenseOrClaimRightShareReference._InitializeFacetMap(LicenseOrClaimRightShareReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'LicenseOrClaimRightShareReference', LicenseOrClaimRightShareReference)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}LicenseOrClaimWorkReference
class LicenseOrClaimWorkReference (pyxb.binding.datatypes.IDREF):

    """A Reference to a Work which is contained within a specific License or Claim."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LicenseOrClaimWorkReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 707, 4)
    _Documentation = 'A Reference to a Work which is contained within a specific License or Claim.'
LicenseOrClaimWorkReference._CF_pattern = pyxb.binding.facets.CF_pattern()
LicenseOrClaimWorkReference._CF_pattern.addPattern(pattern='W[\\d\\-_a-zA-Z]+')
LicenseOrClaimWorkReference._InitializeFacetMap(LicenseOrClaimWorkReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'LicenseOrClaimWorkReference', LicenseOrClaimWorkReference)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}LicenseStatus
class LicenseStatus (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A legal status of a License for a Claim."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LicenseStatus')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 715, 4)
    _Documentation = 'A legal status of a License for a Claim.'
LicenseStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=LicenseStatus, enum_prefix=None)
LicenseStatus.Active = LicenseStatus._CF_enumeration.addEnumeration(unicode_value='Active', tag='Active')
LicenseStatus.Pending = LicenseStatus._CF_enumeration.addEnumeration(unicode_value='Pending', tag='Pending')
LicenseStatus.Revoked = LicenseStatus._CF_enumeration.addEnumeration(unicode_value='Revoked', tag='Revoked')
LicenseStatus._InitializeFacetMap(LicenseStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'LicenseStatus', LicenseStatus)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}LicensingProcessStatus
class LicensingProcessStatus (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An operational status of a licensing process."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LicensingProcessStatus')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 725, 4)
    _Documentation = 'An operational status of a licensing process.'
LicensingProcessStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=LicensingProcessStatus, enum_prefix=None)
LicensingProcessStatus.Pending = LicensingProcessStatus._CF_enumeration.addEnumeration(unicode_value='Pending', tag='Pending')
LicensingProcessStatus.Processed = LicensingProcessStatus._CF_enumeration.addEnumeration(unicode_value='Processed', tag='Processed')
LicensingProcessStatus.ThirdPartyInformationRequested = LicensingProcessStatus._CF_enumeration.addEnumeration(unicode_value='ThirdPartyInformationRequested', tag='ThirdPartyInformationRequested')
LicensingProcessStatus._InitializeFacetMap(LicensingProcessStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'LicensingProcessStatus', LicensingProcessStatus)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}LocalCollectionAnchor
class LocalCollectionAnchor (pyxb.binding.datatypes.ID):

    """A LocalAnchor which acts as a local Identifier of a Collection. This LocalAnchor is a string starting with the letter X."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LocalCollectionAnchor')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 735, 4)
    _Documentation = 'A LocalAnchor which acts as a local Identifier of a Collection. This LocalAnchor is a string starting with the letter X.'
LocalCollectionAnchor._CF_pattern = pyxb.binding.facets.CF_pattern()
LocalCollectionAnchor._CF_pattern.addPattern(pattern='X[\\d\\-_a-zA-Z]+')
LocalCollectionAnchor._InitializeFacetMap(LocalCollectionAnchor._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'LocalCollectionAnchor', LocalCollectionAnchor)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}LocalCollectionAnchorReference
class LocalCollectionAnchorReference (pyxb.binding.datatypes.IDREF):

    """A LocalAnchorReference which acts as a reference to a local Identifier of a Collection. This LocalAnchorReference is a string starting with the letter X."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LocalCollectionAnchorReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 743, 4)
    _Documentation = 'A LocalAnchorReference which acts as a reference to a local Identifier of a Collection. This LocalAnchorReference is a string starting with the letter X.'
LocalCollectionAnchorReference._CF_pattern = pyxb.binding.facets.CF_pattern()
LocalCollectionAnchorReference._CF_pattern.addPattern(pattern='X[\\d\\-_a-zA-Z]+')
LocalCollectionAnchorReference._InitializeFacetMap(LocalCollectionAnchorReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'LocalCollectionAnchorReference', LocalCollectionAnchorReference)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}LocalCueSheetAnchor
class LocalCueSheetAnchor (pyxb.binding.datatypes.ID):

    """A LocalAnchor which acts as a local Identifier of a CueSheet. This LocalAnchor is a string starting with the letter Q."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LocalCueSheetAnchor')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 751, 4)
    _Documentation = 'A LocalAnchor which acts as a local Identifier of a CueSheet. This LocalAnchor is a string starting with the letter Q.'
LocalCueSheetAnchor._CF_pattern = pyxb.binding.facets.CF_pattern()
LocalCueSheetAnchor._CF_pattern.addPattern(pattern='Q[\\d\\-_a-zA-Z]+')
LocalCueSheetAnchor._InitializeFacetMap(LocalCueSheetAnchor._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'LocalCueSheetAnchor', LocalCueSheetAnchor)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}LocalCueSheetAnchorReference
class LocalCueSheetAnchorReference (pyxb.binding.datatypes.IDREF):

    """A LocalAnchorReference which acts as a reference to a local Identifier of a CueSheet. This LocalAnchorReference is a string starting with the letter Q."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LocalCueSheetAnchorReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 759, 4)
    _Documentation = 'A LocalAnchorReference which acts as a reference to a local Identifier of a CueSheet. This LocalAnchorReference is a string starting with the letter Q.'
LocalCueSheetAnchorReference._CF_pattern = pyxb.binding.facets.CF_pattern()
LocalCueSheetAnchorReference._CF_pattern.addPattern(pattern='Q[\\d\\-_a-zA-Z]+')
LocalCueSheetAnchorReference._InitializeFacetMap(LocalCueSheetAnchorReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'LocalCueSheetAnchorReference', LocalCueSheetAnchorReference)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}LocalLicenseOrClaimAnchor
class LocalLicenseOrClaimAnchor (pyxb.binding.datatypes.ID):

    """A LocalAnchor which acts as a local Identifier of a LicenseOrClaim. This LocalAnchor is a string starting with the letter L."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LocalLicenseOrClaimAnchor')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 767, 4)
    _Documentation = 'A LocalAnchor which acts as a local Identifier of a LicenseOrClaim. This LocalAnchor is a string starting with the letter L.'
LocalLicenseOrClaimAnchor._CF_pattern = pyxb.binding.facets.CF_pattern()
LocalLicenseOrClaimAnchor._CF_pattern.addPattern(pattern='L[\\d\\-_a-zA-Z]+')
LocalLicenseOrClaimAnchor._InitializeFacetMap(LocalLicenseOrClaimAnchor._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'LocalLicenseOrClaimAnchor', LocalLicenseOrClaimAnchor)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}LocalLicenseOrClaimAnchorReference
class LocalLicenseOrClaimAnchorReference (pyxb.binding.datatypes.IDREF):

    """A LocalAnchorReference which acts as a reference to a local Identifier of a LicenseOrClaim. This LocalAnchorReference is a string starting with the letter L."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LocalLicenseOrClaimAnchorReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 775, 4)
    _Documentation = 'A LocalAnchorReference which acts as a reference to a local Identifier of a LicenseOrClaim. This LocalAnchorReference is a string starting with the letter L.'
LocalLicenseOrClaimAnchorReference._CF_pattern = pyxb.binding.facets.CF_pattern()
LocalLicenseOrClaimAnchorReference._CF_pattern.addPattern(pattern='L[\\d\\-_a-zA-Z]+')
LocalLicenseOrClaimAnchorReference._InitializeFacetMap(LocalLicenseOrClaimAnchorReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'LocalLicenseOrClaimAnchorReference', LocalLicenseOrClaimAnchorReference)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}LocalLicenseOrClaimConditionAnchor
class LocalLicenseOrClaimConditionAnchor (pyxb.binding.datatypes.ID):

    """A LocalAnchor which acts as a local Identifier of a LicenseOrClaimCondition. This LocalAnchor is a string starting with the letter E."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LocalLicenseOrClaimConditionAnchor')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 783, 4)
    _Documentation = 'A LocalAnchor which acts as a local Identifier of a LicenseOrClaimCondition. This LocalAnchor is a string starting with the letter E.'
LocalLicenseOrClaimConditionAnchor._CF_pattern = pyxb.binding.facets.CF_pattern()
LocalLicenseOrClaimConditionAnchor._CF_pattern.addPattern(pattern='E[\\d\\-_a-zA-Z]+')
LocalLicenseOrClaimConditionAnchor._InitializeFacetMap(LocalLicenseOrClaimConditionAnchor._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'LocalLicenseOrClaimConditionAnchor', LocalLicenseOrClaimConditionAnchor)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}LocalLicenseOrClaimConditionAnchorReference
class LocalLicenseOrClaimConditionAnchorReference (pyxb.binding.datatypes.IDREF):

    """A LocalAnchorReference which acts as a reference to a local Identifier of a LicenseOrClaimCondition. This LocalAnchorReference is a string starting with the letter E."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LocalLicenseOrClaimConditionAnchorReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 791, 4)
    _Documentation = 'A LocalAnchorReference which acts as a reference to a local Identifier of a LicenseOrClaimCondition. This LocalAnchorReference is a string starting with the letter E.'
LocalLicenseOrClaimConditionAnchorReference._CF_pattern = pyxb.binding.facets.CF_pattern()
LocalLicenseOrClaimConditionAnchorReference._CF_pattern.addPattern(pattern='E[\\d\\-_a-zA-Z]+')
LocalLicenseOrClaimConditionAnchorReference._InitializeFacetMap(LocalLicenseOrClaimConditionAnchorReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'LocalLicenseOrClaimConditionAnchorReference', LocalLicenseOrClaimConditionAnchorReference)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}LocalMusicalWorkAnchor
class LocalMusicalWorkAnchor (pyxb.binding.datatypes.ID):

    """A LocalAnchor which acts as a local Identifier of a MusicalWork. This LocalAnchor is a string starting with the letter W."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LocalMusicalWorkAnchor')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 799, 4)
    _Documentation = 'A LocalAnchor which acts as a local Identifier of a MusicalWork. This LocalAnchor is a string starting with the letter W.'
LocalMusicalWorkAnchor._CF_pattern = pyxb.binding.facets.CF_pattern()
LocalMusicalWorkAnchor._CF_pattern.addPattern(pattern='W[\\d\\-_a-zA-Z]+')
LocalMusicalWorkAnchor._InitializeFacetMap(LocalMusicalWorkAnchor._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'LocalMusicalWorkAnchor', LocalMusicalWorkAnchor)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}LocalMusicalWorkAnchorReference
class LocalMusicalWorkAnchorReference (pyxb.binding.datatypes.IDREF):

    """A LocalAnchorReference which acts as a reference to a local Identifier of a MusicalWork. This LocalAnchorReference is a string starting with the letter W."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LocalMusicalWorkAnchorReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 807, 4)
    _Documentation = 'A LocalAnchorReference which acts as a reference to a local Identifier of a MusicalWork. This LocalAnchorReference is a string starting with the letter W.'
LocalMusicalWorkAnchorReference._CF_pattern = pyxb.binding.facets.CF_pattern()
LocalMusicalWorkAnchorReference._CF_pattern.addPattern(pattern='W[\\d\\-_a-zA-Z]+')
LocalMusicalWorkAnchorReference._InitializeFacetMap(LocalMusicalWorkAnchorReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'LocalMusicalWorkAnchorReference', LocalMusicalWorkAnchorReference)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}LocalReleaseAnchor
class LocalReleaseAnchor (pyxb.binding.datatypes.ID):

    """A LocalAnchor which acts as a local Identifier of a Release. This LocalAnchor is a string starting with the letter R."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LocalReleaseAnchor')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 815, 4)
    _Documentation = 'A LocalAnchor which acts as a local Identifier of a Release. This LocalAnchor is a string starting with the letter R.'
LocalReleaseAnchor._CF_pattern = pyxb.binding.facets.CF_pattern()
LocalReleaseAnchor._CF_pattern.addPattern(pattern='R[\\d\\-_a-zA-Z]+')
LocalReleaseAnchor._InitializeFacetMap(LocalReleaseAnchor._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'LocalReleaseAnchor', LocalReleaseAnchor)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}LocalReleaseAnchorReference
class LocalReleaseAnchorReference (pyxb.binding.datatypes.IDREF):

    """A LocalAnchorReference which acts as a reference to a local Identifier of a Release. This LocalAnchorReference is a string starting with the letter R."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LocalReleaseAnchorReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 823, 4)
    _Documentation = 'A LocalAnchorReference which acts as a reference to a local Identifier of a Release. This LocalAnchorReference is a string starting with the letter R.'
LocalReleaseAnchorReference._CF_pattern = pyxb.binding.facets.CF_pattern()
LocalReleaseAnchorReference._CF_pattern.addPattern(pattern='R[\\d\\-_a-zA-Z]+')
LocalReleaseAnchorReference._InitializeFacetMap(LocalReleaseAnchorReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'LocalReleaseAnchorReference', LocalReleaseAnchorReference)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}LocalResourceAnchor
class LocalResourceAnchor (pyxb.binding.datatypes.ID):

    """A LocalAnchor which acts as a local Identifier of a Resource. This LocalAnchor is a string starting with the letter A."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LocalResourceAnchor')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 831, 4)
    _Documentation = 'A LocalAnchor which acts as a local Identifier of a Resource. This LocalAnchor is a string starting with the letter A.'
LocalResourceAnchor._CF_pattern = pyxb.binding.facets.CF_pattern()
LocalResourceAnchor._CF_pattern.addPattern(pattern='A[\\d\\-_a-zA-Z]+')
LocalResourceAnchor._InitializeFacetMap(LocalResourceAnchor._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'LocalResourceAnchor', LocalResourceAnchor)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}LocalResourceAnchorReference
class LocalResourceAnchorReference (pyxb.binding.datatypes.IDREF):

    """A LocalAnchorReference which acts as a reference to a local Identifier of a Resource. This LocalAnchorReference is a string starting with the letter A."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LocalResourceAnchorReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 839, 4)
    _Documentation = 'A LocalAnchorReference which acts as a reference to a local Identifier of a Resource. This LocalAnchorReference is a string starting with the letter A.'
LocalResourceAnchorReference._CF_pattern = pyxb.binding.facets.CF_pattern()
LocalResourceAnchorReference._CF_pattern.addPattern(pattern='A[\\d\\-_a-zA-Z]+')
LocalResourceAnchorReference._InitializeFacetMap(LocalResourceAnchorReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'LocalResourceAnchorReference', LocalResourceAnchorReference)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}LocalRightShareAnchor
class LocalRightShareAnchor (pyxb.binding.datatypes.ID):

    """A LocalAnchor which acts as a local Identifier of a RightShare. This LocalAnchor is a string starting with the letter S."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LocalRightShareAnchor')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 847, 4)
    _Documentation = 'A LocalAnchor which acts as a local Identifier of a RightShare. This LocalAnchor is a string starting with the letter S.'
LocalRightShareAnchor._CF_pattern = pyxb.binding.facets.CF_pattern()
LocalRightShareAnchor._CF_pattern.addPattern(pattern='S[\\d\\-_a-zA-Z]+')
LocalRightShareAnchor._InitializeFacetMap(LocalRightShareAnchor._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'LocalRightShareAnchor', LocalRightShareAnchor)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}LocalRightShareAnchorReference
class LocalRightShareAnchorReference (pyxb.binding.datatypes.IDREF):

    """A LocalAnchorReference which acts as a reference to a local Identifier of a RightShare. This LocalAnchorReference is a string starting with the letter S."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LocalRightShareAnchorReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 855, 4)
    _Documentation = 'A LocalAnchorReference which acts as a reference to a local Identifier of a RightShare. This LocalAnchorReference is a string starting with the letter S.'
LocalRightShareAnchorReference._CF_pattern = pyxb.binding.facets.CF_pattern()
LocalRightShareAnchorReference._CF_pattern.addPattern(pattern='S[\\d\\-_a-zA-Z]+')
LocalRightShareAnchorReference._InitializeFacetMap(LocalRightShareAnchorReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'LocalRightShareAnchorReference', LocalRightShareAnchorReference)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}LocalTechnicalResourceDetailsAnchor
class LocalTechnicalResourceDetailsAnchor (pyxb.binding.datatypes.ID):

    """A LocalAnchor which acts as a local Identifier of a TechnicalResourceDetails Composite. This LocalAnchor is a string starting with the letter T."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LocalTechnicalResourceDetailsAnchor')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 863, 4)
    _Documentation = 'A LocalAnchor which acts as a local Identifier of a TechnicalResourceDetails Composite. This LocalAnchor is a string starting with the letter T.'
LocalTechnicalResourceDetailsAnchor._CF_pattern = pyxb.binding.facets.CF_pattern()
LocalTechnicalResourceDetailsAnchor._CF_pattern.addPattern(pattern='T[\\d\\-_a-zA-Z]+')
LocalTechnicalResourceDetailsAnchor._InitializeFacetMap(LocalTechnicalResourceDetailsAnchor._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'LocalTechnicalResourceDetailsAnchor', LocalTechnicalResourceDetailsAnchor)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}LocalTechnicalResourceDetailsAnchorReference
class LocalTechnicalResourceDetailsAnchorReference (pyxb.binding.datatypes.IDREF):

    """A LocalAnchorReference which acts as a reference to a local Identifier of a TechnicalResourceDetails Composite. This LocalAnchorReference is a string starting with the letter T."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LocalTechnicalResourceDetailsAnchorReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 871, 4)
    _Documentation = 'A LocalAnchorReference which acts as a reference to a local Identifier of a TechnicalResourceDetails Composite. This LocalAnchorReference is a string starting with the letter T.'
LocalTechnicalResourceDetailsAnchorReference._CF_pattern = pyxb.binding.facets.CF_pattern()
LocalTechnicalResourceDetailsAnchorReference._CF_pattern.addPattern(pattern='T[\\d\\-_a-zA-Z]+')
LocalTechnicalResourceDetailsAnchorReference._InitializeFacetMap(LocalTechnicalResourceDetailsAnchorReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'LocalTechnicalResourceDetailsAnchorReference', LocalTechnicalResourceDetailsAnchorReference)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}MessageContentRevenueType
class MessageContentRevenueType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of revenue to which the content of the Message relates."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MessageContentRevenueType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 879, 4)
    _Documentation = 'A Type of revenue to which the content of the Message relates.'
MessageContentRevenueType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MessageContentRevenueType, enum_prefix=None)
MessageContentRevenueType.NonTransactionalRevenue = MessageContentRevenueType._CF_enumeration.addEnumeration(unicode_value='NonTransactionalRevenue', tag='NonTransactionalRevenue')
MessageContentRevenueType.TransactionalRevenue = MessageContentRevenueType._CF_enumeration.addEnumeration(unicode_value='TransactionalRevenue', tag='TransactionalRevenue')
MessageContentRevenueType.UserDefined = MessageContentRevenueType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
MessageContentRevenueType._InitializeFacetMap(MessageContentRevenueType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MessageContentRevenueType', MessageContentRevenueType)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}MessageControlType
class MessageControlType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Message according to its operational status."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MessageControlType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 889, 4)
    _Documentation = 'A Type of Message according to its operational status.'
MessageControlType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MessageControlType, enum_prefix=None)
MessageControlType.LiveMessage = MessageControlType._CF_enumeration.addEnumeration(unicode_value='LiveMessage', tag='LiveMessage')
MessageControlType.TestMessage = MessageControlType._CF_enumeration.addEnumeration(unicode_value='TestMessage', tag='TestMessage')
MessageControlType._InitializeFacetMap(MessageControlType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MessageControlType', MessageControlType)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}MessageType
class MessageType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Message in a DDEX namespace."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MessageType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 898, 4)
    _Documentation = 'A Type of Message in a DDEX namespace.'
MessageType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MessageType, enum_prefix=None)
MessageType.SalesReportToRecordCompanyMessage = MessageType._CF_enumeration.addEnumeration(unicode_value='SalesReportToRecordCompanyMessage', tag='SalesReportToRecordCompanyMessage')
MessageType.SalesReportToSocietyMessage = MessageType._CF_enumeration.addEnumeration(unicode_value='SalesReportToSocietyMessage', tag='SalesReportToSocietyMessage')
MessageType.SalesReportMessage = MessageType._CF_enumeration.addEnumeration(unicode_value='SalesReportMessage', tag='SalesReportMessage')
MessageType.NewReleaseMessage = MessageType._CF_enumeration.addEnumeration(unicode_value='NewReleaseMessage', tag='NewReleaseMessage')
MessageType.NewDealMessage = MessageType._CF_enumeration.addEnumeration(unicode_value='NewDealMessage', tag='NewDealMessage')
MessageType.MusicalWorkLicenseInformationMessage = MessageType._CF_enumeration.addEnumeration(unicode_value='MusicalWorkLicenseInformationMessage', tag='MusicalWorkLicenseInformationMessage')
MessageType.NewReleaseMessage_ = MessageType._CF_enumeration.addEnumeration(unicode_value='NewReleaseMessage', tag='NewReleaseMessage_')
MessageType.DataMismatchMessage = MessageType._CF_enumeration.addEnumeration(unicode_value='DataMismatchMessage', tag='DataMismatchMessage')
MessageType.DataMismatchResponseMessage = MessageType._CF_enumeration.addEnumeration(unicode_value='DataMismatchResponseMessage', tag='DataMismatchResponseMessage')
MessageType.FtpManifestMessage = MessageType._CF_enumeration.addEnumeration(unicode_value='FtpManifestMessage', tag='FtpManifestMessage')
MessageType.FtpAcknowledgementMessage = MessageType._CF_enumeration.addEnumeration(unicode_value='FtpAcknowledgementMessage', tag='FtpAcknowledgementMessage')
MessageType.LicenseOrClaimRequestMessage = MessageType._CF_enumeration.addEnumeration(unicode_value='LicenseOrClaimRequestMessage', tag='LicenseOrClaimRequestMessage')
MessageType.LicenseOrClaimRequestCancellationMessage = MessageType._CF_enumeration.addEnumeration(unicode_value='LicenseOrClaimRequestCancellationMessage', tag='LicenseOrClaimRequestCancellationMessage')
MessageType.LicenseOrClaimMessage = MessageType._CF_enumeration.addEnumeration(unicode_value='LicenseOrClaimMessage', tag='LicenseOrClaimMessage')
MessageType.LicenseOrClaimConfirmationMessage = MessageType._CF_enumeration.addEnumeration(unicode_value='LicenseOrClaimConfirmationMessage', tag='LicenseOrClaimConfirmationMessage')
MessageType.LicensingProcessStatusRequestMessage = MessageType._CF_enumeration.addEnumeration(unicode_value='LicensingProcessStatusRequestMessage', tag='LicensingProcessStatusRequestMessage')
MessageType.LicensingProcessStatusMessage = MessageType._CF_enumeration.addEnumeration(unicode_value='LicensingProcessStatusMessage', tag='LicensingProcessStatusMessage')
MessageType.LicensingInformationRequestMessage = MessageType._CF_enumeration.addEnumeration(unicode_value='LicensingInformationRequestMessage', tag='LicensingInformationRequestMessage')
MessageType.LicenseOrClaimRevocationMessage = MessageType._CF_enumeration.addEnumeration(unicode_value='LicenseOrClaimRevocationMessage', tag='LicenseOrClaimRevocationMessage')
MessageType.SalesReportMessage_ = MessageType._CF_enumeration.addEnumeration(unicode_value='SalesReportMessage', tag='SalesReportMessage_')
MessageType._InitializeFacetMap(MessageType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MessageType', MessageType)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}MidiType
class MidiType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of MIDI."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MidiType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 925, 4)
    _Documentation = 'A Type of MIDI.'
MidiType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MidiType, enum_prefix=None)
MidiType.MonophonicMidi = MidiType._CF_enumeration.addEnumeration(unicode_value='MonophonicMidi', tag='MonophonicMidi')
MidiType.PolyphonicMidi = MidiType._CF_enumeration.addEnumeration(unicode_value='PolyphonicMidi', tag='PolyphonicMidi')
MidiType.Unknown = MidiType._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
MidiType.UserDefined = MidiType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
MidiType._InitializeFacetMap(MidiType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MidiType', MidiType)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}MusicalWorkContributorRole
class MusicalWorkContributorRole (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A role played by a Contributor in relation to a MusicalWork."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MusicalWorkContributorRole')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 936, 4)
    _Documentation = 'A role played by a Contributor in relation to a MusicalWork.'
MusicalWorkContributorRole._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MusicalWorkContributorRole, enum_prefix=None)
MusicalWorkContributorRole.Adapter = MusicalWorkContributorRole._CF_enumeration.addEnumeration(unicode_value='Adapter', tag='Adapter')
MusicalWorkContributorRole.Arranger = MusicalWorkContributorRole._CF_enumeration.addEnumeration(unicode_value='Arranger', tag='Arranger')
MusicalWorkContributorRole.AssociatedPerformer = MusicalWorkContributorRole._CF_enumeration.addEnumeration(unicode_value='AssociatedPerformer', tag='AssociatedPerformer')
MusicalWorkContributorRole.Author = MusicalWorkContributorRole._CF_enumeration.addEnumeration(unicode_value='Author', tag='Author')
MusicalWorkContributorRole.Composer = MusicalWorkContributorRole._CF_enumeration.addEnumeration(unicode_value='Composer', tag='Composer')
MusicalWorkContributorRole.ComposerLyricist = MusicalWorkContributorRole._CF_enumeration.addEnumeration(unicode_value='ComposerLyricist', tag='ComposerLyricist')
MusicalWorkContributorRole.Contributor = MusicalWorkContributorRole._CF_enumeration.addEnumeration(unicode_value='Contributor', tag='Contributor')
MusicalWorkContributorRole.Librettist = MusicalWorkContributorRole._CF_enumeration.addEnumeration(unicode_value='Librettist', tag='Librettist')
MusicalWorkContributorRole.Lyricist = MusicalWorkContributorRole._CF_enumeration.addEnumeration(unicode_value='Lyricist', tag='Lyricist')
MusicalWorkContributorRole.MusicPublisher = MusicalWorkContributorRole._CF_enumeration.addEnumeration(unicode_value='MusicPublisher', tag='MusicPublisher')
MusicalWorkContributorRole.NonLyricAuthor = MusicalWorkContributorRole._CF_enumeration.addEnumeration(unicode_value='NonLyricAuthor', tag='NonLyricAuthor')
MusicalWorkContributorRole.OriginalPublisher = MusicalWorkContributorRole._CF_enumeration.addEnumeration(unicode_value='OriginalPublisher', tag='OriginalPublisher')
MusicalWorkContributorRole.SubArranger = MusicalWorkContributorRole._CF_enumeration.addEnumeration(unicode_value='SubArranger', tag='SubArranger')
MusicalWorkContributorRole.SubPublisher = MusicalWorkContributorRole._CF_enumeration.addEnumeration(unicode_value='SubPublisher', tag='SubPublisher')
MusicalWorkContributorRole.SubstitutedPublisher = MusicalWorkContributorRole._CF_enumeration.addEnumeration(unicode_value='SubstitutedPublisher', tag='SubstitutedPublisher')
MusicalWorkContributorRole.Translator = MusicalWorkContributorRole._CF_enumeration.addEnumeration(unicode_value='Translator', tag='Translator')
MusicalWorkContributorRole.Unknown = MusicalWorkContributorRole._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
MusicalWorkContributorRole.UserDefined = MusicalWorkContributorRole._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
MusicalWorkContributorRole._InitializeFacetMap(MusicalWorkContributorRole._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MusicalWorkContributorRole', MusicalWorkContributorRole)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}MusicalWorkReference
class MusicalWorkReference (pyxb.binding.datatypes.ID):

    """A Reference to a MusicalWork."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MusicalWorkReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 961, 4)
    _Documentation = 'A Reference to a MusicalWork.'
MusicalWorkReference._CF_pattern = pyxb.binding.facets.CF_pattern()
MusicalWorkReference._CF_pattern.addPattern(pattern='W[\\d\\-_a-zA-Z]+')
MusicalWorkReference._InitializeFacetMap(MusicalWorkReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'MusicalWorkReference', MusicalWorkReference)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}MusicalWorkRightsClaimType
class MusicalWorkRightsClaimType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of RightsClaim related to a MusicalWork."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MusicalWorkRightsClaimType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 969, 4)
    _Documentation = 'A Type of RightsClaim related to a MusicalWork.'
MusicalWorkRightsClaimType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MusicalWorkRightsClaimType, enum_prefix=None)
MusicalWorkRightsClaimType.CopyrightControl = MusicalWorkRightsClaimType._CF_enumeration.addEnumeration(unicode_value='CopyrightControl', tag='CopyrightControl')
MusicalWorkRightsClaimType.NonMemberClaim = MusicalWorkRightsClaimType._CF_enumeration.addEnumeration(unicode_value='NonMemberClaim', tag='NonMemberClaim')
MusicalWorkRightsClaimType.PublicDomain = MusicalWorkRightsClaimType._CF_enumeration.addEnumeration(unicode_value='PublicDomain', tag='PublicDomain')
MusicalWorkRightsClaimType.SocietyClaim = MusicalWorkRightsClaimType._CF_enumeration.addEnumeration(unicode_value='SocietyClaim', tag='SocietyClaim')
MusicalWorkRightsClaimType.Unknown = MusicalWorkRightsClaimType._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
MusicalWorkRightsClaimType._InitializeFacetMap(MusicalWorkRightsClaimType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MusicalWorkRightsClaimType', MusicalWorkRightsClaimType)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}MusicalWorkType
class MusicalWorkType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of MusicalWork."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MusicalWorkType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 981, 4)
    _Documentation = 'A Type of MusicalWork.'
MusicalWorkType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MusicalWorkType, enum_prefix=None)
MusicalWorkType.AdaptedInOriginalLanguage = MusicalWorkType._CF_enumeration.addEnumeration(unicode_value='AdaptedInOriginalLanguage', tag='AdaptedInOriginalLanguage')
MusicalWorkType.AdaptedInstrumentalWork = MusicalWorkType._CF_enumeration.addEnumeration(unicode_value='AdaptedInstrumentalWork', tag='AdaptedInstrumentalWork')
MusicalWorkType.AdaptedWithNewLyrics = MusicalWorkType._CF_enumeration.addEnumeration(unicode_value='AdaptedWithNewLyrics', tag='AdaptedWithNewLyrics')
MusicalWorkType.ArrangedWithNewMusic = MusicalWorkType._CF_enumeration.addEnumeration(unicode_value='ArrangedWithNewMusic', tag='ArrangedWithNewMusic')
MusicalWorkType.CompositeMusicalWork = MusicalWorkType._CF_enumeration.addEnumeration(unicode_value='CompositeMusicalWork', tag='CompositeMusicalWork')
MusicalWorkType.DramaticoMusicalWork = MusicalWorkType._CF_enumeration.addEnumeration(unicode_value='DramaticoMusicalWork', tag='DramaticoMusicalWork')
MusicalWorkType.LyricRemoval = MusicalWorkType._CF_enumeration.addEnumeration(unicode_value='LyricRemoval', tag='LyricRemoval')
MusicalWorkType.LyricReplacement = MusicalWorkType._CF_enumeration.addEnumeration(unicode_value='LyricReplacement', tag='LyricReplacement')
MusicalWorkType.LyricTranslation = MusicalWorkType._CF_enumeration.addEnumeration(unicode_value='LyricTranslation', tag='LyricTranslation')
MusicalWorkType.Mashup = MusicalWorkType._CF_enumeration.addEnumeration(unicode_value='Mashup', tag='Mashup')
MusicalWorkType.Medley = MusicalWorkType._CF_enumeration.addEnumeration(unicode_value='Medley', tag='Medley')
MusicalWorkType.MultimediaProductionWork = MusicalWorkType._CF_enumeration.addEnumeration(unicode_value='MultimediaProductionWork', tag='MultimediaProductionWork')
MusicalWorkType.MusicalWorkMovement = MusicalWorkType._CF_enumeration.addEnumeration(unicode_value='MusicalWorkMovement', tag='MusicalWorkMovement')
MusicalWorkType.MusicalWorkWithSamples = MusicalWorkType._CF_enumeration.addEnumeration(unicode_value='MusicalWorkWithSamples', tag='MusicalWorkWithSamples')
MusicalWorkType.MusicArrangement = MusicalWorkType._CF_enumeration.addEnumeration(unicode_value='MusicArrangement', tag='MusicArrangement')
MusicalWorkType.MusicArrangementOfText = MusicalWorkType._CF_enumeration.addEnumeration(unicode_value='MusicArrangementOfText', tag='MusicArrangementOfText')
MusicalWorkType.OriginalLyricsArrangement = MusicalWorkType._CF_enumeration.addEnumeration(unicode_value='OriginalLyricsArrangement', tag='OriginalLyricsArrangement')
MusicalWorkType.OriginalMusicAdaptation = MusicalWorkType._CF_enumeration.addEnumeration(unicode_value='OriginalMusicAdaptation', tag='OriginalMusicAdaptation')
MusicalWorkType.OriginalMusicalWork = MusicalWorkType._CF_enumeration.addEnumeration(unicode_value='OriginalMusicalWork', tag='OriginalMusicalWork')
MusicalWorkType.Potpourri = MusicalWorkType._CF_enumeration.addEnumeration(unicode_value='Potpourri', tag='Potpourri')
MusicalWorkType.ProductionMusicLibraryWork = MusicalWorkType._CF_enumeration.addEnumeration(unicode_value='ProductionMusicLibraryWork', tag='ProductionMusicLibraryWork')
MusicalWorkType.RadioProductionWork = MusicalWorkType._CF_enumeration.addEnumeration(unicode_value='RadioProductionWork', tag='RadioProductionWork')
MusicalWorkType.TheaterProductionWork = MusicalWorkType._CF_enumeration.addEnumeration(unicode_value='TheaterProductionWork', tag='TheaterProductionWork')
MusicalWorkType.TvProductionWork = MusicalWorkType._CF_enumeration.addEnumeration(unicode_value='TvProductionWork', tag='TvProductionWork')
MusicalWorkType.Unknown = MusicalWorkType._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
MusicalWorkType.UnspecifiedArrangement = MusicalWorkType._CF_enumeration.addEnumeration(unicode_value='UnspecifiedArrangement', tag='UnspecifiedArrangement')
MusicalWorkType.UnspecifiedMusicalWorkExcerpt = MusicalWorkType._CF_enumeration.addEnumeration(unicode_value='UnspecifiedMusicalWorkExcerpt', tag='UnspecifiedMusicalWorkExcerpt')
MusicalWorkType.UserDefined = MusicalWorkType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
MusicalWorkType.VideoProductionWork = MusicalWorkType._CF_enumeration.addEnumeration(unicode_value='VideoProductionWork', tag='VideoProductionWork')
MusicalWorkType._InitializeFacetMap(MusicalWorkType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MusicalWorkType', MusicalWorkType)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}NonIsoTerritoryCode
class NonIsoTerritoryCode (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A TerritoryId which is not a TerritoryId according to the ISO 3166-1 standard."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NonIsoTerritoryCode')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 1017, 4)
    _Documentation = 'A TerritoryId which is not a TerritoryId according to the ISO 3166-1 standard.'
NonIsoTerritoryCode._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=NonIsoTerritoryCode, enum_prefix=None)
NonIsoTerritoryCode.Worldwide = NonIsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='Worldwide', tag='Worldwide')
NonIsoTerritoryCode._InitializeFacetMap(NonIsoTerritoryCode._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'NonIsoTerritoryCode', NonIsoTerritoryCode)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}OperatingSystemType
class OperatingSystemType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of OperatingSystem."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OperatingSystemType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 1029, 4)
    _Documentation = 'A Type of OperatingSystem.'
OperatingSystemType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=OperatingSystemType, enum_prefix=None)
OperatingSystemType.MacOS = OperatingSystemType._CF_enumeration.addEnumeration(unicode_value='MacOS', tag='MacOS')
OperatingSystemType.MsWindows = OperatingSystemType._CF_enumeration.addEnumeration(unicode_value='MsWindows', tag='MsWindows')
OperatingSystemType.Symbian = OperatingSystemType._CF_enumeration.addEnumeration(unicode_value='Symbian', tag='Symbian')
OperatingSystemType.Unknown = OperatingSystemType._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
OperatingSystemType._InitializeFacetMap(OperatingSystemType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'OperatingSystemType', OperatingSystemType)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}ParentalWarningType
class ParentalWarningType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Creation according to advice which it carries about the level of explicitness or offensiveness of its content."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ParentalWarningType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 1040, 4)
    _Documentation = 'A Type of Creation according to advice which it carries about the level of explicitness or offensiveness of its content.'
ParentalWarningType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ParentalWarningType, enum_prefix=None)
ParentalWarningType.Explicit = ParentalWarningType._CF_enumeration.addEnumeration(unicode_value='Explicit', tag='Explicit')
ParentalWarningType.ExplicitContentEdited = ParentalWarningType._CF_enumeration.addEnumeration(unicode_value='ExplicitContentEdited', tag='ExplicitContentEdited')
ParentalWarningType.NoAdviceAvailable = ParentalWarningType._CF_enumeration.addEnumeration(unicode_value='NoAdviceAvailable', tag='NoAdviceAvailable')
ParentalWarningType.NotExplicit = ParentalWarningType._CF_enumeration.addEnumeration(unicode_value='NotExplicit', tag='NotExplicit')
ParentalWarningType.Unknown = ParentalWarningType._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
ParentalWarningType.UserDefined = ParentalWarningType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
ParentalWarningType._InitializeFacetMap(ParentalWarningType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ParentalWarningType', ParentalWarningType)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}PercentageType
class PercentageType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of PercentageRate."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PercentageType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 1053, 4)
    _Documentation = 'A Type of PercentageRate.'
PercentageType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PercentageType, enum_prefix=None)
PercentageType.PercentageOfFreeGoodsPermitted = PercentageType._CF_enumeration.addEnumeration(unicode_value='PercentageOfFreeGoodsPermitted', tag='PercentageOfFreeGoodsPermitted')
PercentageType.PercentageOfGrossRevenue = PercentageType._CF_enumeration.addEnumeration(unicode_value='PercentageOfGrossRevenue', tag='PercentageOfGrossRevenue')
PercentageType.PercentageOfNetRevenue = PercentageType._CF_enumeration.addEnumeration(unicode_value='PercentageOfNetRevenue', tag='PercentageOfNetRevenue')
PercentageType.PercentageOfNetSales = PercentageType._CF_enumeration.addEnumeration(unicode_value='PercentageOfNetSales', tag='PercentageOfNetSales')
PercentageType.PercentageOfPriceConsumerPaid = PercentageType._CF_enumeration.addEnumeration(unicode_value='PercentageOfPriceConsumerPaid', tag='PercentageOfPriceConsumerPaid')
PercentageType.PercentageOfStatutoryRoyaltyRate = PercentageType._CF_enumeration.addEnumeration(unicode_value='PercentageOfStatutoryRoyaltyRate', tag='PercentageOfStatutoryRoyaltyRate')
PercentageType._InitializeFacetMap(PercentageType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'PercentageType', PercentageType)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}PriceRangeType
class PriceRangeType (pyxb.binding.datatypes.string):

    """A Type of Price according to its value range."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PriceRangeType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 1066, 4)
    _Documentation = 'A Type of Price according to its value range.'
PriceRangeType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'PriceRangeType', PriceRangeType)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}PriceType
class PriceType (pyxb.binding.datatypes.string):

    """A Type of Price."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PriceType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 1072, 4)
    _Documentation = 'A Type of Price.'
PriceType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'PriceType', PriceType)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}Purpose
class Purpose (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of use that is the purpose of an action."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Purpose')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 1078, 4)
    _Documentation = 'A Type of use that is the purpose of an action.'
Purpose._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Purpose, enum_prefix=None)
Purpose.BackgroundMusic = Purpose._CF_enumeration.addEnumeration(unicode_value='BackgroundMusic', tag='BackgroundMusic')
Purpose.ChannelTrailerMusic = Purpose._CF_enumeration.addEnumeration(unicode_value='ChannelTrailerMusic', tag='ChannelTrailerMusic')
Purpose.Extract = Purpose._CF_enumeration.addEnumeration(unicode_value='Extract', tag='Extract')
Purpose.FilmTrailerMusic = Purpose._CF_enumeration.addEnumeration(unicode_value='FilmTrailerMusic', tag='FilmTrailerMusic')
Purpose.ForegroundMusic = Purpose._CF_enumeration.addEnumeration(unicode_value='ForegroundMusic', tag='ForegroundMusic')
Purpose.TrailerMusic = Purpose._CF_enumeration.addEnumeration(unicode_value='TrailerMusic', tag='TrailerMusic')
Purpose.UserDefined = Purpose._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
Purpose._InitializeFacetMap(Purpose._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'Purpose', Purpose)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}RatingAgency
class RatingAgency (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An Organization that issues ParentalWarnings."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RatingAgency')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 1092, 4)
    _Documentation = 'An Organization that issues ParentalWarnings.'
RatingAgency._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=RatingAgency, enum_prefix=None)
RatingAgency.AFR = RatingAgency._CF_enumeration.addEnumeration(unicode_value='AFR', tag='AFR')
RatingAgency.BBFC = RatingAgency._CF_enumeration.addEnumeration(unicode_value='BBFC', tag='BBFC')
RatingAgency.BFCO = RatingAgency._CF_enumeration.addEnumeration(unicode_value='BFCO', tag='BFCO')
RatingAgency.BFSC = RatingAgency._CF_enumeration.addEnumeration(unicode_value='BFSC', tag='BFSC')
RatingAgency.BMUKK = RatingAgency._CF_enumeration.addEnumeration(unicode_value='BMUKK', tag='BMUKK')
RatingAgency.CBFC = RatingAgency._CF_enumeration.addEnumeration(unicode_value='CBFC', tag='CBFC')
RatingAgency.CCC = RatingAgency._CF_enumeration.addEnumeration(unicode_value='CCC', tag='CCC')
RatingAgency.CCE = RatingAgency._CF_enumeration.addEnumeration(unicode_value='CCE', tag='CCE')
RatingAgency.CHVRS = RatingAgency._CF_enumeration.addEnumeration(unicode_value='CHVRS', tag='CHVRS')
RatingAgency.CNC = RatingAgency._CF_enumeration.addEnumeration(unicode_value='CNC', tag='CNC')
RatingAgency.DJCTQ = RatingAgency._CF_enumeration.addEnumeration(unicode_value='DJCTQ', tag='DJCTQ')
RatingAgency.Eirin = RatingAgency._CF_enumeration.addEnumeration(unicode_value='Eirin', tag='Eirin')
RatingAgency.FCB = RatingAgency._CF_enumeration.addEnumeration(unicode_value='FCB', tag='FCB')
RatingAgency.Filmtilsynet = RatingAgency._CF_enumeration.addEnumeration(unicode_value='Filmtilsynet', tag='Filmtilsynet')
RatingAgency.FPB = RatingAgency._CF_enumeration.addEnumeration(unicode_value='FPB', tag='FPB')
RatingAgency.FSK = RatingAgency._CF_enumeration.addEnumeration(unicode_value='FSK', tag='FSK')
RatingAgency.IFCO = RatingAgency._CF_enumeration.addEnumeration(unicode_value='IFCO', tag='IFCO')
RatingAgency.INCAA = RatingAgency._CF_enumeration.addEnumeration(unicode_value='INCAA', tag='INCAA')
RatingAgency.KMRB = RatingAgency._CF_enumeration.addEnumeration(unicode_value='KMRB', tag='KMRB')
RatingAgency.KR = RatingAgency._CF_enumeration.addEnumeration(unicode_value='KR', tag='KR')
RatingAgency.KRRIT = RatingAgency._CF_enumeration.addEnumeration(unicode_value='KRRIT', tag='KRRIT')
RatingAgency.LSF = RatingAgency._CF_enumeration.addEnumeration(unicode_value='LSF', tag='LSF')
RatingAgency.MBU = RatingAgency._CF_enumeration.addEnumeration(unicode_value='MBU', tag='MBU')
RatingAgency.MDA = RatingAgency._CF_enumeration.addEnumeration(unicode_value='MDA', tag='MDA')
RatingAgency.MDCB = RatingAgency._CF_enumeration.addEnumeration(unicode_value='MDCB', tag='MDCB')
RatingAgency.MFCB = RatingAgency._CF_enumeration.addEnumeration(unicode_value='MFCB', tag='MFCB')
RatingAgency.MIC = RatingAgency._CF_enumeration.addEnumeration(unicode_value='MIC', tag='MIC')
RatingAgency.MPAA = RatingAgency._CF_enumeration.addEnumeration(unicode_value='MPAA', tag='MPAA')
RatingAgency.MTRCB = RatingAgency._CF_enumeration.addEnumeration(unicode_value='MTRCB', tag='MTRCB')
RatingAgency.NBC = RatingAgency._CF_enumeration.addEnumeration(unicode_value='NBC', tag='NBC')
RatingAgency.NFVCB = RatingAgency._CF_enumeration.addEnumeration(unicode_value='NFVCB', tag='NFVCB')
RatingAgency.NICAM = RatingAgency._CF_enumeration.addEnumeration(unicode_value='NICAM', tag='NICAM')
RatingAgency.NKC = RatingAgency._CF_enumeration.addEnumeration(unicode_value='NKC', tag='NKC')
RatingAgency.OFLC = RatingAgency._CF_enumeration.addEnumeration(unicode_value='OFLC', tag='OFLC')
RatingAgency.OFRB = RatingAgency._CF_enumeration.addEnumeration(unicode_value='OFRB', tag='OFRB')
RatingAgency.RDCQ = RatingAgency._CF_enumeration.addEnumeration(unicode_value='RDCQ', tag='RDCQ')
RatingAgency.RTC = RatingAgency._CF_enumeration.addEnumeration(unicode_value='RTC', tag='RTC')
RatingAgency.SBB = RatingAgency._CF_enumeration.addEnumeration(unicode_value='SBB', tag='SBB')
RatingAgency.Smais = RatingAgency._CF_enumeration.addEnumeration(unicode_value='Smais', tag='Smais')
RatingAgency.SPIO_JK = RatingAgency._CF_enumeration.addEnumeration(unicode_value='SPIO-JK', tag='SPIO_JK')
RatingAgency.TELA = RatingAgency._CF_enumeration.addEnumeration(unicode_value='TELA', tag='TELA')
RatingAgency.UserDefined = RatingAgency._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
RatingAgency.VET = RatingAgency._CF_enumeration.addEnumeration(unicode_value='VET', tag='VET')
RatingAgency._InitializeFacetMap(RatingAgency._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'RatingAgency', RatingAgency)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}ReferenceUnit
class ReferenceUnit (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A unit to which a Quantity refers."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReferenceUnit')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 1142, 4)
    _Documentation = 'A unit to which a Quantity refers.'
ReferenceUnit._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ReferenceUnit, enum_prefix=None)
ReferenceUnit.PerLicense = ReferenceUnit._CF_enumeration.addEnumeration(unicode_value='PerLicense', tag='PerLicense')
ReferenceUnit.PerUse = ReferenceUnit._CF_enumeration.addEnumeration(unicode_value='PerUse', tag='PerUse')
ReferenceUnit._InitializeFacetMap(ReferenceUnit._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ReferenceUnit', ReferenceUnit)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}ReleaseReference
class ReleaseReference (pyxb.binding.datatypes.ID):

    """An Identifier of a Release which is specific to a DdexMessage."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReleaseReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 1151, 4)
    _Documentation = 'An Identifier of a Release which is specific to a DdexMessage.'
ReleaseReference._CF_pattern = pyxb.binding.facets.CF_pattern()
ReleaseReference._CF_pattern.addPattern(pattern='R[\\d\\-_a-zA-Z]+')
ReleaseReference._InitializeFacetMap(ReleaseReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'ReleaseReference', ReleaseReference)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}ReleaseRelationshipType
class ReleaseRelationshipType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of relationship between two Releases."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReleaseRelationshipType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 1159, 4)
    _Documentation = 'A Type of relationship between two Releases.'
ReleaseRelationshipType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ReleaseRelationshipType, enum_prefix=None)
ReleaseRelationshipType.HasSameArtist = ReleaseRelationshipType._CF_enumeration.addEnumeration(unicode_value='HasSameArtist', tag='HasSameArtist')
ReleaseRelationshipType.HasSameRecordingProject = ReleaseRelationshipType._CF_enumeration.addEnumeration(unicode_value='HasSameRecordingProject', tag='HasSameRecordingProject')
ReleaseRelationshipType.HasSimilarContent = ReleaseRelationshipType._CF_enumeration.addEnumeration(unicode_value='HasSimilarContent', tag='HasSimilarContent')
ReleaseRelationshipType.IsReleaseFromRelease = ReleaseRelationshipType._CF_enumeration.addEnumeration(unicode_value='IsReleaseFromRelease', tag='IsReleaseFromRelease')
ReleaseRelationshipType.Unknown = ReleaseRelationshipType._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
ReleaseRelationshipType.UserDefined = ReleaseRelationshipType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
ReleaseRelationshipType._InitializeFacetMap(ReleaseRelationshipType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ReleaseRelationshipType', ReleaseRelationshipType)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}ReleaseResourceType
class ReleaseResourceType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Resource in the context of a Release."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReleaseResourceType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 1172, 4)
    _Documentation = 'A Type of Resource in the context of a Release.'
ReleaseResourceType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ReleaseResourceType, enum_prefix=None)
ReleaseResourceType.PrimaryResource = ReleaseResourceType._CF_enumeration.addEnumeration(unicode_value='PrimaryResource', tag='PrimaryResource')
ReleaseResourceType.SecondaryResource = ReleaseResourceType._CF_enumeration.addEnumeration(unicode_value='SecondaryResource', tag='SecondaryResource')
ReleaseResourceType._InitializeFacetMap(ReleaseResourceType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ReleaseResourceType', ReleaseResourceType)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}ReleaseType
class ReleaseType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Release according to its content, Duration and/or number of components. Note: a ReleaseType is the form in which a ReleaseCreator anticipates offering a Release to Consumers."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReleaseType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 1181, 4)
    _Documentation = 'A Type of Release according to its content, Duration and/or number of components. Note: a ReleaseType is the form in which a ReleaseCreator anticipates offering a Release to Consumers.'
ReleaseType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ReleaseType, enum_prefix=None)
ReleaseType.AdvertisementVideo = ReleaseType._CF_enumeration.addEnumeration(unicode_value='AdvertisementVideo', tag='AdvertisementVideo')
ReleaseType.Album = ReleaseType._CF_enumeration.addEnumeration(unicode_value='Album', tag='Album')
ReleaseType.AlertToneRelease = ReleaseType._CF_enumeration.addEnumeration(unicode_value='AlertToneRelease', tag='AlertToneRelease')
ReleaseType.Animation = ReleaseType._CF_enumeration.addEnumeration(unicode_value='Animation', tag='Animation')
ReleaseType.AsPerContract = ReleaseType._CF_enumeration.addEnumeration(unicode_value='AsPerContract', tag='AsPerContract')
ReleaseType.AudioClipRelease = ReleaseType._CF_enumeration.addEnumeration(unicode_value='AudioClipRelease', tag='AudioClipRelease')
ReleaseType.BackCoverImageRelease = ReleaseType._CF_enumeration.addEnumeration(unicode_value='BackCoverImageRelease', tag='BackCoverImageRelease')
ReleaseType.BookletBackImageRelease = ReleaseType._CF_enumeration.addEnumeration(unicode_value='BookletBackImageRelease', tag='BookletBackImageRelease')
ReleaseType.BookletFrontImageRelease = ReleaseType._CF_enumeration.addEnumeration(unicode_value='BookletFrontImageRelease', tag='BookletFrontImageRelease')
ReleaseType.BookletRelease = ReleaseType._CF_enumeration.addEnumeration(unicode_value='BookletRelease', tag='BookletRelease')
ReleaseType.Bundle = ReleaseType._CF_enumeration.addEnumeration(unicode_value='Bundle', tag='Bundle')
ReleaseType.ConcertVideo = ReleaseType._CF_enumeration.addEnumeration(unicode_value='ConcertVideo', tag='ConcertVideo')
ReleaseType.CorporateFilm = ReleaseType._CF_enumeration.addEnumeration(unicode_value='CorporateFilm', tag='CorporateFilm')
ReleaseType.Documentary = ReleaseType._CF_enumeration.addEnumeration(unicode_value='Documentary', tag='Documentary')
ReleaseType.DocumentImageRelease = ReleaseType._CF_enumeration.addEnumeration(unicode_value='DocumentImageRelease', tag='DocumentImageRelease')
ReleaseType.EBookRelease = ReleaseType._CF_enumeration.addEnumeration(unicode_value='EBookRelease', tag='EBookRelease')
ReleaseType.Episode = ReleaseType._CF_enumeration.addEnumeration(unicode_value='Episode', tag='Episode')
ReleaseType.FeatureFilm = ReleaseType._CF_enumeration.addEnumeration(unicode_value='FeatureFilm', tag='FeatureFilm')
ReleaseType.FrontCoverImageRelease = ReleaseType._CF_enumeration.addEnumeration(unicode_value='FrontCoverImageRelease', tag='FrontCoverImageRelease')
ReleaseType.IconRelease = ReleaseType._CF_enumeration.addEnumeration(unicode_value='IconRelease', tag='IconRelease')
ReleaseType.InfomercialVideo = ReleaseType._CF_enumeration.addEnumeration(unicode_value='InfomercialVideo', tag='InfomercialVideo')
ReleaseType.InteractiveBookletRelease = ReleaseType._CF_enumeration.addEnumeration(unicode_value='InteractiveBookletRelease', tag='InteractiveBookletRelease')
ReleaseType.KaraokeRelease = ReleaseType._CF_enumeration.addEnumeration(unicode_value='KaraokeRelease', tag='KaraokeRelease')
ReleaseType.LiveEventVideo = ReleaseType._CF_enumeration.addEnumeration(unicode_value='LiveEventVideo', tag='LiveEventVideo')
ReleaseType.LogoRelease = ReleaseType._CF_enumeration.addEnumeration(unicode_value='LogoRelease', tag='LogoRelease')
ReleaseType.LongFormMusicalWorkVideoRelease = ReleaseType._CF_enumeration.addEnumeration(unicode_value='LongFormMusicalWorkVideoRelease', tag='LongFormMusicalWorkVideoRelease')
ReleaseType.LongFormNonMusicalWorkVideoRelease = ReleaseType._CF_enumeration.addEnumeration(unicode_value='LongFormNonMusicalWorkVideoRelease', tag='LongFormNonMusicalWorkVideoRelease')
ReleaseType.LyricSheetRelease = ReleaseType._CF_enumeration.addEnumeration(unicode_value='LyricSheetRelease', tag='LyricSheetRelease')
ReleaseType.MusicalWorkBasedGameRelease = ReleaseType._CF_enumeration.addEnumeration(unicode_value='MusicalWorkBasedGameRelease', tag='MusicalWorkBasedGameRelease')
ReleaseType.MusicalWorkClipRelease = ReleaseType._CF_enumeration.addEnumeration(unicode_value='MusicalWorkClipRelease', tag='MusicalWorkClipRelease')
ReleaseType.MusicalWorkReadalongVideoRelease = ReleaseType._CF_enumeration.addEnumeration(unicode_value='MusicalWorkReadalongVideoRelease', tag='MusicalWorkReadalongVideoRelease')
ReleaseType.MusicalWorkTrailerRelease = ReleaseType._CF_enumeration.addEnumeration(unicode_value='MusicalWorkTrailerRelease', tag='MusicalWorkTrailerRelease')
ReleaseType.MusicalWorkVideoChapterRelease = ReleaseType._CF_enumeration.addEnumeration(unicode_value='MusicalWorkVideoChapterRelease', tag='MusicalWorkVideoChapterRelease')
ReleaseType.News = ReleaseType._CF_enumeration.addEnumeration(unicode_value='News', tag='News')
ReleaseType.NonMusicalWorkBasedGameRelease = ReleaseType._CF_enumeration.addEnumeration(unicode_value='NonMusicalWorkBasedGameRelease', tag='NonMusicalWorkBasedGameRelease')
ReleaseType.NonMusicalWorkClipRelease = ReleaseType._CF_enumeration.addEnumeration(unicode_value='NonMusicalWorkClipRelease', tag='NonMusicalWorkClipRelease')
ReleaseType.NonMusicalWorkReadalongVideoRelease = ReleaseType._CF_enumeration.addEnumeration(unicode_value='NonMusicalWorkReadalongVideoRelease', tag='NonMusicalWorkReadalongVideoRelease')
ReleaseType.NonMusicalWorkTrailerRelease = ReleaseType._CF_enumeration.addEnumeration(unicode_value='NonMusicalWorkTrailerRelease', tag='NonMusicalWorkTrailerRelease')
ReleaseType.NonMusicalWorkVideoChapterRelease = ReleaseType._CF_enumeration.addEnumeration(unicode_value='NonMusicalWorkVideoChapterRelease', tag='NonMusicalWorkVideoChapterRelease')
ReleaseType.NonSerialAudioVisualRecording = ReleaseType._CF_enumeration.addEnumeration(unicode_value='NonSerialAudioVisualRecording', tag='NonSerialAudioVisualRecording')
ReleaseType.PhotographRelease = ReleaseType._CF_enumeration.addEnumeration(unicode_value='PhotographRelease', tag='PhotographRelease')
ReleaseType.RingbackToneRelease = ReleaseType._CF_enumeration.addEnumeration(unicode_value='RingbackToneRelease', tag='RingbackToneRelease')
ReleaseType.RingtoneRelease = ReleaseType._CF_enumeration.addEnumeration(unicode_value='RingtoneRelease', tag='RingtoneRelease')
ReleaseType.ScreensaverRelease = ReleaseType._CF_enumeration.addEnumeration(unicode_value='ScreensaverRelease', tag='ScreensaverRelease')
ReleaseType.Season = ReleaseType._CF_enumeration.addEnumeration(unicode_value='Season', tag='Season')
ReleaseType.Series = ReleaseType._CF_enumeration.addEnumeration(unicode_value='Series', tag='Series')
ReleaseType.SheetMusicRelease = ReleaseType._CF_enumeration.addEnumeration(unicode_value='SheetMusicRelease', tag='SheetMusicRelease')
ReleaseType.ShortFormMusicalWorkVideoRelease = ReleaseType._CF_enumeration.addEnumeration(unicode_value='ShortFormMusicalWorkVideoRelease', tag='ShortFormMusicalWorkVideoRelease')
ReleaseType.ShortFormNonMusicalWorkVideoRelease = ReleaseType._CF_enumeration.addEnumeration(unicode_value='ShortFormNonMusicalWorkVideoRelease', tag='ShortFormNonMusicalWorkVideoRelease')
ReleaseType.Single = ReleaseType._CF_enumeration.addEnumeration(unicode_value='Single', tag='Single')
ReleaseType.SingleResourceRelease = ReleaseType._CF_enumeration.addEnumeration(unicode_value='SingleResourceRelease', tag='SingleResourceRelease')
ReleaseType.TrackRelease = ReleaseType._CF_enumeration.addEnumeration(unicode_value='TrackRelease', tag='TrackRelease')
ReleaseType.TrailerVideo = ReleaseType._CF_enumeration.addEnumeration(unicode_value='TrailerVideo', tag='TrailerVideo')
ReleaseType.TrayImageRelease = ReleaseType._CF_enumeration.addEnumeration(unicode_value='TrayImageRelease', tag='TrayImageRelease')
ReleaseType.Unknown = ReleaseType._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
ReleaseType.UserDefined = ReleaseType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
ReleaseType.VideoChapterRelease = ReleaseType._CF_enumeration.addEnumeration(unicode_value='VideoChapterRelease', tag='VideoChapterRelease')
ReleaseType.VideoClipRelease = ReleaseType._CF_enumeration.addEnumeration(unicode_value='VideoClipRelease', tag='VideoClipRelease')
ReleaseType.VideoScreenCaptureRelease = ReleaseType._CF_enumeration.addEnumeration(unicode_value='VideoScreenCaptureRelease', tag='VideoScreenCaptureRelease')
ReleaseType.VideoSingle = ReleaseType._CF_enumeration.addEnumeration(unicode_value='VideoSingle', tag='VideoSingle')
ReleaseType.WallpaperRelease = ReleaseType._CF_enumeration.addEnumeration(unicode_value='WallpaperRelease', tag='WallpaperRelease')
ReleaseType._InitializeFacetMap(ReleaseType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ReleaseType', ReleaseType)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}RepresentativeImageReference
class RepresentativeImageReference (pyxb.binding.datatypes.IDREF):

    """A Reference to a Image which is represents a specific Resource ."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RepresentativeImageReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 1249, 4)
    _Documentation = 'A Reference to a Image which is represents a specific Resource .'
RepresentativeImageReference._CF_pattern = pyxb.binding.facets.CF_pattern()
RepresentativeImageReference._CF_pattern.addPattern(pattern='A[\\d\\-_a-zA-Z]+')
RepresentativeImageReference._InitializeFacetMap(RepresentativeImageReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'RepresentativeImageReference', RepresentativeImageReference)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}RequestConditionReference
class RequestConditionReference (pyxb.binding.datatypes.IDREF):

    """A Reference to a LicenseOrClaimCondition which is contained within a specific request."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RequestConditionReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 1257, 4)
    _Documentation = 'A Reference to a LicenseOrClaimCondition which is contained within a specific request.'
RequestConditionReference._CF_pattern = pyxb.binding.facets.CF_pattern()
RequestConditionReference._CF_pattern.addPattern(pattern='E[\\d\\-_a-zA-Z]+')
RequestConditionReference._InitializeFacetMap(RequestConditionReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'RequestConditionReference', RequestConditionReference)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}RequestedActionType
class RequestedActionType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of action requested."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RequestedActionType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 1265, 4)
    _Documentation = 'A Type of action requested.'
RequestedActionType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=RequestedActionType, enum_prefix=None)
RequestedActionType.AdditionalInformationOnly = RequestedActionType._CF_enumeration.addEnumeration(unicode_value='AdditionalInformationOnly', tag='AdditionalInformationOnly')
RequestedActionType.CorrectAndInform = RequestedActionType._CF_enumeration.addEnumeration(unicode_value='CorrectAndInform', tag='CorrectAndInform')
RequestedActionType.CorrectAndResend = RequestedActionType._CF_enumeration.addEnumeration(unicode_value='CorrectAndResend', tag='CorrectAndResend')
RequestedActionType.NoAction = RequestedActionType._CF_enumeration.addEnumeration(unicode_value='NoAction', tag='NoAction')
RequestedActionType.UserDefined = RequestedActionType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
RequestedActionType._InitializeFacetMap(RequestedActionType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'RequestedActionType', RequestedActionType)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}RequestReleaseReference
class RequestReleaseReference (pyxb.binding.datatypes.IDREF):

    """A Reference to a Release which is contained within a specific request."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RequestReleaseReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 1277, 4)
    _Documentation = 'A Reference to a Release which is contained within a specific request.'
RequestReleaseReference._CF_pattern = pyxb.binding.facets.CF_pattern()
RequestReleaseReference._CF_pattern.addPattern(pattern='R[\\d\\-_a-zA-Z]+')
RequestReleaseReference._InitializeFacetMap(RequestReleaseReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'RequestReleaseReference', RequestReleaseReference)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}RequestResourceReference
class RequestResourceReference (pyxb.binding.datatypes.IDREF):

    """A Reference to a Resource which is contained within a specific request."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RequestResourceReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 1285, 4)
    _Documentation = 'A Reference to a Resource which is contained within a specific request.'
RequestResourceReference._CF_pattern = pyxb.binding.facets.CF_pattern()
RequestResourceReference._CF_pattern.addPattern(pattern='A[\\d\\-_a-zA-Z]+')
RequestResourceReference._InitializeFacetMap(RequestResourceReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'RequestResourceReference', RequestResourceReference)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}RequestRightShareReference
class RequestRightShareReference (pyxb.binding.datatypes.IDREF):

    """A Reference to a RightShare which is contained within a specific request."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RequestRightShareReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 1293, 4)
    _Documentation = 'A Reference to a RightShare which is contained within a specific request.'
RequestRightShareReference._CF_pattern = pyxb.binding.facets.CF_pattern()
RequestRightShareReference._CF_pattern.addPattern(pattern='S[\\d\\-_a-zA-Z]+')
RequestRightShareReference._InitializeFacetMap(RequestRightShareReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'RequestRightShareReference', RequestRightShareReference)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}RequestWorkReference
class RequestWorkReference (pyxb.binding.datatypes.IDREF):

    """A Reference to a Work which is contained within a specific request."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RequestWorkReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 1301, 4)
    _Documentation = 'A Reference to a Work which is contained within a specific request.'
RequestWorkReference._CF_pattern = pyxb.binding.facets.CF_pattern()
RequestWorkReference._CF_pattern.addPattern(pattern='W[\\d\\-_a-zA-Z]+')
RequestWorkReference._InitializeFacetMap(RequestWorkReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'RequestWorkReference', RequestWorkReference)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}ResourceContainedResourceReference
class ResourceContainedResourceReference (pyxb.binding.datatypes.IDREF):

    """A Reference to a Resource which is contained within a specific Resource ."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ResourceContainedResourceReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 1309, 4)
    _Documentation = 'A Reference to a Resource which is contained within a specific Resource .'
ResourceContainedResourceReference._CF_pattern = pyxb.binding.facets.CF_pattern()
ResourceContainedResourceReference._CF_pattern.addPattern(pattern='A[\\d\\-_a-zA-Z]+')
ResourceContainedResourceReference._InitializeFacetMap(ResourceContainedResourceReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'ResourceContainedResourceReference', ResourceContainedResourceReference)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}ResourceContributorRole
class ResourceContributorRole (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A role played by a Contributor in relation to a Fixation of an abstract Creation."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ResourceContributorRole')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 1317, 4)
    _Documentation = 'A role played by a Contributor in relation to a Fixation of an abstract Creation.'
ResourceContributorRole._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ResourceContributorRole, enum_prefix=None)
ResourceContributorRole.Actor = ResourceContributorRole._CF_enumeration.addEnumeration(unicode_value='Actor', tag='Actor')
ResourceContributorRole.Architect = ResourceContributorRole._CF_enumeration.addEnumeration(unicode_value='Architect', tag='Architect')
ResourceContributorRole.Artist = ResourceContributorRole._CF_enumeration.addEnumeration(unicode_value='Artist', tag='Artist')
ResourceContributorRole.AssociatedPerformer = ResourceContributorRole._CF_enumeration.addEnumeration(unicode_value='AssociatedPerformer', tag='AssociatedPerformer')
ResourceContributorRole.Band = ResourceContributorRole._CF_enumeration.addEnumeration(unicode_value='Band', tag='Band')
ResourceContributorRole.BookPublisher = ResourceContributorRole._CF_enumeration.addEnumeration(unicode_value='BookPublisher', tag='BookPublisher')
ResourceContributorRole.Cartoonist = ResourceContributorRole._CF_enumeration.addEnumeration(unicode_value='Cartoonist', tag='Cartoonist')
ResourceContributorRole.Choir = ResourceContributorRole._CF_enumeration.addEnumeration(unicode_value='Choir', tag='Choir')
ResourceContributorRole.Choreographer = ResourceContributorRole._CF_enumeration.addEnumeration(unicode_value='Choreographer', tag='Choreographer')
ResourceContributorRole.ComputerGraphicCreator = ResourceContributorRole._CF_enumeration.addEnumeration(unicode_value='ComputerGraphicCreator', tag='ComputerGraphicCreator')
ResourceContributorRole.Conductor = ResourceContributorRole._CF_enumeration.addEnumeration(unicode_value='Conductor', tag='Conductor')
ResourceContributorRole.Contributor = ResourceContributorRole._CF_enumeration.addEnumeration(unicode_value='Contributor', tag='Contributor')
ResourceContributorRole.CostumeDesigner = ResourceContributorRole._CF_enumeration.addEnumeration(unicode_value='CostumeDesigner', tag='CostumeDesigner')
ResourceContributorRole.Designer = ResourceContributorRole._CF_enumeration.addEnumeration(unicode_value='Designer', tag='Designer')
ResourceContributorRole.Ensemble = ResourceContributorRole._CF_enumeration.addEnumeration(unicode_value='Ensemble', tag='Ensemble')
ResourceContributorRole.FeaturedArtist = ResourceContributorRole._CF_enumeration.addEnumeration(unicode_value='FeaturedArtist', tag='FeaturedArtist')
ResourceContributorRole.FilmDirector = ResourceContributorRole._CF_enumeration.addEnumeration(unicode_value='FilmDirector', tag='FilmDirector')
ResourceContributorRole.FilmDistributor = ResourceContributorRole._CF_enumeration.addEnumeration(unicode_value='FilmDistributor', tag='FilmDistributor')
ResourceContributorRole.FilmEditor = ResourceContributorRole._CF_enumeration.addEnumeration(unicode_value='FilmEditor', tag='FilmEditor')
ResourceContributorRole.FilmProducer = ResourceContributorRole._CF_enumeration.addEnumeration(unicode_value='FilmProducer', tag='FilmProducer')
ResourceContributorRole.FilmSoundEngineer = ResourceContributorRole._CF_enumeration.addEnumeration(unicode_value='FilmSoundEngineer', tag='FilmSoundEngineer')
ResourceContributorRole.GraphicArtist = ResourceContributorRole._CF_enumeration.addEnumeration(unicode_value='GraphicArtist', tag='GraphicArtist')
ResourceContributorRole.GraphicDesigner = ResourceContributorRole._CF_enumeration.addEnumeration(unicode_value='GraphicDesigner', tag='GraphicDesigner')
ResourceContributorRole.Journalist = ResourceContributorRole._CF_enumeration.addEnumeration(unicode_value='Journalist', tag='Journalist')
ResourceContributorRole.MainArtist = ResourceContributorRole._CF_enumeration.addEnumeration(unicode_value='MainArtist', tag='MainArtist')
ResourceContributorRole.NewspaperPublisher = ResourceContributorRole._CF_enumeration.addEnumeration(unicode_value='NewspaperPublisher', tag='NewspaperPublisher')
ResourceContributorRole.Orchestra = ResourceContributorRole._CF_enumeration.addEnumeration(unicode_value='Orchestra', tag='Orchestra')
ResourceContributorRole.Painter = ResourceContributorRole._CF_enumeration.addEnumeration(unicode_value='Painter', tag='Painter')
ResourceContributorRole.PeriodicalPublisher = ResourceContributorRole._CF_enumeration.addEnumeration(unicode_value='PeriodicalPublisher', tag='PeriodicalPublisher')
ResourceContributorRole.Photographer = ResourceContributorRole._CF_enumeration.addEnumeration(unicode_value='Photographer', tag='Photographer')
ResourceContributorRole.PhotographyDirector = ResourceContributorRole._CF_enumeration.addEnumeration(unicode_value='PhotographyDirector', tag='PhotographyDirector')
ResourceContributorRole.PrimaryMusician = ResourceContributorRole._CF_enumeration.addEnumeration(unicode_value='PrimaryMusician', tag='PrimaryMusician')
ResourceContributorRole.Producer = ResourceContributorRole._CF_enumeration.addEnumeration(unicode_value='Producer', tag='Producer')
ResourceContributorRole.Programmer = ResourceContributorRole._CF_enumeration.addEnumeration(unicode_value='Programmer', tag='Programmer')
ResourceContributorRole.RightsControllerOnProduct = ResourceContributorRole._CF_enumeration.addEnumeration(unicode_value='RightsControllerOnProduct', tag='RightsControllerOnProduct')
ResourceContributorRole.ScreenplayAuthor = ResourceContributorRole._CF_enumeration.addEnumeration(unicode_value='ScreenplayAuthor', tag='ScreenplayAuthor')
ResourceContributorRole.SetDesigner = ResourceContributorRole._CF_enumeration.addEnumeration(unicode_value='SetDesigner', tag='SetDesigner')
ResourceContributorRole.Soloist = ResourceContributorRole._CF_enumeration.addEnumeration(unicode_value='Soloist', tag='Soloist')
ResourceContributorRole.StageDirector = ResourceContributorRole._CF_enumeration.addEnumeration(unicode_value='StageDirector', tag='StageDirector')
ResourceContributorRole.StudioPersonnel = ResourceContributorRole._CF_enumeration.addEnumeration(unicode_value='StudioPersonnel', tag='StudioPersonnel')
ResourceContributorRole.SubtitlesEditor = ResourceContributorRole._CF_enumeration.addEnumeration(unicode_value='SubtitlesEditor', tag='SubtitlesEditor')
ResourceContributorRole.SubtitlesTranslator = ResourceContributorRole._CF_enumeration.addEnumeration(unicode_value='SubtitlesTranslator', tag='SubtitlesTranslator')
ResourceContributorRole.Unknown = ResourceContributorRole._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
ResourceContributorRole.UserDefined = ResourceContributorRole._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
ResourceContributorRole._InitializeFacetMap(ResourceContributorRole._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ResourceContributorRole', ResourceContributorRole)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}ResourceGroupResourceReference
class ResourceGroupResourceReference (pyxb.binding.datatypes.IDREF):

    """A Reference to a Resource which is contained within a specific group of Resources."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ResourceGroupResourceReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 1368, 4)
    _Documentation = 'A Reference to a Resource which is contained within a specific group of Resources.'
ResourceGroupResourceReference._CF_pattern = pyxb.binding.facets.CF_pattern()
ResourceGroupResourceReference._CF_pattern.addPattern(pattern='A[\\d\\-_a-zA-Z]+')
ResourceGroupResourceReference._InitializeFacetMap(ResourceGroupResourceReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'ResourceGroupResourceReference', ResourceGroupResourceReference)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}ResourceMusicalWorkReference
class ResourceMusicalWorkReference (pyxb.binding.datatypes.IDREF):

    """A Reference to a MusicalWork which is contained within a specific Resource."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ResourceMusicalWorkReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 1376, 4)
    _Documentation = 'A Reference to a MusicalWork which is contained within a specific Resource.'
ResourceMusicalWorkReference._CF_pattern = pyxb.binding.facets.CF_pattern()
ResourceMusicalWorkReference._CF_pattern.addPattern(pattern='W[\\d\\-_a-zA-Z]+')
ResourceMusicalWorkReference._InitializeFacetMap(ResourceMusicalWorkReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'ResourceMusicalWorkReference', ResourceMusicalWorkReference)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}ResourceReference
class ResourceReference (pyxb.binding.datatypes.ID):

    """An Identifier of a Resource which is specific to a DdexMessage."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ResourceReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 1384, 4)
    _Documentation = 'An Identifier of a Resource which is specific to a DdexMessage.'
ResourceReference._CF_pattern = pyxb.binding.facets.CF_pattern()
ResourceReference._CF_pattern.addPattern(pattern='A[\\d\\-_a-zA-Z]+')
ResourceReference._InitializeFacetMap(ResourceReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'ResourceReference', ResourceReference)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}ResourceReleaseReference
class ResourceReleaseReference (pyxb.binding.datatypes.IDREF):

    """A Reference to a Release which is included in a specific Resource."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ResourceReleaseReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 1392, 4)
    _Documentation = 'A Reference to a Release which is included in a specific Resource.'
ResourceReleaseReference._CF_pattern = pyxb.binding.facets.CF_pattern()
ResourceReleaseReference._CF_pattern.addPattern(pattern='R[\\d\\-_a-zA-Z]+')
ResourceReleaseReference._InitializeFacetMap(ResourceReleaseReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'ResourceReleaseReference', ResourceReleaseReference)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}ResourceType
class ResourceType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Resource."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ResourceType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 1400, 4)
    _Documentation = 'A Type of Resource.'
ResourceType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ResourceType, enum_prefix=None)
ResourceType.Image = ResourceType._CF_enumeration.addEnumeration(unicode_value='Image', tag='Image')
ResourceType.MIDI = ResourceType._CF_enumeration.addEnumeration(unicode_value='MIDI', tag='MIDI')
ResourceType.SheetMusic = ResourceType._CF_enumeration.addEnumeration(unicode_value='SheetMusic', tag='SheetMusic')
ResourceType.Software = ResourceType._CF_enumeration.addEnumeration(unicode_value='Software', tag='Software')
ResourceType.SoundRecording = ResourceType._CF_enumeration.addEnumeration(unicode_value='SoundRecording', tag='SoundRecording')
ResourceType.Text = ResourceType._CF_enumeration.addEnumeration(unicode_value='Text', tag='Text')
ResourceType.UserDefinedResource = ResourceType._CF_enumeration.addEnumeration(unicode_value='UserDefinedResource', tag='UserDefinedResource')
ResourceType.Video = ResourceType._CF_enumeration.addEnumeration(unicode_value='Video', tag='Video')
ResourceType._InitializeFacetMap(ResourceType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ResourceType', ResourceType)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}RightsControllerRole
class RightsControllerRole (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A role of a RightsController."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RightsControllerRole')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 1415, 4)
    _Documentation = 'A role of a RightsController.'
RightsControllerRole._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=RightsControllerRole, enum_prefix=None)
RightsControllerRole.AdministratingRecordCompany = RightsControllerRole._CF_enumeration.addEnumeration(unicode_value='AdministratingRecordCompany', tag='AdministratingRecordCompany')
RightsControllerRole.RightsAdministrator = RightsControllerRole._CF_enumeration.addEnumeration(unicode_value='RightsAdministrator', tag='RightsAdministrator')
RightsControllerRole.RightsController = RightsControllerRole._CF_enumeration.addEnumeration(unicode_value='RightsController', tag='RightsController')
RightsControllerRole.RoyaltyAdministrator = RightsControllerRole._CF_enumeration.addEnumeration(unicode_value='RoyaltyAdministrator', tag='RoyaltyAdministrator')
RightsControllerRole.Unknown = RightsControllerRole._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
RightsControllerRole._InitializeFacetMap(RightsControllerRole._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'RightsControllerRole', RightsControllerRole)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}RightsCoverage
class RightsCoverage (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Right which is covered."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RightsCoverage')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 1427, 4)
    _Documentation = 'A Type of Right which is covered.'
RightsCoverage._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=RightsCoverage, enum_prefix=None)
RightsCoverage.MakeAvailableRight = RightsCoverage._CF_enumeration.addEnumeration(unicode_value='MakeAvailableRight', tag='MakeAvailableRight')
RightsCoverage.MechanicalRight = RightsCoverage._CF_enumeration.addEnumeration(unicode_value='MechanicalRight', tag='MechanicalRight')
RightsCoverage.PerformingRight = RightsCoverage._CF_enumeration.addEnumeration(unicode_value='PerformingRight', tag='PerformingRight')
RightsCoverage.ReproductionRight = RightsCoverage._CF_enumeration.addEnumeration(unicode_value='ReproductionRight', tag='ReproductionRight')
RightsCoverage.SynchronizationRight = RightsCoverage._CF_enumeration.addEnumeration(unicode_value='SynchronizationRight', tag='SynchronizationRight')
RightsCoverage._InitializeFacetMap(RightsCoverage._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'RightsCoverage', RightsCoverage)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}RightShareReference
class RightShareReference (pyxb.binding.datatypes.ID):

    """A Reference to a RightShare."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RightShareReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 1439, 4)
    _Documentation = 'A Reference to a RightShare.'
RightShareReference._CF_pattern = pyxb.binding.facets.CF_pattern()
RightShareReference._CF_pattern.addPattern(pattern='S[\\d\\-_a-zA-Z]+')
RightShareReference._InitializeFacetMap(RightShareReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'RightShareReference', RightShareReference)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}RightShareReleaseReference
class RightShareReleaseReference (pyxb.binding.datatypes.IDREF):

    """A Reference to a Release which is contained within a specific RightShare."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RightShareReleaseReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 1447, 4)
    _Documentation = 'A Reference to a Release which is contained within a specific RightShare.'
RightShareReleaseReference._CF_pattern = pyxb.binding.facets.CF_pattern()
RightShareReleaseReference._CF_pattern.addPattern(pattern='R[\\d\\-_a-zA-Z]+')
RightShareReleaseReference._InitializeFacetMap(RightShareReleaseReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'RightShareReleaseReference', RightShareReleaseReference)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}RightShareResourceReference
class RightShareResourceReference (pyxb.binding.datatypes.IDREF):

    """A Reference to a Resource which is contained within a specific RightShare."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RightShareResourceReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 1455, 4)
    _Documentation = 'A Reference to a Resource which is contained within a specific RightShare.'
RightShareResourceReference._CF_pattern = pyxb.binding.facets.CF_pattern()
RightShareResourceReference._CF_pattern.addPattern(pattern='A[\\d\\-_a-zA-Z]+')
RightShareResourceReference._InitializeFacetMap(RightShareResourceReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'RightShareResourceReference', RightShareResourceReference)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}RightShareWorkReference
class RightShareWorkReference (pyxb.binding.datatypes.IDREF):

    """A Reference to a Work which is contained within a specific RightShare."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RightShareWorkReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 1463, 4)
    _Documentation = 'A Reference to a Work which is contained within a specific RightShare.'
RightShareWorkReference._CF_pattern = pyxb.binding.facets.CF_pattern()
RightShareWorkReference._CF_pattern.addPattern(pattern='W[\\d\\-_a-zA-Z]+')
RightShareWorkReference._InitializeFacetMap(RightShareWorkReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'RightShareWorkReference', RightShareWorkReference)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}RoyaltyRateCalculationType
class RoyaltyRateCalculationType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of RoyaltyRate according to the calculation method."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RoyaltyRateCalculationType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 1471, 4)
    _Documentation = 'A Type of RoyaltyRate according to the calculation method.'
RoyaltyRateCalculationType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=RoyaltyRateCalculationType, enum_prefix=None)
RoyaltyRateCalculationType.ControlledCompositionRoyaltyRate = RoyaltyRateCalculationType._CF_enumeration.addEnumeration(unicode_value='ControlledCompositionRoyaltyRate', tag='ControlledCompositionRoyaltyRate')
RoyaltyRateCalculationType.ControlledShareRoyaltyRate = RoyaltyRateCalculationType._CF_enumeration.addEnumeration(unicode_value='ControlledShareRoyaltyRate', tag='ControlledShareRoyaltyRate')
RoyaltyRateCalculationType.MinimumStatutoryRoyaltyRate = RoyaltyRateCalculationType._CF_enumeration.addEnumeration(unicode_value='MinimumStatutoryRoyaltyRate', tag='MinimumStatutoryRoyaltyRate')
RoyaltyRateCalculationType.NegotiatedRoyaltyRate = RoyaltyRateCalculationType._CF_enumeration.addEnumeration(unicode_value='NegotiatedRoyaltyRate', tag='NegotiatedRoyaltyRate')
RoyaltyRateCalculationType.ReducedRoyaltyRate = RoyaltyRateCalculationType._CF_enumeration.addEnumeration(unicode_value='ReducedRoyaltyRate', tag='ReducedRoyaltyRate')
RoyaltyRateCalculationType.ReducedStatutoryRoyaltyRate = RoyaltyRateCalculationType._CF_enumeration.addEnumeration(unicode_value='ReducedStatutoryRoyaltyRate', tag='ReducedStatutoryRoyaltyRate')
RoyaltyRateCalculationType.StatutoryRoyaltyRate = RoyaltyRateCalculationType._CF_enumeration.addEnumeration(unicode_value='StatutoryRoyaltyRate', tag='StatutoryRoyaltyRate')
RoyaltyRateCalculationType._InitializeFacetMap(RoyaltyRateCalculationType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'RoyaltyRateCalculationType', RoyaltyRateCalculationType)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}RoyaltyRateType
class RoyaltyRateType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of RoyaltyRate."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RoyaltyRateType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 1485, 4)
    _Documentation = 'A Type of RoyaltyRate.'
RoyaltyRateType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=RoyaltyRateType, enum_prefix=None)
RoyaltyRateType.PennyRate = RoyaltyRateType._CF_enumeration.addEnumeration(unicode_value='PennyRate', tag='PennyRate')
RoyaltyRateType.PercentageRoyaltyRate = RoyaltyRateType._CF_enumeration.addEnumeration(unicode_value='PercentageRoyaltyRate', tag='PercentageRoyaltyRate')
RoyaltyRateType.UserDefined = RoyaltyRateType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
RoyaltyRateType._InitializeFacetMap(RoyaltyRateType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'RoyaltyRateType', RoyaltyRateType)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}SheetMusicCodecType
class SheetMusicCodecType (pyxb.binding.datatypes.string):

    """A Type of SheetMusicCodec."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SheetMusicCodecType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 1495, 4)
    _Documentation = 'A Type of SheetMusicCodec.'
SheetMusicCodecType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'SheetMusicCodecType', SheetMusicCodecType)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}SheetMusicType
class SheetMusicType (pyxb.binding.datatypes.string):

    """A Type of SheetMusic."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SheetMusicType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 1501, 4)
    _Documentation = 'A Type of SheetMusic.'
SheetMusicType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'SheetMusicType', SheetMusicType)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}SICI
class SICI (pyxb.binding.datatypes.string):

    """A Serial Item and Contribution Identifier, the ANSI/NISO Z39.56-1996 StandardIdentifier for components of serials."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SICI')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 1507, 4)
    _Documentation = 'A Serial Item and Contribution Identifier, the ANSI/NISO Z39.56-1996 StandardIdentifier for components of serials.'
SICI._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'SICI', SICI)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}SoftwareType
class SoftwareType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Software."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SoftwareType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 1513, 4)
    _Documentation = 'A Type of Software.'
SoftwareType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SoftwareType, enum_prefix=None)
SoftwareType.InteractiveBooklet = SoftwareType._CF_enumeration.addEnumeration(unicode_value='InteractiveBooklet', tag='InteractiveBooklet')
SoftwareType.MusicalWorkBasedGame = SoftwareType._CF_enumeration.addEnumeration(unicode_value='MusicalWorkBasedGame', tag='MusicalWorkBasedGame')
SoftwareType.NonMusicalWorkBasedGame = SoftwareType._CF_enumeration.addEnumeration(unicode_value='NonMusicalWorkBasedGame', tag='NonMusicalWorkBasedGame')
SoftwareType.Screensaver = SoftwareType._CF_enumeration.addEnumeration(unicode_value='Screensaver', tag='Screensaver')
SoftwareType.Unknown = SoftwareType._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
SoftwareType.UserDefined = SoftwareType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
SoftwareType._InitializeFacetMap(SoftwareType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'SoftwareType', SoftwareType)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}SoundProcessorType
class SoundProcessorType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of sound processor."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SoundProcessorType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 1526, 4)
    _Documentation = 'A Type of sound processor.'
SoundProcessorType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SoundProcessorType, enum_prefix=None)
SoundProcessorType.MidiProcessor = SoundProcessorType._CF_enumeration.addEnumeration(unicode_value='MidiProcessor', tag='MidiProcessor')
SoundProcessorType.Unknown = SoundProcessorType._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
SoundProcessorType.UserDefined = SoundProcessorType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
SoundProcessorType._InitializeFacetMap(SoundProcessorType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'SoundProcessorType', SoundProcessorType)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}SoundRecordingCollectionReference
class SoundRecordingCollectionReference (pyxb.binding.datatypes.IDREF):

    """A Reference to a Collection which is contained within a specific Release."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SoundRecordingCollectionReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 1536, 4)
    _Documentation = 'A Reference to a Collection which is contained within a specific Release.'
SoundRecordingCollectionReference._CF_pattern = pyxb.binding.facets.CF_pattern()
SoundRecordingCollectionReference._CF_pattern.addPattern(pattern='X[\\d\\-_a-zA-Z]+')
SoundRecordingCollectionReference._InitializeFacetMap(SoundRecordingCollectionReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'SoundRecordingCollectionReference', SoundRecordingCollectionReference)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}SoundRecordingType
class SoundRecordingType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of SoundRecording."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SoundRecordingType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 1544, 4)
    _Documentation = 'A Type of SoundRecording.'
SoundRecordingType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SoundRecordingType, enum_prefix=None)
SoundRecordingType.MusicalWorkReadalongSoundRecording = SoundRecordingType._CF_enumeration.addEnumeration(unicode_value='MusicalWorkReadalongSoundRecording', tag='MusicalWorkReadalongSoundRecording')
SoundRecordingType.MusicalWorkSoundRecording = SoundRecordingType._CF_enumeration.addEnumeration(unicode_value='MusicalWorkSoundRecording', tag='MusicalWorkSoundRecording')
SoundRecordingType.NonMusicalWorkReadalongSoundRecording = SoundRecordingType._CF_enumeration.addEnumeration(unicode_value='NonMusicalWorkReadalongSoundRecording', tag='NonMusicalWorkReadalongSoundRecording')
SoundRecordingType.NonMusicalWorkSoundRecording = SoundRecordingType._CF_enumeration.addEnumeration(unicode_value='NonMusicalWorkSoundRecording', tag='NonMusicalWorkSoundRecording')
SoundRecordingType.Unknown = SoundRecordingType._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
SoundRecordingType.UserDefined = SoundRecordingType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
SoundRecordingType._InitializeFacetMap(SoundRecordingType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'SoundRecordingType', SoundRecordingType)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}TaxScope
class TaxScope (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Tax according to its scope."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TaxScope')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 1557, 4)
    _Documentation = 'A Type of Tax according to its scope.'
TaxScope._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TaxScope, enum_prefix=None)
TaxScope.CombinedTax = TaxScope._CF_enumeration.addEnumeration(unicode_value='CombinedTax', tag='CombinedTax')
TaxScope.FederalTax = TaxScope._CF_enumeration.addEnumeration(unicode_value='FederalTax', tag='FederalTax')
TaxScope.LocalTax = TaxScope._CF_enumeration.addEnumeration(unicode_value='LocalTax', tag='LocalTax')
TaxScope.ProvincialTax = TaxScope._CF_enumeration.addEnumeration(unicode_value='ProvincialTax', tag='ProvincialTax')
TaxScope.StateTax = TaxScope._CF_enumeration.addEnumeration(unicode_value='StateTax', tag='StateTax')
TaxScope.UserDefined = TaxScope._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
TaxScope._InitializeFacetMap(TaxScope._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TaxScope', TaxScope)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}TaxType
class TaxType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Tax."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TaxType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 1570, 4)
    _Documentation = 'A Type of Tax.'
TaxType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TaxType, enum_prefix=None)
TaxType.CombinedTax = TaxType._CF_enumeration.addEnumeration(unicode_value='CombinedTax', tag='CombinedTax')
TaxType.SalesTax = TaxType._CF_enumeration.addEnumeration(unicode_value='SalesTax', tag='SalesTax')
TaxType.ServiceTax = TaxType._CF_enumeration.addEnumeration(unicode_value='ServiceTax', tag='ServiceTax')
TaxType.SourceTax = TaxType._CF_enumeration.addEnumeration(unicode_value='SourceTax', tag='SourceTax')
TaxType.UserDefined = TaxType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
TaxType._InitializeFacetMap(TaxType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TaxType', TaxType)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}TechnicalResourceDetailsReference
class TechnicalResourceDetailsReference (pyxb.binding.datatypes.ID):

    """An Identifier of a Composite specifying technical details of a Resource which is specific to a DdexMessage."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TechnicalResourceDetailsReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 1582, 4)
    _Documentation = 'An Identifier of a Composite specifying technical details of a Resource which is specific to a DdexMessage.'
TechnicalResourceDetailsReference._CF_pattern = pyxb.binding.facets.CF_pattern()
TechnicalResourceDetailsReference._CF_pattern.addPattern(pattern='T[\\d\\-_a-zA-Z]+')
TechnicalResourceDetailsReference._InitializeFacetMap(TechnicalResourceDetailsReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'TechnicalResourceDetailsReference', TechnicalResourceDetailsReference)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}TextCodecType
class TextCodecType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of TextCodec."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TextCodecType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 1590, 4)
    _Documentation = 'A Type of TextCodec.'
TextCodecType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TextCodecType, enum_prefix=None)
TextCodecType.ASCII = TextCodecType._CF_enumeration.addEnumeration(unicode_value='ASCII', tag='ASCII')
TextCodecType.HTML = TextCodecType._CF_enumeration.addEnumeration(unicode_value='HTML', tag='HTML')
TextCodecType.PDF = TextCodecType._CF_enumeration.addEnumeration(unicode_value='PDF', tag='PDF')
TextCodecType.PostScript = TextCodecType._CF_enumeration.addEnumeration(unicode_value='PostScript', tag='PostScript')
TextCodecType.RTF = TextCodecType._CF_enumeration.addEnumeration(unicode_value='RTF', tag='RTF')
TextCodecType.Unknown = TextCodecType._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
TextCodecType.UserDefined = TextCodecType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
TextCodecType._InitializeFacetMap(TextCodecType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TextCodecType', TextCodecType)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}TextType
class TextType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Text."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TextType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 1604, 4)
    _Documentation = 'A Type of Text.'
TextType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TextType, enum_prefix=None)
TextType.EBook = TextType._CF_enumeration.addEnumeration(unicode_value='EBook', tag='EBook')
TextType.LinerNotes = TextType._CF_enumeration.addEnumeration(unicode_value='LinerNotes', tag='LinerNotes')
TextType.LyricText = TextType._CF_enumeration.addEnumeration(unicode_value='LyricText', tag='LyricText')
TextType.NonInteractiveBooklet = TextType._CF_enumeration.addEnumeration(unicode_value='NonInteractiveBooklet', tag='NonInteractiveBooklet')
TextType.TextDocument = TextType._CF_enumeration.addEnumeration(unicode_value='TextDocument', tag='TextDocument')
TextType.Unknown = TextType._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
TextType.UserDefined = TextType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
TextType._InitializeFacetMap(TextType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TextType', TextType)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}ThemeType
class ThemeType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Theme."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ThemeType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 1618, 4)
    _Documentation = 'A Type of Theme.'
ThemeType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ThemeType, enum_prefix=None)
ThemeType.ClosingTheme = ThemeType._CF_enumeration.addEnumeration(unicode_value='ClosingTheme', tag='ClosingTheme')
ThemeType.MainTheme = ThemeType._CF_enumeration.addEnumeration(unicode_value='MainTheme', tag='MainTheme')
ThemeType.OpeningTheme = ThemeType._CF_enumeration.addEnumeration(unicode_value='OpeningTheme', tag='OpeningTheme')
ThemeType.SegmentTheme = ThemeType._CF_enumeration.addEnumeration(unicode_value='SegmentTheme', tag='SegmentTheme')
ThemeType.TitleTheme = ThemeType._CF_enumeration.addEnumeration(unicode_value='TitleTheme', tag='TitleTheme')
ThemeType.UserDefined = ThemeType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
ThemeType._InitializeFacetMap(ThemeType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ThemeType', ThemeType)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}TitleType
class TitleType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Title which defines its origin, form or the function it fulfils in relation to a Creation. Note: A Title may fulfil more than one role. Example: "Help" may be both the OriginalTitle and the DisplayTitle for the well-known Beatles song."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TitleType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 1631, 4)
    _Documentation = 'A Type of Title which defines its origin, form or the function it fulfils in relation to a Creation. Note: A Title may fulfil more than one role. Example: "Help" may be both the OriginalTitle and the DisplayTitle for the well-known Beatles song.'
TitleType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TitleType, enum_prefix=None)
TitleType.AbbreviatedDisplayTitle = TitleType._CF_enumeration.addEnumeration(unicode_value='AbbreviatedDisplayTitle', tag='AbbreviatedDisplayTitle')
TitleType.AlternativeTitle = TitleType._CF_enumeration.addEnumeration(unicode_value='AlternativeTitle', tag='AlternativeTitle')
TitleType.DisplayTitle = TitleType._CF_enumeration.addEnumeration(unicode_value='DisplayTitle', tag='DisplayTitle')
TitleType.FirstLineOfText = TitleType._CF_enumeration.addEnumeration(unicode_value='FirstLineOfText', tag='FirstLineOfText')
TitleType.FormalTitle = TitleType._CF_enumeration.addEnumeration(unicode_value='FormalTitle', tag='FormalTitle')
TitleType.GroupingTitle = TitleType._CF_enumeration.addEnumeration(unicode_value='GroupingTitle', tag='GroupingTitle')
TitleType.IncorrectTitle = TitleType._CF_enumeration.addEnumeration(unicode_value='IncorrectTitle', tag='IncorrectTitle')
TitleType.MisspelledTitle = TitleType._CF_enumeration.addEnumeration(unicode_value='MisspelledTitle', tag='MisspelledTitle')
TitleType.OriginalTitle = TitleType._CF_enumeration.addEnumeration(unicode_value='OriginalTitle', tag='OriginalTitle')
TitleType.SearchTitle = TitleType._CF_enumeration.addEnumeration(unicode_value='SearchTitle', tag='SearchTitle')
TitleType.SortingTitle = TitleType._CF_enumeration.addEnumeration(unicode_value='SortingTitle', tag='SortingTitle')
TitleType.TitleAsPart = TitleType._CF_enumeration.addEnumeration(unicode_value='TitleAsPart', tag='TitleAsPart')
TitleType.TitleWithoutPunctuation = TitleType._CF_enumeration.addEnumeration(unicode_value='TitleWithoutPunctuation', tag='TitleWithoutPunctuation')
TitleType.TranslatedTitle = TitleType._CF_enumeration.addEnumeration(unicode_value='TranslatedTitle', tag='TranslatedTitle')
TitleType.Unknown = TitleType._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
TitleType.UserDefined = TitleType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
TitleType._InitializeFacetMap(TitleType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TitleType', TitleType)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}UnitOfBitRate
class UnitOfBitRate (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A UnitOfMeasure for a BitRate."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UnitOfBitRate')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 1654, 4)
    _Documentation = 'A UnitOfMeasure for a BitRate.'
UnitOfBitRate._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=UnitOfBitRate, enum_prefix=None)
UnitOfBitRate.bps = UnitOfBitRate._CF_enumeration.addEnumeration(unicode_value='bps', tag='bps')
UnitOfBitRate.Gbps = UnitOfBitRate._CF_enumeration.addEnumeration(unicode_value='Gbps', tag='Gbps')
UnitOfBitRate.kbps = UnitOfBitRate._CF_enumeration.addEnumeration(unicode_value='kbps', tag='kbps')
UnitOfBitRate.Mbps = UnitOfBitRate._CF_enumeration.addEnumeration(unicode_value='Mbps', tag='Mbps')
UnitOfBitRate._InitializeFacetMap(UnitOfBitRate._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'UnitOfBitRate', UnitOfBitRate)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}UnitOfExtent
class UnitOfExtent (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A UnitOfMeasure for an Extent."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UnitOfExtent')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 1665, 4)
    _Documentation = 'A UnitOfMeasure for an Extent.'
UnitOfExtent._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=UnitOfExtent, enum_prefix=None)
UnitOfExtent.cm = UnitOfExtent._CF_enumeration.addEnumeration(unicode_value='cm', tag='cm')
UnitOfExtent.Inch = UnitOfExtent._CF_enumeration.addEnumeration(unicode_value='Inch', tag='Inch')
UnitOfExtent.mm = UnitOfExtent._CF_enumeration.addEnumeration(unicode_value='mm', tag='mm')
UnitOfExtent.PercentOfScreen = UnitOfExtent._CF_enumeration.addEnumeration(unicode_value='PercentOfScreen', tag='PercentOfScreen')
UnitOfExtent.Pixel = UnitOfExtent._CF_enumeration.addEnumeration(unicode_value='Pixel', tag='Pixel')
UnitOfExtent._InitializeFacetMap(UnitOfExtent._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'UnitOfExtent', UnitOfExtent)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}UnitOfFrameRate
class UnitOfFrameRate (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A UnitOfMeasure for a FrameRate."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UnitOfFrameRate')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 1677, 4)
    _Documentation = 'A UnitOfMeasure for a FrameRate.'
UnitOfFrameRate._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=UnitOfFrameRate, enum_prefix=None)
UnitOfFrameRate.Hzinterlaced = UnitOfFrameRate._CF_enumeration.addEnumeration(unicode_value='Hz(interlaced)', tag='Hzinterlaced')
UnitOfFrameRate.Hznon_interlaced = UnitOfFrameRate._CF_enumeration.addEnumeration(unicode_value='Hz(non-interlaced)', tag='Hznon_interlaced')
UnitOfFrameRate._InitializeFacetMap(UnitOfFrameRate._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'UnitOfFrameRate', UnitOfFrameRate)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}UnitOfFrequency
class UnitOfFrequency (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A UnitOfMeasure for a frequency."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UnitOfFrequency')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 1686, 4)
    _Documentation = 'A UnitOfMeasure for a frequency.'
UnitOfFrequency._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=UnitOfFrequency, enum_prefix=None)
UnitOfFrequency.GHz = UnitOfFrequency._CF_enumeration.addEnumeration(unicode_value='GHz', tag='GHz')
UnitOfFrequency.Hz = UnitOfFrequency._CF_enumeration.addEnumeration(unicode_value='Hz', tag='Hz')
UnitOfFrequency.kHz = UnitOfFrequency._CF_enumeration.addEnumeration(unicode_value='kHz', tag='kHz')
UnitOfFrequency.MHz = UnitOfFrequency._CF_enumeration.addEnumeration(unicode_value='MHz', tag='MHz')
UnitOfFrequency._InitializeFacetMap(UnitOfFrequency._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'UnitOfFrequency', UnitOfFrequency)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}UpdateIndicator
class UpdateIndicator (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Message according to whether the Message contains original data or updates to previously sent data."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UpdateIndicator')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 1697, 4)
    _Documentation = 'A Type of Message according to whether the Message contains original data or updates to previously sent data.'
UpdateIndicator._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=UpdateIndicator, enum_prefix=None)
UpdateIndicator.OriginalMessage = UpdateIndicator._CF_enumeration.addEnumeration(unicode_value='OriginalMessage', tag='OriginalMessage')
UpdateIndicator.UpdateMessage = UpdateIndicator._CF_enumeration.addEnumeration(unicode_value='UpdateMessage', tag='UpdateMessage')
UpdateIndicator._InitializeFacetMap(UpdateIndicator._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'UpdateIndicator', UpdateIndicator)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}UserInterfaceType
class UserInterfaceType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of physical interface by which a Consumer uses a Service or Release."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UserInterfaceType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 1706, 4)
    _Documentation = 'A Type of physical interface by which a Consumer uses a Service or Release.'
UserInterfaceType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=UserInterfaceType, enum_prefix=None)
UserInterfaceType.AsPerContract = UserInterfaceType._CF_enumeration.addEnumeration(unicode_value='AsPerContract', tag='AsPerContract')
UserInterfaceType.ConnectedDevice = UserInterfaceType._CF_enumeration.addEnumeration(unicode_value='ConnectedDevice', tag='ConnectedDevice')
UserInterfaceType.GameConsole = UserInterfaceType._CF_enumeration.addEnumeration(unicode_value='GameConsole', tag='GameConsole')
UserInterfaceType.Jukebox = UserInterfaceType._CF_enumeration.addEnumeration(unicode_value='Jukebox', tag='Jukebox')
UserInterfaceType.KaraokeMachine = UserInterfaceType._CF_enumeration.addEnumeration(unicode_value='KaraokeMachine', tag='KaraokeMachine')
UserInterfaceType.Kiosk = UserInterfaceType._CF_enumeration.addEnumeration(unicode_value='Kiosk', tag='Kiosk')
UserInterfaceType.LocalStorageJukebox = UserInterfaceType._CF_enumeration.addEnumeration(unicode_value='LocalStorageJukebox', tag='LocalStorageJukebox')
UserInterfaceType.PersonalComputer = UserInterfaceType._CF_enumeration.addEnumeration(unicode_value='PersonalComputer', tag='PersonalComputer')
UserInterfaceType.PhysicalMediaWriter = UserInterfaceType._CF_enumeration.addEnumeration(unicode_value='PhysicalMediaWriter', tag='PhysicalMediaWriter')
UserInterfaceType.PortableDevice = UserInterfaceType._CF_enumeration.addEnumeration(unicode_value='PortableDevice', tag='PortableDevice')
UserInterfaceType.RemoteStorageJukebox = UserInterfaceType._CF_enumeration.addEnumeration(unicode_value='RemoteStorageJukebox', tag='RemoteStorageJukebox')
UserInterfaceType.Unknown = UserInterfaceType._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
UserInterfaceType.UserDefined = UserInterfaceType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
UserInterfaceType._InitializeFacetMap(UserInterfaceType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'UserInterfaceType', UserInterfaceType)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}UseType
class UseType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of a nature of a Service, or a Release, as used by a Consumer."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UseType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 1726, 4)
    _Documentation = 'A Type of a nature of a Service, or a Release, as used by a Consumer.'
UseType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=UseType, enum_prefix=None)
UseType.AsPerContract = UseType._CF_enumeration.addEnumeration(unicode_value='AsPerContract', tag='AsPerContract')
UseType.ConditionalDownload = UseType._CF_enumeration.addEnumeration(unicode_value='ConditionalDownload', tag='ConditionalDownload')
UseType.ContentInfluencedStream = UseType._CF_enumeration.addEnumeration(unicode_value='ContentInfluencedStream', tag='ContentInfluencedStream')
UseType.Display = UseType._CF_enumeration.addEnumeration(unicode_value='Display', tag='Display')
UseType.Download = UseType._CF_enumeration.addEnumeration(unicode_value='Download', tag='Download')
UseType.Narrowcast = UseType._CF_enumeration.addEnumeration(unicode_value='Narrowcast', tag='Narrowcast')
UseType.NonInteractiveStream = UseType._CF_enumeration.addEnumeration(unicode_value='NonInteractiveStream', tag='NonInteractiveStream')
UseType.OnDemandStream = UseType._CF_enumeration.addEnumeration(unicode_value='OnDemandStream', tag='OnDemandStream')
UseType.PermanentDownload = UseType._CF_enumeration.addEnumeration(unicode_value='PermanentDownload', tag='PermanentDownload')
UseType.PlayInPublic = UseType._CF_enumeration.addEnumeration(unicode_value='PlayInPublic', tag='PlayInPublic')
UseType.Podcast = UseType._CF_enumeration.addEnumeration(unicode_value='Podcast', tag='Podcast')
UseType.Print = UseType._CF_enumeration.addEnumeration(unicode_value='Print', tag='Print')
UseType.Rent = UseType._CF_enumeration.addEnumeration(unicode_value='Rent', tag='Rent')
UseType.TimeInfluencedStream = UseType._CF_enumeration.addEnumeration(unicode_value='TimeInfluencedStream', tag='TimeInfluencedStream')
UseType.Unknown = UseType._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
UseType.UseAsAlertTone = UseType._CF_enumeration.addEnumeration(unicode_value='UseAsAlertTone', tag='UseAsAlertTone')
UseType.UseAsKaraoke = UseType._CF_enumeration.addEnumeration(unicode_value='UseAsKaraoke', tag='UseAsKaraoke')
UseType.UseAsRingbackTone = UseType._CF_enumeration.addEnumeration(unicode_value='UseAsRingbackTone', tag='UseAsRingbackTone')
UseType.UseAsRingtone = UseType._CF_enumeration.addEnumeration(unicode_value='UseAsRingtone', tag='UseAsRingtone')
UseType.UseAsScreensaver = UseType._CF_enumeration.addEnumeration(unicode_value='UseAsScreensaver', tag='UseAsScreensaver')
UseType.UserDefined = UseType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
UseType.UserMakeAvailableLabelProvided = UseType._CF_enumeration.addEnumeration(unicode_value='UserMakeAvailableLabelProvided', tag='UserMakeAvailableLabelProvided')
UseType.UserMakeAvailableUserProvided = UseType._CF_enumeration.addEnumeration(unicode_value='UserMakeAvailableUserProvided', tag='UserMakeAvailableUserProvided')
UseType.Webcast = UseType._CF_enumeration.addEnumeration(unicode_value='Webcast', tag='Webcast')
UseType._InitializeFacetMap(UseType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'UseType', UseType)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}ValueType
class ValueType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of RoyaltyRate."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ValueType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 1757, 4)
    _Documentation = 'A Type of RoyaltyRate.'
ValueType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ValueType, enum_prefix=None)
ValueType.Calculated = ValueType._CF_enumeration.addEnumeration(unicode_value='Calculated', tag='Calculated')
ValueType.Maximum = ValueType._CF_enumeration.addEnumeration(unicode_value='Maximum', tag='Maximum')
ValueType.Minimum = ValueType._CF_enumeration.addEnumeration(unicode_value='Minimum', tag='Minimum')
ValueType._InitializeFacetMap(ValueType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ValueType', ValueType)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}VideoCodecType
class VideoCodecType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of VideoCodec."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VideoCodecType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 1767, 4)
    _Documentation = 'A Type of VideoCodec.'
VideoCodecType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=VideoCodecType, enum_prefix=None)
VideoCodecType.AVC = VideoCodecType._CF_enumeration.addEnumeration(unicode_value='AVC', tag='AVC')
VideoCodecType.H_261 = VideoCodecType._CF_enumeration.addEnumeration(unicode_value='H.261', tag='H_261')
VideoCodecType.H_263 = VideoCodecType._CF_enumeration.addEnumeration(unicode_value='H.263', tag='H_263')
VideoCodecType.MPEG_1 = VideoCodecType._CF_enumeration.addEnumeration(unicode_value='MPEG-1', tag='MPEG_1')
VideoCodecType.MPEG_2 = VideoCodecType._CF_enumeration.addEnumeration(unicode_value='MPEG-2', tag='MPEG_2')
VideoCodecType.MPEG_4 = VideoCodecType._CF_enumeration.addEnumeration(unicode_value='MPEG-4', tag='MPEG_4')
VideoCodecType.QuickTime = VideoCodecType._CF_enumeration.addEnumeration(unicode_value='QuickTime', tag='QuickTime')
VideoCodecType.RealVideo = VideoCodecType._CF_enumeration.addEnumeration(unicode_value='RealVideo', tag='RealVideo')
VideoCodecType.Unknown = VideoCodecType._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
VideoCodecType.UserDefined = VideoCodecType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
VideoCodecType.WMV = VideoCodecType._CF_enumeration.addEnumeration(unicode_value='WMV', tag='WMV')
VideoCodecType._InitializeFacetMap(VideoCodecType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'VideoCodecType', VideoCodecType)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}VideoCueSheetReference
class VideoCueSheetReference (pyxb.binding.datatypes.IDREF):

    """A Reference to a CueSheet which is contained within a specific Video."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VideoCueSheetReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 1785, 4)
    _Documentation = 'A Reference to a CueSheet which is contained within a specific Video.'
VideoCueSheetReference._CF_pattern = pyxb.binding.facets.CF_pattern()
VideoCueSheetReference._CF_pattern.addPattern(pattern='Q[\\d\\-_a-zA-Z]+')
VideoCueSheetReference._InitializeFacetMap(VideoCueSheetReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'VideoCueSheetReference', VideoCueSheetReference)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}VideoDefinitionType
class VideoDefinitionType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of resolution (or definition) in which a Video is provided."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VideoDefinitionType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 1793, 4)
    _Documentation = 'A Type of resolution (or definition) in which a Video is provided.'
VideoDefinitionType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=VideoDefinitionType, enum_prefix=None)
VideoDefinitionType.HighDefinition = VideoDefinitionType._CF_enumeration.addEnumeration(unicode_value='HighDefinition', tag='HighDefinition')
VideoDefinitionType.StandardDefinition = VideoDefinitionType._CF_enumeration.addEnumeration(unicode_value='StandardDefinition', tag='StandardDefinition')
VideoDefinitionType._InitializeFacetMap(VideoDefinitionType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'VideoDefinitionType', VideoDefinitionType)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}VideoType
class VideoType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Video."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VideoType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 1802, 4)
    _Documentation = 'A Type of Video.'
VideoType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=VideoType, enum_prefix=None)
VideoType.AdvertisementVideo = VideoType._CF_enumeration.addEnumeration(unicode_value='AdvertisementVideo', tag='AdvertisementVideo')
VideoType.Animation = VideoType._CF_enumeration.addEnumeration(unicode_value='Animation', tag='Animation')
VideoType.ConcertClip = VideoType._CF_enumeration.addEnumeration(unicode_value='ConcertClip', tag='ConcertClip')
VideoType.ConcertVideo = VideoType._CF_enumeration.addEnumeration(unicode_value='ConcertVideo', tag='ConcertVideo')
VideoType.CorporateFilm = VideoType._CF_enumeration.addEnumeration(unicode_value='CorporateFilm', tag='CorporateFilm')
VideoType.Documentary = VideoType._CF_enumeration.addEnumeration(unicode_value='Documentary', tag='Documentary')
VideoType.Episode = VideoType._CF_enumeration.addEnumeration(unicode_value='Episode', tag='Episode')
VideoType.FeatureFilm = VideoType._CF_enumeration.addEnumeration(unicode_value='FeatureFilm', tag='FeatureFilm')
VideoType.InfomercialVideo = VideoType._CF_enumeration.addEnumeration(unicode_value='InfomercialVideo', tag='InfomercialVideo')
VideoType.Karaoke = VideoType._CF_enumeration.addEnumeration(unicode_value='Karaoke', tag='Karaoke')
VideoType.LiveEventVideo = VideoType._CF_enumeration.addEnumeration(unicode_value='LiveEventVideo', tag='LiveEventVideo')
VideoType.LongFormMusicalWorkVideo = VideoType._CF_enumeration.addEnumeration(unicode_value='LongFormMusicalWorkVideo', tag='LongFormMusicalWorkVideo')
VideoType.LongFormNonMusicalWorkVideo = VideoType._CF_enumeration.addEnumeration(unicode_value='LongFormNonMusicalWorkVideo', tag='LongFormNonMusicalWorkVideo')
VideoType.Menu = VideoType._CF_enumeration.addEnumeration(unicode_value='Menu', tag='Menu')
VideoType.MusicalWorkClip = VideoType._CF_enumeration.addEnumeration(unicode_value='MusicalWorkClip', tag='MusicalWorkClip')
VideoType.MusicalWorkReadalongVideo = VideoType._CF_enumeration.addEnumeration(unicode_value='MusicalWorkReadalongVideo', tag='MusicalWorkReadalongVideo')
VideoType.MusicalWorkTrailer = VideoType._CF_enumeration.addEnumeration(unicode_value='MusicalWorkTrailer', tag='MusicalWorkTrailer')
VideoType.MusicalWorkVideoChapter = VideoType._CF_enumeration.addEnumeration(unicode_value='MusicalWorkVideoChapter', tag='MusicalWorkVideoChapter')
VideoType.News = VideoType._CF_enumeration.addEnumeration(unicode_value='News', tag='News')
VideoType.NonMusicalWorkClip = VideoType._CF_enumeration.addEnumeration(unicode_value='NonMusicalWorkClip', tag='NonMusicalWorkClip')
VideoType.NonMusicalWorkReadalongVideo = VideoType._CF_enumeration.addEnumeration(unicode_value='NonMusicalWorkReadalongVideo', tag='NonMusicalWorkReadalongVideo')
VideoType.NonMusicalWorkTrailer = VideoType._CF_enumeration.addEnumeration(unicode_value='NonMusicalWorkTrailer', tag='NonMusicalWorkTrailer')
VideoType.NonMusicalWorkVideoChapter = VideoType._CF_enumeration.addEnumeration(unicode_value='NonMusicalWorkVideoChapter', tag='NonMusicalWorkVideoChapter')
VideoType.NonSerialAudioVisualRecording = VideoType._CF_enumeration.addEnumeration(unicode_value='NonSerialAudioVisualRecording', tag='NonSerialAudioVisualRecording')
VideoType.Season = VideoType._CF_enumeration.addEnumeration(unicode_value='Season', tag='Season')
VideoType.Series = VideoType._CF_enumeration.addEnumeration(unicode_value='Series', tag='Series')
VideoType.ShortFormMusicalWorkVideo = VideoType._CF_enumeration.addEnumeration(unicode_value='ShortFormMusicalWorkVideo', tag='ShortFormMusicalWorkVideo')
VideoType.ShortFormNonMusicalWorkVideo = VideoType._CF_enumeration.addEnumeration(unicode_value='ShortFormNonMusicalWorkVideo', tag='ShortFormNonMusicalWorkVideo')
VideoType.TrailerVideo = VideoType._CF_enumeration.addEnumeration(unicode_value='TrailerVideo', tag='TrailerVideo')
VideoType.Unknown = VideoType._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
VideoType.UserDefined = VideoType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
VideoType.VideoChapter = VideoType._CF_enumeration.addEnumeration(unicode_value='VideoChapter', tag='VideoChapter')
VideoType._InitializeFacetMap(VideoType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'VideoType', VideoType)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}VisualPerceptionType
class VisualPerceptionType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of MusicalCreation according to how it is experienced in an AudioVisual Creation."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VisualPerceptionType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 1841, 4)
    _Documentation = 'A Type of MusicalCreation according to how it is experienced in an AudioVisual Creation.'
VisualPerceptionType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=VisualPerceptionType, enum_prefix=None)
VisualPerceptionType.Background = VisualPerceptionType._CF_enumeration.addEnumeration(unicode_value='Background', tag='Background')
VisualPerceptionType.UserDefined = VisualPerceptionType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
VisualPerceptionType.Visual = VisualPerceptionType._CF_enumeration.addEnumeration(unicode_value='Visual', tag='Visual')
VisualPerceptionType._InitializeFacetMap(VisualPerceptionType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'VisualPerceptionType', VisualPerceptionType)

# Atomic simple type: {http://ddex.net/xml/20100121/ddex}VocalType
class VocalType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of a MusicalCreation according to the occurrence of vocals."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VocalType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20100121/ddex.xsd', 1851, 4)
    _Documentation = 'A Type of a MusicalCreation according to the occurrence of vocals.'
VocalType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=VocalType, enum_prefix=None)
VocalType.Instrumental = VocalType._CF_enumeration.addEnumeration(unicode_value='Instrumental', tag='Instrumental')
VocalType.UserDefined = VocalType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
VocalType.Vocal = VocalType._CF_enumeration.addEnumeration(unicode_value='Vocal', tag='Vocal')
VocalType._InitializeFacetMap(VocalType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'VocalType', VocalType)
