# ./_avs.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:7160bdf2eec8b2464ee2e1193e7abcc5a3221f95
# Generated 2015-07-06 15:58:03.784491 by PyXB version 1.2.4 using Python 2.7.6.final.0
# Namespace http://ddex.net/xml/avs/avs [xmlns:avs]

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:b747fe78-23f7-11e5-9249-080027960975')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://ddex.net/xml/avs/avs', create_if_missing=True)
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


# Atomic simple type: {http://ddex.net/xml/avs/avs}AccessLimitation
class AccessLimitation (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of limitation on the access of a site."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AccessLimitation')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 13, 3)
    _Documentation = 'A Type of limitation on the access of a site.'
AccessLimitation._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=AccessLimitation, enum_prefix=None)
AccessLimitation.NoLimitation = AccessLimitation._CF_enumeration.addEnumeration(unicode_value='NoLimitation', tag='NoLimitation')
AccessLimitation.PrivateAccessOnly = AccessLimitation._CF_enumeration.addEnumeration(unicode_value='PrivateAccessOnly', tag='PrivateAccessOnly')
AccessLimitation._InitializeFacetMap(AccessLimitation._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'AccessLimitation', AccessLimitation)

# Atomic simple type: {http://ddex.net/xml/avs/avs}AdministratingRecordCompanyRole
class AdministratingRecordCompanyRole (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A role played by a Party responsible for administering Rights in a Resource or a Release."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AdministratingRecordCompanyRole')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 30, 3)
    _Documentation = 'A role played by a Party responsible for administering Rights in a Resource or a Release.'
AdministratingRecordCompanyRole._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=AdministratingRecordCompanyRole, enum_prefix=None)
AdministratingRecordCompanyRole.DesignatedDsrMessageRecipient = AdministratingRecordCompanyRole._CF_enumeration.addEnumeration(unicode_value='DesignatedDsrMessageRecipient', tag='DesignatedDsrMessageRecipient')
AdministratingRecordCompanyRole.RightsAdministrator = AdministratingRecordCompanyRole._CF_enumeration.addEnumeration(unicode_value='RightsAdministrator', tag='RightsAdministrator')
AdministratingRecordCompanyRole.RoyaltyAdministrator = AdministratingRecordCompanyRole._CF_enumeration.addEnumeration(unicode_value='RoyaltyAdministrator', tag='RoyaltyAdministrator')
AdministratingRecordCompanyRole.Unknown = AdministratingRecordCompanyRole._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
AdministratingRecordCompanyRole.UserDefined = AdministratingRecordCompanyRole._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
AdministratingRecordCompanyRole._InitializeFacetMap(AdministratingRecordCompanyRole._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'AdministratingRecordCompanyRole', AdministratingRecordCompanyRole)

# Atomic simple type: {http://ddex.net/xml/avs/avs}ArtistRole
class ArtistRole (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A role of a principal Contributor in relation to a Performance or a Fixation."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ArtistRole')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 68, 3)
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
ArtistRole.Dancer = ArtistRole._CF_enumeration.addEnumeration(unicode_value='Dancer', tag='Dancer')
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
ArtistRole.Narrator = ArtistRole._CF_enumeration.addEnumeration(unicode_value='Narrator', tag='Narrator')
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
ArtistRole.StudioMusician = ArtistRole._CF_enumeration.addEnumeration(unicode_value='StudioMusician', tag='StudioMusician')
ArtistRole.StudioPersonnel = ArtistRole._CF_enumeration.addEnumeration(unicode_value='StudioPersonnel', tag='StudioPersonnel')
ArtistRole.SubArranger = ArtistRole._CF_enumeration.addEnumeration(unicode_value='SubArranger', tag='SubArranger')
ArtistRole.Translator = ArtistRole._CF_enumeration.addEnumeration(unicode_value='Translator', tag='Translator')
ArtistRole.Unknown = ArtistRole._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
ArtistRole.UserDefined = ArtistRole._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
ArtistRole._InitializeFacetMap(ArtistRole._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ArtistRole', ArtistRole)

# Atomic simple type: {http://ddex.net/xml/avs/avs}AudioCodecType
class AudioCodecType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of AudioCodec."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AudioCodecType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 310, 3)
    _Documentation = 'A Type of AudioCodec.'
AudioCodecType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=AudioCodecType, enum_prefix=None)
AudioCodecType.AAC = AudioCodecType._CF_enumeration.addEnumeration(unicode_value='AAC', tag='AAC')
AudioCodecType.ADPCM = AudioCodecType._CF_enumeration.addEnumeration(unicode_value='ADPCM', tag='ADPCM')
AudioCodecType.ALaw = AudioCodecType._CF_enumeration.addEnumeration(unicode_value='ALaw', tag='ALaw')
AudioCodecType.AMR_NB = AudioCodecType._CF_enumeration.addEnumeration(unicode_value='AMR-NB', tag='AMR_NB')
AudioCodecType.AMR_WB = AudioCodecType._CF_enumeration.addEnumeration(unicode_value='AMR-WB', tag='AMR_WB')
AudioCodecType.FLAC = AudioCodecType._CF_enumeration.addEnumeration(unicode_value='FLAC', tag='FLAC')
AudioCodecType.MP2 = AudioCodecType._CF_enumeration.addEnumeration(unicode_value='MP2', tag='MP2')
AudioCodecType.MP3 = AudioCodecType._CF_enumeration.addEnumeration(unicode_value='MP3', tag='MP3')
AudioCodecType.MuLaw = AudioCodecType._CF_enumeration.addEnumeration(unicode_value='MuLaw', tag='MuLaw')
AudioCodecType.PCM = AudioCodecType._CF_enumeration.addEnumeration(unicode_value='PCM', tag='PCM')
AudioCodecType.PDM = AudioCodecType._CF_enumeration.addEnumeration(unicode_value='PDM', tag='PDM')
AudioCodecType.QCELP = AudioCodecType._CF_enumeration.addEnumeration(unicode_value='QCELP', tag='QCELP')
AudioCodecType.RealAudio = AudioCodecType._CF_enumeration.addEnumeration(unicode_value='RealAudio', tag='RealAudio')
AudioCodecType.Shockwave = AudioCodecType._CF_enumeration.addEnumeration(unicode_value='Shockwave', tag='Shockwave')
AudioCodecType.Unknown = AudioCodecType._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
AudioCodecType.UserDefined = AudioCodecType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
AudioCodecType.Vorbis = AudioCodecType._CF_enumeration.addEnumeration(unicode_value='Vorbis', tag='Vorbis')
AudioCodecType.WMA = AudioCodecType._CF_enumeration.addEnumeration(unicode_value='WMA', tag='WMA')
AudioCodecType._InitializeFacetMap(AudioCodecType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'AudioCodecType', AudioCodecType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}BinaryDataType
class BinaryDataType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A format of a Fingerprint."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BinaryDataType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 407, 3)
    _Documentation = 'A format of a Fingerprint.'
BinaryDataType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=BinaryDataType, enum_prefix=None)
BinaryDataType.Binary64 = BinaryDataType._CF_enumeration.addEnumeration(unicode_value='Binary64', tag='Binary64')
BinaryDataType.HexBinary = BinaryDataType._CF_enumeration.addEnumeration(unicode_value='HexBinary', tag='HexBinary')
BinaryDataType._InitializeFacetMap(BinaryDataType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'BinaryDataType', BinaryDataType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}BusinessContributorRole
class BusinessContributorRole (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A business-related role played by a Contributor in relation to a MusicalWork."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BusinessContributorRole')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 424, 3)
    _Documentation = 'A business-related role played by a Contributor in relation to a MusicalWork.'
BusinessContributorRole._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=BusinessContributorRole, enum_prefix=None)
BusinessContributorRole.Contributor = BusinessContributorRole._CF_enumeration.addEnumeration(unicode_value='Contributor', tag='Contributor')
BusinessContributorRole.MusicPublisher = BusinessContributorRole._CF_enumeration.addEnumeration(unicode_value='MusicPublisher', tag='MusicPublisher')
BusinessContributorRole.OriginalPublisher = BusinessContributorRole._CF_enumeration.addEnumeration(unicode_value='OriginalPublisher', tag='OriginalPublisher')
BusinessContributorRole.SubPublisher = BusinessContributorRole._CF_enumeration.addEnumeration(unicode_value='SubPublisher', tag='SubPublisher')
BusinessContributorRole.SubstitutedPublisher = BusinessContributorRole._CF_enumeration.addEnumeration(unicode_value='SubstitutedPublisher', tag='SubstitutedPublisher')
BusinessContributorRole.Unknown = BusinessContributorRole._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
BusinessContributorRole.UserDefined = BusinessContributorRole._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
BusinessContributorRole._InitializeFacetMap(BusinessContributorRole._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'BusinessContributorRole', BusinessContributorRole)

# Atomic simple type: {http://ddex.net/xml/avs/avs}CalculationType
class CalculationType (pyxb.binding.datatypes.string):

    """A Type of Calculation used to determine an actual Amount paid."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CalculationType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 466, 3)
    _Documentation = 'A Type of Calculation used to determine an actual Amount paid.'
CalculationType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'CalculationType', CalculationType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}CarrierType
class CarrierType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Carrier used for a Fixation."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CarrierType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 472, 3)
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
CarrierType.UserDefined = CarrierType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
CarrierType.VhsNTSC = CarrierType._CF_enumeration.addEnumeration(unicode_value='VhsNTSC', tag='VhsNTSC')
CarrierType.VhsPAL = CarrierType._CF_enumeration.addEnumeration(unicode_value='VhsPAL', tag='VhsPAL')
CarrierType.VhsPlusCdLp = CarrierType._CF_enumeration.addEnumeration(unicode_value='VhsPlusCdLp', tag='VhsPlusCdLp')
CarrierType.VhsSECAM = CarrierType._CF_enumeration.addEnumeration(unicode_value='VhsSECAM', tag='VhsSECAM')
CarrierType._InitializeFacetMap(CarrierType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CarrierType', CarrierType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}CdProtectionType
class CdProtectionType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of CD protection."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CdProtectionType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 1024, 3)
    _Documentation = 'A Type of CD protection.'
CdProtectionType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CdProtectionType, enum_prefix=None)
CdProtectionType.CDS100 = CdProtectionType._CF_enumeration.addEnumeration(unicode_value='CDS100', tag='CDS100')
CdProtectionType.CDS200 = CdProtectionType._CF_enumeration.addEnumeration(unicode_value='CDS200', tag='CDS200')
CdProtectionType.CDS300 = CdProtectionType._CF_enumeration.addEnumeration(unicode_value='CDS300', tag='CDS300')
CdProtectionType.Key2Audio = CdProtectionType._CF_enumeration.addEnumeration(unicode_value='Key2Audio', tag='Key2Audio')
CdProtectionType.MediaMaxCD3 = CdProtectionType._CF_enumeration.addEnumeration(unicode_value='MediaMaxCD3', tag='MediaMaxCD3')
CdProtectionType.NotProtected = CdProtectionType._CF_enumeration.addEnumeration(unicode_value='NotProtected', tag='NotProtected')
CdProtectionType.Unknown = CdProtectionType._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
CdProtectionType.UserDefined = CdProtectionType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
CdProtectionType._InitializeFacetMap(CdProtectionType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CdProtectionType', CdProtectionType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}CharacterType
class CharacterType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of a Character."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CharacterType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 1071, 3)
    _Documentation = 'A Type of a Character.'
CharacterType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CharacterType, enum_prefix=None)
CharacterType.MainCharacter = CharacterType._CF_enumeration.addEnumeration(unicode_value='MainCharacter', tag='MainCharacter')
CharacterType.OtherCharacter = CharacterType._CF_enumeration.addEnumeration(unicode_value='OtherCharacter', tag='OtherCharacter')
CharacterType.SupportingCharacter = CharacterType._CF_enumeration.addEnumeration(unicode_value='SupportingCharacter', tag='SupportingCharacter')
CharacterType._InitializeFacetMap(CharacterType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CharacterType', CharacterType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}CodingType
class CodingType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of coding used to encode a Resource."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CodingType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 1093, 3)
    _Documentation = 'A Type of coding used to encode a Resource.'
CodingType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CodingType, enum_prefix=None)
CodingType.Lossless = CodingType._CF_enumeration.addEnumeration(unicode_value='Lossless', tag='Lossless')
CodingType.Lossy = CodingType._CF_enumeration.addEnumeration(unicode_value='Lossy', tag='Lossy')
CodingType._InitializeFacetMap(CodingType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CodingType', CodingType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}CollectionType
class CollectionType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Collection."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CollectionType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 1110, 3)
    _Documentation = 'A Type of Collection.'
CollectionType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CollectionType, enum_prefix=None)
CollectionType.AudioChapter = CollectionType._CF_enumeration.addEnumeration(unicode_value='AudioChapter', tag='AudioChapter')
CollectionType.Episode = CollectionType._CF_enumeration.addEnumeration(unicode_value='Episode', tag='Episode')
CollectionType.FilmBundle = CollectionType._CF_enumeration.addEnumeration(unicode_value='FilmBundle', tag='FilmBundle')
CollectionType.MedleySegment = CollectionType._CF_enumeration.addEnumeration(unicode_value='MedleySegment', tag='MedleySegment')
CollectionType.PotpourriSegment = CollectionType._CF_enumeration.addEnumeration(unicode_value='PotpourriSegment', tag='PotpourriSegment')
CollectionType.Season = CollectionType._CF_enumeration.addEnumeration(unicode_value='Season', tag='Season')
CollectionType.Series = CollectionType._CF_enumeration.addEnumeration(unicode_value='Series', tag='Series')
CollectionType.VideoChapter = CollectionType._CF_enumeration.addEnumeration(unicode_value='VideoChapter', tag='VideoChapter')
CollectionType._InitializeFacetMap(CollectionType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CollectionType', CollectionType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}CommercialModelType
class CommercialModelType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of CommercialModel (e.g. SubscriptionModel and PayAsYouGoModel). The CommercialModelType indicates how a Consumer pays for a Service or Release."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CommercialModelType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 1157, 3)
    _Documentation = 'A Type of CommercialModel (e.g. SubscriptionModel and PayAsYouGoModel). The CommercialModelType indicates how a Consumer pays for a Service or Release.'
CommercialModelType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CommercialModelType, enum_prefix=None)
CommercialModelType.AdvertisementSupportedModel = CommercialModelType._CF_enumeration.addEnumeration(unicode_value='AdvertisementSupportedModel', tag='AdvertisementSupportedModel')
CommercialModelType.AsPerContract = CommercialModelType._CF_enumeration.addEnumeration(unicode_value='AsPerContract', tag='AsPerContract')
CommercialModelType.DeviceFeeModel = CommercialModelType._CF_enumeration.addEnumeration(unicode_value='DeviceFeeModel', tag='DeviceFeeModel')
CommercialModelType.FreeOfChargeModel = CommercialModelType._CF_enumeration.addEnumeration(unicode_value='FreeOfChargeModel', tag='FreeOfChargeModel')
CommercialModelType.PayAsYouGoModel = CommercialModelType._CF_enumeration.addEnumeration(unicode_value='PayAsYouGoModel', tag='PayAsYouGoModel')
CommercialModelType.PerformanceRoyaltiesModel = CommercialModelType._CF_enumeration.addEnumeration(unicode_value='PerformanceRoyaltiesModel', tag='PerformanceRoyaltiesModel')
CommercialModelType.RightsClaimModel = CommercialModelType._CF_enumeration.addEnumeration(unicode_value='RightsClaimModel', tag='RightsClaimModel')
CommercialModelType.SubscriptionModel = CommercialModelType._CF_enumeration.addEnumeration(unicode_value='SubscriptionModel', tag='SubscriptionModel')
CommercialModelType.Unknown = CommercialModelType._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
CommercialModelType.UserDefined = CommercialModelType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
CommercialModelType._InitializeFacetMap(CommercialModelType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CommercialModelType', CommercialModelType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}CompilationType
class CompilationType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Compilation."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CompilationType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 1214, 3)
    _Documentation = 'A Type of Compilation.'
CompilationType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CompilationType, enum_prefix=None)
CompilationType.InternalCompilation = CompilationType._CF_enumeration.addEnumeration(unicode_value='InternalCompilation', tag='InternalCompilation')
CompilationType.NonInternalCompilation = CompilationType._CF_enumeration.addEnumeration(unicode_value='NonInternalCompilation', tag='NonInternalCompilation')
CompilationType.NotCompiled = CompilationType._CF_enumeration.addEnumeration(unicode_value='NotCompiled', tag='NotCompiled')
CompilationType._InitializeFacetMap(CompilationType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CompilationType', CompilationType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}ContainerFormat
class ContainerFormat (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of container according to its FileFormat."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ContainerFormat')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 1236, 3)
    _Documentation = 'A Type of container according to its FileFormat.'
ContainerFormat._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ContainerFormat, enum_prefix=None)
ContainerFormat.AIFF = ContainerFormat._CF_enumeration.addEnumeration(unicode_value='AIFF', tag='AIFF')
ContainerFormat.AVI = ContainerFormat._CF_enumeration.addEnumeration(unicode_value='AVI', tag='AVI')
ContainerFormat.MP4 = ContainerFormat._CF_enumeration.addEnumeration(unicode_value='MP4', tag='MP4')
ContainerFormat.Ogg = ContainerFormat._CF_enumeration.addEnumeration(unicode_value='Ogg', tag='Ogg')
ContainerFormat.QuickTime = ContainerFormat._CF_enumeration.addEnumeration(unicode_value='QuickTime', tag='QuickTime')
ContainerFormat.RealMedia = ContainerFormat._CF_enumeration.addEnumeration(unicode_value='RealMedia', tag='RealMedia')
ContainerFormat.RMF = ContainerFormat._CF_enumeration.addEnumeration(unicode_value='RMF', tag='RMF')
ContainerFormat.UserDefined = ContainerFormat._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
ContainerFormat.WAV = ContainerFormat._CF_enumeration.addEnumeration(unicode_value='WAV', tag='WAV')
ContainerFormat._InitializeFacetMap(ContainerFormat._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ContainerFormat', ContainerFormat)

# Atomic simple type: {http://ddex.net/xml/avs/avs}CreationType
class CreationType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Creation."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CreationType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 1288, 3)
    _Documentation = 'A Type of Creation.'
CreationType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CreationType, enum_prefix=None)
CreationType.MusicalWork = CreationType._CF_enumeration.addEnumeration(unicode_value='MusicalWork', tag='MusicalWork')
CreationType.Release = CreationType._CF_enumeration.addEnumeration(unicode_value='Release', tag='Release')
CreationType.Resource = CreationType._CF_enumeration.addEnumeration(unicode_value='Resource', tag='Resource')
CreationType._InitializeFacetMap(CreationType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CreationType', CreationType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}CreativeContributorRole
class CreativeContributorRole (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A creative role played by a Contributor in relation to a MusicalWork."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CreativeContributorRole')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 1310, 3)
    _Documentation = 'A creative role played by a Contributor in relation to a MusicalWork.'
CreativeContributorRole._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CreativeContributorRole, enum_prefix=None)
CreativeContributorRole.Adapter = CreativeContributorRole._CF_enumeration.addEnumeration(unicode_value='Adapter', tag='Adapter')
CreativeContributorRole.Arranger = CreativeContributorRole._CF_enumeration.addEnumeration(unicode_value='Arranger', tag='Arranger')
CreativeContributorRole.AssociatedPerformer = CreativeContributorRole._CF_enumeration.addEnumeration(unicode_value='AssociatedPerformer', tag='AssociatedPerformer')
CreativeContributorRole.Author = CreativeContributorRole._CF_enumeration.addEnumeration(unicode_value='Author', tag='Author')
CreativeContributorRole.Composer = CreativeContributorRole._CF_enumeration.addEnumeration(unicode_value='Composer', tag='Composer')
CreativeContributorRole.ComposerLyricist = CreativeContributorRole._CF_enumeration.addEnumeration(unicode_value='ComposerLyricist', tag='ComposerLyricist')
CreativeContributorRole.Librettist = CreativeContributorRole._CF_enumeration.addEnumeration(unicode_value='Librettist', tag='Librettist')
CreativeContributorRole.Lyricist = CreativeContributorRole._CF_enumeration.addEnumeration(unicode_value='Lyricist', tag='Lyricist')
CreativeContributorRole.NonLyricAuthor = CreativeContributorRole._CF_enumeration.addEnumeration(unicode_value='NonLyricAuthor', tag='NonLyricAuthor')
CreativeContributorRole.SubArranger = CreativeContributorRole._CF_enumeration.addEnumeration(unicode_value='SubArranger', tag='SubArranger')
CreativeContributorRole.SubLyricist = CreativeContributorRole._CF_enumeration.addEnumeration(unicode_value='SubLyricist', tag='SubLyricist')
CreativeContributorRole.Translator = CreativeContributorRole._CF_enumeration.addEnumeration(unicode_value='Translator', tag='Translator')
CreativeContributorRole._InitializeFacetMap(CreativeContributorRole._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CreativeContributorRole', CreativeContributorRole)

# Atomic simple type: {http://ddex.net/xml/avs/avs}CueOrigin
class CueOrigin (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Cue according to its origin."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CueOrigin')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 1377, 3)
    _Documentation = 'A Type of Cue according to its origin.'
CueOrigin._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CueOrigin, enum_prefix=None)
CueOrigin.LibraryMusic = CueOrigin._CF_enumeration.addEnumeration(unicode_value='LibraryMusic', tag='LibraryMusic')
CueOrigin.PreexistingMusic = CueOrigin._CF_enumeration.addEnumeration(unicode_value='PreexistingMusic', tag='PreexistingMusic')
CueOrigin.SpeciallyCommissionedMusic = CueOrigin._CF_enumeration.addEnumeration(unicode_value='SpeciallyCommissionedMusic', tag='SpeciallyCommissionedMusic')
CueOrigin.Unknown = CueOrigin._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
CueOrigin.UserDefined = CueOrigin._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
CueOrigin._InitializeFacetMap(CueOrigin._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CueOrigin', CueOrigin)

# Atomic simple type: {http://ddex.net/xml/avs/avs}CueSheetType
class CueSheetType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of CueSheet."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CueSheetType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 1409, 3)
    _Documentation = 'A Type of CueSheet.'
CueSheetType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CueSheetType, enum_prefix=None)
CueSheetType.AverageCueSheet = CueSheetType._CF_enumeration.addEnumeration(unicode_value='AverageCueSheet', tag='AverageCueSheet')
CueSheetType.CompositeCueSheet = CueSheetType._CF_enumeration.addEnumeration(unicode_value='CompositeCueSheet', tag='CompositeCueSheet')
CueSheetType.StandardCueSheet = CueSheetType._CF_enumeration.addEnumeration(unicode_value='StandardCueSheet', tag='StandardCueSheet')
CueSheetType.SummarisedCueSheet = CueSheetType._CF_enumeration.addEnumeration(unicode_value='SummarisedCueSheet', tag='SummarisedCueSheet')
CueSheetType.SurrogateCueSheet = CueSheetType._CF_enumeration.addEnumeration(unicode_value='SurrogateCueSheet', tag='SurrogateCueSheet')
CueSheetType._InitializeFacetMap(CueSheetType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CueSheetType', CueSheetType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}CueUseType
class CueUseType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of use of a Cue."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CueUseType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 1441, 3)
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

# Atomic simple type: {http://ddex.net/xml/avs/avs}DataMismatchResponseType
class DataMismatchResponseType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of action that is a response to a DataMismatch."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DataMismatchResponseType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 1510, 3)
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

# Atomic simple type: {http://ddex.net/xml/avs/avs}DataMismatchStatus
class DataMismatchStatus (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Status of a DataMismatch."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DataMismatchStatus')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 1547, 3)
    _Documentation = 'A Status of a DataMismatch.'
DataMismatchStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DataMismatchStatus, enum_prefix=None)
DataMismatchStatus.AdditionalInformationOnly = DataMismatchStatus._CF_enumeration.addEnumeration(unicode_value='AdditionalInformationOnly', tag='AdditionalInformationOnly')
DataMismatchStatus.Corrected = DataMismatchStatus._CF_enumeration.addEnumeration(unicode_value='Corrected', tag='Corrected')
DataMismatchStatus.Fatal = DataMismatchStatus._CF_enumeration.addEnumeration(unicode_value='Fatal', tag='Fatal')
DataMismatchStatus.NotCorrected = DataMismatchStatus._CF_enumeration.addEnumeration(unicode_value='NotCorrected', tag='NotCorrected')
DataMismatchStatus.UserDefined = DataMismatchStatus._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
DataMismatchStatus._InitializeFacetMap(DataMismatchStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DataMismatchStatus', DataMismatchStatus)

# Atomic simple type: {http://ddex.net/xml/avs/avs}DataMismatchType
class DataMismatchType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of DataMismatch."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DataMismatchType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 1579, 3)
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

# Atomic simple type: {http://ddex.net/xml/avs/avs}DdexTerritoryCode
class DdexTerritoryCode (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A TerritoryId which is not a TerritoryId according to the ISO 3166-1 standard or the TIS standard."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DdexTerritoryCode')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 1691, 3)
    _Documentation = 'A TerritoryId which is not a TerritoryId according to the ISO 3166-1 standard or the TIS standard.'
DdexTerritoryCode._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DdexTerritoryCode, enum_prefix=None)
DdexTerritoryCode.Worldwide = DdexTerritoryCode._CF_enumeration.addEnumeration(unicode_value='Worldwide', tag='Worldwide')
DdexTerritoryCode._InitializeFacetMap(DdexTerritoryCode._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DdexTerritoryCode', DdexTerritoryCode)

# Atomic simple type: {http://ddex.net/xml/avs/avs}DeductionRateType
class DeductionRateType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of DeductionRate."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DeductionRateType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 1703, 3)
    _Documentation = 'A Type of DeductionRate.'
DeductionRateType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DeductionRateType, enum_prefix=None)
DeductionRateType.PennyRate = DeductionRateType._CF_enumeration.addEnumeration(unicode_value='PennyRate', tag='PennyRate')
DeductionRateType.PercentageRate = DeductionRateType._CF_enumeration.addEnumeration(unicode_value='PercentageRate', tag='PercentageRate')
DeductionRateType.UserDefined = DeductionRateType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
DeductionRateType._InitializeFacetMap(DeductionRateType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DeductionRateType', DeductionRateType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}DeliveryActionType
class DeliveryActionType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of action requested for deliveries."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DeliveryActionType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 1725, 3)
    _Documentation = 'A Type of action requested for deliveries.'
DeliveryActionType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DeliveryActionType, enum_prefix=None)
DeliveryActionType.ChangeDeliveryLimits = DeliveryActionType._CF_enumeration.addEnumeration(unicode_value='ChangeDeliveryLimits', tag='ChangeDeliveryLimits')
DeliveryActionType.RestartDeliveryWithLimits = DeliveryActionType._CF_enumeration.addEnumeration(unicode_value='RestartDeliveryWithLimits', tag='RestartDeliveryWithLimits')
DeliveryActionType.RestartDeliveryWithPreviousLimits = DeliveryActionType._CF_enumeration.addEnumeration(unicode_value='RestartDeliveryWithPreviousLimits', tag='RestartDeliveryWithPreviousLimits')
DeliveryActionType.StopDelivery = DeliveryActionType._CF_enumeration.addEnumeration(unicode_value='StopDelivery', tag='StopDelivery')
DeliveryActionType._InitializeFacetMap(DeliveryActionType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DeliveryActionType', DeliveryActionType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}DeliveryMessageType
class DeliveryMessageType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of delivery Message."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DeliveryMessageType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 1752, 3)
    _Documentation = 'A Type of delivery Message.'
DeliveryMessageType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DeliveryMessageType, enum_prefix=None)
DeliveryMessageType.NewReleaseMessage = DeliveryMessageType._CF_enumeration.addEnumeration(unicode_value='NewReleaseMessage', tag='NewReleaseMessage')
DeliveryMessageType.NonDdexMessage = DeliveryMessageType._CF_enumeration.addEnumeration(unicode_value='NonDdexMessage', tag='NonDdexMessage')
DeliveryMessageType.Unknown = DeliveryMessageType._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
DeliveryMessageType._InitializeFacetMap(DeliveryMessageType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DeliveryMessageType', DeliveryMessageType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}DeprecatedCurrencyCode
class DeprecatedCurrencyCode (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A CurrencyCode which is not valid anymore."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DeprecatedCurrencyCode')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 1774, 3)
    _Documentation = 'A CurrencyCode which is not valid anymore.'
DeprecatedCurrencyCode._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DeprecatedCurrencyCode, enum_prefix=None)
DeprecatedCurrencyCode.CYP = DeprecatedCurrencyCode._CF_enumeration.addEnumeration(unicode_value='CYP', tag='CYP')
DeprecatedCurrencyCode.EEK = DeprecatedCurrencyCode._CF_enumeration.addEnumeration(unicode_value='EEK', tag='EEK')
DeprecatedCurrencyCode.MTL = DeprecatedCurrencyCode._CF_enumeration.addEnumeration(unicode_value='MTL', tag='MTL')
DeprecatedCurrencyCode.ROL = DeprecatedCurrencyCode._CF_enumeration.addEnumeration(unicode_value='ROL', tag='ROL')
DeprecatedCurrencyCode.SIT = DeprecatedCurrencyCode._CF_enumeration.addEnumeration(unicode_value='SIT', tag='SIT')
DeprecatedCurrencyCode.SKK = DeprecatedCurrencyCode._CF_enumeration.addEnumeration(unicode_value='SKK', tag='SKK')
DeprecatedCurrencyCode._InitializeFacetMap(DeprecatedCurrencyCode._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DeprecatedCurrencyCode', DeprecatedCurrencyCode)

# Atomic simple type: {http://ddex.net/xml/avs/avs}DeprecatedIsoTerritoryCode
class DeprecatedIsoTerritoryCode (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An ISO 3166-3 four-letter code representing a Territory, which is a replacement for a deprecated ISO 3166-1 code."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DeprecatedIsoTerritoryCode')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 1811, 3)
    _Documentation = 'An ISO 3166-3 four-letter code representing a Territory, which is a replacement for a deprecated ISO 3166-1 code.'
DeprecatedIsoTerritoryCode._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DeprecatedIsoTerritoryCode, enum_prefix=None)
DeprecatedIsoTerritoryCode.AIDJ = DeprecatedIsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='AIDJ', tag='AIDJ')
DeprecatedIsoTerritoryCode.ANHH = DeprecatedIsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='ANHH', tag='ANHH')
DeprecatedIsoTerritoryCode.BQAQ = DeprecatedIsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='BQAQ', tag='BQAQ')
DeprecatedIsoTerritoryCode.BUMM = DeprecatedIsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='BUMM', tag='BUMM')
DeprecatedIsoTerritoryCode.BYAA = DeprecatedIsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='BYAA', tag='BYAA')
DeprecatedIsoTerritoryCode.CSHH = DeprecatedIsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='CSHH', tag='CSHH')
DeprecatedIsoTerritoryCode.CSXX = DeprecatedIsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='CSXX', tag='CSXX')
DeprecatedIsoTerritoryCode.CTKI = DeprecatedIsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='CTKI', tag='CTKI')
DeprecatedIsoTerritoryCode.DDDE = DeprecatedIsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='DDDE', tag='DDDE')
DeprecatedIsoTerritoryCode.DYBJ = DeprecatedIsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='DYBJ', tag='DYBJ')
DeprecatedIsoTerritoryCode.FQHH = DeprecatedIsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='FQHH', tag='FQHH')
DeprecatedIsoTerritoryCode.FXFR = DeprecatedIsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='FXFR', tag='FXFR')
DeprecatedIsoTerritoryCode.GEHH = DeprecatedIsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='GEHH', tag='GEHH')
DeprecatedIsoTerritoryCode.HVBF = DeprecatedIsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='HVBF', tag='HVBF')
DeprecatedIsoTerritoryCode.JTUM = DeprecatedIsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='JTUM', tag='JTUM')
DeprecatedIsoTerritoryCode.MIUM = DeprecatedIsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='MIUM', tag='MIUM')
DeprecatedIsoTerritoryCode.NHVU = DeprecatedIsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='NHVU', tag='NHVU')
DeprecatedIsoTerritoryCode.NQAQ = DeprecatedIsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='NQAQ', tag='NQAQ')
DeprecatedIsoTerritoryCode.NTHH = DeprecatedIsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='NTHH', tag='NTHH')
DeprecatedIsoTerritoryCode.PCHH = DeprecatedIsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='PCHH', tag='PCHH')
DeprecatedIsoTerritoryCode.PUUM = DeprecatedIsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='PUUM', tag='PUUM')
DeprecatedIsoTerritoryCode.PZPA = DeprecatedIsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='PZPA', tag='PZPA')
DeprecatedIsoTerritoryCode.RHZW = DeprecatedIsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='RHZW', tag='RHZW')
DeprecatedIsoTerritoryCode.SKIN = DeprecatedIsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='SKIN', tag='SKIN')
DeprecatedIsoTerritoryCode.SUHH = DeprecatedIsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='SUHH', tag='SUHH')
DeprecatedIsoTerritoryCode.TPTL = DeprecatedIsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='TPTL', tag='TPTL')
DeprecatedIsoTerritoryCode.VDVN = DeprecatedIsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='VDVN', tag='VDVN')
DeprecatedIsoTerritoryCode.WKUM = DeprecatedIsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='WKUM', tag='WKUM')
DeprecatedIsoTerritoryCode.YDYE = DeprecatedIsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='YDYE', tag='YDYE')
DeprecatedIsoTerritoryCode.YUCS = DeprecatedIsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='YUCS', tag='YUCS')
DeprecatedIsoTerritoryCode.ZRCD = DeprecatedIsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='ZRCD', tag='ZRCD')
DeprecatedIsoTerritoryCode._InitializeFacetMap(DeprecatedIsoTerritoryCode._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DeprecatedIsoTerritoryCode', DeprecatedIsoTerritoryCode)

# Atomic simple type: {http://ddex.net/xml/avs/avs}DigitizationMode
class DigitizationMode (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Digitization mode of a Resource."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DigitizationMode')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 1973, 3)
    _Documentation = 'A Digitization mode of a Resource.'
DigitizationMode._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DigitizationMode, enum_prefix=None)
DigitizationMode.AAD = DigitizationMode._CF_enumeration.addEnumeration(unicode_value='AAD', tag='AAD')
DigitizationMode.ADD = DigitizationMode._CF_enumeration.addEnumeration(unicode_value='ADD', tag='ADD')
DigitizationMode.DDD = DigitizationMode._CF_enumeration.addEnumeration(unicode_value='DDD', tag='DDD')
DigitizationMode.Unknown = DigitizationMode._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
DigitizationMode._InitializeFacetMap(DigitizationMode._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DigitizationMode', DigitizationMode)

# Atomic simple type: {http://ddex.net/xml/avs/avs}DisputeReason
class DisputeReason (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of reason for a Dispute."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DisputeReason')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 2000, 3)
    _Documentation = 'A Type of reason for a Dispute.'
DisputeReason._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DisputeReason, enum_prefix=None)
DisputeReason.MissingInformation = DisputeReason._CF_enumeration.addEnumeration(unicode_value='MissingInformation', tag='MissingInformation')
DisputeReason.NotPartOfCatalogTransfer = DisputeReason._CF_enumeration.addEnumeration(unicode_value='NotPartOfCatalogTransfer', tag='NotPartOfCatalogTransfer')
DisputeReason.MoreResearchNeeded = DisputeReason._CF_enumeration.addEnumeration(unicode_value='MoreResearchNeeded', tag='MoreResearchNeeded')
DisputeReason.UserDefined = DisputeReason._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
DisputeReason._InitializeFacetMap(DisputeReason._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DisputeReason', DisputeReason)

# Atomic simple type: {http://ddex.net/xml/avs/avs}DistributionChannelType
class DistributionChannelType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of DistributionChannel used to disseminate a Service or Release to a Consumer."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DistributionChannelType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 2027, 3)
    _Documentation = 'A Type of DistributionChannel used to disseminate a Service or Release to a Consumer.'
DistributionChannelType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DistributionChannelType, enum_prefix=None)
DistributionChannelType.AsPerContract = DistributionChannelType._CF_enumeration.addEnumeration(unicode_value='AsPerContract', tag='AsPerContract')
DistributionChannelType.Broadcast = DistributionChannelType._CF_enumeration.addEnumeration(unicode_value='Broadcast', tag='Broadcast')
DistributionChannelType.Cable = DistributionChannelType._CF_enumeration.addEnumeration(unicode_value='Cable', tag='Cable')
DistributionChannelType.Internet = DistributionChannelType._CF_enumeration.addEnumeration(unicode_value='Internet', tag='Internet')
DistributionChannelType.InternetAndMobile = DistributionChannelType._CF_enumeration.addEnumeration(unicode_value='InternetAndMobile', tag='InternetAndMobile')
DistributionChannelType.IPTV = DistributionChannelType._CF_enumeration.addEnumeration(unicode_value='IPTV', tag='IPTV')
DistributionChannelType.MobileTelephone = DistributionChannelType._CF_enumeration.addEnumeration(unicode_value='MobileTelephone', tag='MobileTelephone')
DistributionChannelType.Narrowcast = DistributionChannelType._CF_enumeration.addEnumeration(unicode_value='Narrowcast', tag='Narrowcast')
DistributionChannelType.OnDemandStream = DistributionChannelType._CF_enumeration.addEnumeration(unicode_value='OnDemandStream', tag='OnDemandStream')
DistributionChannelType.PeerToPeer = DistributionChannelType._CF_enumeration.addEnumeration(unicode_value='PeerToPeer', tag='PeerToPeer')
DistributionChannelType.Physical = DistributionChannelType._CF_enumeration.addEnumeration(unicode_value='Physical', tag='Physical')
DistributionChannelType.Satellite = DistributionChannelType._CF_enumeration.addEnumeration(unicode_value='Satellite', tag='Satellite')
DistributionChannelType.Simulcast = DistributionChannelType._CF_enumeration.addEnumeration(unicode_value='Simulcast', tag='Simulcast')
DistributionChannelType.Unknown = DistributionChannelType._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
DistributionChannelType.UserDefined = DistributionChannelType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
DistributionChannelType.Webcast = DistributionChannelType._CF_enumeration.addEnumeration(unicode_value='Webcast', tag='Webcast')
DistributionChannelType._InitializeFacetMap(DistributionChannelType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DistributionChannelType', DistributionChannelType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}DpidStatus
class DpidStatus (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Status of a DdexPartyId."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DpidStatus')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 2114, 3)
    _Documentation = 'A Status of a DdexPartyId.'
DpidStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DpidStatus, enum_prefix=None)
DpidStatus.Active = DpidStatus._CF_enumeration.addEnumeration(unicode_value='Active', tag='Active')
DpidStatus.Deleted = DpidStatus._CF_enumeration.addEnumeration(unicode_value='Deleted', tag='Deleted')
DpidStatus.Replaced = DpidStatus._CF_enumeration.addEnumeration(unicode_value='Replaced', tag='Replaced')
DpidStatus._InitializeFacetMap(DpidStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DpidStatus', DpidStatus)

# Atomic simple type: {http://ddex.net/xml/avs/avs}DrmEnforcementType
class DrmEnforcementType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of DRM enforcement."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DrmEnforcementType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 2136, 3)
    _Documentation = 'A Type of DRM enforcement.'
DrmEnforcementType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DrmEnforcementType, enum_prefix=None)
DrmEnforcementType.DrmEnforced = DrmEnforcementType._CF_enumeration.addEnumeration(unicode_value='DrmEnforced', tag='DrmEnforced')
DrmEnforcementType.NotDrmEnforced = DrmEnforcementType._CF_enumeration.addEnumeration(unicode_value='NotDrmEnforced', tag='NotDrmEnforced')
DrmEnforcementType._InitializeFacetMap(DrmEnforcementType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DrmEnforcementType', DrmEnforcementType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}DrmPlatformType
class DrmPlatformType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of DrmPlatform."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DrmPlatformType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 2153, 3)
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

# Atomic simple type: {http://ddex.net/xml/avs/avs}DsrMessageType
class DsrMessageType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Message in the Sales Reporting Message Suite Standard."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DsrMessageType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 2190, 3)
    _Documentation = 'A Type of Message in the Sales Reporting Message Suite Standard.'
DsrMessageType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DsrMessageType, enum_prefix=None)
DsrMessageType.SalesReportToRecordCompanyMessage = DsrMessageType._CF_enumeration.addEnumeration(unicode_value='SalesReportToRecordCompanyMessage', tag='SalesReportToRecordCompanyMessage')
DsrMessageType.SalesReportToSocietyMessage = DsrMessageType._CF_enumeration.addEnumeration(unicode_value='SalesReportToSocietyMessage', tag='SalesReportToSocietyMessage')
DsrMessageType._InitializeFacetMap(DsrMessageType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DsrMessageType', DsrMessageType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}EquipmentType
class EquipmentType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Equipment."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'EquipmentType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 2207, 3)
    _Documentation = 'A Type of Equipment.'
EquipmentType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=EquipmentType, enum_prefix=None)
EquipmentType.Computer = EquipmentType._CF_enumeration.addEnumeration(unicode_value='Computer', tag='Computer')
EquipmentType.Microphone = EquipmentType._CF_enumeration.addEnumeration(unicode_value='Microphone', tag='Microphone')
EquipmentType.Recorder = EquipmentType._CF_enumeration.addEnumeration(unicode_value='Recorder', tag='Recorder')
EquipmentType.SignalProcessor = EquipmentType._CF_enumeration.addEnumeration(unicode_value='SignalProcessor', tag='SignalProcessor')
EquipmentType.Software = EquipmentType._CF_enumeration.addEnumeration(unicode_value='Software', tag='Software')
EquipmentType.Loudspeaker = EquipmentType._CF_enumeration.addEnumeration(unicode_value='Loudspeaker', tag='Loudspeaker')
EquipmentType._InitializeFacetMap(EquipmentType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'EquipmentType', EquipmentType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}ErnMessageType
class ErnMessageType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Message in the Release Notification Message Suite Standard."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ErnMessageType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 2244, 3)
    _Documentation = 'A Type of Message in the Release Notification Message Suite Standard.'
ErnMessageType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ErnMessageType, enum_prefix=None)
ErnMessageType.NewReleaseMessage = ErnMessageType._CF_enumeration.addEnumeration(unicode_value='NewReleaseMessage', tag='NewReleaseMessage')
ErnMessageType._InitializeFacetMap(ErnMessageType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ErnMessageType', ErnMessageType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}ErncFileStatus
class ErncFileStatus (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Status of a File in terms of its validity in the Release Delivery Choreography Standard."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ErncFileStatus')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 2256, 3)
    _Documentation = 'A Status of a File in terms of its validity in the Release Delivery Choreography Standard.'
ErncFileStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ErncFileStatus, enum_prefix=None)
ErncFileStatus.ArtistRoleUnknown = ErncFileStatus._CF_enumeration.addEnumeration(unicode_value='ArtistRoleUnknown', tag='ArtistRoleUnknown')
ErncFileStatus.CommercialReleaseDateInvalid = ErncFileStatus._CF_enumeration.addEnumeration(unicode_value='CommercialReleaseDateInvalid', tag='CommercialReleaseDateInvalid')
ErncFileStatus.ConflictingAvailabilityPeriods = ErncFileStatus._CF_enumeration.addEnumeration(unicode_value='ConflictingAvailabilityPeriods', tag='ConflictingAvailabilityPeriods')
ErncFileStatus.DuplicatedPublisherNames = ErncFileStatus._CF_enumeration.addEnumeration(unicode_value='DuplicatedPublisherNames', tag='DuplicatedPublisherNames')
ErncFileStatus.ErnMissing = ErncFileStatus._CF_enumeration.addEnumeration(unicode_value='ErnMissing', tag='ErnMissing')
ErncFileStatus.FileOK = ErncFileStatus._CF_enumeration.addEnumeration(unicode_value='FileOK', tag='FileOK')
ErncFileStatus.IdentifierInvalid = ErncFileStatus._CF_enumeration.addEnumeration(unicode_value='IdentifierInvalid', tag='IdentifierInvalid')
ErncFileStatus.IdentifierSyntaxInvalid = ErncFileStatus._CF_enumeration.addEnumeration(unicode_value='IdentifierSyntaxInvalid', tag='IdentifierSyntaxInvalid')
ErncFileStatus.InternalError = ErncFileStatus._CF_enumeration.addEnumeration(unicode_value='InternalError', tag='InternalError')
ErncFileStatus.MetadataMissing = ErncFileStatus._CF_enumeration.addEnumeration(unicode_value='MetadataMissing', tag='MetadataMissing')
ErncFileStatus.NewReleaseMessageInvalid = ErncFileStatus._CF_enumeration.addEnumeration(unicode_value='NewReleaseMessageInvalid', tag='NewReleaseMessageInvalid')
ErncFileStatus.NoDealForTrackRelease = ErncFileStatus._CF_enumeration.addEnumeration(unicode_value='NoDealForTrackRelease', tag='NoDealForTrackRelease')
ErncFileStatus.NoDealInNewReleaseMessage = ErncFileStatus._CF_enumeration.addEnumeration(unicode_value='NoDealInNewReleaseMessage', tag='NoDealInNewReleaseMessage')
ErncFileStatus.OriginalReleaseDateLaterThanReleaseDate = ErncFileStatus._CF_enumeration.addEnumeration(unicode_value='OriginalReleaseDateLaterThanReleaseDate', tag='OriginalReleaseDateLaterThanReleaseDate')
ErncFileStatus.PrimaryArtistNameMissing = ErncFileStatus._CF_enumeration.addEnumeration(unicode_value='PrimaryArtistNameMissing', tag='PrimaryArtistNameMissing')
ErncFileStatus.ResourceCorrupt = ErncFileStatus._CF_enumeration.addEnumeration(unicode_value='ResourceCorrupt', tag='ResourceCorrupt')
ErncFileStatus.ResourceMissing = ErncFileStatus._CF_enumeration.addEnumeration(unicode_value='ResourceMissing', tag='ResourceMissing')
ErncFileStatus.ResourceNotMeetingSpecifications = ErncFileStatus._CF_enumeration.addEnumeration(unicode_value='ResourceNotMeetingSpecifications', tag='ResourceNotMeetingSpecifications')
ErncFileStatus.SignatureOrHashSumWrongOrMissing = ErncFileStatus._CF_enumeration.addEnumeration(unicode_value='SignatureOrHashSumWrongOrMissing', tag='SignatureOrHashSumWrongOrMissing')
ErncFileStatus.UnsupportedUsage = ErncFileStatus._CF_enumeration.addEnumeration(unicode_value='UnsupportedUsage', tag='UnsupportedUsage')
ErncFileStatus.UserDefined = ErncFileStatus._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
ErncFileStatus._InitializeFacetMap(ErncFileStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ErncFileStatus', ErncFileStatus)

# Atomic simple type: {http://ddex.net/xml/avs/avs}ErncProposedActionType
class ErncProposedActionType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of action that is proposed."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ErncProposedActionType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 2368, 3)
    _Documentation = 'A Type of action that is proposed.'
ErncProposedActionType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ErncProposedActionType, enum_prefix=None)
ErncProposedActionType.ResendXmlOnly = ErncProposedActionType._CF_enumeration.addEnumeration(unicode_value='ResendXmlOnly', tag='ResendXmlOnly')
ErncProposedActionType.ResendXmlAndResources = ErncProposedActionType._CF_enumeration.addEnumeration(unicode_value='ResendXmlAndResources', tag='ResendXmlAndResources')
ErncProposedActionType.UserDefined = ErncProposedActionType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
ErncProposedActionType._InitializeFacetMap(ErncProposedActionType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ErncProposedActionType', ErncProposedActionType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}ExpressionType
class ExpressionType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of expression indicating how it should be perceived."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ExpressionType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 2390, 3)
    _Documentation = 'A Type of expression indicating how it should be perceived.'
ExpressionType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ExpressionType, enum_prefix=None)
ExpressionType.Informative = ExpressionType._CF_enumeration.addEnumeration(unicode_value='Informative', tag='Informative')
ExpressionType.Instructive = ExpressionType._CF_enumeration.addEnumeration(unicode_value='Instructive', tag='Instructive')
ExpressionType._InitializeFacetMap(ExpressionType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ExpressionType', ExpressionType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}ExternallyLinkedResourceType
class ExternallyLinkedResourceType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Resource pointed to by an ExternalLink."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ExternallyLinkedResourceType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 2407, 3)
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

# Atomic simple type: {http://ddex.net/xml/avs/avs}FileStatus
class FileStatus (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Status of a File in terms of its validity."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FileStatus')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 2449, 3)
    _Documentation = 'A Status of a File in terms of its validity.'
FileStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=FileStatus, enum_prefix=None)
FileStatus.FileMissing = FileStatus._CF_enumeration.addEnumeration(unicode_value='FileMissing', tag='FileMissing')
FileStatus.FileOK = FileStatus._CF_enumeration.addEnumeration(unicode_value='FileOK', tag='FileOK')
FileStatus.HashSumWrong = FileStatus._CF_enumeration.addEnumeration(unicode_value='HashSumWrong', tag='HashSumWrong')
FileStatus.SignatureWrong = FileStatus._CF_enumeration.addEnumeration(unicode_value='SignatureWrong', tag='SignatureWrong')
FileStatus._InitializeFacetMap(FileStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'FileStatus', FileStatus)

# Atomic simple type: {http://ddex.net/xml/avs/avs}FingerprintAlgorithmType
class FingerprintAlgorithmType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Fingerprint algorithm."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FingerprintAlgorithmType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 2476, 3)
    _Documentation = 'A Type of Fingerprint algorithm.'
FingerprintAlgorithmType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=FingerprintAlgorithmType, enum_prefix=None)
FingerprintAlgorithmType.UserDefined = FingerprintAlgorithmType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
FingerprintAlgorithmType._InitializeFacetMap(FingerprintAlgorithmType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'FingerprintAlgorithmType', FingerprintAlgorithmType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}GoverningAgreementType
class GoverningAgreementType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of governing agreement."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GoverningAgreementType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 2488, 3)
    _Documentation = 'A Type of governing agreement.'
GoverningAgreementType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=GoverningAgreementType, enum_prefix=None)
GoverningAgreementType.UserDefined = GoverningAgreementType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
GoverningAgreementType._InitializeFacetMap(GoverningAgreementType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'GoverningAgreementType', GoverningAgreementType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}HashSumAlgorithmType
class HashSumAlgorithmType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of HashSumAlgorithm."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'HashSumAlgorithmType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 2500, 3)
    _Documentation = 'A Type of HashSumAlgorithm.'
HashSumAlgorithmType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=HashSumAlgorithmType, enum_prefix=None)
HashSumAlgorithmType.MD4 = HashSumAlgorithmType._CF_enumeration.addEnumeration(unicode_value='MD4', tag='MD4')
HashSumAlgorithmType.MD5 = HashSumAlgorithmType._CF_enumeration.addEnumeration(unicode_value='MD5', tag='MD5')
HashSumAlgorithmType.SHA = HashSumAlgorithmType._CF_enumeration.addEnumeration(unicode_value='SHA', tag='SHA')
HashSumAlgorithmType.SHA1 = HashSumAlgorithmType._CF_enumeration.addEnumeration(unicode_value='SHA1', tag='SHA1')
HashSumAlgorithmType.UserDefined = HashSumAlgorithmType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
HashSumAlgorithmType._InitializeFacetMap(HashSumAlgorithmType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'HashSumAlgorithmType', HashSumAlgorithmType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}ImageCodecType
class ImageCodecType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of ImageCodec."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ImageCodecType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 2532, 3)
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

# Atomic simple type: {http://ddex.net/xml/avs/avs}ImageType
class ImageType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Image."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ImageType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 2574, 3)
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

# Atomic simple type: {http://ddex.net/xml/avs/avs}InvoiceAvailabilityStatus
class InvoiceAvailabilityStatus (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Status of the availability of an invoice."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InvoiceAvailabilityStatus')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 2651, 3)
    _Documentation = 'A Status of the availability of an invoice.'
InvoiceAvailabilityStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=InvoiceAvailabilityStatus, enum_prefix=None)
InvoiceAvailabilityStatus.InvoiceAvailable = InvoiceAvailabilityStatus._CF_enumeration.addEnumeration(unicode_value='InvoiceAvailable', tag='InvoiceAvailable')
InvoiceAvailabilityStatus.InvoiceNotAvailable = InvoiceAvailabilityStatus._CF_enumeration.addEnumeration(unicode_value='InvoiceNotAvailable', tag='InvoiceNotAvailable')
InvoiceAvailabilityStatus._InitializeFacetMap(InvoiceAvailabilityStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'InvoiceAvailabilityStatus', InvoiceAvailabilityStatus)

# Atomic simple type: {http://ddex.net/xml/avs/avs}IsoCurrencyCode
class IsoCurrencyCode (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An ISO4217 three-letter code representing a Currency."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'IsoCurrencyCode')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 2668, 3)
    _Documentation = 'An ISO4217 three-letter code representing a Currency.'
IsoCurrencyCode._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=IsoCurrencyCode, enum_prefix=None)
IsoCurrencyCode.AED = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='AED', tag='AED')
IsoCurrencyCode.AFN = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='AFN', tag='AFN')
IsoCurrencyCode.ALL = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='ALL', tag='ALL')
IsoCurrencyCode.AMD = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='AMD', tag='AMD')
IsoCurrencyCode.ANG = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='ANG', tag='ANG')
IsoCurrencyCode.AOA = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='AOA', tag='AOA')
IsoCurrencyCode.ARS = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='ARS', tag='ARS')
IsoCurrencyCode.AUD = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='AUD', tag='AUD')
IsoCurrencyCode.AWG = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='AWG', tag='AWG')
IsoCurrencyCode.AZN = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='AZN', tag='AZN')
IsoCurrencyCode.BAM = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='BAM', tag='BAM')
IsoCurrencyCode.BBD = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='BBD', tag='BBD')
IsoCurrencyCode.BDT = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='BDT', tag='BDT')
IsoCurrencyCode.BGN = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='BGN', tag='BGN')
IsoCurrencyCode.BHD = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='BHD', tag='BHD')
IsoCurrencyCode.BIF = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='BIF', tag='BIF')
IsoCurrencyCode.BMD = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='BMD', tag='BMD')
IsoCurrencyCode.BND = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='BND', tag='BND')
IsoCurrencyCode.BOB = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='BOB', tag='BOB')
IsoCurrencyCode.BOV = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='BOV', tag='BOV')
IsoCurrencyCode.BRL = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='BRL', tag='BRL')
IsoCurrencyCode.BSD = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='BSD', tag='BSD')
IsoCurrencyCode.BTN = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='BTN', tag='BTN')
IsoCurrencyCode.BWP = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='BWP', tag='BWP')
IsoCurrencyCode.BYR = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='BYR', tag='BYR')
IsoCurrencyCode.BZD = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='BZD', tag='BZD')
IsoCurrencyCode.CAD = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='CAD', tag='CAD')
IsoCurrencyCode.CDF = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='CDF', tag='CDF')
IsoCurrencyCode.CHF = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='CHF', tag='CHF')
IsoCurrencyCode.CLF = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='CLF', tag='CLF')
IsoCurrencyCode.CLP = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='CLP', tag='CLP')
IsoCurrencyCode.CNY = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='CNY', tag='CNY')
IsoCurrencyCode.COP = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='COP', tag='COP')
IsoCurrencyCode.COU = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='COU', tag='COU')
IsoCurrencyCode.CRC = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='CRC', tag='CRC')
IsoCurrencyCode.CUC = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='CUC', tag='CUC')
IsoCurrencyCode.CUP = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='CUP', tag='CUP')
IsoCurrencyCode.CVE = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='CVE', tag='CVE')
IsoCurrencyCode.CZK = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='CZK', tag='CZK')
IsoCurrencyCode.DJF = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='DJF', tag='DJF')
IsoCurrencyCode.DKK = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='DKK', tag='DKK')
IsoCurrencyCode.DOP = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='DOP', tag='DOP')
IsoCurrencyCode.DZD = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='DZD', tag='DZD')
IsoCurrencyCode.EGP = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='EGP', tag='EGP')
IsoCurrencyCode.ERN = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='ERN', tag='ERN')
IsoCurrencyCode.ETB = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='ETB', tag='ETB')
IsoCurrencyCode.EUR = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='EUR', tag='EUR')
IsoCurrencyCode.FJD = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='FJD', tag='FJD')
IsoCurrencyCode.FKP = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='FKP', tag='FKP')
IsoCurrencyCode.GBP = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='GBP', tag='GBP')
IsoCurrencyCode.GEL = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='GEL', tag='GEL')
IsoCurrencyCode.GHS = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='GHS', tag='GHS')
IsoCurrencyCode.GIP = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='GIP', tag='GIP')
IsoCurrencyCode.GMD = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='GMD', tag='GMD')
IsoCurrencyCode.GNF = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='GNF', tag='GNF')
IsoCurrencyCode.GTQ = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='GTQ', tag='GTQ')
IsoCurrencyCode.GYD = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='GYD', tag='GYD')
IsoCurrencyCode.HKD = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='HKD', tag='HKD')
IsoCurrencyCode.HNL = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='HNL', tag='HNL')
IsoCurrencyCode.HRK = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='HRK', tag='HRK')
IsoCurrencyCode.HTG = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='HTG', tag='HTG')
IsoCurrencyCode.HUF = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='HUF', tag='HUF')
IsoCurrencyCode.IDR = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='IDR', tag='IDR')
IsoCurrencyCode.ILS = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='ILS', tag='ILS')
IsoCurrencyCode.INR = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='INR', tag='INR')
IsoCurrencyCode.IQD = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='IQD', tag='IQD')
IsoCurrencyCode.IRR = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='IRR', tag='IRR')
IsoCurrencyCode.ISK = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='ISK', tag='ISK')
IsoCurrencyCode.JMD = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='JMD', tag='JMD')
IsoCurrencyCode.JOD = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='JOD', tag='JOD')
IsoCurrencyCode.JPY = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='JPY', tag='JPY')
IsoCurrencyCode.KES = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='KES', tag='KES')
IsoCurrencyCode.KGS = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='KGS', tag='KGS')
IsoCurrencyCode.KHR = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='KHR', tag='KHR')
IsoCurrencyCode.KMF = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='KMF', tag='KMF')
IsoCurrencyCode.KPW = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='KPW', tag='KPW')
IsoCurrencyCode.KRW = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='KRW', tag='KRW')
IsoCurrencyCode.KWD = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='KWD', tag='KWD')
IsoCurrencyCode.KYD = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='KYD', tag='KYD')
IsoCurrencyCode.KZT = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='KZT', tag='KZT')
IsoCurrencyCode.LAK = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='LAK', tag='LAK')
IsoCurrencyCode.LBP = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='LBP', tag='LBP')
IsoCurrencyCode.LKR = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='LKR', tag='LKR')
IsoCurrencyCode.LRD = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='LRD', tag='LRD')
IsoCurrencyCode.LSL = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='LSL', tag='LSL')
IsoCurrencyCode.LTL = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='LTL', tag='LTL')
IsoCurrencyCode.LVL = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='LVL', tag='LVL')
IsoCurrencyCode.LYD = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='LYD', tag='LYD')
IsoCurrencyCode.MAD = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='MAD', tag='MAD')
IsoCurrencyCode.MDL = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='MDL', tag='MDL')
IsoCurrencyCode.MGA = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='MGA', tag='MGA')
IsoCurrencyCode.MKD = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='MKD', tag='MKD')
IsoCurrencyCode.MMK = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='MMK', tag='MMK')
IsoCurrencyCode.MNT = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='MNT', tag='MNT')
IsoCurrencyCode.MOP = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='MOP', tag='MOP')
IsoCurrencyCode.MRO = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='MRO', tag='MRO')
IsoCurrencyCode.MUR = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='MUR', tag='MUR')
IsoCurrencyCode.MVR = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='MVR', tag='MVR')
IsoCurrencyCode.MWK = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='MWK', tag='MWK')
IsoCurrencyCode.MXN = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='MXN', tag='MXN')
IsoCurrencyCode.MXV = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='MXV', tag='MXV')
IsoCurrencyCode.MYR = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='MYR', tag='MYR')
IsoCurrencyCode.MZM = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='MZM', tag='MZM')
IsoCurrencyCode.NAD = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='NAD', tag='NAD')
IsoCurrencyCode.NGN = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='NGN', tag='NGN')
IsoCurrencyCode.NIO = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='NIO', tag='NIO')
IsoCurrencyCode.NOK = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='NOK', tag='NOK')
IsoCurrencyCode.NPR = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='NPR', tag='NPR')
IsoCurrencyCode.NZD = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='NZD', tag='NZD')
IsoCurrencyCode.OMR = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='OMR', tag='OMR')
IsoCurrencyCode.PAB = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='PAB', tag='PAB')
IsoCurrencyCode.PEN = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='PEN', tag='PEN')
IsoCurrencyCode.PGK = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='PGK', tag='PGK')
IsoCurrencyCode.PHP = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='PHP', tag='PHP')
IsoCurrencyCode.PKR = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='PKR', tag='PKR')
IsoCurrencyCode.PLN = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='PLN', tag='PLN')
IsoCurrencyCode.PYG = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='PYG', tag='PYG')
IsoCurrencyCode.QAR = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='QAR', tag='QAR')
IsoCurrencyCode.RON = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='RON', tag='RON')
IsoCurrencyCode.RSD = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='RSD', tag='RSD')
IsoCurrencyCode.RUB = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='RUB', tag='RUB')
IsoCurrencyCode.RWF = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='RWF', tag='RWF')
IsoCurrencyCode.SAR = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='SAR', tag='SAR')
IsoCurrencyCode.SBD = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='SBD', tag='SBD')
IsoCurrencyCode.SCR = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='SCR', tag='SCR')
IsoCurrencyCode.SDG = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='SDG', tag='SDG')
IsoCurrencyCode.SEK = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='SEK', tag='SEK')
IsoCurrencyCode.SGD = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='SGD', tag='SGD')
IsoCurrencyCode.SHP = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='SHP', tag='SHP')
IsoCurrencyCode.SLL = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='SLL', tag='SLL')
IsoCurrencyCode.SOS = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='SOS', tag='SOS')
IsoCurrencyCode.SRD = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='SRD', tag='SRD')
IsoCurrencyCode.STD = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='STD', tag='STD')
IsoCurrencyCode.SVC = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='SVC', tag='SVC')
IsoCurrencyCode.SYP = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='SYP', tag='SYP')
IsoCurrencyCode.SZL = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='SZL', tag='SZL')
IsoCurrencyCode.THB = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='THB', tag='THB')
IsoCurrencyCode.TJS = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='TJS', tag='TJS')
IsoCurrencyCode.TMT = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='TMT', tag='TMT')
IsoCurrencyCode.TND = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='TND', tag='TND')
IsoCurrencyCode.TOP = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='TOP', tag='TOP')
IsoCurrencyCode.TRY = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='TRY', tag='TRY')
IsoCurrencyCode.TTD = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='TTD', tag='TTD')
IsoCurrencyCode.TWD = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='TWD', tag='TWD')
IsoCurrencyCode.TZS = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='TZS', tag='TZS')
IsoCurrencyCode.UAH = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='UAH', tag='UAH')
IsoCurrencyCode.UGX = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='UGX', tag='UGX')
IsoCurrencyCode.USD = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='USD', tag='USD')
IsoCurrencyCode.UYI = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='UYI', tag='UYI')
IsoCurrencyCode.UYU = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='UYU', tag='UYU')
IsoCurrencyCode.UZS = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='UZS', tag='UZS')
IsoCurrencyCode.VEF = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='VEF', tag='VEF')
IsoCurrencyCode.VND = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='VND', tag='VND')
IsoCurrencyCode.VUV = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='VUV', tag='VUV')
IsoCurrencyCode.WST = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='WST', tag='WST')
IsoCurrencyCode.XAF = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='XAF', tag='XAF')
IsoCurrencyCode.XCD = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='XCD', tag='XCD')
IsoCurrencyCode.XOF = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='XOF', tag='XOF')
IsoCurrencyCode.XPF = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='XPF', tag='XPF')
IsoCurrencyCode.YER = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='YER', tag='YER')
IsoCurrencyCode.ZAR = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='ZAR', tag='ZAR')
IsoCurrencyCode.ZMK = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='ZMK', tag='ZMK')
IsoCurrencyCode.ZWL = IsoCurrencyCode._CF_enumeration.addEnumeration(unicode_value='ZWL', tag='ZWL')
IsoCurrencyCode._InitializeFacetMap(IsoCurrencyCode._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'IsoCurrencyCode', IsoCurrencyCode)

# Atomic simple type: {http://ddex.net/xml/avs/avs}IsoLanguageCode
class IsoLanguageCode (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An ISO639-1 two-letter code representing a Language."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'IsoLanguageCode')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 3490, 3)
    _Documentation = 'An ISO639-1 two-letter code representing a Language.'
IsoLanguageCode._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=IsoLanguageCode, enum_prefix=None)
IsoLanguageCode.aa = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='aa', tag='aa')
IsoLanguageCode.ab = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='ab', tag='ab')
IsoLanguageCode.ae = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='ae', tag='ae')
IsoLanguageCode.af = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='af', tag='af')
IsoLanguageCode.ak = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='ak', tag='ak')
IsoLanguageCode.am = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='am', tag='am')
IsoLanguageCode.an = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='an', tag='an')
IsoLanguageCode.ar = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='ar', tag='ar')
IsoLanguageCode.as_ = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='as', tag='as_')
IsoLanguageCode.av = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='av', tag='av')
IsoLanguageCode.ay = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='ay', tag='ay')
IsoLanguageCode.az = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='az', tag='az')
IsoLanguageCode.ba = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='ba', tag='ba')
IsoLanguageCode.be = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='be', tag='be')
IsoLanguageCode.bg = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='bg', tag='bg')
IsoLanguageCode.bh = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='bh', tag='bh')
IsoLanguageCode.bi = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='bi', tag='bi')
IsoLanguageCode.bm = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='bm', tag='bm')
IsoLanguageCode.bn = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='bn', tag='bn')
IsoLanguageCode.bo = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='bo', tag='bo')
IsoLanguageCode.br = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='br', tag='br')
IsoLanguageCode.bs = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='bs', tag='bs')
IsoLanguageCode.ca = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='ca', tag='ca')
IsoLanguageCode.ce = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='ce', tag='ce')
IsoLanguageCode.ch = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='ch', tag='ch')
IsoLanguageCode.co = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='co', tag='co')
IsoLanguageCode.cr = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='cr', tag='cr')
IsoLanguageCode.cs = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='cs', tag='cs')
IsoLanguageCode.cu = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='cu', tag='cu')
IsoLanguageCode.cv = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='cv', tag='cv')
IsoLanguageCode.cy = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='cy', tag='cy')
IsoLanguageCode.da = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='da', tag='da')
IsoLanguageCode.de = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='de', tag='de')
IsoLanguageCode.dv = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='dv', tag='dv')
IsoLanguageCode.dz = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='dz', tag='dz')
IsoLanguageCode.ee = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='ee', tag='ee')
IsoLanguageCode.el = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='el', tag='el')
IsoLanguageCode.en = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='en', tag='en')
IsoLanguageCode.eo = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='eo', tag='eo')
IsoLanguageCode.es = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='es', tag='es')
IsoLanguageCode.et = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='et', tag='et')
IsoLanguageCode.eu = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='eu', tag='eu')
IsoLanguageCode.fa = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='fa', tag='fa')
IsoLanguageCode.ff = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='ff', tag='ff')
IsoLanguageCode.fi = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='fi', tag='fi')
IsoLanguageCode.fj = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='fj', tag='fj')
IsoLanguageCode.fo = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='fo', tag='fo')
IsoLanguageCode.fr = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='fr', tag='fr')
IsoLanguageCode.fy = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='fy', tag='fy')
IsoLanguageCode.ga = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='ga', tag='ga')
IsoLanguageCode.gd = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='gd', tag='gd')
IsoLanguageCode.gl = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='gl', tag='gl')
IsoLanguageCode.gn = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='gn', tag='gn')
IsoLanguageCode.gu = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='gu', tag='gu')
IsoLanguageCode.gv = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='gv', tag='gv')
IsoLanguageCode.ha = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='ha', tag='ha')
IsoLanguageCode.he = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='he', tag='he')
IsoLanguageCode.hi = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='hi', tag='hi')
IsoLanguageCode.ho = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='ho', tag='ho')
IsoLanguageCode.hr = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='hr', tag='hr')
IsoLanguageCode.ht = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='ht', tag='ht')
IsoLanguageCode.hu = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='hu', tag='hu')
IsoLanguageCode.hy = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='hy', tag='hy')
IsoLanguageCode.hz = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='hz', tag='hz')
IsoLanguageCode.ia = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='ia', tag='ia')
IsoLanguageCode.id = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='id', tag='id')
IsoLanguageCode.ie = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='ie', tag='ie')
IsoLanguageCode.ig = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='ig', tag='ig')
IsoLanguageCode.ii = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='ii', tag='ii')
IsoLanguageCode.ik = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='ik', tag='ik')
IsoLanguageCode.io = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='io', tag='io')
IsoLanguageCode.is_ = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='is', tag='is_')
IsoLanguageCode.it = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='it', tag='it')
IsoLanguageCode.iu = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='iu', tag='iu')
IsoLanguageCode.ja = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='ja', tag='ja')
IsoLanguageCode.jv = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='jv', tag='jv')
IsoLanguageCode.ka = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='ka', tag='ka')
IsoLanguageCode.kg = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='kg', tag='kg')
IsoLanguageCode.ki = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='ki', tag='ki')
IsoLanguageCode.kj = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='kj', tag='kj')
IsoLanguageCode.kk = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='kk', tag='kk')
IsoLanguageCode.kl = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='kl', tag='kl')
IsoLanguageCode.km = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='km', tag='km')
IsoLanguageCode.kn = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='kn', tag='kn')
IsoLanguageCode.ko = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='ko', tag='ko')
IsoLanguageCode.kr = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='kr', tag='kr')
IsoLanguageCode.ks = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='ks', tag='ks')
IsoLanguageCode.ku = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='ku', tag='ku')
IsoLanguageCode.kv = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='kv', tag='kv')
IsoLanguageCode.kw = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='kw', tag='kw')
IsoLanguageCode.ky = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='ky', tag='ky')
IsoLanguageCode.la = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='la', tag='la')
IsoLanguageCode.lb = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='lb', tag='lb')
IsoLanguageCode.lg = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='lg', tag='lg')
IsoLanguageCode.li = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='li', tag='li')
IsoLanguageCode.ln = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='ln', tag='ln')
IsoLanguageCode.lo = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='lo', tag='lo')
IsoLanguageCode.lt = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='lt', tag='lt')
IsoLanguageCode.lu = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='lu', tag='lu')
IsoLanguageCode.lv = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='lv', tag='lv')
IsoLanguageCode.mg = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='mg', tag='mg')
IsoLanguageCode.mh = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='mh', tag='mh')
IsoLanguageCode.mi = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='mi', tag='mi')
IsoLanguageCode.mk = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='mk', tag='mk')
IsoLanguageCode.ml = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='ml', tag='ml')
IsoLanguageCode.mn = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='mn', tag='mn')
IsoLanguageCode.mo = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='mo', tag='mo')
IsoLanguageCode.mr = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='mr', tag='mr')
IsoLanguageCode.ms = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='ms', tag='ms')
IsoLanguageCode.mt = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='mt', tag='mt')
IsoLanguageCode.my = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='my', tag='my')
IsoLanguageCode.na = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='na', tag='na')
IsoLanguageCode.nb = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='nb', tag='nb')
IsoLanguageCode.nd = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='nd', tag='nd')
IsoLanguageCode.ne = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='ne', tag='ne')
IsoLanguageCode.ng = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='ng', tag='ng')
IsoLanguageCode.nl = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='nl', tag='nl')
IsoLanguageCode.nn = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='nn', tag='nn')
IsoLanguageCode.no = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='no', tag='no')
IsoLanguageCode.nr = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='nr', tag='nr')
IsoLanguageCode.nv = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='nv', tag='nv')
IsoLanguageCode.ny = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='ny', tag='ny')
IsoLanguageCode.oc = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='oc', tag='oc')
IsoLanguageCode.oj = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='oj', tag='oj')
IsoLanguageCode.om = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='om', tag='om')
IsoLanguageCode.or_ = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='or', tag='or_')
IsoLanguageCode.os = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='os', tag='os')
IsoLanguageCode.pa = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='pa', tag='pa')
IsoLanguageCode.pi = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='pi', tag='pi')
IsoLanguageCode.pl = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='pl', tag='pl')
IsoLanguageCode.ps = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='ps', tag='ps')
IsoLanguageCode.pt = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='pt', tag='pt')
IsoLanguageCode.qu = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='qu', tag='qu')
IsoLanguageCode.rm = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='rm', tag='rm')
IsoLanguageCode.rn = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='rn', tag='rn')
IsoLanguageCode.ro = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='ro', tag='ro')
IsoLanguageCode.ru = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='ru', tag='ru')
IsoLanguageCode.rw = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='rw', tag='rw')
IsoLanguageCode.sa = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='sa', tag='sa')
IsoLanguageCode.sc = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='sc', tag='sc')
IsoLanguageCode.sd = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='sd', tag='sd')
IsoLanguageCode.se = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='se', tag='se')
IsoLanguageCode.sg = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='sg', tag='sg')
IsoLanguageCode.si = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='si', tag='si')
IsoLanguageCode.sk = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='sk', tag='sk')
IsoLanguageCode.sl = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='sl', tag='sl')
IsoLanguageCode.sm = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='sm', tag='sm')
IsoLanguageCode.sn = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='sn', tag='sn')
IsoLanguageCode.so = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='so', tag='so')
IsoLanguageCode.sq = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='sq', tag='sq')
IsoLanguageCode.sr = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='sr', tag='sr')
IsoLanguageCode.ss = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='ss', tag='ss')
IsoLanguageCode.st = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='st', tag='st')
IsoLanguageCode.su = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='su', tag='su')
IsoLanguageCode.sv = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='sv', tag='sv')
IsoLanguageCode.sw = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='sw', tag='sw')
IsoLanguageCode.ta = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='ta', tag='ta')
IsoLanguageCode.te = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='te', tag='te')
IsoLanguageCode.tg = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='tg', tag='tg')
IsoLanguageCode.th = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='th', tag='th')
IsoLanguageCode.ti = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='ti', tag='ti')
IsoLanguageCode.tk = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='tk', tag='tk')
IsoLanguageCode.tl = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='tl', tag='tl')
IsoLanguageCode.tn = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='tn', tag='tn')
IsoLanguageCode.to = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='to', tag='to')
IsoLanguageCode.tr = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='tr', tag='tr')
IsoLanguageCode.ts = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='ts', tag='ts')
IsoLanguageCode.tt = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='tt', tag='tt')
IsoLanguageCode.tw = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='tw', tag='tw')
IsoLanguageCode.ty = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='ty', tag='ty')
IsoLanguageCode.ug = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='ug', tag='ug')
IsoLanguageCode.uk = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='uk', tag='uk')
IsoLanguageCode.ur = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='ur', tag='ur')
IsoLanguageCode.uz = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='uz', tag='uz')
IsoLanguageCode.ve = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='ve', tag='ve')
IsoLanguageCode.vi = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='vi', tag='vi')
IsoLanguageCode.vo = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='vo', tag='vo')
IsoLanguageCode.wa = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='wa', tag='wa')
IsoLanguageCode.wo = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='wo', tag='wo')
IsoLanguageCode.xh = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='xh', tag='xh')
IsoLanguageCode.yi = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='yi', tag='yi')
IsoLanguageCode.yo = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='yo', tag='yo')
IsoLanguageCode.za = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='za', tag='za')
IsoLanguageCode.zh = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='zh', tag='zh')
IsoLanguageCode.zu = IsoLanguageCode._CF_enumeration.addEnumeration(unicode_value='zu', tag='zu')
IsoLanguageCode._InitializeFacetMap(IsoLanguageCode._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'IsoLanguageCode', IsoLanguageCode)

# Atomic simple type: {http://ddex.net/xml/avs/avs}IsoTerritoryCode
class IsoTerritoryCode (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An ISO 3166-1 two-letter code representing a Territory."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'IsoTerritoryCode')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 4422, 3)
    _Documentation = 'An ISO 3166-1 two-letter code representing a Territory.'
IsoTerritoryCode._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=IsoTerritoryCode, enum_prefix=None)
IsoTerritoryCode.AD = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='AD', tag='AD')
IsoTerritoryCode.AE = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='AE', tag='AE')
IsoTerritoryCode.AF = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='AF', tag='AF')
IsoTerritoryCode.AG = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='AG', tag='AG')
IsoTerritoryCode.AI = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='AI', tag='AI')
IsoTerritoryCode.AL = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='AL', tag='AL')
IsoTerritoryCode.AM = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='AM', tag='AM')
IsoTerritoryCode.AN = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='AN', tag='AN')
IsoTerritoryCode.AO = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='AO', tag='AO')
IsoTerritoryCode.AQ = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='AQ', tag='AQ')
IsoTerritoryCode.AR = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='AR', tag='AR')
IsoTerritoryCode.AS = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='AS', tag='AS')
IsoTerritoryCode.AT = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='AT', tag='AT')
IsoTerritoryCode.AU = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='AU', tag='AU')
IsoTerritoryCode.AW = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='AW', tag='AW')
IsoTerritoryCode.AX = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='AX', tag='AX')
IsoTerritoryCode.AZ = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='AZ', tag='AZ')
IsoTerritoryCode.BA = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='BA', tag='BA')
IsoTerritoryCode.BB = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='BB', tag='BB')
IsoTerritoryCode.BD = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='BD', tag='BD')
IsoTerritoryCode.BE = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='BE', tag='BE')
IsoTerritoryCode.BF = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='BF', tag='BF')
IsoTerritoryCode.BG = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='BG', tag='BG')
IsoTerritoryCode.BH = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='BH', tag='BH')
IsoTerritoryCode.BI = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='BI', tag='BI')
IsoTerritoryCode.BJ = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='BJ', tag='BJ')
IsoTerritoryCode.BL = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='BL', tag='BL')
IsoTerritoryCode.BM = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='BM', tag='BM')
IsoTerritoryCode.BN = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='BN', tag='BN')
IsoTerritoryCode.BO = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='BO', tag='BO')
IsoTerritoryCode.BQ = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='BQ', tag='BQ')
IsoTerritoryCode.BR = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='BR', tag='BR')
IsoTerritoryCode.BS = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='BS', tag='BS')
IsoTerritoryCode.BT = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='BT', tag='BT')
IsoTerritoryCode.BV = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='BV', tag='BV')
IsoTerritoryCode.BW = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='BW', tag='BW')
IsoTerritoryCode.BY = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='BY', tag='BY')
IsoTerritoryCode.BZ = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='BZ', tag='BZ')
IsoTerritoryCode.CA = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='CA', tag='CA')
IsoTerritoryCode.CC = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='CC', tag='CC')
IsoTerritoryCode.CD = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='CD', tag='CD')
IsoTerritoryCode.CF = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='CF', tag='CF')
IsoTerritoryCode.CG = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='CG', tag='CG')
IsoTerritoryCode.CH = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='CH', tag='CH')
IsoTerritoryCode.CI = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='CI', tag='CI')
IsoTerritoryCode.CK = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='CK', tag='CK')
IsoTerritoryCode.CL = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='CL', tag='CL')
IsoTerritoryCode.CM = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='CM', tag='CM')
IsoTerritoryCode.CN = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='CN', tag='CN')
IsoTerritoryCode.CO = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='CO', tag='CO')
IsoTerritoryCode.CR = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='CR', tag='CR')
IsoTerritoryCode.CS = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='CS', tag='CS')
IsoTerritoryCode.CU = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='CU', tag='CU')
IsoTerritoryCode.CV = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='CV', tag='CV')
IsoTerritoryCode.CW = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='CW', tag='CW')
IsoTerritoryCode.CX = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='CX', tag='CX')
IsoTerritoryCode.CY = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='CY', tag='CY')
IsoTerritoryCode.CZ = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='CZ', tag='CZ')
IsoTerritoryCode.DE = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='DE', tag='DE')
IsoTerritoryCode.DJ = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='DJ', tag='DJ')
IsoTerritoryCode.DK = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='DK', tag='DK')
IsoTerritoryCode.DM = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='DM', tag='DM')
IsoTerritoryCode.DO = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='DO', tag='DO')
IsoTerritoryCode.DZ = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='DZ', tag='DZ')
IsoTerritoryCode.EC = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='EC', tag='EC')
IsoTerritoryCode.EE = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='EE', tag='EE')
IsoTerritoryCode.EG = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='EG', tag='EG')
IsoTerritoryCode.EH = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='EH', tag='EH')
IsoTerritoryCode.ER = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='ER', tag='ER')
IsoTerritoryCode.ES = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='ES', tag='ES')
IsoTerritoryCode.ET = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='ET', tag='ET')
IsoTerritoryCode.FI = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='FI', tag='FI')
IsoTerritoryCode.FJ = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='FJ', tag='FJ')
IsoTerritoryCode.FK = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='FK', tag='FK')
IsoTerritoryCode.FM = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='FM', tag='FM')
IsoTerritoryCode.FO = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='FO', tag='FO')
IsoTerritoryCode.FR = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='FR', tag='FR')
IsoTerritoryCode.GA = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='GA', tag='GA')
IsoTerritoryCode.GB = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='GB', tag='GB')
IsoTerritoryCode.GD = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='GD', tag='GD')
IsoTerritoryCode.GE = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='GE', tag='GE')
IsoTerritoryCode.GF = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='GF', tag='GF')
IsoTerritoryCode.GG = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='GG', tag='GG')
IsoTerritoryCode.GH = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='GH', tag='GH')
IsoTerritoryCode.GI = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='GI', tag='GI')
IsoTerritoryCode.GL = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='GL', tag='GL')
IsoTerritoryCode.GM = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='GM', tag='GM')
IsoTerritoryCode.GN = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='GN', tag='GN')
IsoTerritoryCode.GP = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='GP', tag='GP')
IsoTerritoryCode.GQ = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='GQ', tag='GQ')
IsoTerritoryCode.GR = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='GR', tag='GR')
IsoTerritoryCode.GS = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='GS', tag='GS')
IsoTerritoryCode.GT = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='GT', tag='GT')
IsoTerritoryCode.GU = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='GU', tag='GU')
IsoTerritoryCode.GW = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='GW', tag='GW')
IsoTerritoryCode.GY = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='GY', tag='GY')
IsoTerritoryCode.HK = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='HK', tag='HK')
IsoTerritoryCode.HM = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='HM', tag='HM')
IsoTerritoryCode.HN = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='HN', tag='HN')
IsoTerritoryCode.HR = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='HR', tag='HR')
IsoTerritoryCode.HT = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='HT', tag='HT')
IsoTerritoryCode.HU = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='HU', tag='HU')
IsoTerritoryCode.ID = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='ID', tag='ID')
IsoTerritoryCode.IE = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='IE', tag='IE')
IsoTerritoryCode.IL = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='IL', tag='IL')
IsoTerritoryCode.IM = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='IM', tag='IM')
IsoTerritoryCode.IN = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='IN', tag='IN')
IsoTerritoryCode.IO = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='IO', tag='IO')
IsoTerritoryCode.IQ = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='IQ', tag='IQ')
IsoTerritoryCode.IR = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='IR', tag='IR')
IsoTerritoryCode.IS = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='IS', tag='IS')
IsoTerritoryCode.IT = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='IT', tag='IT')
IsoTerritoryCode.JE = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='JE', tag='JE')
IsoTerritoryCode.JM = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='JM', tag='JM')
IsoTerritoryCode.JO = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='JO', tag='JO')
IsoTerritoryCode.JP = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='JP', tag='JP')
IsoTerritoryCode.KE = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='KE', tag='KE')
IsoTerritoryCode.KG = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='KG', tag='KG')
IsoTerritoryCode.KH = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='KH', tag='KH')
IsoTerritoryCode.KI = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='KI', tag='KI')
IsoTerritoryCode.KM = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='KM', tag='KM')
IsoTerritoryCode.KN = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='KN', tag='KN')
IsoTerritoryCode.KP = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='KP', tag='KP')
IsoTerritoryCode.KR = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='KR', tag='KR')
IsoTerritoryCode.KW = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='KW', tag='KW')
IsoTerritoryCode.KY = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='KY', tag='KY')
IsoTerritoryCode.KZ = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='KZ', tag='KZ')
IsoTerritoryCode.LA = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='LA', tag='LA')
IsoTerritoryCode.LB = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='LB', tag='LB')
IsoTerritoryCode.LC = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='LC', tag='LC')
IsoTerritoryCode.LI = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='LI', tag='LI')
IsoTerritoryCode.LK = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='LK', tag='LK')
IsoTerritoryCode.LR = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='LR', tag='LR')
IsoTerritoryCode.LS = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='LS', tag='LS')
IsoTerritoryCode.LT = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='LT', tag='LT')
IsoTerritoryCode.LU = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='LU', tag='LU')
IsoTerritoryCode.LV = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='LV', tag='LV')
IsoTerritoryCode.LY = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='LY', tag='LY')
IsoTerritoryCode.MA = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='MA', tag='MA')
IsoTerritoryCode.MC = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='MC', tag='MC')
IsoTerritoryCode.MD = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='MD', tag='MD')
IsoTerritoryCode.ME = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='ME', tag='ME')
IsoTerritoryCode.MF = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='MF', tag='MF')
IsoTerritoryCode.MG = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='MG', tag='MG')
IsoTerritoryCode.MH = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='MH', tag='MH')
IsoTerritoryCode.MK = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='MK', tag='MK')
IsoTerritoryCode.ML = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='ML', tag='ML')
IsoTerritoryCode.MM = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='MM', tag='MM')
IsoTerritoryCode.MN = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='MN', tag='MN')
IsoTerritoryCode.MO = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='MO', tag='MO')
IsoTerritoryCode.MP = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='MP', tag='MP')
IsoTerritoryCode.MQ = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='MQ', tag='MQ')
IsoTerritoryCode.MR = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='MR', tag='MR')
IsoTerritoryCode.MS = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='MS', tag='MS')
IsoTerritoryCode.MT = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='MT', tag='MT')
IsoTerritoryCode.MU = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='MU', tag='MU')
IsoTerritoryCode.MV = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='MV', tag='MV')
IsoTerritoryCode.MW = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='MW', tag='MW')
IsoTerritoryCode.MX = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='MX', tag='MX')
IsoTerritoryCode.MY = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='MY', tag='MY')
IsoTerritoryCode.MZ = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='MZ', tag='MZ')
IsoTerritoryCode.NA = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='NA', tag='NA')
IsoTerritoryCode.NC = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='NC', tag='NC')
IsoTerritoryCode.NE = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='NE', tag='NE')
IsoTerritoryCode.NF = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='NF', tag='NF')
IsoTerritoryCode.NG = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='NG', tag='NG')
IsoTerritoryCode.NI = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='NI', tag='NI')
IsoTerritoryCode.NL = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='NL', tag='NL')
IsoTerritoryCode.NO = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='NO', tag='NO')
IsoTerritoryCode.NP = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='NP', tag='NP')
IsoTerritoryCode.NR = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='NR', tag='NR')
IsoTerritoryCode.NU = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='NU', tag='NU')
IsoTerritoryCode.NZ = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='NZ', tag='NZ')
IsoTerritoryCode.OM = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='OM', tag='OM')
IsoTerritoryCode.PA = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='PA', tag='PA')
IsoTerritoryCode.PE = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='PE', tag='PE')
IsoTerritoryCode.PF = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='PF', tag='PF')
IsoTerritoryCode.PG = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='PG', tag='PG')
IsoTerritoryCode.PH = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='PH', tag='PH')
IsoTerritoryCode.PK = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='PK', tag='PK')
IsoTerritoryCode.PL = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='PL', tag='PL')
IsoTerritoryCode.PM = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='PM', tag='PM')
IsoTerritoryCode.PN = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='PN', tag='PN')
IsoTerritoryCode.PR = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='PR', tag='PR')
IsoTerritoryCode.PS = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='PS', tag='PS')
IsoTerritoryCode.PT = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='PT', tag='PT')
IsoTerritoryCode.PW = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='PW', tag='PW')
IsoTerritoryCode.PY = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='PY', tag='PY')
IsoTerritoryCode.QA = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='QA', tag='QA')
IsoTerritoryCode.RE = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='RE', tag='RE')
IsoTerritoryCode.RO = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='RO', tag='RO')
IsoTerritoryCode.RS = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='RS', tag='RS')
IsoTerritoryCode.RU = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='RU', tag='RU')
IsoTerritoryCode.RW = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='RW', tag='RW')
IsoTerritoryCode.SA = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='SA', tag='SA')
IsoTerritoryCode.SB = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='SB', tag='SB')
IsoTerritoryCode.SC = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='SC', tag='SC')
IsoTerritoryCode.SD = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='SD', tag='SD')
IsoTerritoryCode.SE = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='SE', tag='SE')
IsoTerritoryCode.SG = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='SG', tag='SG')
IsoTerritoryCode.SH = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='SH', tag='SH')
IsoTerritoryCode.SI = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='SI', tag='SI')
IsoTerritoryCode.SJ = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='SJ', tag='SJ')
IsoTerritoryCode.SK = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='SK', tag='SK')
IsoTerritoryCode.SL = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='SL', tag='SL')
IsoTerritoryCode.SM = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='SM', tag='SM')
IsoTerritoryCode.SN = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='SN', tag='SN')
IsoTerritoryCode.SO = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='SO', tag='SO')
IsoTerritoryCode.SR = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='SR', tag='SR')
IsoTerritoryCode.SS = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='SS', tag='SS')
IsoTerritoryCode.ST = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='ST', tag='ST')
IsoTerritoryCode.SV = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='SV', tag='SV')
IsoTerritoryCode.SX = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='SX', tag='SX')
IsoTerritoryCode.SY = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='SY', tag='SY')
IsoTerritoryCode.SZ = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='SZ', tag='SZ')
IsoTerritoryCode.TC = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='TC', tag='TC')
IsoTerritoryCode.TD = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='TD', tag='TD')
IsoTerritoryCode.TF = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='TF', tag='TF')
IsoTerritoryCode.TG = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='TG', tag='TG')
IsoTerritoryCode.TH = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='TH', tag='TH')
IsoTerritoryCode.TJ = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='TJ', tag='TJ')
IsoTerritoryCode.TK = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='TK', tag='TK')
IsoTerritoryCode.TL = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='TL', tag='TL')
IsoTerritoryCode.TM = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='TM', tag='TM')
IsoTerritoryCode.TN = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='TN', tag='TN')
IsoTerritoryCode.TO = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='TO', tag='TO')
IsoTerritoryCode.TR = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='TR', tag='TR')
IsoTerritoryCode.TT = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='TT', tag='TT')
IsoTerritoryCode.TV = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='TV', tag='TV')
IsoTerritoryCode.TW = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='TW', tag='TW')
IsoTerritoryCode.TZ = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='TZ', tag='TZ')
IsoTerritoryCode.UA = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='UA', tag='UA')
IsoTerritoryCode.UG = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='UG', tag='UG')
IsoTerritoryCode.UM = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='UM', tag='UM')
IsoTerritoryCode.US = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='US', tag='US')
IsoTerritoryCode.UY = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='UY', tag='UY')
IsoTerritoryCode.UZ = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='UZ', tag='UZ')
IsoTerritoryCode.VA = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='VA', tag='VA')
IsoTerritoryCode.VC = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='VC', tag='VC')
IsoTerritoryCode.VE = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='VE', tag='VE')
IsoTerritoryCode.VG = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='VG', tag='VG')
IsoTerritoryCode.VI = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='VI', tag='VI')
IsoTerritoryCode.VN = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='VN', tag='VN')
IsoTerritoryCode.VU = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='VU', tag='VU')
IsoTerritoryCode.WF = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='WF', tag='WF')
IsoTerritoryCode.WS = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='WS', tag='WS')
IsoTerritoryCode.YE = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='YE', tag='YE')
IsoTerritoryCode.YT = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='YT', tag='YT')
IsoTerritoryCode.ZA = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='ZA', tag='ZA')
IsoTerritoryCode.ZM = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='ZM', tag='ZM')
IsoTerritoryCode.ZW = IsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='ZW', tag='ZW')
IsoTerritoryCode._InitializeFacetMap(IsoTerritoryCode._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'IsoTerritoryCode', IsoTerritoryCode)

# Atomic simple type: {http://ddex.net/xml/avs/avs}LabelNameType
class LabelNameType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of LabelName."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LabelNameType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 5684, 3)
    _Documentation = 'A Type of LabelName.'
LabelNameType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=LabelNameType, enum_prefix=None)
LabelNameType.DisplayLabelName = LabelNameType._CF_enumeration.addEnumeration(unicode_value='DisplayLabelName', tag='DisplayLabelName')
LabelNameType.UserDefined = LabelNameType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
LabelNameType._InitializeFacetMap(LabelNameType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'LabelNameType', LabelNameType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}LicenseOrClaimRefusalReason
class LicenseOrClaimRefusalReason (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of reason for a refusing a License or Claim."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LicenseOrClaimRefusalReason')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 5701, 3)
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
LicenseOrClaimRefusalReason.ImportLicenseExists = LicenseOrClaimRefusalReason._CF_enumeration.addEnumeration(unicode_value='ImportLicenseExists', tag='ImportLicenseExists')
LicenseOrClaimRefusalReason.IncorrectClaim = LicenseOrClaimRefusalReason._CF_enumeration.addEnumeration(unicode_value='IncorrectClaim', tag='IncorrectClaim')
LicenseOrClaimRefusalReason.IncorrectControlledCompositionRate = LicenseOrClaimRefusalReason._CF_enumeration.addEnumeration(unicode_value='IncorrectControlledCompositionRate', tag='IncorrectControlledCompositionRate')
LicenseOrClaimRefusalReason.InHouseLicenseExists = LicenseOrClaimRefusalReason._CF_enumeration.addEnumeration(unicode_value='InHouseLicenseExists', tag='InHouseLicenseExists')
LicenseOrClaimRefusalReason.InsufficientInformation = LicenseOrClaimRefusalReason._CF_enumeration.addEnumeration(unicode_value='InsufficientInformation', tag='InsufficientInformation')
LicenseOrClaimRefusalReason.LicenseeNotAuthorized = LicenseOrClaimRefusalReason._CF_enumeration.addEnumeration(unicode_value='LicenseeNotAuthorized', tag='LicenseeNotAuthorized')
LicenseOrClaimRefusalReason.MedleyRequest = LicenseOrClaimRefusalReason._CF_enumeration.addEnumeration(unicode_value='MedleyRequest', tag='MedleyRequest')
LicenseOrClaimRefusalReason.NoOptIn = LicenseOrClaimRefusalReason._CF_enumeration.addEnumeration(unicode_value='NoOptIn', tag='NoOptIn')
LicenseOrClaimRefusalReason.NoPublisherClaim = LicenseOrClaimRefusalReason._CF_enumeration.addEnumeration(unicode_value='NoPublisherClaim', tag='NoPublisherClaim')
LicenseOrClaimRefusalReason.OwnershipUnconfirmed = LicenseOrClaimRefusalReason._CF_enumeration.addEnumeration(unicode_value='OwnershipUnconfirmed', tag='OwnershipUnconfirmed')
LicenseOrClaimRefusalReason.ProductUnavailable = LicenseOrClaimRefusalReason._CF_enumeration.addEnumeration(unicode_value='ProductUnavailable', tag='ProductUnavailable')
LicenseOrClaimRefusalReason.PublisherNotRepresented = LicenseOrClaimRefusalReason._CF_enumeration.addEnumeration(unicode_value='PublisherNotRepresented', tag='PublisherNotRepresented')
LicenseOrClaimRefusalReason.ReleaseWithdrawn = LicenseOrClaimRefusalReason._CF_enumeration.addEnumeration(unicode_value='ReleaseWithdrawn', tag='ReleaseWithdrawn')
LicenseOrClaimRefusalReason.RelinquishedClaim = LicenseOrClaimRefusalReason._CF_enumeration.addEnumeration(unicode_value='RelinquishedClaim', tag='RelinquishedClaim')
LicenseOrClaimRefusalReason.UserDefined = LicenseOrClaimRefusalReason._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
LicenseOrClaimRefusalReason.WorkDeletedFromRelease = LicenseOrClaimRefusalReason._CF_enumeration.addEnumeration(unicode_value='WorkDeletedFromRelease', tag='WorkDeletedFromRelease')
LicenseOrClaimRefusalReason.WorkIncorrectlyIdentified = LicenseOrClaimRefusalReason._CF_enumeration.addEnumeration(unicode_value='WorkIncorrectlyIdentified', tag='WorkIncorrectlyIdentified')
LicenseOrClaimRefusalReason.WorkInPublicDomain = LicenseOrClaimRefusalReason._CF_enumeration.addEnumeration(unicode_value='WorkInPublicDomain', tag='WorkInPublicDomain')
LicenseOrClaimRefusalReason.WorkNotUsed = LicenseOrClaimRefusalReason._CF_enumeration.addEnumeration(unicode_value='WorkNotUsed', tag='WorkNotUsed')
LicenseOrClaimRefusalReason.WorkUnknown = LicenseOrClaimRefusalReason._CF_enumeration.addEnumeration(unicode_value='WorkUnknown', tag='WorkUnknown')
LicenseOrClaimRefusalReason._InitializeFacetMap(LicenseOrClaimRefusalReason._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'LicenseOrClaimRefusalReason', LicenseOrClaimRefusalReason)

# Atomic simple type: {http://ddex.net/xml/avs/avs}LicenseOrClaimRequestUpdateReason
class LicenseOrClaimRequestUpdateReason (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of reason for updating a License request."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LicenseOrClaimRequestUpdateReason')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 5908, 3)
    _Documentation = 'A Type of reason for updating a License request.'
LicenseOrClaimRequestUpdateReason._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=LicenseOrClaimRequestUpdateReason, enum_prefix=None)
LicenseOrClaimRequestUpdateReason.AdditionalInformationProvided = LicenseOrClaimRequestUpdateReason._CF_enumeration.addEnumeration(unicode_value='AdditionalInformationProvided', tag='AdditionalInformationProvided')
LicenseOrClaimRequestUpdateReason.AdditionalInformationProvidedAsRequested = LicenseOrClaimRequestUpdateReason._CF_enumeration.addEnumeration(unicode_value='AdditionalInformationProvidedAsRequested', tag='AdditionalInformationProvidedAsRequested')
LicenseOrClaimRequestUpdateReason.UserDefined = LicenseOrClaimRequestUpdateReason._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
LicenseOrClaimRequestUpdateReason._InitializeFacetMap(LicenseOrClaimRequestUpdateReason._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'LicenseOrClaimRequestUpdateReason', LicenseOrClaimRequestUpdateReason)

# Atomic simple type: {http://ddex.net/xml/avs/avs}LicenseOrClaimUpdateReason
class LicenseOrClaimUpdateReason (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of reason for updating a License."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LicenseOrClaimUpdateReason')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 5930, 3)
    _Documentation = 'A Type of reason for updating a License.'
LicenseOrClaimUpdateReason._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=LicenseOrClaimUpdateReason, enum_prefix=None)
LicenseOrClaimUpdateReason.NewLicenseIssued = LicenseOrClaimUpdateReason._CF_enumeration.addEnumeration(unicode_value='NewLicenseIssued', tag='NewLicenseIssued')
LicenseOrClaimUpdateReason.NewRightShareIdentified = LicenseOrClaimUpdateReason._CF_enumeration.addEnumeration(unicode_value='NewRightShareIdentified', tag='NewRightShareIdentified')
LicenseOrClaimUpdateReason.NewRightsholderIdentified = LicenseOrClaimUpdateReason._CF_enumeration.addEnumeration(unicode_value='NewRightsholderIdentified', tag='NewRightsholderIdentified')
LicenseOrClaimUpdateReason.NewWorkIdentified = LicenseOrClaimUpdateReason._CF_enumeration.addEnumeration(unicode_value='NewWorkIdentified', tag='NewWorkIdentified')
LicenseOrClaimUpdateReason.Revoked = LicenseOrClaimUpdateReason._CF_enumeration.addEnumeration(unicode_value='Revoked', tag='Revoked')
LicenseOrClaimUpdateReason.UserDefined = LicenseOrClaimUpdateReason._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
LicenseOrClaimUpdateReason._InitializeFacetMap(LicenseOrClaimUpdateReason._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'LicenseOrClaimUpdateReason', LicenseOrClaimUpdateReason)

# Atomic simple type: {http://ddex.net/xml/avs/avs}LicenseRejectionReason
class LicenseRejectionReason (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of reason for a rejecting a License."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LicenseRejectionReason')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 5967, 3)
    _Documentation = 'A Type of reason for a rejecting a License.'
LicenseRejectionReason._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=LicenseRejectionReason, enum_prefix=None)
LicenseRejectionReason.DisagreementOverRoyalties = LicenseRejectionReason._CF_enumeration.addEnumeration(unicode_value='DisagreementOverRoyalties', tag='DisagreementOverRoyalties')
LicenseRejectionReason.DisagreementOverScopeOfLicense = LicenseRejectionReason._CF_enumeration.addEnumeration(unicode_value='DisagreementOverScopeOfLicense', tag='DisagreementOverScopeOfLicense')
LicenseRejectionReason.LicenseExists = LicenseRejectionReason._CF_enumeration.addEnumeration(unicode_value='LicenseExists', tag='LicenseExists')
LicenseRejectionReason.LicenseNotNeeded = LicenseRejectionReason._CF_enumeration.addEnumeration(unicode_value='LicenseNotNeeded', tag='LicenseNotNeeded')
LicenseRejectionReason.WrongAddressee = LicenseRejectionReason._CF_enumeration.addEnumeration(unicode_value='WrongAddressee', tag='WrongAddressee')
LicenseRejectionReason.UserDefined = LicenseRejectionReason._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
LicenseRejectionReason.WorkInPublicDomain = LicenseRejectionReason._CF_enumeration.addEnumeration(unicode_value='WorkInPublicDomain', tag='WorkInPublicDomain')
LicenseRejectionReason._InitializeFacetMap(LicenseRejectionReason._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'LicenseRejectionReason', LicenseRejectionReason)

# Atomic simple type: {http://ddex.net/xml/avs/avs}LicenseStatus
class LicenseStatus (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A legal Status of a License for a Claim."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LicenseStatus')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 6009, 3)
    _Documentation = 'A legal Status of a License for a Claim.'
LicenseStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=LicenseStatus, enum_prefix=None)
LicenseStatus.Active = LicenseStatus._CF_enumeration.addEnumeration(unicode_value='Active', tag='Active')
LicenseStatus.Pending = LicenseStatus._CF_enumeration.addEnumeration(unicode_value='Pending', tag='Pending')
LicenseStatus.Revoked = LicenseStatus._CF_enumeration.addEnumeration(unicode_value='Revoked', tag='Revoked')
LicenseStatus._InitializeFacetMap(LicenseStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'LicenseStatus', LicenseStatus)

# Atomic simple type: {http://ddex.net/xml/avs/avs}LicensingProcessStatus
class LicensingProcessStatus (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An operational Status of a licensing process."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LicensingProcessStatus')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 6031, 3)
    _Documentation = 'An operational Status of a licensing process.'
LicensingProcessStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=LicensingProcessStatus, enum_prefix=None)
LicensingProcessStatus.Pending = LicensingProcessStatus._CF_enumeration.addEnumeration(unicode_value='Pending', tag='Pending')
LicensingProcessStatus.Processed = LicensingProcessStatus._CF_enumeration.addEnumeration(unicode_value='Processed', tag='Processed')
LicensingProcessStatus.ThirdPartyInformationRequested = LicensingProcessStatus._CF_enumeration.addEnumeration(unicode_value='ThirdPartyInformationRequested', tag='ThirdPartyInformationRequested')
LicensingProcessStatus._InitializeFacetMap(LicensingProcessStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'LicensingProcessStatus', LicensingProcessStatus)

# Atomic simple type: {http://ddex.net/xml/avs/avs}LodFileStatus
class LodFileStatus (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Status of a File in terms of its validity in the Release Delivery Choreography Standard."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LodFileStatus')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 6053, 3)
    _Documentation = 'A Status of a File in terms of its validity in the Release Delivery Choreography Standard.'
LodFileStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=LodFileStatus, enum_prefix=None)
LodFileStatus.FileOK = LodFileStatus._CF_enumeration.addEnumeration(unicode_value='FileOK', tag='FileOK')
LodFileStatus._InitializeFacetMap(LodFileStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'LodFileStatus', LodFileStatus)

# Atomic simple type: {http://ddex.net/xml/avs/avs}LodProposedActionType
class LodProposedActionType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of action that is proposed."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LodProposedActionType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 6065, 3)
    _Documentation = 'A Type of action that is proposed.'
LodProposedActionType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=LodProposedActionType, enum_prefix=None)
LodProposedActionType.ResendXmlOnly = LodProposedActionType._CF_enumeration.addEnumeration(unicode_value='ResendXmlOnly', tag='ResendXmlOnly')
LodProposedActionType._InitializeFacetMap(LodProposedActionType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'LodProposedActionType', LodProposedActionType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}MembershipType
class MembershipType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of membership."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MembershipType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 6077, 3)
    _Documentation = 'A Type of membership.'
MembershipType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MembershipType, enum_prefix=None)
MembershipType.NationalMember = MembershipType._CF_enumeration.addEnumeration(unicode_value='NationalMember', tag='NationalMember')
MembershipType.RegionalMember = MembershipType._CF_enumeration.addEnumeration(unicode_value='RegionalMember', tag='RegionalMember')
MembershipType.WorldwideMember = MembershipType._CF_enumeration.addEnumeration(unicode_value='WorldwideMember', tag='WorldwideMember')
MembershipType._InitializeFacetMap(MembershipType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MembershipType', MembershipType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}MessageActionType
class MessageActionType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of action requested in a Message."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MessageActionType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 6099, 3)
    _Documentation = 'A Type of action requested in a Message.'
MessageActionType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MessageActionType, enum_prefix=None)
MessageActionType.BackCatalogDelivery = MessageActionType._CF_enumeration.addEnumeration(unicode_value='BackCatalogDelivery', tag='BackCatalogDelivery')
MessageActionType.HighPriorityDelivery = MessageActionType._CF_enumeration.addEnumeration(unicode_value='HighPriorityDelivery', tag='HighPriorityDelivery')
MessageActionType.NewReleaseDelivery = MessageActionType._CF_enumeration.addEnumeration(unicode_value='NewReleaseDelivery', tag='NewReleaseDelivery')
MessageActionType.ReDelivery = MessageActionType._CF_enumeration.addEnumeration(unicode_value='ReDelivery', tag='ReDelivery')
MessageActionType.TakeDown = MessageActionType._CF_enumeration.addEnumeration(unicode_value='TakeDown', tag='TakeDown')
MessageActionType.UserDefined = MessageActionType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
MessageActionType._InitializeFacetMap(MessageActionType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MessageActionType', MessageActionType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}MessageContentRevenueType
class MessageContentRevenueType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of revenue to which the content of the Message relates."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MessageContentRevenueType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 6136, 3)
    _Documentation = 'A Type of revenue to which the content of the Message relates.'
MessageContentRevenueType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MessageContentRevenueType, enum_prefix=None)
MessageContentRevenueType.NonTransactionalRevenue = MessageContentRevenueType._CF_enumeration.addEnumeration(unicode_value='NonTransactionalRevenue', tag='NonTransactionalRevenue')
MessageContentRevenueType.TransactionalRevenue = MessageContentRevenueType._CF_enumeration.addEnumeration(unicode_value='TransactionalRevenue', tag='TransactionalRevenue')
MessageContentRevenueType.UserDefined = MessageContentRevenueType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
MessageContentRevenueType._InitializeFacetMap(MessageContentRevenueType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MessageContentRevenueType', MessageContentRevenueType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}MessageContextType
class MessageContextType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Message in the Letters Of Direction Choreography Standard."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MessageContextType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 6158, 3)
    _Documentation = 'A Type of Message in the Letters Of Direction Choreography Standard.'
MessageContextType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MessageContextType, enum_prefix=None)
MessageContextType.MusicalWorkClaimRequestMessageInIdentificationCycle = MessageContextType._CF_enumeration.addEnumeration(unicode_value='MusicalWorkClaimRequestMessageInIdentificationCycle', tag='MusicalWorkClaimRequestMessageInIdentificationCycle')
MessageContextType.MusicalWorkClaimNotificationMessageInIdentificationCycle = MessageContextType._CF_enumeration.addEnumeration(unicode_value='MusicalWorkClaimNotificationMessageInIdentificationCycle', tag='MusicalWorkClaimNotificationMessageInIdentificationCycle')
MessageContextType.MusicalWorkClaimRequestMessageInConfirmationCycle = MessageContextType._CF_enumeration.addEnumeration(unicode_value='MusicalWorkClaimRequestMessageInConfirmationCycle', tag='MusicalWorkClaimRequestMessageInConfirmationCycle')
MessageContextType.MusicalWorkClaimNotificationMessageInConfirmationCycle = MessageContextType._CF_enumeration.addEnumeration(unicode_value='MusicalWorkClaimNotificationMessageInConfirmationCycle', tag='MusicalWorkClaimNotificationMessageInConfirmationCycle')
MessageContextType.MusicalWorkClaimNotificationMessageInLoCCycleAsLoDMessage = MessageContextType._CF_enumeration.addEnumeration(unicode_value='MusicalWorkClaimNotificationMessageInLoCCycleAsLoDMessage', tag='MusicalWorkClaimNotificationMessageInLoCCycleAsLoDMessage')
MessageContextType.MusicalWorkClaimNotificationMessageInLoCCycleAsLoDConfirmation = MessageContextType._CF_enumeration.addEnumeration(unicode_value='MusicalWorkClaimNotificationMessageInLoCCycleAsLoDConfirmation', tag='MusicalWorkClaimNotificationMessageInLoCCycleAsLoDConfirmation')
MessageContextType._InitializeFacetMap(MessageContextType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MessageContextType', MessageContextType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}MessageControlType
class MessageControlType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Message according to its operational status."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MessageControlType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 6195, 3)
    _Documentation = 'A Type of Message according to its operational status.'
MessageControlType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MessageControlType, enum_prefix=None)
MessageControlType.LiveMessage = MessageControlType._CF_enumeration.addEnumeration(unicode_value='LiveMessage', tag='LiveMessage')
MessageControlType.TestMessage = MessageControlType._CF_enumeration.addEnumeration(unicode_value='TestMessage', tag='TestMessage')
MessageControlType._InitializeFacetMap(MessageControlType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MessageControlType', MessageControlType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}MidiType
class MidiType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of MIDI."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MidiType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 6212, 3)
    _Documentation = 'A Type of MIDI.'
MidiType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MidiType, enum_prefix=None)
MidiType.MonophonicMidi = MidiType._CF_enumeration.addEnumeration(unicode_value='MonophonicMidi', tag='MonophonicMidi')
MidiType.PolyphonicMidi = MidiType._CF_enumeration.addEnumeration(unicode_value='PolyphonicMidi', tag='PolyphonicMidi')
MidiType.Unknown = MidiType._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
MidiType.UserDefined = MidiType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
MidiType._InitializeFacetMap(MidiType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MidiType', MidiType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}MlcMessageType
class MlcMessageType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Message in the Music Licensing Company Message Suite."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MlcMessageType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 6239, 3)
    _Documentation = 'A Type of Message in the Music Licensing Company Message Suite.'
MlcMessageType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MlcMessageType, enum_prefix=None)
MlcMessageType.DeclarationOfSoundRecordingRightsClaimMessage = MlcMessageType._CF_enumeration.addEnumeration(unicode_value='DeclarationOfSoundRecordingRightsClaimMessage', tag='DeclarationOfSoundRecordingRightsClaimMessage')
MlcMessageType.RequestSoundRecordingInformationMessage = MlcMessageType._CF_enumeration.addEnumeration(unicode_value='RequestSoundRecordingInformationMessage', tag='RequestSoundRecordingInformationMessage')
MlcMessageType.RevokeSoundRecordingRightsClaimMessage = MlcMessageType._CF_enumeration.addEnumeration(unicode_value='RevokeSoundRecordingRightsClaimMessage', tag='RevokeSoundRecordingRightsClaimMessage')
MlcMessageType.SalesReportMessage = MlcMessageType._CF_enumeration.addEnumeration(unicode_value='SalesReportMessage', tag='SalesReportMessage')
MlcMessageType.DeclarationOfRevenueMessage = MlcMessageType._CF_enumeration.addEnumeration(unicode_value='DeclarationOfRevenueMessage', tag='DeclarationOfRevenueMessage')
MlcMessageType._InitializeFacetMap(MlcMessageType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MlcMessageType', MlcMessageType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}MusicalWorkRightsClaimType
class MusicalWorkRightsClaimType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of RightsClaim related to a MusicalWork."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MusicalWorkRightsClaimType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 6277, 3)
    _Documentation = 'A Type of RightsClaim related to a MusicalWork.'
MusicalWorkRightsClaimType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MusicalWorkRightsClaimType, enum_prefix=None)
MusicalWorkRightsClaimType.CopyrightControl = MusicalWorkRightsClaimType._CF_enumeration.addEnumeration(unicode_value='CopyrightControl', tag='CopyrightControl')
MusicalWorkRightsClaimType.NonMemberClaim = MusicalWorkRightsClaimType._CF_enumeration.addEnumeration(unicode_value='NonMemberClaim', tag='NonMemberClaim')
MusicalWorkRightsClaimType.PublicDomain = MusicalWorkRightsClaimType._CF_enumeration.addEnumeration(unicode_value='PublicDomain', tag='PublicDomain')
MusicalWorkRightsClaimType.SocietyClaim = MusicalWorkRightsClaimType._CF_enumeration.addEnumeration(unicode_value='SocietyClaim', tag='SocietyClaim')
MusicalWorkRightsClaimType.Unknown = MusicalWorkRightsClaimType._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
MusicalWorkRightsClaimType._InitializeFacetMap(MusicalWorkRightsClaimType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MusicalWorkRightsClaimType', MusicalWorkRightsClaimType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}MusicalWorkType
class MusicalWorkType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of MusicalWork."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MusicalWorkType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 6309, 3)
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

# Atomic simple type: {http://ddex.net/xml/avs/avs}MwlCaCMessageInBatchType
class MwlCaCMessageInBatchType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Message in a batch in the Choreography for the Mechanical Licensing of Musical Works in Canada."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MwlCaCMessageInBatchType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 6461, 3)
    _Documentation = 'A Type of Message in a batch in the Choreography for the Mechanical Licensing of Musical Works in Canada.'
MwlCaCMessageInBatchType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MwlCaCMessageInBatchType, enum_prefix=None)
MwlCaCMessageInBatchType.LicenseOrClaimRequestMessage = MwlCaCMessageInBatchType._CF_enumeration.addEnumeration(unicode_value='LicenseOrClaimRequestMessage', tag='LicenseOrClaimRequestMessage')
MwlCaCMessageInBatchType.LicenseOrClaimMessage = MwlCaCMessageInBatchType._CF_enumeration.addEnumeration(unicode_value='LicenseOrClaimMessage', tag='LicenseOrClaimMessage')
MwlCaCMessageInBatchType.LicensingInformationRequestMessage = MwlCaCMessageInBatchType._CF_enumeration.addEnumeration(unicode_value='LicensingInformationRequestMessage', tag='LicensingInformationRequestMessage')
MwlCaCMessageInBatchType.LicenseOrClaimConfirmationMessage = MwlCaCMessageInBatchType._CF_enumeration.addEnumeration(unicode_value='LicenseOrClaimConfirmationMessage', tag='LicenseOrClaimConfirmationMessage')
MwlCaCMessageInBatchType.NewReleaseMessage = MwlCaCMessageInBatchType._CF_enumeration.addEnumeration(unicode_value='NewReleaseMessage', tag='NewReleaseMessage')
MwlCaCMessageInBatchType.ContractDeliveryMessage = MwlCaCMessageInBatchType._CF_enumeration.addEnumeration(unicode_value='ContractDeliveryMessage', tag='ContractDeliveryMessage')
MwlCaCMessageInBatchType.ProductDeletionMessage = MwlCaCMessageInBatchType._CF_enumeration.addEnumeration(unicode_value='ProductDeletionMessage', tag='ProductDeletionMessage')
MwlCaCMessageInBatchType._InitializeFacetMap(MwlCaCMessageInBatchType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MwlCaCMessageInBatchType', MwlCaCMessageInBatchType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}MwnMessageType
class MwnMessageType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Message in the Electronic Musical Work Notification Message Suite."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MwnMessageType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 6503, 3)
    _Documentation = 'A Type of Message in the Electronic Musical Work Notification Message Suite.'
MwnMessageType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MwnMessageType, enum_prefix=None)
MwnMessageType.MusicalWorkClaimNotificationMessage = MwnMessageType._CF_enumeration.addEnumeration(unicode_value='MusicalWorkClaimNotificationMessage', tag='MusicalWorkClaimNotificationMessage')
MwnMessageType.MusicalWorkClaimConflictNotificationMessage = MwnMessageType._CF_enumeration.addEnumeration(unicode_value='MusicalWorkClaimConflictNotificationMessage', tag='MusicalWorkClaimConflictNotificationMessage')
MwnMessageType.MusicalWorkClaimRequestMessage = MwnMessageType._CF_enumeration.addEnumeration(unicode_value='MusicalWorkClaimRequestMessage', tag='MusicalWorkClaimRequestMessage')
MwnMessageType.FtpAcknowledgementMessage = MwnMessageType._CF_enumeration.addEnumeration(unicode_value='FtpAcknowledgementMessage', tag='FtpAcknowledgementMessage')
MwnMessageType.ManifestMessage = MwnMessageType._CF_enumeration.addEnumeration(unicode_value='ManifestMessage', tag='ManifestMessage')
MwnMessageType._InitializeFacetMap(MwnMessageType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MwnMessageType', MwnMessageType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}NewReleaseMessageStatus
class NewReleaseMessageStatus (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Status of a NewReleaseMessage."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NewReleaseMessageStatus')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 6535, 3)
    _Documentation = 'A Status of a NewReleaseMessage.'
NewReleaseMessageStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=NewReleaseMessageStatus, enum_prefix=None)
NewReleaseMessageStatus.NewReleaseMessageNotProvided = NewReleaseMessageStatus._CF_enumeration.addEnumeration(unicode_value='NewReleaseMessageNotProvided', tag='NewReleaseMessageNotProvided')
NewReleaseMessageStatus.NewReleaseMessageProvided = NewReleaseMessageStatus._CF_enumeration.addEnumeration(unicode_value='NewReleaseMessageProvided', tag='NewReleaseMessageProvided')
NewReleaseMessageStatus._InitializeFacetMap(NewReleaseMessageStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'NewReleaseMessageStatus', NewReleaseMessageStatus)

# Atomic simple type: {http://ddex.net/xml/avs/avs}OperatingSystemType
class OperatingSystemType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of OperatingSystem."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OperatingSystemType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 6552, 3)
    _Documentation = 'A Type of OperatingSystem.'
OperatingSystemType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=OperatingSystemType, enum_prefix=None)
OperatingSystemType.MacOS = OperatingSystemType._CF_enumeration.addEnumeration(unicode_value='MacOS', tag='MacOS')
OperatingSystemType.MsWindows = OperatingSystemType._CF_enumeration.addEnumeration(unicode_value='MsWindows', tag='MsWindows')
OperatingSystemType.Symbian = OperatingSystemType._CF_enumeration.addEnumeration(unicode_value='Symbian', tag='Symbian')
OperatingSystemType.Unknown = OperatingSystemType._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
OperatingSystemType._InitializeFacetMap(OperatingSystemType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'OperatingSystemType', OperatingSystemType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}OrderType
class OrderType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of order."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OrderType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 6579, 3)
    _Documentation = 'A Type of order.'
OrderType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=OrderType, enum_prefix=None)
OrderType.BackCatalogOrder = OrderType._CF_enumeration.addEnumeration(unicode_value='BackCatalogOrder', tag='BackCatalogOrder')
OrderType.ExpressOrder = OrderType._CF_enumeration.addEnumeration(unicode_value='ExpressOrder', tag='ExpressOrder')
OrderType.HardDiskOrder = OrderType._CF_enumeration.addEnumeration(unicode_value='HardDiskOrder', tag='HardDiskOrder')
OrderType.MetadataOnlyOrder = OrderType._CF_enumeration.addEnumeration(unicode_value='MetadataOnlyOrder', tag='MetadataOnlyOrder')
OrderType.NewReleaseOrder = OrderType._CF_enumeration.addEnumeration(unicode_value='NewReleaseOrder', tag='NewReleaseOrder')
OrderType.OffCycleRushOrder = OrderType._CF_enumeration.addEnumeration(unicode_value='OffCycleRushOrder', tag='OffCycleRushOrder')
OrderType.PreOrder = OrderType._CF_enumeration.addEnumeration(unicode_value='PreOrder', tag='PreOrder')
OrderType.ReDeliveryOrder = OrderType._CF_enumeration.addEnumeration(unicode_value='ReDeliveryOrder', tag='ReDeliveryOrder')
OrderType.TakeDownOrder = OrderType._CF_enumeration.addEnumeration(unicode_value='TakeDownOrder', tag='TakeDownOrder')
OrderType.UserDefined = OrderType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
OrderType._InitializeFacetMap(OrderType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'OrderType', OrderType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}PLineType
class PLineType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of PLine."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PLineType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 6636, 3)
    _Documentation = 'A Type of PLine.'
PLineType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PLineType, enum_prefix=None)
PLineType.OriginalPLine = PLineType._CF_enumeration.addEnumeration(unicode_value='OriginalPLine', tag='OriginalPLine')
PLineType.RemasteringPLine = PLineType._CF_enumeration.addEnumeration(unicode_value='RemasteringPLine', tag='RemasteringPLine')
PLineType._InitializeFacetMap(PLineType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'PLineType', PLineType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}ParentalWarningType
class ParentalWarningType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Creation according to advice which it carries about the level of explicitness or offensiveness of its content."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ParentalWarningType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 6653, 3)
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

# Atomic simple type: {http://ddex.net/xml/avs/avs}PartyRelationshipType
class PartyRelationshipType (pyxb.binding.datatypes.string):

    """A Type of relationship between two Parties."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PartyRelationshipType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 6690, 3)
    _Documentation = 'A Type of relationship between two Parties.'
PartyRelationshipType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'PartyRelationshipType', PartyRelationshipType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}PercentageType
class PercentageType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of PercentageRate."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PercentageType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 6696, 3)
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

# Atomic simple type: {http://ddex.net/xml/avs/avs}PriceInformationType
class PriceInformationType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Price for which information is provided."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PriceInformationType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 6733, 3)
    _Documentation = 'A Type of Price for which information is provided.'
PriceInformationType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PriceInformationType, enum_prefix=None)
PriceInformationType.StandardRetailPrice = PriceInformationType._CF_enumeration.addEnumeration(unicode_value='StandardRetailPrice', tag='StandardRetailPrice')
PriceInformationType.PreOrderPrice = PriceInformationType._CF_enumeration.addEnumeration(unicode_value='PreOrderPrice', tag='PreOrderPrice')
PriceInformationType._InitializeFacetMap(PriceInformationType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'PriceInformationType', PriceInformationType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}PriceRangeType
class PriceRangeType (pyxb.binding.datatypes.string):

    """A Type of Price according to its value range."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PriceRangeType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 6750, 3)
    _Documentation = 'A Type of Price according to its value range.'
PriceRangeType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'PriceRangeType', PriceRangeType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}PriceType
class PriceType (pyxb.binding.datatypes.string):

    """A Type of Price."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PriceType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 6756, 3)
    _Documentation = 'A Type of Price.'
PriceType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'PriceType', PriceType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}Priority
class Priority (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of priority."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Priority')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 6762, 3)
    _Documentation = 'A Type of priority.'
Priority._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Priority, enum_prefix=None)
Priority.High = Priority._CF_enumeration.addEnumeration(unicode_value='High', tag='High')
Priority.Low = Priority._CF_enumeration.addEnumeration(unicode_value='Low', tag='Low')
Priority.Normal = Priority._CF_enumeration.addEnumeration(unicode_value='Normal', tag='Normal')
Priority._InitializeFacetMap(Priority._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'Priority', Priority)

# Atomic simple type: {http://ddex.net/xml/avs/avs}ProductType
class ProductType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Product."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ProductType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 6784, 3)
    _Documentation = 'A Type of Product.'
ProductType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ProductType, enum_prefix=None)
ProductType.AudioProduct = ProductType._CF_enumeration.addEnumeration(unicode_value='AudioProduct', tag='AudioProduct')
ProductType.GraphicsProduct = ProductType._CF_enumeration.addEnumeration(unicode_value='GraphicsProduct', tag='GraphicsProduct')
ProductType.MixedMediaBundleProduct = ProductType._CF_enumeration.addEnumeration(unicode_value='MixedMediaBundleProduct', tag='MixedMediaBundleProduct')
ProductType.MobileProduct = ProductType._CF_enumeration.addEnumeration(unicode_value='MobileProduct', tag='MobileProduct')
ProductType.UserDefined = ProductType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
ProductType.VideoProduct = ProductType._CF_enumeration.addEnumeration(unicode_value='VideoProduct', tag='VideoProduct')
ProductType._InitializeFacetMap(ProductType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ProductType', ProductType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}ProjectContributorRelationshipType
class ProjectContributorRelationshipType (pyxb.binding.datatypes.string):

    """A Type of relationship between a Project and a Contributor."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ProjectContributorRelationshipType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 6821, 3)
    _Documentation = 'A Type of relationship between a Project and a Contributor.'
ProjectContributorRelationshipType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'ProjectContributorRelationshipType', ProjectContributorRelationshipType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}Purpose
class Purpose (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of use that is the purpose of an action."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Purpose')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 6827, 3)
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

# Atomic simple type: {http://ddex.net/xml/avs/avs}RateModificationType
class RateModificationType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of a rate modification."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RateModificationType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 6869, 3)
    _Documentation = 'A Type of a rate modification.'
RateModificationType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=RateModificationType, enum_prefix=None)
RateModificationType.MultipleDiscProvision = RateModificationType._CF_enumeration.addEnumeration(unicode_value='MultipleDiscProvision', tag='MultipleDiscProvision')
RateModificationType.OtherProvision = RateModificationType._CF_enumeration.addEnumeration(unicode_value='OtherProvision', tag='OtherProvision')
RateModificationType.SalesVolumeProvision = RateModificationType._CF_enumeration.addEnumeration(unicode_value='SalesVolumeProvision', tag='SalesVolumeProvision')
RateModificationType.VideoProvision = RateModificationType._CF_enumeration.addEnumeration(unicode_value='VideoProvision', tag='VideoProvision')
RateModificationType._InitializeFacetMap(RateModificationType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'RateModificationType', RateModificationType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}RatingAgency
class RatingAgency (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An Organization that issues ParentalWarnings."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RatingAgency')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 6896, 3)
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
RatingAgency.OFLC_NZ = RatingAgency._CF_enumeration.addEnumeration(unicode_value='OFLC-NZ', tag='OFLC_NZ')
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

# Atomic simple type: {http://ddex.net/xml/avs/avs}ReasonType
class ReasonType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of reason."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReasonType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 7123, 3)
    _Documentation = 'A Type of reason.'
ReasonType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ReasonType, enum_prefix=None)
ReasonType.ChartReporting = ReasonType._CF_enumeration.addEnumeration(unicode_value='ChartReporting', tag='ChartReporting')
ReasonType.RoyaltyReporting = ReasonType._CF_enumeration.addEnumeration(unicode_value='RoyaltyReporting', tag='RoyaltyReporting')
ReasonType.UserDefined = ReasonType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
ReasonType._InitializeFacetMap(ReasonType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ReasonType', ReasonType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}RecipientRevenueType
class RecipientRevenueType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of revenue according to the recipient of the payment."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RecipientRevenueType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 7145, 3)
    _Documentation = 'A Type of revenue according to the recipient of the payment.'
RecipientRevenueType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=RecipientRevenueType, enum_prefix=None)
RecipientRevenueType.PerformerAndProducerRevenue = RecipientRevenueType._CF_enumeration.addEnumeration(unicode_value='PerformerAndProducerRevenue', tag='PerformerAndProducerRevenue')
RecipientRevenueType.PerformerRevenue = RecipientRevenueType._CF_enumeration.addEnumeration(unicode_value='PerformerRevenue', tag='PerformerRevenue')
RecipientRevenueType.ProducerRevenue = RecipientRevenueType._CF_enumeration.addEnumeration(unicode_value='ProducerRevenue', tag='ProducerRevenue')
RecipientRevenueType._InitializeFacetMap(RecipientRevenueType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'RecipientRevenueType', RecipientRevenueType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}RecordingMode
class RecordingMode (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A mode of a Recording."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RecordingMode')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 7167, 3)
    _Documentation = 'A mode of a Recording.'
RecordingMode._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=RecordingMode, enum_prefix=None)
RecordingMode.Mono = RecordingMode._CF_enumeration.addEnumeration(unicode_value='Mono', tag='Mono')
RecordingMode.MultichannelAudio = RecordingMode._CF_enumeration.addEnumeration(unicode_value='MultichannelAudio', tag='MultichannelAudio')
RecordingMode.Stereo = RecordingMode._CF_enumeration.addEnumeration(unicode_value='Stereo', tag='Stereo')
RecordingMode.Unknown = RecordingMode._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
RecordingMode._InitializeFacetMap(RecordingMode._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'RecordingMode', RecordingMode)

# Atomic simple type: {http://ddex.net/xml/avs/avs}RedeliveryReasonType
class RedeliveryReasonType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A reason for a redelivery."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RedeliveryReasonType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 7194, 3)
    _Documentation = 'A reason for a redelivery.'
RedeliveryReasonType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=RedeliveryReasonType, enum_prefix=None)
RedeliveryReasonType.BinaryCorrupted = RedeliveryReasonType._CF_enumeration.addEnumeration(unicode_value='BinaryCorrupted', tag='BinaryCorrupted')
RedeliveryReasonType.MetadataInadequate = RedeliveryReasonType._CF_enumeration.addEnumeration(unicode_value='MetadataInadequate', tag='MetadataInadequate')
RedeliveryReasonType.PackageIncomplete = RedeliveryReasonType._CF_enumeration.addEnumeration(unicode_value='PackageIncomplete', tag='PackageIncomplete')
RedeliveryReasonType.ProcessingErrorAtReleaseDistributor = RedeliveryReasonType._CF_enumeration.addEnumeration(unicode_value='ProcessingErrorAtReleaseDistributor', tag='ProcessingErrorAtReleaseDistributor')
RedeliveryReasonType.UserDefined = RedeliveryReasonType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
RedeliveryReasonType._InitializeFacetMap(RedeliveryReasonType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'RedeliveryReasonType', RedeliveryReasonType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}ReferenceUnit
class ReferenceUnit (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A unit to which a Quantity refers."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReferenceUnit')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 7226, 3)
    _Documentation = 'A unit to which a Quantity refers.'
ReferenceUnit._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ReferenceUnit, enum_prefix=None)
ReferenceUnit.PerLicense = ReferenceUnit._CF_enumeration.addEnumeration(unicode_value='PerLicense', tag='PerLicense')
ReferenceUnit.PerUse = ReferenceUnit._CF_enumeration.addEnumeration(unicode_value='PerUse', tag='PerUse')
ReferenceUnit._InitializeFacetMap(ReferenceUnit._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ReferenceUnit', ReferenceUnit)

# Atomic simple type: {http://ddex.net/xml/avs/avs}RelationalRelator
class RelationalRelator (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Relator between two Entities expressing a measurable relationship."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RelationalRelator')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 7243, 3)
    _Documentation = 'A Relator between two Entities expressing a measurable relationship.'
RelationalRelator._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=RelationalRelator, enum_prefix=None)
RelationalRelator.EqualTo = RelationalRelator._CF_enumeration.addEnumeration(unicode_value='EqualTo', tag='EqualTo')
RelationalRelator.LessThan = RelationalRelator._CF_enumeration.addEnumeration(unicode_value='LessThan', tag='LessThan')
RelationalRelator.LessThanOrEqualTo = RelationalRelator._CF_enumeration.addEnumeration(unicode_value='LessThanOrEqualTo', tag='LessThanOrEqualTo')
RelationalRelator.MoreThan = RelationalRelator._CF_enumeration.addEnumeration(unicode_value='MoreThan', tag='MoreThan')
RelationalRelator.MoreThanOrEqualTo = RelationalRelator._CF_enumeration.addEnumeration(unicode_value='MoreThanOrEqualTo', tag='MoreThanOrEqualTo')
RelationalRelator.NotEqualTo = RelationalRelator._CF_enumeration.addEnumeration(unicode_value='NotEqualTo', tag='NotEqualTo')
RelationalRelator._InitializeFacetMap(RelationalRelator._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'RelationalRelator', RelationalRelator)

# Atomic simple type: {http://ddex.net/xml/avs/avs}ReleaseAvailabilityStatus
class ReleaseAvailabilityStatus (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Status of the availability of a Release."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReleaseAvailabilityStatus')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 7280, 3)
    _Documentation = 'A Status of the availability of a Release.'
ReleaseAvailabilityStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ReleaseAvailabilityStatus, enum_prefix=None)
ReleaseAvailabilityStatus.AvailableForDSP = ReleaseAvailabilityStatus._CF_enumeration.addEnumeration(unicode_value='AvailableForDSP', tag='AvailableForDSP')
ReleaseAvailabilityStatus.NotAvailableForDSP = ReleaseAvailabilityStatus._CF_enumeration.addEnumeration(unicode_value='NotAvailableForDSP', tag='NotAvailableForDSP')
ReleaseAvailabilityStatus.NotClearedForDSP = ReleaseAvailabilityStatus._CF_enumeration.addEnumeration(unicode_value='NotClearedForDSP', tag='NotClearedForDSP')
ReleaseAvailabilityStatus.NotClearedForTerritory = ReleaseAvailabilityStatus._CF_enumeration.addEnumeration(unicode_value='NotClearedForTerritory', tag='NotClearedForTerritory')
ReleaseAvailabilityStatus.NotYetPrepared = ReleaseAvailabilityStatus._CF_enumeration.addEnumeration(unicode_value='NotYetPrepared', tag='NotYetPrepared')
ReleaseAvailabilityStatus.UserDefined = ReleaseAvailabilityStatus._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
ReleaseAvailabilityStatus._InitializeFacetMap(ReleaseAvailabilityStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ReleaseAvailabilityStatus', ReleaseAvailabilityStatus)

# Atomic simple type: {http://ddex.net/xml/avs/avs}ReleaseRelationshipType
class ReleaseRelationshipType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of relationship between two Releases."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReleaseRelationshipType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 7317, 3)
    _Documentation = 'A Type of relationship between two Releases.'
ReleaseRelationshipType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ReleaseRelationshipType, enum_prefix=None)
ReleaseRelationshipType.HasArtistFromEnsemble = ReleaseRelationshipType._CF_enumeration.addEnumeration(unicode_value='HasArtistFromEnsemble', tag='HasArtistFromEnsemble')
ReleaseRelationshipType.HasArtistFromSameEnsemble = ReleaseRelationshipType._CF_enumeration.addEnumeration(unicode_value='HasArtistFromSameEnsemble', tag='HasArtistFromSameEnsemble')
ReleaseRelationshipType.HasEnsembleWithArtist = ReleaseRelationshipType._CF_enumeration.addEnumeration(unicode_value='HasEnsembleWithArtist', tag='HasEnsembleWithArtist')
ReleaseRelationshipType.HasSameArtist = ReleaseRelationshipType._CF_enumeration.addEnumeration(unicode_value='HasSameArtist', tag='HasSameArtist')
ReleaseRelationshipType.HasSameRecordingProject = ReleaseRelationshipType._CF_enumeration.addEnumeration(unicode_value='HasSameRecordingProject', tag='HasSameRecordingProject')
ReleaseRelationshipType.HasSimilarContent = ReleaseRelationshipType._CF_enumeration.addEnumeration(unicode_value='HasSimilarContent', tag='HasSimilarContent')
ReleaseRelationshipType.IsDigitalEquivalentToPhysical = ReleaseRelationshipType._CF_enumeration.addEnumeration(unicode_value='IsDigitalEquivalentToPhysical', tag='IsDigitalEquivalentToPhysical')
ReleaseRelationshipType.IsEquivalentToAudio = ReleaseRelationshipType._CF_enumeration.addEnumeration(unicode_value='IsEquivalentToAudio', tag='IsEquivalentToAudio')
ReleaseRelationshipType.IsEquivalentToVideo = ReleaseRelationshipType._CF_enumeration.addEnumeration(unicode_value='IsEquivalentToVideo', tag='IsEquivalentToVideo')
ReleaseRelationshipType.IsExtendedFromAlbum = ReleaseRelationshipType._CF_enumeration.addEnumeration(unicode_value='IsExtendedFromAlbum', tag='IsExtendedFromAlbum')
ReleaseRelationshipType.IsFromAudio = ReleaseRelationshipType._CF_enumeration.addEnumeration(unicode_value='IsFromAudio', tag='IsFromAudio')
ReleaseRelationshipType.IsFromVideo = ReleaseRelationshipType._CF_enumeration.addEnumeration(unicode_value='IsFromVideo', tag='IsFromVideo')
ReleaseRelationshipType.IsParentRelease = ReleaseRelationshipType._CF_enumeration.addEnumeration(unicode_value='IsParentRelease', tag='IsParentRelease')
ReleaseRelationshipType.IsPhysicalEquivalentToDigital = ReleaseRelationshipType._CF_enumeration.addEnumeration(unicode_value='IsPhysicalEquivalentToDigital', tag='IsPhysicalEquivalentToDigital')
ReleaseRelationshipType.IsReleaseFromRelease = ReleaseRelationshipType._CF_enumeration.addEnumeration(unicode_value='IsReleaseFromRelease', tag='IsReleaseFromRelease')
ReleaseRelationshipType.IsShortenedFromAlbum = ReleaseRelationshipType._CF_enumeration.addEnumeration(unicode_value='IsShortenedFromAlbum', tag='IsShortenedFromAlbum')
ReleaseRelationshipType.Unknown = ReleaseRelationshipType._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
ReleaseRelationshipType.UserDefined = ReleaseRelationshipType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
ReleaseRelationshipType._InitializeFacetMap(ReleaseRelationshipType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ReleaseRelationshipType', ReleaseRelationshipType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}ReleaseResourceType
class ReleaseResourceType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Resource in the context of a Release."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReleaseResourceType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 7414, 3)
    _Documentation = 'A Type of Resource in the context of a Release.'
ReleaseResourceType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ReleaseResourceType, enum_prefix=None)
ReleaseResourceType.PrimaryResource = ReleaseResourceType._CF_enumeration.addEnumeration(unicode_value='PrimaryResource', tag='PrimaryResource')
ReleaseResourceType.SecondaryResource = ReleaseResourceType._CF_enumeration.addEnumeration(unicode_value='SecondaryResource', tag='SecondaryResource')
ReleaseResourceType._InitializeFacetMap(ReleaseResourceType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ReleaseResourceType', ReleaseResourceType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}ReleaseType
class ReleaseType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Release according to its content, Duration and/or number of components. Note: a ReleaseType is the form in which a ReleaseCreator anticipates offering a Release to Consumers."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReleaseType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 7431, 3)
    _Documentation = 'A Type of Release according to its content, Duration and/or number of components. Note: a ReleaseType is the form in which a ReleaseCreator anticipates offering a Release to Consumers.'
ReleaseType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ReleaseType, enum_prefix=None)
ReleaseType.AdvertisementVideo = ReleaseType._CF_enumeration.addEnumeration(unicode_value='AdvertisementVideo', tag='AdvertisementVideo')
ReleaseType.Album = ReleaseType._CF_enumeration.addEnumeration(unicode_value='Album', tag='Album')
ReleaseType.AlertToneRelease = ReleaseType._CF_enumeration.addEnumeration(unicode_value='AlertToneRelease', tag='AlertToneRelease')
ReleaseType.Animation = ReleaseType._CF_enumeration.addEnumeration(unicode_value='Animation', tag='Animation')
ReleaseType.AsPerContract = ReleaseType._CF_enumeration.addEnumeration(unicode_value='AsPerContract', tag='AsPerContract')
ReleaseType.AudioBookRelease = ReleaseType._CF_enumeration.addEnumeration(unicode_value='AudioBookRelease', tag='AudioBookRelease')
ReleaseType.AudioClipRelease = ReleaseType._CF_enumeration.addEnumeration(unicode_value='AudioClipRelease', tag='AudioClipRelease')
ReleaseType.BackCoverImageRelease = ReleaseType._CF_enumeration.addEnumeration(unicode_value='BackCoverImageRelease', tag='BackCoverImageRelease')
ReleaseType.BookletBackImageRelease = ReleaseType._CF_enumeration.addEnumeration(unicode_value='BookletBackImageRelease', tag='BookletBackImageRelease')
ReleaseType.BookletFrontImageRelease = ReleaseType._CF_enumeration.addEnumeration(unicode_value='BookletFrontImageRelease', tag='BookletFrontImageRelease')
ReleaseType.BookletRelease = ReleaseType._CF_enumeration.addEnumeration(unicode_value='BookletRelease', tag='BookletRelease')
ReleaseType.Bundle = ReleaseType._CF_enumeration.addEnumeration(unicode_value='Bundle', tag='Bundle')
ReleaseType.ClassicalAlbum = ReleaseType._CF_enumeration.addEnumeration(unicode_value='ClassicalAlbum', tag='ClassicalAlbum')
ReleaseType.ConcertVideo = ReleaseType._CF_enumeration.addEnumeration(unicode_value='ConcertVideo', tag='ConcertVideo')
ReleaseType.CorporateFilm = ReleaseType._CF_enumeration.addEnumeration(unicode_value='CorporateFilm', tag='CorporateFilm')
ReleaseType.DigitalBoxSetRelease = ReleaseType._CF_enumeration.addEnumeration(unicode_value='DigitalBoxSetRelease', tag='DigitalBoxSetRelease')
ReleaseType.Documentary = ReleaseType._CF_enumeration.addEnumeration(unicode_value='Documentary', tag='Documentary')
ReleaseType.DocumentImageRelease = ReleaseType._CF_enumeration.addEnumeration(unicode_value='DocumentImageRelease', tag='DocumentImageRelease')
ReleaseType.EBookRelease = ReleaseType._CF_enumeration.addEnumeration(unicode_value='EBookRelease', tag='EBookRelease')
ReleaseType.Episode = ReleaseType._CF_enumeration.addEnumeration(unicode_value='Episode', tag='Episode')
ReleaseType.FeatureFilm = ReleaseType._CF_enumeration.addEnumeration(unicode_value='FeatureFilm', tag='FeatureFilm')
ReleaseType.FilmBundle = ReleaseType._CF_enumeration.addEnumeration(unicode_value='FilmBundle', tag='FilmBundle')
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
ReleaseType.MultimediaAlbum = ReleaseType._CF_enumeration.addEnumeration(unicode_value='MultimediaAlbum', tag='MultimediaAlbum')
ReleaseType.MultimediaSingle = ReleaseType._CF_enumeration.addEnumeration(unicode_value='MultimediaSingle', tag='MultimediaSingle')
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
ReleaseType.SingleResourceReleaseWithCoverArt = ReleaseType._CF_enumeration.addEnumeration(unicode_value='SingleResourceReleaseWithCoverArt', tag='SingleResourceReleaseWithCoverArt')
ReleaseType.TrackRelease = ReleaseType._CF_enumeration.addEnumeration(unicode_value='TrackRelease', tag='TrackRelease')
ReleaseType.TrailerVideo = ReleaseType._CF_enumeration.addEnumeration(unicode_value='TrailerVideo', tag='TrailerVideo')
ReleaseType.TrayImageRelease = ReleaseType._CF_enumeration.addEnumeration(unicode_value='TrayImageRelease', tag='TrayImageRelease')
ReleaseType.Unknown = ReleaseType._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
ReleaseType.UserDefined = ReleaseType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
ReleaseType.VideoAlbum = ReleaseType._CF_enumeration.addEnumeration(unicode_value='VideoAlbum', tag='VideoAlbum')
ReleaseType.VideoChapterRelease = ReleaseType._CF_enumeration.addEnumeration(unicode_value='VideoChapterRelease', tag='VideoChapterRelease')
ReleaseType.VideoClipRelease = ReleaseType._CF_enumeration.addEnumeration(unicode_value='VideoClipRelease', tag='VideoClipRelease')
ReleaseType.VideoScreenCaptureRelease = ReleaseType._CF_enumeration.addEnumeration(unicode_value='VideoScreenCaptureRelease', tag='VideoScreenCaptureRelease')
ReleaseType.VideoSingle = ReleaseType._CF_enumeration.addEnumeration(unicode_value='VideoSingle', tag='VideoSingle')
ReleaseType.VideoTrackRelease = ReleaseType._CF_enumeration.addEnumeration(unicode_value='VideoTrackRelease', tag='VideoTrackRelease')
ReleaseType.WallpaperRelease = ReleaseType._CF_enumeration.addEnumeration(unicode_value='WallpaperRelease', tag='WallpaperRelease')
ReleaseType._InitializeFacetMap(ReleaseType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ReleaseType', ReleaseType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}ReportFormat
class ReportFormat (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of report according to its FileFormat."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReportFormat')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 7789, 3)
    _Documentation = 'A Type of report according to its FileFormat.'
ReportFormat._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ReportFormat, enum_prefix=None)
ReportFormat.ASCII = ReportFormat._CF_enumeration.addEnumeration(unicode_value='ASCII', tag='ASCII')
ReportFormat.CSV = ReportFormat._CF_enumeration.addEnumeration(unicode_value='CSV', tag='CSV')
ReportFormat.Excel2000 = ReportFormat._CF_enumeration.addEnumeration(unicode_value='Excel2000', tag='Excel2000')
ReportFormat.Excel2007 = ReportFormat._CF_enumeration.addEnumeration(unicode_value='Excel2007', tag='Excel2007')
ReportFormat.Excel2010 = ReportFormat._CF_enumeration.addEnumeration(unicode_value='Excel2010', tag='Excel2010')
ReportFormat.UserDefined = ReportFormat._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
ReportFormat.XML = ReportFormat._CF_enumeration.addEnumeration(unicode_value='XML', tag='XML')
ReportFormat._InitializeFacetMap(ReportFormat._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ReportFormat', ReportFormat)

# Atomic simple type: {http://ddex.net/xml/avs/avs}ReportType
class ReportType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of report."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReportType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 7831, 3)
    _Documentation = 'A Type of report.'
ReportType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ReportType, enum_prefix=None)
ReportType.DeliveryFrequencyRequestCall = ReportType._CF_enumeration.addEnumeration(unicode_value='DeliveryFrequencyRequestCall', tag='DeliveryFrequencyRequestCall')
ReportType.InformationAboutDeliveredAndAvailableReleasesCall = ReportType._CF_enumeration.addEnumeration(unicode_value='InformationAboutDeliveredAndAvailableReleasesCall', tag='InformationAboutDeliveredAndAvailableReleasesCall')
ReportType.OrderedReleasesInQueueRequestCall = ReportType._CF_enumeration.addEnumeration(unicode_value='OrderedReleasesInQueueRequestCall', tag='OrderedReleasesInQueueRequestCall')
ReportType.RedeliveryRequestCall = ReportType._CF_enumeration.addEnumeration(unicode_value='RedeliveryRequestCall', tag='RedeliveryRequestCall')
ReportType.ReleaseAvailabilityCall = ReportType._CF_enumeration.addEnumeration(unicode_value='ReleaseAvailabilityCall', tag='ReleaseAvailabilityCall')
ReportType.ReleaseAvailabilityRequestCall = ReportType._CF_enumeration.addEnumeration(unicode_value='ReleaseAvailabilityRequestCall', tag='ReleaseAvailabilityRequestCall')
ReportType.ReleaseStatusInformationCall = ReportType._CF_enumeration.addEnumeration(unicode_value='ReleaseStatusInformationCall', tag='ReleaseStatusInformationCall')
ReportType.ReleaseStatusRequestCall = ReportType._CF_enumeration.addEnumeration(unicode_value='ReleaseStatusRequestCall', tag='ReleaseStatusRequestCall')
ReportType.ReleaseSupplyChainRequestCall = ReportType._CF_enumeration.addEnumeration(unicode_value='ReleaseSupplyChainRequestCall', tag='ReleaseSupplyChainRequestCall')
ReportType.ReportDeliveryCall = ReportType._CF_enumeration.addEnumeration(unicode_value='ReportDeliveryCall', tag='ReportDeliveryCall')
ReportType.ReportRequestCall = ReportType._CF_enumeration.addEnumeration(unicode_value='ReportRequestCall', tag='ReportRequestCall')
ReportType.SupplyChainStatusCall = ReportType._CF_enumeration.addEnumeration(unicode_value='SupplyChainStatusCall', tag='SupplyChainStatusCall')
ReportType.UserDefined = ReportType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
ReportType._InitializeFacetMap(ReportType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ReportType', ReportType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}RequestReason
class RequestReason (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of reason for requesting something."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RequestReason')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 7903, 3)
    _Documentation = 'A Type of reason for requesting something.'
RequestReason._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=RequestReason, enum_prefix=None)
RequestReason.UserDefined = RequestReason._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
RequestReason._InitializeFacetMap(RequestReason._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'RequestReason', RequestReason)

# Atomic simple type: {http://ddex.net/xml/avs/avs}RequestedActionType
class RequestedActionType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of action requested."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RequestedActionType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 7915, 3)
    _Documentation = 'A Type of action requested.'
RequestedActionType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=RequestedActionType, enum_prefix=None)
RequestedActionType.AdditionalInformationOnly = RequestedActionType._CF_enumeration.addEnumeration(unicode_value='AdditionalInformationOnly', tag='AdditionalInformationOnly')
RequestedActionType.CorrectAndInform = RequestedActionType._CF_enumeration.addEnumeration(unicode_value='CorrectAndInform', tag='CorrectAndInform')
RequestedActionType.CorrectAndResend = RequestedActionType._CF_enumeration.addEnumeration(unicode_value='CorrectAndResend', tag='CorrectAndResend')
RequestedActionType.NoAction = RequestedActionType._CF_enumeration.addEnumeration(unicode_value='NoAction', tag='NoAction')
RequestedActionType.UserDefined = RequestedActionType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
RequestedActionType._InitializeFacetMap(RequestedActionType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'RequestedActionType', RequestedActionType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}ResourceContributorRole
class ResourceContributorRole (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A role played by a Contributor in relation to a Fixation of an abstract Creation."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ResourceContributorRole')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 7947, 3)
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
ResourceContributorRole.Dubber = ResourceContributorRole._CF_enumeration.addEnumeration(unicode_value='Dubber', tag='Dubber')
ResourceContributorRole.Encoder = ResourceContributorRole._CF_enumeration.addEnumeration(unicode_value='Encoder', tag='Encoder')
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
ResourceContributorRole.Member = ResourceContributorRole._CF_enumeration.addEnumeration(unicode_value='Member', tag='Member')
ResourceContributorRole.Narrator = ResourceContributorRole._CF_enumeration.addEnumeration(unicode_value='Narrator', tag='Narrator')
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

# Atomic simple type: {http://ddex.net/xml/avs/avs}ResourceOmissionReason
class ResourceOmissionReason (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of reason for omitting a Resource."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ResourceOmissionReason')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 8194, 3)
    _Documentation = 'A Type of reason for omitting a Resource.'
ResourceOmissionReason._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ResourceOmissionReason, enum_prefix=None)
ResourceOmissionReason.PassportServiceRelease = ResourceOmissionReason._CF_enumeration.addEnumeration(unicode_value='PassportServiceRelease', tag='PassportServiceRelease')
ResourceOmissionReason.PreRelease = ResourceOmissionReason._CF_enumeration.addEnumeration(unicode_value='PreRelease', tag='PreRelease')
ResourceOmissionReason.UserDefined = ResourceOmissionReason._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
ResourceOmissionReason.VirtualRelease = ResourceOmissionReason._CF_enumeration.addEnumeration(unicode_value='VirtualRelease', tag='VirtualRelease')
ResourceOmissionReason._InitializeFacetMap(ResourceOmissionReason._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ResourceOmissionReason', ResourceOmissionReason)

# Atomic simple type: {http://ddex.net/xml/avs/avs}ResourceType
class ResourceType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Resource."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ResourceType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 8221, 3)
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

# Atomic simple type: {http://ddex.net/xml/avs/avs}RevenueSourceType
class RevenueSourceType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of revenue earned by the SoundRecording, according to the way the revenue is generated."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RevenueSourceType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 8268, 3)
    _Documentation = 'A Type of revenue earned by the SoundRecording, according to the way the revenue is generated.'
RevenueSourceType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=RevenueSourceType, enum_prefix=None)
RevenueSourceType.FinancialRevenue = RevenueSourceType._CF_enumeration.addEnumeration(unicode_value='FinancialRevenue', tag='FinancialRevenue')
RevenueSourceType.IndemnityRevenue = RevenueSourceType._CF_enumeration.addEnumeration(unicode_value='IndemnityRevenue', tag='IndemnityRevenue')
RevenueSourceType.RoyaltyRevenue = RevenueSourceType._CF_enumeration.addEnumeration(unicode_value='RoyaltyRevenue', tag='RoyaltyRevenue')
RevenueSourceType._InitializeFacetMap(RevenueSourceType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'RevenueSourceType', RevenueSourceType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}RightShareRelationshipType
class RightShareRelationshipType (pyxb.binding.datatypes.string):

    """A Type of relationship between two RightShares."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RightShareRelationshipType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 8290, 3)
    _Documentation = 'A Type of relationship between two RightShares.'
RightShareRelationshipType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'RightShareRelationshipType', RightShareRelationshipType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}RightShareType
class RightShareType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of RightShare."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RightShareType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 8296, 3)
    _Documentation = 'A Type of RightShare.'
RightShareType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=RightShareType, enum_prefix=None)
RightShareType.MusicalWorkManuscriptShare = RightShareType._CF_enumeration.addEnumeration(unicode_value='MusicalWorkManuscriptShare', tag='MusicalWorkManuscriptShare')
RightShareType.MusicalWorkCollectionShare = RightShareType._CF_enumeration.addEnumeration(unicode_value='MusicalWorkCollectionShare', tag='MusicalWorkCollectionShare')
RightShareType.OriginalPublisherShare = RightShareType._CF_enumeration.addEnumeration(unicode_value='OriginalPublisherShare', tag='OriginalPublisherShare')
RightShareType._InitializeFacetMap(RightShareType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'RightShareType', RightShareType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}RightsClaimPolicyType
class RightsClaimPolicyType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of rights claim policy."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RightsClaimPolicyType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 8318, 3)
    _Documentation = 'A Type of rights claim policy.'
RightsClaimPolicyType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=RightsClaimPolicyType, enum_prefix=None)
RightsClaimPolicyType.ReportUsage = RightsClaimPolicyType._CF_enumeration.addEnumeration(unicode_value='ReportUsage', tag='ReportUsage')
RightsClaimPolicyType.BlockAccess = RightsClaimPolicyType._CF_enumeration.addEnumeration(unicode_value='BlockAccess', tag='BlockAccess')
RightsClaimPolicyType.Monetize = RightsClaimPolicyType._CF_enumeration.addEnumeration(unicode_value='Monetize', tag='Monetize')
RightsClaimPolicyType._InitializeFacetMap(RightsClaimPolicyType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'RightsClaimPolicyType', RightsClaimPolicyType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}RightsControllerRole
class RightsControllerRole (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A role of a RightsController."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RightsControllerRole')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 8340, 3)
    _Documentation = 'A role of a RightsController.'
RightsControllerRole._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=RightsControllerRole, enum_prefix=None)
RightsControllerRole.AdministratingRecordCompany = RightsControllerRole._CF_enumeration.addEnumeration(unicode_value='AdministratingRecordCompany', tag='AdministratingRecordCompany')
RightsControllerRole.RightsAdministrator = RightsControllerRole._CF_enumeration.addEnumeration(unicode_value='RightsAdministrator', tag='RightsAdministrator')
RightsControllerRole.RightsController = RightsControllerRole._CF_enumeration.addEnumeration(unicode_value='RightsController', tag='RightsController')
RightsControllerRole.RoyaltyAdministrator = RightsControllerRole._CF_enumeration.addEnumeration(unicode_value='RoyaltyAdministrator', tag='RoyaltyAdministrator')
RightsControllerRole.Unknown = RightsControllerRole._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
RightsControllerRole._InitializeFacetMap(RightsControllerRole._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'RightsControllerRole', RightsControllerRole)

# Atomic simple type: {http://ddex.net/xml/avs/avs}RightsControllerType
class RightsControllerType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of a RightsController."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RightsControllerType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 8372, 3)
    _Documentation = 'A Type of a RightsController.'
RightsControllerType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=RightsControllerType, enum_prefix=None)
RightsControllerType.OriginalOwner = RightsControllerType._CF_enumeration.addEnumeration(unicode_value='OriginalOwner', tag='OriginalOwner')
RightsControllerType.SuccessorInTitle = RightsControllerType._CF_enumeration.addEnumeration(unicode_value='SuccessorInTitle', tag='SuccessorInTitle')
RightsControllerType.ExclusiveLicensee = RightsControllerType._CF_enumeration.addEnumeration(unicode_value='ExclusiveLicensee', tag='ExclusiveLicensee')
RightsControllerType._InitializeFacetMap(RightsControllerType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'RightsControllerType', RightsControllerType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}RightsCoverage
class RightsCoverage (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Right which is covered."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RightsCoverage')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 8394, 3)
    _Documentation = 'A Type of Right which is covered.'
RightsCoverage._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=RightsCoverage, enum_prefix=None)
RightsCoverage.MakeAvailableRight = RightsCoverage._CF_enumeration.addEnumeration(unicode_value='MakeAvailableRight', tag='MakeAvailableRight')
RightsCoverage.MechanicalRight = RightsCoverage._CF_enumeration.addEnumeration(unicode_value='MechanicalRight', tag='MechanicalRight')
RightsCoverage.PerformingRight = RightsCoverage._CF_enumeration.addEnumeration(unicode_value='PerformingRight', tag='PerformingRight')
RightsCoverage.PrintRight = RightsCoverage._CF_enumeration.addEnumeration(unicode_value='PrintRight', tag='PrintRight')
RightsCoverage.ReproductionRight = RightsCoverage._CF_enumeration.addEnumeration(unicode_value='ReproductionRight', tag='ReproductionRight')
RightsCoverage.SynchronizationRight = RightsCoverage._CF_enumeration.addEnumeration(unicode_value='SynchronizationRight', tag='SynchronizationRight')
RightsCoverage.UserDefined = RightsCoverage._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
RightsCoverage._InitializeFacetMap(RightsCoverage._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'RightsCoverage', RightsCoverage)

# Atomic simple type: {http://ddex.net/xml/avs/avs}RoyaltyRateCalculationType
class RoyaltyRateCalculationType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of RoyaltyRate according to the calculation method."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RoyaltyRateCalculationType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 8436, 3)
    _Documentation = 'A Type of RoyaltyRate according to the calculation method.'
RoyaltyRateCalculationType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=RoyaltyRateCalculationType, enum_prefix=None)
RoyaltyRateCalculationType.BudgetRoyaltyRate = RoyaltyRateCalculationType._CF_enumeration.addEnumeration(unicode_value='BudgetRoyaltyRate', tag='BudgetRoyaltyRate')
RoyaltyRateCalculationType.ControlledCompositionRoyaltyRate = RoyaltyRateCalculationType._CF_enumeration.addEnumeration(unicode_value='ControlledCompositionRoyaltyRate', tag='ControlledCompositionRoyaltyRate')
RoyaltyRateCalculationType.ControlledShareRoyaltyRate = RoyaltyRateCalculationType._CF_enumeration.addEnumeration(unicode_value='ControlledShareRoyaltyRate', tag='ControlledShareRoyaltyRate')
RoyaltyRateCalculationType.MinimumStatutoryRoyaltyRate = RoyaltyRateCalculationType._CF_enumeration.addEnumeration(unicode_value='MinimumStatutoryRoyaltyRate', tag='MinimumStatutoryRoyaltyRate')
RoyaltyRateCalculationType.NegotiatedRoyaltyRate = RoyaltyRateCalculationType._CF_enumeration.addEnumeration(unicode_value='NegotiatedRoyaltyRate', tag='NegotiatedRoyaltyRate')
RoyaltyRateCalculationType.ReducedRoyaltyRate = RoyaltyRateCalculationType._CF_enumeration.addEnumeration(unicode_value='ReducedRoyaltyRate', tag='ReducedRoyaltyRate')
RoyaltyRateCalculationType.ReducedStatutoryRoyaltyRate = RoyaltyRateCalculationType._CF_enumeration.addEnumeration(unicode_value='ReducedStatutoryRoyaltyRate', tag='ReducedStatutoryRoyaltyRate')
RoyaltyRateCalculationType.StatutoryRoyaltyRate = RoyaltyRateCalculationType._CF_enumeration.addEnumeration(unicode_value='StatutoryRoyaltyRate', tag='StatutoryRoyaltyRate')
RoyaltyRateCalculationType._InitializeFacetMap(RoyaltyRateCalculationType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'RoyaltyRateCalculationType', RoyaltyRateCalculationType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}RoyaltyRateType
class RoyaltyRateType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of RoyaltyRate."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RoyaltyRateType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 8483, 3)
    _Documentation = 'A Type of RoyaltyRate.'
RoyaltyRateType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=RoyaltyRateType, enum_prefix=None)
RoyaltyRateType.PennyRate = RoyaltyRateType._CF_enumeration.addEnumeration(unicode_value='PennyRate', tag='PennyRate')
RoyaltyRateType.PercentageRoyaltyRate = RoyaltyRateType._CF_enumeration.addEnumeration(unicode_value='PercentageRoyaltyRate', tag='PercentageRoyaltyRate')
RoyaltyRateType.UserDefined = RoyaltyRateType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
RoyaltyRateType._InitializeFacetMap(RoyaltyRateType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'RoyaltyRateType', RoyaltyRateType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}SalesReportAvailabilityStatus
class SalesReportAvailabilityStatus (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Status of the availability of a sales report."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SalesReportAvailabilityStatus')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 8505, 3)
    _Documentation = 'A Status of the availability of a sales report.'
SalesReportAvailabilityStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SalesReportAvailabilityStatus, enum_prefix=None)
SalesReportAvailabilityStatus.SalesReportAvailable = SalesReportAvailabilityStatus._CF_enumeration.addEnumeration(unicode_value='SalesReportAvailable', tag='SalesReportAvailable')
SalesReportAvailabilityStatus.SalesReportNotAvailable = SalesReportAvailabilityStatus._CF_enumeration.addEnumeration(unicode_value='SalesReportNotAvailable', tag='SalesReportNotAvailable')
SalesReportAvailabilityStatus._InitializeFacetMap(SalesReportAvailabilityStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'SalesReportAvailabilityStatus', SalesReportAvailabilityStatus)

# Atomic simple type: {http://ddex.net/xml/avs/avs}Sex
class Sex (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """The biological sex of a being."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Sex')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 8522, 3)
    _Documentation = 'The biological sex of a being.'
Sex._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Sex, enum_prefix=None)
Sex.Female = Sex._CF_enumeration.addEnumeration(unicode_value='Female', tag='Female')
Sex.Male = Sex._CF_enumeration.addEnumeration(unicode_value='Male', tag='Male')
Sex.Unknown = Sex._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
Sex._InitializeFacetMap(Sex._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'Sex', Sex)

# Atomic simple type: {http://ddex.net/xml/avs/avs}SheetMusicCodecType
class SheetMusicCodecType (pyxb.binding.datatypes.string):

    """A Type of SheetMusicCodec."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SheetMusicCodecType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 8544, 3)
    _Documentation = 'A Type of SheetMusicCodec.'
SheetMusicCodecType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'SheetMusicCodecType', SheetMusicCodecType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}SheetMusicType
class SheetMusicType (pyxb.binding.datatypes.string):

    """A Type of SheetMusic."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SheetMusicType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 8550, 3)
    _Documentation = 'A Type of SheetMusic.'
SheetMusicType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'SheetMusicType', SheetMusicType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}SoftwareType
class SoftwareType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Software."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SoftwareType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 8556, 3)
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

# Atomic simple type: {http://ddex.net/xml/avs/avs}SoundProcessorType
class SoundProcessorType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of sound processor."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SoundProcessorType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 8593, 3)
    _Documentation = 'A Type of sound processor.'
SoundProcessorType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SoundProcessorType, enum_prefix=None)
SoundProcessorType.MidiProcessor = SoundProcessorType._CF_enumeration.addEnumeration(unicode_value='MidiProcessor', tag='MidiProcessor')
SoundProcessorType.SMAF_MA2 = SoundProcessorType._CF_enumeration.addEnumeration(unicode_value='SMAF-MA2', tag='SMAF_MA2')
SoundProcessorType.SMAF_MA3 = SoundProcessorType._CF_enumeration.addEnumeration(unicode_value='SMAF-MA3', tag='SMAF_MA3')
SoundProcessorType.Unknown = SoundProcessorType._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
SoundProcessorType.UserDefined = SoundProcessorType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
SoundProcessorType._InitializeFacetMap(SoundProcessorType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'SoundProcessorType', SoundProcessorType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}SoundRecordingType
class SoundRecordingType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of SoundRecording."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SoundRecordingType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 8625, 3)
    _Documentation = 'A Type of SoundRecording.'
SoundRecordingType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SoundRecordingType, enum_prefix=None)
SoundRecordingType.MusicalWorkReadalongSoundRecording = SoundRecordingType._CF_enumeration.addEnumeration(unicode_value='MusicalWorkReadalongSoundRecording', tag='MusicalWorkReadalongSoundRecording')
SoundRecordingType.MusicalWorkSoundRecording = SoundRecordingType._CF_enumeration.addEnumeration(unicode_value='MusicalWorkSoundRecording', tag='MusicalWorkSoundRecording')
SoundRecordingType.NonMusicalWorkReadalongSoundRecording = SoundRecordingType._CF_enumeration.addEnumeration(unicode_value='NonMusicalWorkReadalongSoundRecording', tag='NonMusicalWorkReadalongSoundRecording')
SoundRecordingType.NonMusicalWorkSoundRecording = SoundRecordingType._CF_enumeration.addEnumeration(unicode_value='NonMusicalWorkSoundRecording', tag='NonMusicalWorkSoundRecording')
SoundRecordingType.SpokenWordSoundRecording = SoundRecordingType._CF_enumeration.addEnumeration(unicode_value='SpokenWordSoundRecording', tag='SpokenWordSoundRecording')
SoundRecordingType.Unknown = SoundRecordingType._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
SoundRecordingType.UserDefined = SoundRecordingType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
SoundRecordingType._InitializeFacetMap(SoundRecordingType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'SoundRecordingType', SoundRecordingType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}SupplyChainStatus
class SupplyChainStatus (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Status of a Release in a supply chain."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SupplyChainStatus')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 8667, 3)
    _Documentation = 'A Status of a Release in a supply chain.'
SupplyChainStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SupplyChainStatus, enum_prefix=None)
SupplyChainStatus.DeliveredToReleaseDistributor = SupplyChainStatus._CF_enumeration.addEnumeration(unicode_value='DeliveredToReleaseDistributor', tag='DeliveredToReleaseDistributor')
SupplyChainStatus.InDeliveryToReleaseDistributor = SupplyChainStatus._CF_enumeration.addEnumeration(unicode_value='InDeliveryToReleaseDistributor', tag='InDeliveryToReleaseDistributor')
SupplyChainStatus.InPreparationForDeliveryToReleaseDistributor = SupplyChainStatus._CF_enumeration.addEnumeration(unicode_value='InPreparationForDeliveryToReleaseDistributor', tag='InPreparationForDeliveryToReleaseDistributor')
SupplyChainStatus.OrderPlacedForReleaseDistributor = SupplyChainStatus._CF_enumeration.addEnumeration(unicode_value='OrderPlacedForReleaseDistributor', tag='OrderPlacedForReleaseDistributor')
SupplyChainStatus.ProcessingErrorAtReleaseCreator = SupplyChainStatus._CF_enumeration.addEnumeration(unicode_value='ProcessingErrorAtReleaseCreator', tag='ProcessingErrorAtReleaseCreator')
SupplyChainStatus.ProcessingErrorAtReleaseDistributor = SupplyChainStatus._CF_enumeration.addEnumeration(unicode_value='ProcessingErrorAtReleaseDistributor', tag='ProcessingErrorAtReleaseDistributor')
SupplyChainStatus.ReleaseMadeAvailableToConsumers = SupplyChainStatus._CF_enumeration.addEnumeration(unicode_value='ReleaseMadeAvailableToConsumers', tag='ReleaseMadeAvailableToConsumers')
SupplyChainStatus.ReleaseNotAvailable = SupplyChainStatus._CF_enumeration.addEnumeration(unicode_value='ReleaseNotAvailable', tag='ReleaseNotAvailable')
SupplyChainStatus.ReleaseReceivedByReleaseDistributor = SupplyChainStatus._CF_enumeration.addEnumeration(unicode_value='ReleaseReceivedByReleaseDistributor', tag='ReleaseReceivedByReleaseDistributor')
SupplyChainStatus.ReleaseStagedForPublication = SupplyChainStatus._CF_enumeration.addEnumeration(unicode_value='ReleaseStagedForPublication', tag='ReleaseStagedForPublication')
SupplyChainStatus.SuccessfullyIngestedByReleaseDistributor = SupplyChainStatus._CF_enumeration.addEnumeration(unicode_value='SuccessfullyIngestedByReleaseDistributor', tag='SuccessfullyIngestedByReleaseDistributor')
SupplyChainStatus.UserDefined = SupplyChainStatus._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
SupplyChainStatus._InitializeFacetMap(SupplyChainStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'SupplyChainStatus', SupplyChainStatus)

# Atomic simple type: {http://ddex.net/xml/avs/avs}TaxScope
class TaxScope (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Tax according to its scope."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TaxScope')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 8734, 3)
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

# Atomic simple type: {http://ddex.net/xml/avs/avs}TaxType
class TaxType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Tax."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TaxType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 8771, 3)
    _Documentation = 'A Type of Tax.'
TaxType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TaxType, enum_prefix=None)
TaxType.CombinedTax = TaxType._CF_enumeration.addEnumeration(unicode_value='CombinedTax', tag='CombinedTax')
TaxType.SalesTax = TaxType._CF_enumeration.addEnumeration(unicode_value='SalesTax', tag='SalesTax')
TaxType.ServiceTax = TaxType._CF_enumeration.addEnumeration(unicode_value='ServiceTax', tag='ServiceTax')
TaxType.SourceTax = TaxType._CF_enumeration.addEnumeration(unicode_value='SourceTax', tag='SourceTax')
TaxType.UserDefined = TaxType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
TaxType._InitializeFacetMap(TaxType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TaxType', TaxType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}TerritoryCodeType
class TerritoryCodeType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of code."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TerritoryCodeType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 8803, 3)
    _Documentation = 'A Type of code.'
TerritoryCodeType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TerritoryCodeType, enum_prefix=None)
TerritoryCodeType.ISO = TerritoryCodeType._CF_enumeration.addEnumeration(unicode_value='ISO', tag='ISO')
TerritoryCodeType.TIS = TerritoryCodeType._CF_enumeration.addEnumeration(unicode_value='TIS', tag='TIS')
TerritoryCodeType._InitializeFacetMap(TerritoryCodeType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TerritoryCodeType', TerritoryCodeType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}TerritoryCodeTypeIncludingDeprecatedCodes
class TerritoryCodeTypeIncludingDeprecatedCodes (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of code which also includes deprecated codes."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TerritoryCodeTypeIncludingDeprecatedCodes')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 8820, 3)
    _Documentation = 'A Type of code which also includes deprecated codes.'
TerritoryCodeTypeIncludingDeprecatedCodes._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TerritoryCodeTypeIncludingDeprecatedCodes, enum_prefix=None)
TerritoryCodeTypeIncludingDeprecatedCodes.DeprecatedISO = TerritoryCodeTypeIncludingDeprecatedCodes._CF_enumeration.addEnumeration(unicode_value='DeprecatedISO', tag='DeprecatedISO')
TerritoryCodeTypeIncludingDeprecatedCodes.ISO = TerritoryCodeTypeIncludingDeprecatedCodes._CF_enumeration.addEnumeration(unicode_value='ISO', tag='ISO')
TerritoryCodeTypeIncludingDeprecatedCodes.TIS = TerritoryCodeTypeIncludingDeprecatedCodes._CF_enumeration.addEnumeration(unicode_value='TIS', tag='TIS')
TerritoryCodeTypeIncludingDeprecatedCodes._InitializeFacetMap(TerritoryCodeTypeIncludingDeprecatedCodes._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TerritoryCodeTypeIncludingDeprecatedCodes', TerritoryCodeTypeIncludingDeprecatedCodes)

# Atomic simple type: {http://ddex.net/xml/avs/avs}TextCodecType
class TextCodecType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of TextCodec."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TextCodecType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 8842, 3)
    _Documentation = 'A Type of TextCodec.'
TextCodecType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TextCodecType, enum_prefix=None)
TextCodecType.ASCII = TextCodecType._CF_enumeration.addEnumeration(unicode_value='ASCII', tag='ASCII')
TextCodecType.EBU_TT = TextCodecType._CF_enumeration.addEnumeration(unicode_value='EBU-TT', tag='EBU_TT')
TextCodecType.HTML = TextCodecType._CF_enumeration.addEnumeration(unicode_value='HTML', tag='HTML')
TextCodecType.OOXML = TextCodecType._CF_enumeration.addEnumeration(unicode_value='OOXML', tag='OOXML')
TextCodecType.PDF = TextCodecType._CF_enumeration.addEnumeration(unicode_value='PDF', tag='PDF')
TextCodecType.PostScript = TextCodecType._CF_enumeration.addEnumeration(unicode_value='PostScript', tag='PostScript')
TextCodecType.RTF = TextCodecType._CF_enumeration.addEnumeration(unicode_value='RTF', tag='RTF')
TextCodecType.SRT = TextCodecType._CF_enumeration.addEnumeration(unicode_value='SRT', tag='SRT')
TextCodecType.TTML = TextCodecType._CF_enumeration.addEnumeration(unicode_value='TTML', tag='TTML')
TextCodecType.Unknown = TextCodecType._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
TextCodecType.UserDefined = TextCodecType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
TextCodecType.VTT = TextCodecType._CF_enumeration.addEnumeration(unicode_value='VTT', tag='VTT')
TextCodecType._InitializeFacetMap(TextCodecType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TextCodecType', TextCodecType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}TextType
class TextType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Text."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TextType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 8909, 3)
    _Documentation = 'A Type of Text.'
TextType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TextType, enum_prefix=None)
TextType.Caption = TextType._CF_enumeration.addEnumeration(unicode_value='Caption', tag='Caption')
TextType.EBook = TextType._CF_enumeration.addEnumeration(unicode_value='EBook', tag='EBook')
TextType.LinerNotes = TextType._CF_enumeration.addEnumeration(unicode_value='LinerNotes', tag='LinerNotes')
TextType.LyricText = TextType._CF_enumeration.addEnumeration(unicode_value='LyricText', tag='LyricText')
TextType.NonInteractiveBooklet = TextType._CF_enumeration.addEnumeration(unicode_value='NonInteractiveBooklet', tag='NonInteractiveBooklet')
TextType.TextDocument = TextType._CF_enumeration.addEnumeration(unicode_value='TextDocument', tag='TextDocument')
TextType.Unknown = TextType._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
TextType.UserDefined = TextType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
TextType._InitializeFacetMap(TextType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TextType', TextType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}ThemeType
class ThemeType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Theme."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ThemeType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 8956, 3)
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

# Atomic simple type: {http://ddex.net/xml/avs/avs}TisTerritoryCode
class TisTerritoryCode (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A CISAC four-digit TIS code representing a Territory."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TisTerritoryCode')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 8993, 3)
    _Documentation = 'A CISAC four-digit TIS code representing a Territory.'
TisTerritoryCode._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TisTerritoryCode, enum_prefix=None)
TisTerritoryCode.n4 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='4', tag='n4')
TisTerritoryCode.n8 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='8', tag='n8')
TisTerritoryCode.n12 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='12', tag='n12')
TisTerritoryCode.n20 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='20', tag='n20')
TisTerritoryCode.n24 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='24', tag='n24')
TisTerritoryCode.n28 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='28', tag='n28')
TisTerritoryCode.n31 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='31', tag='n31')
TisTerritoryCode.n32 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='32', tag='n32')
TisTerritoryCode.n36 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='36', tag='n36')
TisTerritoryCode.n40 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='40', tag='n40')
TisTerritoryCode.n44 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='44', tag='n44')
TisTerritoryCode.n48 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='48', tag='n48')
TisTerritoryCode.n50 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='50', tag='n50')
TisTerritoryCode.n51 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='51', tag='n51')
TisTerritoryCode.n52 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='52', tag='n52')
TisTerritoryCode.n56 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='56', tag='n56')
TisTerritoryCode.n64 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='64', tag='n64')
TisTerritoryCode.n68 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='68', tag='n68')
TisTerritoryCode.n70 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='70', tag='n70')
TisTerritoryCode.n72 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='72', tag='n72')
TisTerritoryCode.n76 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='76', tag='n76')
TisTerritoryCode.n84 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='84', tag='n84')
TisTerritoryCode.n90 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='90', tag='n90')
TisTerritoryCode.n96 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='96', tag='n96')
TisTerritoryCode.n100 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='100', tag='n100')
TisTerritoryCode.n104 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='104', tag='n104')
TisTerritoryCode.n108 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='108', tag='n108')
TisTerritoryCode.n112 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='112', tag='n112')
TisTerritoryCode.n116 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='116', tag='n116')
TisTerritoryCode.n120 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='120', tag='n120')
TisTerritoryCode.n124 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='124', tag='n124')
TisTerritoryCode.n132 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='132', tag='n132')
TisTerritoryCode.n140 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='140', tag='n140')
TisTerritoryCode.n144 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='144', tag='n144')
TisTerritoryCode.n148 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='148', tag='n148')
TisTerritoryCode.n152 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='152', tag='n152')
TisTerritoryCode.n156 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='156', tag='n156')
TisTerritoryCode.n158 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='158', tag='n158')
TisTerritoryCode.n170 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='170', tag='n170')
TisTerritoryCode.n174 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='174', tag='n174')
TisTerritoryCode.n178 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='178', tag='n178')
TisTerritoryCode.n180 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='180', tag='n180')
TisTerritoryCode.n188 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='188', tag='n188')
TisTerritoryCode.n191 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='191', tag='n191')
TisTerritoryCode.n192 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='192', tag='n192')
TisTerritoryCode.n196 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='196', tag='n196')
TisTerritoryCode.n200 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='200', tag='n200')
TisTerritoryCode.n203 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='203', tag='n203')
TisTerritoryCode.n204 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='204', tag='n204')
TisTerritoryCode.n208 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='208', tag='n208')
TisTerritoryCode.n212 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='212', tag='n212')
TisTerritoryCode.n214 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='214', tag='n214')
TisTerritoryCode.n218 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='218', tag='n218')
TisTerritoryCode.n222 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='222', tag='n222')
TisTerritoryCode.n226 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='226', tag='n226')
TisTerritoryCode.n230 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='230', tag='n230')
TisTerritoryCode.n231 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='231', tag='n231')
TisTerritoryCode.n232 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='232', tag='n232')
TisTerritoryCode.n233 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='233', tag='n233')
TisTerritoryCode.n242 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='242', tag='n242')
TisTerritoryCode.n246 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='246', tag='n246')
TisTerritoryCode.n250 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='250', tag='n250')
TisTerritoryCode.n258 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='258', tag='n258')
TisTerritoryCode.n262 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='262', tag='n262')
TisTerritoryCode.n266 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='266', tag='n266')
TisTerritoryCode.n268 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='268', tag='n268')
TisTerritoryCode.n270 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='270', tag='n270')
TisTerritoryCode.n276 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='276', tag='n276')
TisTerritoryCode.n278 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='278', tag='n278')
TisTerritoryCode.n280 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='280', tag='n280')
TisTerritoryCode.n288 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='288', tag='n288')
TisTerritoryCode.n296 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='296', tag='n296')
TisTerritoryCode.n300 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='300', tag='n300')
TisTerritoryCode.n308 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='308', tag='n308')
TisTerritoryCode.n320 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='320', tag='n320')
TisTerritoryCode.n324 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='324', tag='n324')
TisTerritoryCode.n328 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='328', tag='n328')
TisTerritoryCode.n332 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='332', tag='n332')
TisTerritoryCode.n336 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='336', tag='n336')
TisTerritoryCode.n340 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='340', tag='n340')
TisTerritoryCode.n344 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='344', tag='n344')
TisTerritoryCode.n348 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='348', tag='n348')
TisTerritoryCode.n352 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='352', tag='n352')
TisTerritoryCode.n356 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='356', tag='n356')
TisTerritoryCode.n360 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='360', tag='n360')
TisTerritoryCode.n364 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='364', tag='n364')
TisTerritoryCode.n368 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='368', tag='n368')
TisTerritoryCode.n372 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='372', tag='n372')
TisTerritoryCode.n376 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='376', tag='n376')
TisTerritoryCode.n380 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='380', tag='n380')
TisTerritoryCode.n384 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='384', tag='n384')
TisTerritoryCode.n388 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='388', tag='n388')
TisTerritoryCode.n392 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='392', tag='n392')
TisTerritoryCode.n398 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='398', tag='n398')
TisTerritoryCode.n400 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='400', tag='n400')
TisTerritoryCode.n404 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='404', tag='n404')
TisTerritoryCode.n408 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='408', tag='n408')
TisTerritoryCode.n410 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='410', tag='n410')
TisTerritoryCode.n414 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='414', tag='n414')
TisTerritoryCode.n417 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='417', tag='n417')
TisTerritoryCode.n418 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='418', tag='n418')
TisTerritoryCode.n422 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='422', tag='n422')
TisTerritoryCode.n426 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='426', tag='n426')
TisTerritoryCode.n428 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='428', tag='n428')
TisTerritoryCode.n430 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='430', tag='n430')
TisTerritoryCode.n434 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='434', tag='n434')
TisTerritoryCode.n438 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='438', tag='n438')
TisTerritoryCode.n440 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='440', tag='n440')
TisTerritoryCode.n442 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='442', tag='n442')
TisTerritoryCode.n450 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='450', tag='n450')
TisTerritoryCode.n454 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='454', tag='n454')
TisTerritoryCode.n458 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='458', tag='n458')
TisTerritoryCode.n462 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='462', tag='n462')
TisTerritoryCode.n466 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='466', tag='n466')
TisTerritoryCode.n470 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='470', tag='n470')
TisTerritoryCode.n478 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='478', tag='n478')
TisTerritoryCode.n480 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='480', tag='n480')
TisTerritoryCode.n484 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='484', tag='n484')
TisTerritoryCode.n492 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='492', tag='n492')
TisTerritoryCode.n496 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='496', tag='n496')
TisTerritoryCode.n498 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='498', tag='n498')
TisTerritoryCode.n499 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='499', tag='n499')
TisTerritoryCode.n504 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='504', tag='n504')
TisTerritoryCode.n508 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='508', tag='n508')
TisTerritoryCode.n512 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='512', tag='n512')
TisTerritoryCode.n516 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='516', tag='n516')
TisTerritoryCode.n520 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='520', tag='n520')
TisTerritoryCode.n524 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='524', tag='n524')
TisTerritoryCode.n528 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='528', tag='n528')
TisTerritoryCode.n540 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='540', tag='n540')
TisTerritoryCode.n548 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='548', tag='n548')
TisTerritoryCode.n554 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='554', tag='n554')
TisTerritoryCode.n558 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='558', tag='n558')
TisTerritoryCode.n562 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='562', tag='n562')
TisTerritoryCode.n566 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='566', tag='n566')
TisTerritoryCode.n578 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='578', tag='n578')
TisTerritoryCode.n583 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='583', tag='n583')
TisTerritoryCode.n584 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='584', tag='n584')
TisTerritoryCode.n585 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='585', tag='n585')
TisTerritoryCode.n586 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='586', tag='n586')
TisTerritoryCode.n591 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='591', tag='n591')
TisTerritoryCode.n598 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='598', tag='n598')
TisTerritoryCode.n600 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='600', tag='n600')
TisTerritoryCode.n604 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='604', tag='n604')
TisTerritoryCode.n608 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='608', tag='n608')
TisTerritoryCode.n616 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='616', tag='n616')
TisTerritoryCode.n620 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='620', tag='n620')
TisTerritoryCode.n624 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='624', tag='n624')
TisTerritoryCode.n626 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='626', tag='n626')
TisTerritoryCode.n630 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='630', tag='n630')
TisTerritoryCode.n634 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='634', tag='n634')
TisTerritoryCode.n642 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='642', tag='n642')
TisTerritoryCode.n643 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='643', tag='n643')
TisTerritoryCode.n646 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='646', tag='n646')
TisTerritoryCode.n659 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='659', tag='n659')
TisTerritoryCode.n662 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='662', tag='n662')
TisTerritoryCode.n670 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='670', tag='n670')
TisTerritoryCode.n674 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='674', tag='n674')
TisTerritoryCode.n678 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='678', tag='n678')
TisTerritoryCode.n682 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='682', tag='n682')
TisTerritoryCode.n686 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='686', tag='n686')
TisTerritoryCode.n688 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='688', tag='n688')
TisTerritoryCode.n690 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='690', tag='n690')
TisTerritoryCode.n694 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='694', tag='n694')
TisTerritoryCode.n702 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='702', tag='n702')
TisTerritoryCode.n703 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='703', tag='n703')
TisTerritoryCode.n704 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='704', tag='n704')
TisTerritoryCode.n705 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='705', tag='n705')
TisTerritoryCode.n706 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='706', tag='n706')
TisTerritoryCode.n710 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='710', tag='n710')
TisTerritoryCode.n716 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='716', tag='n716')
TisTerritoryCode.n720 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='720', tag='n720')
TisTerritoryCode.n724 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='724', tag='n724')
TisTerritoryCode.n728 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='728', tag='n728')
TisTerritoryCode.n729 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='729', tag='n729')
TisTerritoryCode.n732 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='732', tag='n732')
TisTerritoryCode.n736 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='736', tag='n736')
TisTerritoryCode.n740 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='740', tag='n740')
TisTerritoryCode.n748 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='748', tag='n748')
TisTerritoryCode.n752 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='752', tag='n752')
TisTerritoryCode.n756 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='756', tag='n756')
TisTerritoryCode.n760 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='760', tag='n760')
TisTerritoryCode.n762 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='762', tag='n762')
TisTerritoryCode.n764 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='764', tag='n764')
TisTerritoryCode.n768 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='768', tag='n768')
TisTerritoryCode.n776 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='776', tag='n776')
TisTerritoryCode.n780 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='780', tag='n780')
TisTerritoryCode.n784 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='784', tag='n784')
TisTerritoryCode.n788 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='788', tag='n788')
TisTerritoryCode.n792 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='792', tag='n792')
TisTerritoryCode.n795 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='795', tag='n795')
TisTerritoryCode.n798 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='798', tag='n798')
TisTerritoryCode.n800 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='800', tag='n800')
TisTerritoryCode.n804 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='804', tag='n804')
TisTerritoryCode.n807 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='807', tag='n807')
TisTerritoryCode.n810 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='810', tag='n810')
TisTerritoryCode.n818 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='818', tag='n818')
TisTerritoryCode.n826 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='826', tag='n826')
TisTerritoryCode.n834 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='834', tag='n834')
TisTerritoryCode.n840 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='840', tag='n840')
TisTerritoryCode.n854 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='854', tag='n854')
TisTerritoryCode.n858 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='858', tag='n858')
TisTerritoryCode.n860 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='860', tag='n860')
TisTerritoryCode.n862 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='862', tag='n862')
TisTerritoryCode.n882 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='882', tag='n882')
TisTerritoryCode.n886 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='886', tag='n886')
TisTerritoryCode.n887 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='887', tag='n887')
TisTerritoryCode.n890 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='890', tag='n890')
TisTerritoryCode.n891 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='891', tag='n891')
TisTerritoryCode.n894 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='894', tag='n894')
TisTerritoryCode.n2100 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='2100', tag='n2100')
TisTerritoryCode.n2101 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='2101', tag='n2101')
TisTerritoryCode.n2102 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='2102', tag='n2102')
TisTerritoryCode.n2103 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='2103', tag='n2103')
TisTerritoryCode.n2104 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='2104', tag='n2104')
TisTerritoryCode.n2105 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='2105', tag='n2105')
TisTerritoryCode.n2106 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='2106', tag='n2106')
TisTerritoryCode.n2107 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='2107', tag='n2107')
TisTerritoryCode.n2108 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='2108', tag='n2108')
TisTerritoryCode.n2109 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='2109', tag='n2109')
TisTerritoryCode.n2110 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='2110', tag='n2110')
TisTerritoryCode.n2111 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='2111', tag='n2111')
TisTerritoryCode.n2112 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='2112', tag='n2112')
TisTerritoryCode.n2113 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='2113', tag='n2113')
TisTerritoryCode.n2114 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='2114', tag='n2114')
TisTerritoryCode.n2115 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='2115', tag='n2115')
TisTerritoryCode.n2116 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='2116', tag='n2116')
TisTerritoryCode.n2117 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='2117', tag='n2117')
TisTerritoryCode.n2118 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='2118', tag='n2118')
TisTerritoryCode.n2119 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='2119', tag='n2119')
TisTerritoryCode.n2120 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='2120', tag='n2120')
TisTerritoryCode.n2121 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='2121', tag='n2121')
TisTerritoryCode.n2122 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='2122', tag='n2122')
TisTerritoryCode.n2123 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='2123', tag='n2123')
TisTerritoryCode.n2124 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='2124', tag='n2124')
TisTerritoryCode.n2125 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='2125', tag='n2125')
TisTerritoryCode.n2126 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='2126', tag='n2126')
TisTerritoryCode.n2127 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='2127', tag='n2127')
TisTerritoryCode.n2128 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='2128', tag='n2128')
TisTerritoryCode.n2129 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='2129', tag='n2129')
TisTerritoryCode.n2130 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='2130', tag='n2130')
TisTerritoryCode.n2131 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='2131', tag='n2131')
TisTerritoryCode.n2132 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='2132', tag='n2132')
TisTerritoryCode.n2133 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='2133', tag='n2133')
TisTerritoryCode.n2134 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='2134', tag='n2134')
TisTerritoryCode.n2136 = TisTerritoryCode._CF_enumeration.addEnumeration(unicode_value='2136', tag='n2136')
TisTerritoryCode._InitializeFacetMap(TisTerritoryCode._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TisTerritoryCode', TisTerritoryCode)

# Atomic simple type: {http://ddex.net/xml/avs/avs}TitleType
class TitleType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Title which defines its origin, form or the function it fulfils in relation to a Creation. Note: A Title may fulfil more than one role. Example: 'Help' may be both the OriginalTitle and the DisplayTitle for the well-known Beatles song.  """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TitleType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 10230, 3)
    _Documentation = "A Type of Title which defines its origin, form or the function it fulfils in relation to a Creation. Note: A Title may fulfil more than one role. Example: 'Help' may be both the OriginalTitle and the DisplayTitle for the well-known Beatles song.  "
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

# Atomic simple type: {http://ddex.net/xml/avs/avs}TrackContributorRelationshipType
class TrackContributorRelationshipType (pyxb.binding.datatypes.string):

    """A Type of relationship between a Track and a Contributor."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TrackContributorRelationshipType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 10317, 3)
    _Documentation = 'A Type of relationship between a Track and a Contributor.'
TrackContributorRelationshipType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'TrackContributorRelationshipType', TrackContributorRelationshipType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}UnitOfBitRate
class UnitOfBitRate (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A UnitOfMeasure for a BitRate."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UnitOfBitRate')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 10323, 3)
    _Documentation = 'A UnitOfMeasure for a BitRate.'
UnitOfBitRate._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=UnitOfBitRate, enum_prefix=None)
UnitOfBitRate.bps = UnitOfBitRate._CF_enumeration.addEnumeration(unicode_value='bps', tag='bps')
UnitOfBitRate.Gbps = UnitOfBitRate._CF_enumeration.addEnumeration(unicode_value='Gbps', tag='Gbps')
UnitOfBitRate.kbps = UnitOfBitRate._CF_enumeration.addEnumeration(unicode_value='kbps', tag='kbps')
UnitOfBitRate.Mbps = UnitOfBitRate._CF_enumeration.addEnumeration(unicode_value='Mbps', tag='Mbps')
UnitOfBitRate._InitializeFacetMap(UnitOfBitRate._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'UnitOfBitRate', UnitOfBitRate)

# Atomic simple type: {http://ddex.net/xml/avs/avs}UnitOfConditionValue
class UnitOfConditionValue (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A UnitOfMeasure for a condition value."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UnitOfConditionValue')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 10350, 3)
    _Documentation = 'A UnitOfMeasure for a condition value.'
UnitOfConditionValue._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=UnitOfConditionValue, enum_prefix=None)
UnitOfConditionValue.Millisecond = UnitOfConditionValue._CF_enumeration.addEnumeration(unicode_value='Millisecond', tag='Millisecond')
UnitOfConditionValue.Minute = UnitOfConditionValue._CF_enumeration.addEnumeration(unicode_value='Minute', tag='Minute')
UnitOfConditionValue.Percent = UnitOfConditionValue._CF_enumeration.addEnumeration(unicode_value='Percent', tag='Percent')
UnitOfConditionValue.Pixel = UnitOfConditionValue._CF_enumeration.addEnumeration(unicode_value='Pixel', tag='Pixel')
UnitOfConditionValue.Second = UnitOfConditionValue._CF_enumeration.addEnumeration(unicode_value='Second', tag='Second')
UnitOfConditionValue._InitializeFacetMap(UnitOfConditionValue._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'UnitOfConditionValue', UnitOfConditionValue)

# Atomic simple type: {http://ddex.net/xml/avs/avs}UnitOfExtent
class UnitOfExtent (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A UnitOfMeasure for an Extent."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UnitOfExtent')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 10382, 3)
    _Documentation = 'A UnitOfMeasure for an Extent.'
UnitOfExtent._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=UnitOfExtent, enum_prefix=None)
UnitOfExtent.cm = UnitOfExtent._CF_enumeration.addEnumeration(unicode_value='cm', tag='cm')
UnitOfExtent.Inch = UnitOfExtent._CF_enumeration.addEnumeration(unicode_value='Inch', tag='Inch')
UnitOfExtent.mm = UnitOfExtent._CF_enumeration.addEnumeration(unicode_value='mm', tag='mm')
UnitOfExtent.PercentOfScreen = UnitOfExtent._CF_enumeration.addEnumeration(unicode_value='PercentOfScreen', tag='PercentOfScreen')
UnitOfExtent.Pixel = UnitOfExtent._CF_enumeration.addEnumeration(unicode_value='Pixel', tag='Pixel')
UnitOfExtent._InitializeFacetMap(UnitOfExtent._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'UnitOfExtent', UnitOfExtent)

# Atomic simple type: {http://ddex.net/xml/avs/avs}UnitOfFrameRate
class UnitOfFrameRate (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A UnitOfMeasure for a FrameRate."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UnitOfFrameRate')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 10414, 3)
    _Documentation = 'A UnitOfMeasure for a FrameRate.'
UnitOfFrameRate._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=UnitOfFrameRate, enum_prefix=None)
UnitOfFrameRate.Hzinterlaced = UnitOfFrameRate._CF_enumeration.addEnumeration(unicode_value='Hz(interlaced)', tag='Hzinterlaced')
UnitOfFrameRate.Hznon_interlaced = UnitOfFrameRate._CF_enumeration.addEnumeration(unicode_value='Hz(non-interlaced)', tag='Hznon_interlaced')
UnitOfFrameRate._InitializeFacetMap(UnitOfFrameRate._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'UnitOfFrameRate', UnitOfFrameRate)

# Atomic simple type: {http://ddex.net/xml/avs/avs}UnitOfFrequency
class UnitOfFrequency (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A UnitOfMeasure for a frequency."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UnitOfFrequency')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 10431, 3)
    _Documentation = 'A UnitOfMeasure for a frequency.'
UnitOfFrequency._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=UnitOfFrequency, enum_prefix=None)
UnitOfFrequency.GHz = UnitOfFrequency._CF_enumeration.addEnumeration(unicode_value='GHz', tag='GHz')
UnitOfFrequency.Hz = UnitOfFrequency._CF_enumeration.addEnumeration(unicode_value='Hz', tag='Hz')
UnitOfFrequency.kHz = UnitOfFrequency._CF_enumeration.addEnumeration(unicode_value='kHz', tag='kHz')
UnitOfFrequency.MHz = UnitOfFrequency._CF_enumeration.addEnumeration(unicode_value='MHz', tag='MHz')
UnitOfFrequency._InitializeFacetMap(UnitOfFrequency._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'UnitOfFrequency', UnitOfFrequency)

# Atomic simple type: {http://ddex.net/xml/avs/avs}UpdateIndicator
class UpdateIndicator (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Message according to whether the Message contains original data or updates to previously sent data."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UpdateIndicator')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 10458, 3)
    _Documentation = 'A Type of Message according to whether the Message contains original data or updates to previously sent data.'
UpdateIndicator._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=UpdateIndicator, enum_prefix=None)
UpdateIndicator.OriginalMessage = UpdateIndicator._CF_enumeration.addEnumeration(unicode_value='OriginalMessage', tag='OriginalMessage')
UpdateIndicator.UpdateMessage = UpdateIndicator._CF_enumeration.addEnumeration(unicode_value='UpdateMessage', tag='UpdateMessage')
UpdateIndicator._InitializeFacetMap(UpdateIndicator._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'UpdateIndicator', UpdateIndicator)

# Atomic simple type: {http://ddex.net/xml/avs/avs}UseType
class UseType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of a nature of a Service, or a Release, as used by a Consumer."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UseType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 10475, 3)
    _Documentation = 'A Type of a nature of a Service, or a Release, as used by a Consumer.'
UseType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=UseType, enum_prefix=None)
UseType.AsPerContract = UseType._CF_enumeration.addEnumeration(unicode_value='AsPerContract', tag='AsPerContract')
UseType.Broadcast = UseType._CF_enumeration.addEnumeration(unicode_value='Broadcast', tag='Broadcast')
UseType.ConditionalDownload = UseType._CF_enumeration.addEnumeration(unicode_value='ConditionalDownload', tag='ConditionalDownload')
UseType.ContentInfluencedStream = UseType._CF_enumeration.addEnumeration(unicode_value='ContentInfluencedStream', tag='ContentInfluencedStream')
UseType.Display = UseType._CF_enumeration.addEnumeration(unicode_value='Display', tag='Display')
UseType.Download = UseType._CF_enumeration.addEnumeration(unicode_value='Download', tag='Download')
UseType.DubForAdvertisement = UseType._CF_enumeration.addEnumeration(unicode_value='DubForAdvertisement', tag='DubForAdvertisement')
UseType.DubForLivePerformance = UseType._CF_enumeration.addEnumeration(unicode_value='DubForLivePerformance', tag='DubForLivePerformance')
UseType.DubForMovies = UseType._CF_enumeration.addEnumeration(unicode_value='DubForMovies', tag='DubForMovies')
UseType.DubForMusicOnHold = UseType._CF_enumeration.addEnumeration(unicode_value='DubForMusicOnHold', tag='DubForMusicOnHold')
UseType.DubForPublicPerformance = UseType._CF_enumeration.addEnumeration(unicode_value='DubForPublicPerformance', tag='DubForPublicPerformance')
UseType.DubForRadio = UseType._CF_enumeration.addEnumeration(unicode_value='DubForRadio', tag='DubForRadio')
UseType.DubForTV = UseType._CF_enumeration.addEnumeration(unicode_value='DubForTV', tag='DubForTV')
UseType.ExtractForInternet = UseType._CF_enumeration.addEnumeration(unicode_value='ExtractForInternet', tag='ExtractForInternet')
UseType.KioskDownload = UseType._CF_enumeration.addEnumeration(unicode_value='KioskDownload', tag='KioskDownload')
UseType.Narrowcast = UseType._CF_enumeration.addEnumeration(unicode_value='Narrowcast', tag='Narrowcast')
UseType.NonInteractiveStream = UseType._CF_enumeration.addEnumeration(unicode_value='NonInteractiveStream', tag='NonInteractiveStream')
UseType.OnDemandStream = UseType._CF_enumeration.addEnumeration(unicode_value='OnDemandStream', tag='OnDemandStream')
UseType.PerformAsMusicOnHold = UseType._CF_enumeration.addEnumeration(unicode_value='PerformAsMusicOnHold', tag='PerformAsMusicOnHold')
UseType.PerformInLivePerformance = UseType._CF_enumeration.addEnumeration(unicode_value='PerformInLivePerformance', tag='PerformInLivePerformance')
UseType.PerformInPublic = UseType._CF_enumeration.addEnumeration(unicode_value='PerformInPublic', tag='PerformInPublic')
UseType.PermanentDownload = UseType._CF_enumeration.addEnumeration(unicode_value='PermanentDownload', tag='PermanentDownload')
UseType.Playback = UseType._CF_enumeration.addEnumeration(unicode_value='Playback', tag='Playback')
UseType.PlayInPublic = UseType._CF_enumeration.addEnumeration(unicode_value='PlayInPublic', tag='PlayInPublic')
UseType.Podcast = UseType._CF_enumeration.addEnumeration(unicode_value='Podcast', tag='Podcast')
UseType.Print = UseType._CF_enumeration.addEnumeration(unicode_value='Print', tag='Print')
UseType.PrivateCopy = UseType._CF_enumeration.addEnumeration(unicode_value='PrivateCopy', tag='PrivateCopy')
UseType.PurchaseAsPhysicalProduct = UseType._CF_enumeration.addEnumeration(unicode_value='PurchaseAsPhysicalProduct', tag='PurchaseAsPhysicalProduct')
UseType.Rent = UseType._CF_enumeration.addEnumeration(unicode_value='Rent', tag='Rent')
UseType.Simulcast = UseType._CF_enumeration.addEnumeration(unicode_value='Simulcast', tag='Simulcast')
UseType.Stream = UseType._CF_enumeration.addEnumeration(unicode_value='Stream', tag='Stream')
UseType.TetheredDownload = UseType._CF_enumeration.addEnumeration(unicode_value='TetheredDownload', tag='TetheredDownload')
UseType.TimeInfluencedStream = UseType._CF_enumeration.addEnumeration(unicode_value='TimeInfluencedStream', tag='TimeInfluencedStream')
UseType.Unknown = UseType._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
UseType.UseAsAlertTone = UseType._CF_enumeration.addEnumeration(unicode_value='UseAsAlertTone', tag='UseAsAlertTone')
UseType.UseAsDevice = UseType._CF_enumeration.addEnumeration(unicode_value='UseAsDevice', tag='UseAsDevice')
UseType.UseAsKaraoke = UseType._CF_enumeration.addEnumeration(unicode_value='UseAsKaraoke', tag='UseAsKaraoke')
UseType.UseAsRingbackTone = UseType._CF_enumeration.addEnumeration(unicode_value='UseAsRingbackTone', tag='UseAsRingbackTone')
UseType.UseAsRingbackTune = UseType._CF_enumeration.addEnumeration(unicode_value='UseAsRingbackTune', tag='UseAsRingbackTune')
UseType.UseAsRingtone = UseType._CF_enumeration.addEnumeration(unicode_value='UseAsRingtone', tag='UseAsRingtone')
UseType.UseAsRingtune = UseType._CF_enumeration.addEnumeration(unicode_value='UseAsRingtune', tag='UseAsRingtune')
UseType.UseAsScreensaver = UseType._CF_enumeration.addEnumeration(unicode_value='UseAsScreensaver', tag='UseAsScreensaver')
UseType.UseAsVoiceMail = UseType._CF_enumeration.addEnumeration(unicode_value='UseAsVoiceMail', tag='UseAsVoiceMail')
UseType.UseAsWallpaper = UseType._CF_enumeration.addEnumeration(unicode_value='UseAsWallpaper', tag='UseAsWallpaper')
UseType.UseForIdentification = UseType._CF_enumeration.addEnumeration(unicode_value='UseForIdentification', tag='UseForIdentification')
UseType.UseInMobilePhoneMessaging = UseType._CF_enumeration.addEnumeration(unicode_value='UseInMobilePhoneMessaging', tag='UseInMobilePhoneMessaging')
UseType.UseInPhoneListening = UseType._CF_enumeration.addEnumeration(unicode_value='UseInPhoneListening', tag='UseInPhoneListening')
UseType.UserDefined = UseType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
UseType.UserMakeAvailableLabelProvided = UseType._CF_enumeration.addEnumeration(unicode_value='UserMakeAvailableLabelProvided', tag='UserMakeAvailableLabelProvided')
UseType.UserMakeAvailableUserProvided = UseType._CF_enumeration.addEnumeration(unicode_value='UserMakeAvailableUserProvided', tag='UserMakeAvailableUserProvided')
UseType.Webcast = UseType._CF_enumeration.addEnumeration(unicode_value='Webcast', tag='Webcast')
UseType._InitializeFacetMap(UseType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'UseType', UseType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}UserInterfaceType
class UserInterfaceType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of physical interface by which a Consumer uses a Service or Release."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UserInterfaceType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 10737, 3)
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

# Atomic simple type: {http://ddex.net/xml/avs/avs}ValueType
class ValueType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of RoyaltyRate."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ValueType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 10809, 3)
    _Documentation = 'A Type of RoyaltyRate.'
ValueType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ValueType, enum_prefix=None)
ValueType.Calculated = ValueType._CF_enumeration.addEnumeration(unicode_value='Calculated', tag='Calculated')
ValueType.Maximum = ValueType._CF_enumeration.addEnumeration(unicode_value='Maximum', tag='Maximum')
ValueType.Minimum = ValueType._CF_enumeration.addEnumeration(unicode_value='Minimum', tag='Minimum')
ValueType._InitializeFacetMap(ValueType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ValueType', ValueType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}VideoCodecType
class VideoCodecType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of VideoCodec."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VideoCodecType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 10831, 3)
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
VideoCodecType.Shockwave = VideoCodecType._CF_enumeration.addEnumeration(unicode_value='Shockwave', tag='Shockwave')
VideoCodecType.Unknown = VideoCodecType._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
VideoCodecType.UserDefined = VideoCodecType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
VideoCodecType.WMV = VideoCodecType._CF_enumeration.addEnumeration(unicode_value='WMV', tag='WMV')
VideoCodecType._InitializeFacetMap(VideoCodecType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'VideoCodecType', VideoCodecType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}VideoContentType
class VideoContentType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Video."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VideoContentType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 10898, 3)
    _Documentation = 'A Type of Video.'
VideoContentType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=VideoContentType, enum_prefix=None)
VideoContentType.ActedVideo = VideoContentType._CF_enumeration.addEnumeration(unicode_value='ActedVideo', tag='ActedVideo')
VideoContentType.Animation = VideoContentType._CF_enumeration.addEnumeration(unicode_value='Animation', tag='Animation')
VideoContentType.AnimationAndActedVideo = VideoContentType._CF_enumeration.addEnumeration(unicode_value='AnimationAndActedVideo', tag='AnimationAndActedVideo')
VideoContentType._InitializeFacetMap(VideoContentType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'VideoContentType', VideoContentType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}VideoDefinitionType
class VideoDefinitionType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of resolution (or definition) in which a Video is provided."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VideoDefinitionType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 10920, 3)
    _Documentation = 'A Type of resolution (or definition) in which a Video is provided.'
VideoDefinitionType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=VideoDefinitionType, enum_prefix=None)
VideoDefinitionType.HighDefinition = VideoDefinitionType._CF_enumeration.addEnumeration(unicode_value='HighDefinition', tag='HighDefinition')
VideoDefinitionType.StandardDefinition = VideoDefinitionType._CF_enumeration.addEnumeration(unicode_value='StandardDefinition', tag='StandardDefinition')
VideoDefinitionType._InitializeFacetMap(VideoDefinitionType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'VideoDefinitionType', VideoDefinitionType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}VideoType
class VideoType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Video."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VideoType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 10937, 3)
    _Documentation = 'A Type of Video.'
VideoType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=VideoType, enum_prefix=None)
VideoType.AdvertisementVideo = VideoType._CF_enumeration.addEnumeration(unicode_value='AdvertisementVideo', tag='AdvertisementVideo')
VideoType.Animation = VideoType._CF_enumeration.addEnumeration(unicode_value='Animation', tag='Animation')
VideoType.BehindTheScenes = VideoType._CF_enumeration.addEnumeration(unicode_value='BehindTheScenes', tag='BehindTheScenes')
VideoType.ConcertClip = VideoType._CF_enumeration.addEnumeration(unicode_value='ConcertClip', tag='ConcertClip')
VideoType.ConcertVideo = VideoType._CF_enumeration.addEnumeration(unicode_value='ConcertVideo', tag='ConcertVideo')
VideoType.CorporateFilm = VideoType._CF_enumeration.addEnumeration(unicode_value='CorporateFilm', tag='CorporateFilm')
VideoType.Credits = VideoType._CF_enumeration.addEnumeration(unicode_value='Credits', tag='Credits')
VideoType.Documentary = VideoType._CF_enumeration.addEnumeration(unicode_value='Documentary', tag='Documentary')
VideoType.EducationalVideo = VideoType._CF_enumeration.addEnumeration(unicode_value='EducationalVideo', tag='EducationalVideo')
VideoType.Episode = VideoType._CF_enumeration.addEnumeration(unicode_value='Episode', tag='Episode')
VideoType.FeatureFilm = VideoType._CF_enumeration.addEnumeration(unicode_value='FeatureFilm', tag='FeatureFilm')
VideoType.InfomercialVideo = VideoType._CF_enumeration.addEnumeration(unicode_value='InfomercialVideo', tag='InfomercialVideo')
VideoType.Interview = VideoType._CF_enumeration.addEnumeration(unicode_value='Interview', tag='Interview')
VideoType.Karaoke = VideoType._CF_enumeration.addEnumeration(unicode_value='Karaoke', tag='Karaoke')
VideoType.LiveEventVideo = VideoType._CF_enumeration.addEnumeration(unicode_value='LiveEventVideo', tag='LiveEventVideo')
VideoType.LongFormMusicalWorkVideo = VideoType._CF_enumeration.addEnumeration(unicode_value='LongFormMusicalWorkVideo', tag='LongFormMusicalWorkVideo')
VideoType.LongFormNonMusicalWorkVideo = VideoType._CF_enumeration.addEnumeration(unicode_value='LongFormNonMusicalWorkVideo', tag='LongFormNonMusicalWorkVideo')
VideoType.LyricVideo = VideoType._CF_enumeration.addEnumeration(unicode_value='LyricVideo', tag='LyricVideo')
VideoType.Menu = VideoType._CF_enumeration.addEnumeration(unicode_value='Menu', tag='Menu')
VideoType.MultimediaVideo = VideoType._CF_enumeration.addEnumeration(unicode_value='MultimediaVideo', tag='MultimediaVideo')
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
VideoType.OperaVideo = VideoType._CF_enumeration.addEnumeration(unicode_value='OperaVideo', tag='OperaVideo')
VideoType.Performance = VideoType._CF_enumeration.addEnumeration(unicode_value='Performance', tag='Performance')
VideoType.Season = VideoType._CF_enumeration.addEnumeration(unicode_value='Season', tag='Season')
VideoType.Series = VideoType._CF_enumeration.addEnumeration(unicode_value='Series', tag='Series')
VideoType.ShortFilm = VideoType._CF_enumeration.addEnumeration(unicode_value='ShortFilm', tag='ShortFilm')
VideoType.ShortFormMusicalWorkVideo = VideoType._CF_enumeration.addEnumeration(unicode_value='ShortFormMusicalWorkVideo', tag='ShortFormMusicalWorkVideo')
VideoType.ShortFormNonMusicalWorkVideo = VideoType._CF_enumeration.addEnumeration(unicode_value='ShortFormNonMusicalWorkVideo', tag='ShortFormNonMusicalWorkVideo')
VideoType.SpecialEvent = VideoType._CF_enumeration.addEnumeration(unicode_value='SpecialEvent', tag='SpecialEvent')
VideoType.Sport = VideoType._CF_enumeration.addEnumeration(unicode_value='Sport', tag='Sport')
VideoType.TheatricalWorkVideo = VideoType._CF_enumeration.addEnumeration(unicode_value='TheatricalWorkVideo', tag='TheatricalWorkVideo')
VideoType.TrailerVideo = VideoType._CF_enumeration.addEnumeration(unicode_value='TrailerVideo', tag='TrailerVideo')
VideoType.TvFilm = VideoType._CF_enumeration.addEnumeration(unicode_value='TvFilm', tag='TvFilm')
VideoType.TvShowVideo = VideoType._CF_enumeration.addEnumeration(unicode_value='TvShowVideo', tag='TvShowVideo')
VideoType.Unknown = VideoType._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
VideoType.UserDefined = VideoType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
VideoType.VideoChapter = VideoType._CF_enumeration.addEnumeration(unicode_value='VideoChapter', tag='VideoChapter')
VideoType.VideoStem = VideoType._CF_enumeration.addEnumeration(unicode_value='VideoStem', tag='VideoStem')
VideoType._InitializeFacetMap(VideoType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'VideoType', VideoType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}VisualPerceptionType
class VisualPerceptionType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of MusicalCreation according to how it is experienced in an audio-visual Creation."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VisualPerceptionType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 11180, 3)
    _Documentation = 'A Type of MusicalCreation according to how it is experienced in an audio-visual Creation.'
VisualPerceptionType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=VisualPerceptionType, enum_prefix=None)
VisualPerceptionType.Background = VisualPerceptionType._CF_enumeration.addEnumeration(unicode_value='Background', tag='Background')
VisualPerceptionType.UserDefined = VisualPerceptionType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
VisualPerceptionType.Visual = VisualPerceptionType._CF_enumeration.addEnumeration(unicode_value='Visual', tag='Visual')
VisualPerceptionType._InitializeFacetMap(VisualPerceptionType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'VisualPerceptionType', VisualPerceptionType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}VocalType
class VocalType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of a MusicalCreation according to the occurrence of vocals."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VocalType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 11202, 3)
    _Documentation = 'A Type of a MusicalCreation according to the occurrence of vocals.'
VocalType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=VocalType, enum_prefix=None)
VocalType.Instrumental = VocalType._CF_enumeration.addEnumeration(unicode_value='Instrumental', tag='Instrumental')
VocalType.UserDefined = VocalType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
VocalType.Vocal = VocalType._CF_enumeration.addEnumeration(unicode_value='Vocal', tag='Vocal')
VocalType._InitializeFacetMap(VocalType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'VocalType', VocalType)

# Atomic simple type: {http://ddex.net/xml/avs/avs}WsMessageStatus
class WsMessageStatus (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Status of a WsMessage."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'WsMessageStatus')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 11224, 3)
    _Documentation = 'A Status of a WsMessage.'
WsMessageStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=WsMessageStatus, enum_prefix=None)
WsMessageStatus.BackendProcessingError = WsMessageStatus._CF_enumeration.addEnumeration(unicode_value='BackendProcessingError', tag='BackendProcessingError')
WsMessageStatus.NoValidMessageReceived = WsMessageStatus._CF_enumeration.addEnumeration(unicode_value='NoValidMessageReceived', tag='NoValidMessageReceived')
WsMessageStatus.ValidMessageQueuedForProcessing = WsMessageStatus._CF_enumeration.addEnumeration(unicode_value='ValidMessageQueuedForProcessing', tag='ValidMessageQueuedForProcessing')
WsMessageStatus.ValidMessageReceived = WsMessageStatus._CF_enumeration.addEnumeration(unicode_value='ValidMessageReceived', tag='ValidMessageReceived')
WsMessageStatus._InitializeFacetMap(WsMessageStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'WsMessageStatus', WsMessageStatus)

# Union simple type: {http://ddex.net/xml/avs/avs}AllTerritoryCode
# superclasses pyxb.binding.datatypes.anySimpleType
class AllTerritoryCode (pyxb.binding.basis.STD_union):

    """A code representing a Territory. This includes ISO 3166-1 two-letter codes, CISAC TIS codes, plus a code for Worldwide. It also includes deprecated ISO codes defined in ISO 3166-3."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AllTerritoryCode')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 62, 3)
    _Documentation = 'A code representing a Territory. This includes ISO 3166-1 two-letter codes, CISAC TIS codes, plus a code for Worldwide. It also includes deprecated ISO codes defined in ISO 3166-3.'

    _MemberTypes = ( IsoTerritoryCode, TisTerritoryCode, DdexTerritoryCode, DeprecatedIsoTerritoryCode, )
AllTerritoryCode._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=AllTerritoryCode)
AllTerritoryCode._CF_pattern = pyxb.binding.facets.CF_pattern()
AllTerritoryCode.AD = 'AD'                        # originally IsoTerritoryCode.AD
AllTerritoryCode.AE = 'AE'                        # originally IsoTerritoryCode.AE
AllTerritoryCode.AF = 'AF'                        # originally IsoTerritoryCode.AF
AllTerritoryCode.AG = 'AG'                        # originally IsoTerritoryCode.AG
AllTerritoryCode.AI = 'AI'                        # originally IsoTerritoryCode.AI
AllTerritoryCode.AL = 'AL'                        # originally IsoTerritoryCode.AL
AllTerritoryCode.AM = 'AM'                        # originally IsoTerritoryCode.AM
AllTerritoryCode.AN = 'AN'                        # originally IsoTerritoryCode.AN
AllTerritoryCode.AO = 'AO'                        # originally IsoTerritoryCode.AO
AllTerritoryCode.AQ = 'AQ'                        # originally IsoTerritoryCode.AQ
AllTerritoryCode.AR = 'AR'                        # originally IsoTerritoryCode.AR
AllTerritoryCode.AS = 'AS'                        # originally IsoTerritoryCode.AS
AllTerritoryCode.AT = 'AT'                        # originally IsoTerritoryCode.AT
AllTerritoryCode.AU = 'AU'                        # originally IsoTerritoryCode.AU
AllTerritoryCode.AW = 'AW'                        # originally IsoTerritoryCode.AW
AllTerritoryCode.AX = 'AX'                        # originally IsoTerritoryCode.AX
AllTerritoryCode.AZ = 'AZ'                        # originally IsoTerritoryCode.AZ
AllTerritoryCode.BA = 'BA'                        # originally IsoTerritoryCode.BA
AllTerritoryCode.BB = 'BB'                        # originally IsoTerritoryCode.BB
AllTerritoryCode.BD = 'BD'                        # originally IsoTerritoryCode.BD
AllTerritoryCode.BE = 'BE'                        # originally IsoTerritoryCode.BE
AllTerritoryCode.BF = 'BF'                        # originally IsoTerritoryCode.BF
AllTerritoryCode.BG = 'BG'                        # originally IsoTerritoryCode.BG
AllTerritoryCode.BH = 'BH'                        # originally IsoTerritoryCode.BH
AllTerritoryCode.BI = 'BI'                        # originally IsoTerritoryCode.BI
AllTerritoryCode.BJ = 'BJ'                        # originally IsoTerritoryCode.BJ
AllTerritoryCode.BL = 'BL'                        # originally IsoTerritoryCode.BL
AllTerritoryCode.BM = 'BM'                        # originally IsoTerritoryCode.BM
AllTerritoryCode.BN = 'BN'                        # originally IsoTerritoryCode.BN
AllTerritoryCode.BO = 'BO'                        # originally IsoTerritoryCode.BO
AllTerritoryCode.BQ = 'BQ'                        # originally IsoTerritoryCode.BQ
AllTerritoryCode.BR = 'BR'                        # originally IsoTerritoryCode.BR
AllTerritoryCode.BS = 'BS'                        # originally IsoTerritoryCode.BS
AllTerritoryCode.BT = 'BT'                        # originally IsoTerritoryCode.BT
AllTerritoryCode.BV = 'BV'                        # originally IsoTerritoryCode.BV
AllTerritoryCode.BW = 'BW'                        # originally IsoTerritoryCode.BW
AllTerritoryCode.BY = 'BY'                        # originally IsoTerritoryCode.BY
AllTerritoryCode.BZ = 'BZ'                        # originally IsoTerritoryCode.BZ
AllTerritoryCode.CA = 'CA'                        # originally IsoTerritoryCode.CA
AllTerritoryCode.CC = 'CC'                        # originally IsoTerritoryCode.CC
AllTerritoryCode.CD = 'CD'                        # originally IsoTerritoryCode.CD
AllTerritoryCode.CF = 'CF'                        # originally IsoTerritoryCode.CF
AllTerritoryCode.CG = 'CG'                        # originally IsoTerritoryCode.CG
AllTerritoryCode.CH = 'CH'                        # originally IsoTerritoryCode.CH
AllTerritoryCode.CI = 'CI'                        # originally IsoTerritoryCode.CI
AllTerritoryCode.CK = 'CK'                        # originally IsoTerritoryCode.CK
AllTerritoryCode.CL = 'CL'                        # originally IsoTerritoryCode.CL
AllTerritoryCode.CM = 'CM'                        # originally IsoTerritoryCode.CM
AllTerritoryCode.CN = 'CN'                        # originally IsoTerritoryCode.CN
AllTerritoryCode.CO = 'CO'                        # originally IsoTerritoryCode.CO
AllTerritoryCode.CR = 'CR'                        # originally IsoTerritoryCode.CR
AllTerritoryCode.CS = 'CS'                        # originally IsoTerritoryCode.CS
AllTerritoryCode.CU = 'CU'                        # originally IsoTerritoryCode.CU
AllTerritoryCode.CV = 'CV'                        # originally IsoTerritoryCode.CV
AllTerritoryCode.CW = 'CW'                        # originally IsoTerritoryCode.CW
AllTerritoryCode.CX = 'CX'                        # originally IsoTerritoryCode.CX
AllTerritoryCode.CY = 'CY'                        # originally IsoTerritoryCode.CY
AllTerritoryCode.CZ = 'CZ'                        # originally IsoTerritoryCode.CZ
AllTerritoryCode.DE = 'DE'                        # originally IsoTerritoryCode.DE
AllTerritoryCode.DJ = 'DJ'                        # originally IsoTerritoryCode.DJ
AllTerritoryCode.DK = 'DK'                        # originally IsoTerritoryCode.DK
AllTerritoryCode.DM = 'DM'                        # originally IsoTerritoryCode.DM
AllTerritoryCode.DO = 'DO'                        # originally IsoTerritoryCode.DO
AllTerritoryCode.DZ = 'DZ'                        # originally IsoTerritoryCode.DZ
AllTerritoryCode.EC = 'EC'                        # originally IsoTerritoryCode.EC
AllTerritoryCode.EE = 'EE'                        # originally IsoTerritoryCode.EE
AllTerritoryCode.EG = 'EG'                        # originally IsoTerritoryCode.EG
AllTerritoryCode.EH = 'EH'                        # originally IsoTerritoryCode.EH
AllTerritoryCode.ER = 'ER'                        # originally IsoTerritoryCode.ER
AllTerritoryCode.ES = 'ES'                        # originally IsoTerritoryCode.ES
AllTerritoryCode.ET = 'ET'                        # originally IsoTerritoryCode.ET
AllTerritoryCode.FI = 'FI'                        # originally IsoTerritoryCode.FI
AllTerritoryCode.FJ = 'FJ'                        # originally IsoTerritoryCode.FJ
AllTerritoryCode.FK = 'FK'                        # originally IsoTerritoryCode.FK
AllTerritoryCode.FM = 'FM'                        # originally IsoTerritoryCode.FM
AllTerritoryCode.FO = 'FO'                        # originally IsoTerritoryCode.FO
AllTerritoryCode.FR = 'FR'                        # originally IsoTerritoryCode.FR
AllTerritoryCode.GA = 'GA'                        # originally IsoTerritoryCode.GA
AllTerritoryCode.GB = 'GB'                        # originally IsoTerritoryCode.GB
AllTerritoryCode.GD = 'GD'                        # originally IsoTerritoryCode.GD
AllTerritoryCode.GE = 'GE'                        # originally IsoTerritoryCode.GE
AllTerritoryCode.GF = 'GF'                        # originally IsoTerritoryCode.GF
AllTerritoryCode.GG = 'GG'                        # originally IsoTerritoryCode.GG
AllTerritoryCode.GH = 'GH'                        # originally IsoTerritoryCode.GH
AllTerritoryCode.GI = 'GI'                        # originally IsoTerritoryCode.GI
AllTerritoryCode.GL = 'GL'                        # originally IsoTerritoryCode.GL
AllTerritoryCode.GM = 'GM'                        # originally IsoTerritoryCode.GM
AllTerritoryCode.GN = 'GN'                        # originally IsoTerritoryCode.GN
AllTerritoryCode.GP = 'GP'                        # originally IsoTerritoryCode.GP
AllTerritoryCode.GQ = 'GQ'                        # originally IsoTerritoryCode.GQ
AllTerritoryCode.GR = 'GR'                        # originally IsoTerritoryCode.GR
AllTerritoryCode.GS = 'GS'                        # originally IsoTerritoryCode.GS
AllTerritoryCode.GT = 'GT'                        # originally IsoTerritoryCode.GT
AllTerritoryCode.GU = 'GU'                        # originally IsoTerritoryCode.GU
AllTerritoryCode.GW = 'GW'                        # originally IsoTerritoryCode.GW
AllTerritoryCode.GY = 'GY'                        # originally IsoTerritoryCode.GY
AllTerritoryCode.HK = 'HK'                        # originally IsoTerritoryCode.HK
AllTerritoryCode.HM = 'HM'                        # originally IsoTerritoryCode.HM
AllTerritoryCode.HN = 'HN'                        # originally IsoTerritoryCode.HN
AllTerritoryCode.HR = 'HR'                        # originally IsoTerritoryCode.HR
AllTerritoryCode.HT = 'HT'                        # originally IsoTerritoryCode.HT
AllTerritoryCode.HU = 'HU'                        # originally IsoTerritoryCode.HU
AllTerritoryCode.ID = 'ID'                        # originally IsoTerritoryCode.ID
AllTerritoryCode.IE = 'IE'                        # originally IsoTerritoryCode.IE
AllTerritoryCode.IL = 'IL'                        # originally IsoTerritoryCode.IL
AllTerritoryCode.IM = 'IM'                        # originally IsoTerritoryCode.IM
AllTerritoryCode.IN = 'IN'                        # originally IsoTerritoryCode.IN
AllTerritoryCode.IO = 'IO'                        # originally IsoTerritoryCode.IO
AllTerritoryCode.IQ = 'IQ'                        # originally IsoTerritoryCode.IQ
AllTerritoryCode.IR = 'IR'                        # originally IsoTerritoryCode.IR
AllTerritoryCode.IS = 'IS'                        # originally IsoTerritoryCode.IS
AllTerritoryCode.IT = 'IT'                        # originally IsoTerritoryCode.IT
AllTerritoryCode.JE = 'JE'                        # originally IsoTerritoryCode.JE
AllTerritoryCode.JM = 'JM'                        # originally IsoTerritoryCode.JM
AllTerritoryCode.JO = 'JO'                        # originally IsoTerritoryCode.JO
AllTerritoryCode.JP = 'JP'                        # originally IsoTerritoryCode.JP
AllTerritoryCode.KE = 'KE'                        # originally IsoTerritoryCode.KE
AllTerritoryCode.KG = 'KG'                        # originally IsoTerritoryCode.KG
AllTerritoryCode.KH = 'KH'                        # originally IsoTerritoryCode.KH
AllTerritoryCode.KI = 'KI'                        # originally IsoTerritoryCode.KI
AllTerritoryCode.KM = 'KM'                        # originally IsoTerritoryCode.KM
AllTerritoryCode.KN = 'KN'                        # originally IsoTerritoryCode.KN
AllTerritoryCode.KP = 'KP'                        # originally IsoTerritoryCode.KP
AllTerritoryCode.KR = 'KR'                        # originally IsoTerritoryCode.KR
AllTerritoryCode.KW = 'KW'                        # originally IsoTerritoryCode.KW
AllTerritoryCode.KY = 'KY'                        # originally IsoTerritoryCode.KY
AllTerritoryCode.KZ = 'KZ'                        # originally IsoTerritoryCode.KZ
AllTerritoryCode.LA = 'LA'                        # originally IsoTerritoryCode.LA
AllTerritoryCode.LB = 'LB'                        # originally IsoTerritoryCode.LB
AllTerritoryCode.LC = 'LC'                        # originally IsoTerritoryCode.LC
AllTerritoryCode.LI = 'LI'                        # originally IsoTerritoryCode.LI
AllTerritoryCode.LK = 'LK'                        # originally IsoTerritoryCode.LK
AllTerritoryCode.LR = 'LR'                        # originally IsoTerritoryCode.LR
AllTerritoryCode.LS = 'LS'                        # originally IsoTerritoryCode.LS
AllTerritoryCode.LT = 'LT'                        # originally IsoTerritoryCode.LT
AllTerritoryCode.LU = 'LU'                        # originally IsoTerritoryCode.LU
AllTerritoryCode.LV = 'LV'                        # originally IsoTerritoryCode.LV
AllTerritoryCode.LY = 'LY'                        # originally IsoTerritoryCode.LY
AllTerritoryCode.MA = 'MA'                        # originally IsoTerritoryCode.MA
AllTerritoryCode.MC = 'MC'                        # originally IsoTerritoryCode.MC
AllTerritoryCode.MD = 'MD'                        # originally IsoTerritoryCode.MD
AllTerritoryCode.ME = 'ME'                        # originally IsoTerritoryCode.ME
AllTerritoryCode.MF = 'MF'                        # originally IsoTerritoryCode.MF
AllTerritoryCode.MG = 'MG'                        # originally IsoTerritoryCode.MG
AllTerritoryCode.MH = 'MH'                        # originally IsoTerritoryCode.MH
AllTerritoryCode.MK = 'MK'                        # originally IsoTerritoryCode.MK
AllTerritoryCode.ML = 'ML'                        # originally IsoTerritoryCode.ML
AllTerritoryCode.MM = 'MM'                        # originally IsoTerritoryCode.MM
AllTerritoryCode.MN = 'MN'                        # originally IsoTerritoryCode.MN
AllTerritoryCode.MO = 'MO'                        # originally IsoTerritoryCode.MO
AllTerritoryCode.MP = 'MP'                        # originally IsoTerritoryCode.MP
AllTerritoryCode.MQ = 'MQ'                        # originally IsoTerritoryCode.MQ
AllTerritoryCode.MR = 'MR'                        # originally IsoTerritoryCode.MR
AllTerritoryCode.MS = 'MS'                        # originally IsoTerritoryCode.MS
AllTerritoryCode.MT = 'MT'                        # originally IsoTerritoryCode.MT
AllTerritoryCode.MU = 'MU'                        # originally IsoTerritoryCode.MU
AllTerritoryCode.MV = 'MV'                        # originally IsoTerritoryCode.MV
AllTerritoryCode.MW = 'MW'                        # originally IsoTerritoryCode.MW
AllTerritoryCode.MX = 'MX'                        # originally IsoTerritoryCode.MX
AllTerritoryCode.MY = 'MY'                        # originally IsoTerritoryCode.MY
AllTerritoryCode.MZ = 'MZ'                        # originally IsoTerritoryCode.MZ
AllTerritoryCode.NA = 'NA'                        # originally IsoTerritoryCode.NA
AllTerritoryCode.NC = 'NC'                        # originally IsoTerritoryCode.NC
AllTerritoryCode.NE = 'NE'                        # originally IsoTerritoryCode.NE
AllTerritoryCode.NF = 'NF'                        # originally IsoTerritoryCode.NF
AllTerritoryCode.NG = 'NG'                        # originally IsoTerritoryCode.NG
AllTerritoryCode.NI = 'NI'                        # originally IsoTerritoryCode.NI
AllTerritoryCode.NL = 'NL'                        # originally IsoTerritoryCode.NL
AllTerritoryCode.NO = 'NO'                        # originally IsoTerritoryCode.NO
AllTerritoryCode.NP = 'NP'                        # originally IsoTerritoryCode.NP
AllTerritoryCode.NR = 'NR'                        # originally IsoTerritoryCode.NR
AllTerritoryCode.NU = 'NU'                        # originally IsoTerritoryCode.NU
AllTerritoryCode.NZ = 'NZ'                        # originally IsoTerritoryCode.NZ
AllTerritoryCode.OM = 'OM'                        # originally IsoTerritoryCode.OM
AllTerritoryCode.PA = 'PA'                        # originally IsoTerritoryCode.PA
AllTerritoryCode.PE = 'PE'                        # originally IsoTerritoryCode.PE
AllTerritoryCode.PF = 'PF'                        # originally IsoTerritoryCode.PF
AllTerritoryCode.PG = 'PG'                        # originally IsoTerritoryCode.PG
AllTerritoryCode.PH = 'PH'                        # originally IsoTerritoryCode.PH
AllTerritoryCode.PK = 'PK'                        # originally IsoTerritoryCode.PK
AllTerritoryCode.PL = 'PL'                        # originally IsoTerritoryCode.PL
AllTerritoryCode.PM = 'PM'                        # originally IsoTerritoryCode.PM
AllTerritoryCode.PN = 'PN'                        # originally IsoTerritoryCode.PN
AllTerritoryCode.PR = 'PR'                        # originally IsoTerritoryCode.PR
AllTerritoryCode.PS = 'PS'                        # originally IsoTerritoryCode.PS
AllTerritoryCode.PT = 'PT'                        # originally IsoTerritoryCode.PT
AllTerritoryCode.PW = 'PW'                        # originally IsoTerritoryCode.PW
AllTerritoryCode.PY = 'PY'                        # originally IsoTerritoryCode.PY
AllTerritoryCode.QA = 'QA'                        # originally IsoTerritoryCode.QA
AllTerritoryCode.RE = 'RE'                        # originally IsoTerritoryCode.RE
AllTerritoryCode.RO = 'RO'                        # originally IsoTerritoryCode.RO
AllTerritoryCode.RS = 'RS'                        # originally IsoTerritoryCode.RS
AllTerritoryCode.RU = 'RU'                        # originally IsoTerritoryCode.RU
AllTerritoryCode.RW = 'RW'                        # originally IsoTerritoryCode.RW
AllTerritoryCode.SA = 'SA'                        # originally IsoTerritoryCode.SA
AllTerritoryCode.SB = 'SB'                        # originally IsoTerritoryCode.SB
AllTerritoryCode.SC = 'SC'                        # originally IsoTerritoryCode.SC
AllTerritoryCode.SD = 'SD'                        # originally IsoTerritoryCode.SD
AllTerritoryCode.SE = 'SE'                        # originally IsoTerritoryCode.SE
AllTerritoryCode.SG = 'SG'                        # originally IsoTerritoryCode.SG
AllTerritoryCode.SH = 'SH'                        # originally IsoTerritoryCode.SH
AllTerritoryCode.SI = 'SI'                        # originally IsoTerritoryCode.SI
AllTerritoryCode.SJ = 'SJ'                        # originally IsoTerritoryCode.SJ
AllTerritoryCode.SK = 'SK'                        # originally IsoTerritoryCode.SK
AllTerritoryCode.SL = 'SL'                        # originally IsoTerritoryCode.SL
AllTerritoryCode.SM = 'SM'                        # originally IsoTerritoryCode.SM
AllTerritoryCode.SN = 'SN'                        # originally IsoTerritoryCode.SN
AllTerritoryCode.SO = 'SO'                        # originally IsoTerritoryCode.SO
AllTerritoryCode.SR = 'SR'                        # originally IsoTerritoryCode.SR
AllTerritoryCode.SS = 'SS'                        # originally IsoTerritoryCode.SS
AllTerritoryCode.ST = 'ST'                        # originally IsoTerritoryCode.ST
AllTerritoryCode.SV = 'SV'                        # originally IsoTerritoryCode.SV
AllTerritoryCode.SX = 'SX'                        # originally IsoTerritoryCode.SX
AllTerritoryCode.SY = 'SY'                        # originally IsoTerritoryCode.SY
AllTerritoryCode.SZ = 'SZ'                        # originally IsoTerritoryCode.SZ
AllTerritoryCode.TC = 'TC'                        # originally IsoTerritoryCode.TC
AllTerritoryCode.TD = 'TD'                        # originally IsoTerritoryCode.TD
AllTerritoryCode.TF = 'TF'                        # originally IsoTerritoryCode.TF
AllTerritoryCode.TG = 'TG'                        # originally IsoTerritoryCode.TG
AllTerritoryCode.TH = 'TH'                        # originally IsoTerritoryCode.TH
AllTerritoryCode.TJ = 'TJ'                        # originally IsoTerritoryCode.TJ
AllTerritoryCode.TK = 'TK'                        # originally IsoTerritoryCode.TK
AllTerritoryCode.TL = 'TL'                        # originally IsoTerritoryCode.TL
AllTerritoryCode.TM = 'TM'                        # originally IsoTerritoryCode.TM
AllTerritoryCode.TN = 'TN'                        # originally IsoTerritoryCode.TN
AllTerritoryCode.TO = 'TO'                        # originally IsoTerritoryCode.TO
AllTerritoryCode.TR = 'TR'                        # originally IsoTerritoryCode.TR
AllTerritoryCode.TT = 'TT'                        # originally IsoTerritoryCode.TT
AllTerritoryCode.TV = 'TV'                        # originally IsoTerritoryCode.TV
AllTerritoryCode.TW = 'TW'                        # originally IsoTerritoryCode.TW
AllTerritoryCode.TZ = 'TZ'                        # originally IsoTerritoryCode.TZ
AllTerritoryCode.UA = 'UA'                        # originally IsoTerritoryCode.UA
AllTerritoryCode.UG = 'UG'                        # originally IsoTerritoryCode.UG
AllTerritoryCode.UM = 'UM'                        # originally IsoTerritoryCode.UM
AllTerritoryCode.US = 'US'                        # originally IsoTerritoryCode.US
AllTerritoryCode.UY = 'UY'                        # originally IsoTerritoryCode.UY
AllTerritoryCode.UZ = 'UZ'                        # originally IsoTerritoryCode.UZ
AllTerritoryCode.VA = 'VA'                        # originally IsoTerritoryCode.VA
AllTerritoryCode.VC = 'VC'                        # originally IsoTerritoryCode.VC
AllTerritoryCode.VE = 'VE'                        # originally IsoTerritoryCode.VE
AllTerritoryCode.VG = 'VG'                        # originally IsoTerritoryCode.VG
AllTerritoryCode.VI = 'VI'                        # originally IsoTerritoryCode.VI
AllTerritoryCode.VN = 'VN'                        # originally IsoTerritoryCode.VN
AllTerritoryCode.VU = 'VU'                        # originally IsoTerritoryCode.VU
AllTerritoryCode.WF = 'WF'                        # originally IsoTerritoryCode.WF
AllTerritoryCode.WS = 'WS'                        # originally IsoTerritoryCode.WS
AllTerritoryCode.YE = 'YE'                        # originally IsoTerritoryCode.YE
AllTerritoryCode.YT = 'YT'                        # originally IsoTerritoryCode.YT
AllTerritoryCode.ZA = 'ZA'                        # originally IsoTerritoryCode.ZA
AllTerritoryCode.ZM = 'ZM'                        # originally IsoTerritoryCode.ZM
AllTerritoryCode.ZW = 'ZW'                        # originally IsoTerritoryCode.ZW
AllTerritoryCode.n4 = '4'                         # originally TisTerritoryCode.n4
AllTerritoryCode.n8 = '8'                         # originally TisTerritoryCode.n8
AllTerritoryCode.n12 = '12'                       # originally TisTerritoryCode.n12
AllTerritoryCode.n20 = '20'                       # originally TisTerritoryCode.n20
AllTerritoryCode.n24 = '24'                       # originally TisTerritoryCode.n24
AllTerritoryCode.n28 = '28'                       # originally TisTerritoryCode.n28
AllTerritoryCode.n31 = '31'                       # originally TisTerritoryCode.n31
AllTerritoryCode.n32 = '32'                       # originally TisTerritoryCode.n32
AllTerritoryCode.n36 = '36'                       # originally TisTerritoryCode.n36
AllTerritoryCode.n40 = '40'                       # originally TisTerritoryCode.n40
AllTerritoryCode.n44 = '44'                       # originally TisTerritoryCode.n44
AllTerritoryCode.n48 = '48'                       # originally TisTerritoryCode.n48
AllTerritoryCode.n50 = '50'                       # originally TisTerritoryCode.n50
AllTerritoryCode.n51 = '51'                       # originally TisTerritoryCode.n51
AllTerritoryCode.n52 = '52'                       # originally TisTerritoryCode.n52
AllTerritoryCode.n56 = '56'                       # originally TisTerritoryCode.n56
AllTerritoryCode.n64 = '64'                       # originally TisTerritoryCode.n64
AllTerritoryCode.n68 = '68'                       # originally TisTerritoryCode.n68
AllTerritoryCode.n70 = '70'                       # originally TisTerritoryCode.n70
AllTerritoryCode.n72 = '72'                       # originally TisTerritoryCode.n72
AllTerritoryCode.n76 = '76'                       # originally TisTerritoryCode.n76
AllTerritoryCode.n84 = '84'                       # originally TisTerritoryCode.n84
AllTerritoryCode.n90 = '90'                       # originally TisTerritoryCode.n90
AllTerritoryCode.n96 = '96'                       # originally TisTerritoryCode.n96
AllTerritoryCode.n100 = '100'                     # originally TisTerritoryCode.n100
AllTerritoryCode.n104 = '104'                     # originally TisTerritoryCode.n104
AllTerritoryCode.n108 = '108'                     # originally TisTerritoryCode.n108
AllTerritoryCode.n112 = '112'                     # originally TisTerritoryCode.n112
AllTerritoryCode.n116 = '116'                     # originally TisTerritoryCode.n116
AllTerritoryCode.n120 = '120'                     # originally TisTerritoryCode.n120
AllTerritoryCode.n124 = '124'                     # originally TisTerritoryCode.n124
AllTerritoryCode.n132 = '132'                     # originally TisTerritoryCode.n132
AllTerritoryCode.n140 = '140'                     # originally TisTerritoryCode.n140
AllTerritoryCode.n144 = '144'                     # originally TisTerritoryCode.n144
AllTerritoryCode.n148 = '148'                     # originally TisTerritoryCode.n148
AllTerritoryCode.n152 = '152'                     # originally TisTerritoryCode.n152
AllTerritoryCode.n156 = '156'                     # originally TisTerritoryCode.n156
AllTerritoryCode.n158 = '158'                     # originally TisTerritoryCode.n158
AllTerritoryCode.n170 = '170'                     # originally TisTerritoryCode.n170
AllTerritoryCode.n174 = '174'                     # originally TisTerritoryCode.n174
AllTerritoryCode.n178 = '178'                     # originally TisTerritoryCode.n178
AllTerritoryCode.n180 = '180'                     # originally TisTerritoryCode.n180
AllTerritoryCode.n188 = '188'                     # originally TisTerritoryCode.n188
AllTerritoryCode.n191 = '191'                     # originally TisTerritoryCode.n191
AllTerritoryCode.n192 = '192'                     # originally TisTerritoryCode.n192
AllTerritoryCode.n196 = '196'                     # originally TisTerritoryCode.n196
AllTerritoryCode.n200 = '200'                     # originally TisTerritoryCode.n200
AllTerritoryCode.n203 = '203'                     # originally TisTerritoryCode.n203
AllTerritoryCode.n204 = '204'                     # originally TisTerritoryCode.n204
AllTerritoryCode.n208 = '208'                     # originally TisTerritoryCode.n208
AllTerritoryCode.n212 = '212'                     # originally TisTerritoryCode.n212
AllTerritoryCode.n214 = '214'                     # originally TisTerritoryCode.n214
AllTerritoryCode.n218 = '218'                     # originally TisTerritoryCode.n218
AllTerritoryCode.n222 = '222'                     # originally TisTerritoryCode.n222
AllTerritoryCode.n226 = '226'                     # originally TisTerritoryCode.n226
AllTerritoryCode.n230 = '230'                     # originally TisTerritoryCode.n230
AllTerritoryCode.n231 = '231'                     # originally TisTerritoryCode.n231
AllTerritoryCode.n232 = '232'                     # originally TisTerritoryCode.n232
AllTerritoryCode.n233 = '233'                     # originally TisTerritoryCode.n233
AllTerritoryCode.n242 = '242'                     # originally TisTerritoryCode.n242
AllTerritoryCode.n246 = '246'                     # originally TisTerritoryCode.n246
AllTerritoryCode.n250 = '250'                     # originally TisTerritoryCode.n250
AllTerritoryCode.n258 = '258'                     # originally TisTerritoryCode.n258
AllTerritoryCode.n262 = '262'                     # originally TisTerritoryCode.n262
AllTerritoryCode.n266 = '266'                     # originally TisTerritoryCode.n266
AllTerritoryCode.n268 = '268'                     # originally TisTerritoryCode.n268
AllTerritoryCode.n270 = '270'                     # originally TisTerritoryCode.n270
AllTerritoryCode.n276 = '276'                     # originally TisTerritoryCode.n276
AllTerritoryCode.n278 = '278'                     # originally TisTerritoryCode.n278
AllTerritoryCode.n280 = '280'                     # originally TisTerritoryCode.n280
AllTerritoryCode.n288 = '288'                     # originally TisTerritoryCode.n288
AllTerritoryCode.n296 = '296'                     # originally TisTerritoryCode.n296
AllTerritoryCode.n300 = '300'                     # originally TisTerritoryCode.n300
AllTerritoryCode.n308 = '308'                     # originally TisTerritoryCode.n308
AllTerritoryCode.n320 = '320'                     # originally TisTerritoryCode.n320
AllTerritoryCode.n324 = '324'                     # originally TisTerritoryCode.n324
AllTerritoryCode.n328 = '328'                     # originally TisTerritoryCode.n328
AllTerritoryCode.n332 = '332'                     # originally TisTerritoryCode.n332
AllTerritoryCode.n336 = '336'                     # originally TisTerritoryCode.n336
AllTerritoryCode.n340 = '340'                     # originally TisTerritoryCode.n340
AllTerritoryCode.n344 = '344'                     # originally TisTerritoryCode.n344
AllTerritoryCode.n348 = '348'                     # originally TisTerritoryCode.n348
AllTerritoryCode.n352 = '352'                     # originally TisTerritoryCode.n352
AllTerritoryCode.n356 = '356'                     # originally TisTerritoryCode.n356
AllTerritoryCode.n360 = '360'                     # originally TisTerritoryCode.n360
AllTerritoryCode.n364 = '364'                     # originally TisTerritoryCode.n364
AllTerritoryCode.n368 = '368'                     # originally TisTerritoryCode.n368
AllTerritoryCode.n372 = '372'                     # originally TisTerritoryCode.n372
AllTerritoryCode.n376 = '376'                     # originally TisTerritoryCode.n376
AllTerritoryCode.n380 = '380'                     # originally TisTerritoryCode.n380
AllTerritoryCode.n384 = '384'                     # originally TisTerritoryCode.n384
AllTerritoryCode.n388 = '388'                     # originally TisTerritoryCode.n388
AllTerritoryCode.n392 = '392'                     # originally TisTerritoryCode.n392
AllTerritoryCode.n398 = '398'                     # originally TisTerritoryCode.n398
AllTerritoryCode.n400 = '400'                     # originally TisTerritoryCode.n400
AllTerritoryCode.n404 = '404'                     # originally TisTerritoryCode.n404
AllTerritoryCode.n408 = '408'                     # originally TisTerritoryCode.n408
AllTerritoryCode.n410 = '410'                     # originally TisTerritoryCode.n410
AllTerritoryCode.n414 = '414'                     # originally TisTerritoryCode.n414
AllTerritoryCode.n417 = '417'                     # originally TisTerritoryCode.n417
AllTerritoryCode.n418 = '418'                     # originally TisTerritoryCode.n418
AllTerritoryCode.n422 = '422'                     # originally TisTerritoryCode.n422
AllTerritoryCode.n426 = '426'                     # originally TisTerritoryCode.n426
AllTerritoryCode.n428 = '428'                     # originally TisTerritoryCode.n428
AllTerritoryCode.n430 = '430'                     # originally TisTerritoryCode.n430
AllTerritoryCode.n434 = '434'                     # originally TisTerritoryCode.n434
AllTerritoryCode.n438 = '438'                     # originally TisTerritoryCode.n438
AllTerritoryCode.n440 = '440'                     # originally TisTerritoryCode.n440
AllTerritoryCode.n442 = '442'                     # originally TisTerritoryCode.n442
AllTerritoryCode.n450 = '450'                     # originally TisTerritoryCode.n450
AllTerritoryCode.n454 = '454'                     # originally TisTerritoryCode.n454
AllTerritoryCode.n458 = '458'                     # originally TisTerritoryCode.n458
AllTerritoryCode.n462 = '462'                     # originally TisTerritoryCode.n462
AllTerritoryCode.n466 = '466'                     # originally TisTerritoryCode.n466
AllTerritoryCode.n470 = '470'                     # originally TisTerritoryCode.n470
AllTerritoryCode.n478 = '478'                     # originally TisTerritoryCode.n478
AllTerritoryCode.n480 = '480'                     # originally TisTerritoryCode.n480
AllTerritoryCode.n484 = '484'                     # originally TisTerritoryCode.n484
AllTerritoryCode.n492 = '492'                     # originally TisTerritoryCode.n492
AllTerritoryCode.n496 = '496'                     # originally TisTerritoryCode.n496
AllTerritoryCode.n498 = '498'                     # originally TisTerritoryCode.n498
AllTerritoryCode.n499 = '499'                     # originally TisTerritoryCode.n499
AllTerritoryCode.n504 = '504'                     # originally TisTerritoryCode.n504
AllTerritoryCode.n508 = '508'                     # originally TisTerritoryCode.n508
AllTerritoryCode.n512 = '512'                     # originally TisTerritoryCode.n512
AllTerritoryCode.n516 = '516'                     # originally TisTerritoryCode.n516
AllTerritoryCode.n520 = '520'                     # originally TisTerritoryCode.n520
AllTerritoryCode.n524 = '524'                     # originally TisTerritoryCode.n524
AllTerritoryCode.n528 = '528'                     # originally TisTerritoryCode.n528
AllTerritoryCode.n540 = '540'                     # originally TisTerritoryCode.n540
AllTerritoryCode.n548 = '548'                     # originally TisTerritoryCode.n548
AllTerritoryCode.n554 = '554'                     # originally TisTerritoryCode.n554
AllTerritoryCode.n558 = '558'                     # originally TisTerritoryCode.n558
AllTerritoryCode.n562 = '562'                     # originally TisTerritoryCode.n562
AllTerritoryCode.n566 = '566'                     # originally TisTerritoryCode.n566
AllTerritoryCode.n578 = '578'                     # originally TisTerritoryCode.n578
AllTerritoryCode.n583 = '583'                     # originally TisTerritoryCode.n583
AllTerritoryCode.n584 = '584'                     # originally TisTerritoryCode.n584
AllTerritoryCode.n585 = '585'                     # originally TisTerritoryCode.n585
AllTerritoryCode.n586 = '586'                     # originally TisTerritoryCode.n586
AllTerritoryCode.n591 = '591'                     # originally TisTerritoryCode.n591
AllTerritoryCode.n598 = '598'                     # originally TisTerritoryCode.n598
AllTerritoryCode.n600 = '600'                     # originally TisTerritoryCode.n600
AllTerritoryCode.n604 = '604'                     # originally TisTerritoryCode.n604
AllTerritoryCode.n608 = '608'                     # originally TisTerritoryCode.n608
AllTerritoryCode.n616 = '616'                     # originally TisTerritoryCode.n616
AllTerritoryCode.n620 = '620'                     # originally TisTerritoryCode.n620
AllTerritoryCode.n624 = '624'                     # originally TisTerritoryCode.n624
AllTerritoryCode.n626 = '626'                     # originally TisTerritoryCode.n626
AllTerritoryCode.n630 = '630'                     # originally TisTerritoryCode.n630
AllTerritoryCode.n634 = '634'                     # originally TisTerritoryCode.n634
AllTerritoryCode.n642 = '642'                     # originally TisTerritoryCode.n642
AllTerritoryCode.n643 = '643'                     # originally TisTerritoryCode.n643
AllTerritoryCode.n646 = '646'                     # originally TisTerritoryCode.n646
AllTerritoryCode.n659 = '659'                     # originally TisTerritoryCode.n659
AllTerritoryCode.n662 = '662'                     # originally TisTerritoryCode.n662
AllTerritoryCode.n670 = '670'                     # originally TisTerritoryCode.n670
AllTerritoryCode.n674 = '674'                     # originally TisTerritoryCode.n674
AllTerritoryCode.n678 = '678'                     # originally TisTerritoryCode.n678
AllTerritoryCode.n682 = '682'                     # originally TisTerritoryCode.n682
AllTerritoryCode.n686 = '686'                     # originally TisTerritoryCode.n686
AllTerritoryCode.n688 = '688'                     # originally TisTerritoryCode.n688
AllTerritoryCode.n690 = '690'                     # originally TisTerritoryCode.n690
AllTerritoryCode.n694 = '694'                     # originally TisTerritoryCode.n694
AllTerritoryCode.n702 = '702'                     # originally TisTerritoryCode.n702
AllTerritoryCode.n703 = '703'                     # originally TisTerritoryCode.n703
AllTerritoryCode.n704 = '704'                     # originally TisTerritoryCode.n704
AllTerritoryCode.n705 = '705'                     # originally TisTerritoryCode.n705
AllTerritoryCode.n706 = '706'                     # originally TisTerritoryCode.n706
AllTerritoryCode.n710 = '710'                     # originally TisTerritoryCode.n710
AllTerritoryCode.n716 = '716'                     # originally TisTerritoryCode.n716
AllTerritoryCode.n720 = '720'                     # originally TisTerritoryCode.n720
AllTerritoryCode.n724 = '724'                     # originally TisTerritoryCode.n724
AllTerritoryCode.n728 = '728'                     # originally TisTerritoryCode.n728
AllTerritoryCode.n729 = '729'                     # originally TisTerritoryCode.n729
AllTerritoryCode.n732 = '732'                     # originally TisTerritoryCode.n732
AllTerritoryCode.n736 = '736'                     # originally TisTerritoryCode.n736
AllTerritoryCode.n740 = '740'                     # originally TisTerritoryCode.n740
AllTerritoryCode.n748 = '748'                     # originally TisTerritoryCode.n748
AllTerritoryCode.n752 = '752'                     # originally TisTerritoryCode.n752
AllTerritoryCode.n756 = '756'                     # originally TisTerritoryCode.n756
AllTerritoryCode.n760 = '760'                     # originally TisTerritoryCode.n760
AllTerritoryCode.n762 = '762'                     # originally TisTerritoryCode.n762
AllTerritoryCode.n764 = '764'                     # originally TisTerritoryCode.n764
AllTerritoryCode.n768 = '768'                     # originally TisTerritoryCode.n768
AllTerritoryCode.n776 = '776'                     # originally TisTerritoryCode.n776
AllTerritoryCode.n780 = '780'                     # originally TisTerritoryCode.n780
AllTerritoryCode.n784 = '784'                     # originally TisTerritoryCode.n784
AllTerritoryCode.n788 = '788'                     # originally TisTerritoryCode.n788
AllTerritoryCode.n792 = '792'                     # originally TisTerritoryCode.n792
AllTerritoryCode.n795 = '795'                     # originally TisTerritoryCode.n795
AllTerritoryCode.n798 = '798'                     # originally TisTerritoryCode.n798
AllTerritoryCode.n800 = '800'                     # originally TisTerritoryCode.n800
AllTerritoryCode.n804 = '804'                     # originally TisTerritoryCode.n804
AllTerritoryCode.n807 = '807'                     # originally TisTerritoryCode.n807
AllTerritoryCode.n810 = '810'                     # originally TisTerritoryCode.n810
AllTerritoryCode.n818 = '818'                     # originally TisTerritoryCode.n818
AllTerritoryCode.n826 = '826'                     # originally TisTerritoryCode.n826
AllTerritoryCode.n834 = '834'                     # originally TisTerritoryCode.n834
AllTerritoryCode.n840 = '840'                     # originally TisTerritoryCode.n840
AllTerritoryCode.n854 = '854'                     # originally TisTerritoryCode.n854
AllTerritoryCode.n858 = '858'                     # originally TisTerritoryCode.n858
AllTerritoryCode.n860 = '860'                     # originally TisTerritoryCode.n860
AllTerritoryCode.n862 = '862'                     # originally TisTerritoryCode.n862
AllTerritoryCode.n882 = '882'                     # originally TisTerritoryCode.n882
AllTerritoryCode.n886 = '886'                     # originally TisTerritoryCode.n886
AllTerritoryCode.n887 = '887'                     # originally TisTerritoryCode.n887
AllTerritoryCode.n890 = '890'                     # originally TisTerritoryCode.n890
AllTerritoryCode.n891 = '891'                     # originally TisTerritoryCode.n891
AllTerritoryCode.n894 = '894'                     # originally TisTerritoryCode.n894
AllTerritoryCode.n2100 = '2100'                   # originally TisTerritoryCode.n2100
AllTerritoryCode.n2101 = '2101'                   # originally TisTerritoryCode.n2101
AllTerritoryCode.n2102 = '2102'                   # originally TisTerritoryCode.n2102
AllTerritoryCode.n2103 = '2103'                   # originally TisTerritoryCode.n2103
AllTerritoryCode.n2104 = '2104'                   # originally TisTerritoryCode.n2104
AllTerritoryCode.n2105 = '2105'                   # originally TisTerritoryCode.n2105
AllTerritoryCode.n2106 = '2106'                   # originally TisTerritoryCode.n2106
AllTerritoryCode.n2107 = '2107'                   # originally TisTerritoryCode.n2107
AllTerritoryCode.n2108 = '2108'                   # originally TisTerritoryCode.n2108
AllTerritoryCode.n2109 = '2109'                   # originally TisTerritoryCode.n2109
AllTerritoryCode.n2110 = '2110'                   # originally TisTerritoryCode.n2110
AllTerritoryCode.n2111 = '2111'                   # originally TisTerritoryCode.n2111
AllTerritoryCode.n2112 = '2112'                   # originally TisTerritoryCode.n2112
AllTerritoryCode.n2113 = '2113'                   # originally TisTerritoryCode.n2113
AllTerritoryCode.n2114 = '2114'                   # originally TisTerritoryCode.n2114
AllTerritoryCode.n2115 = '2115'                   # originally TisTerritoryCode.n2115
AllTerritoryCode.n2116 = '2116'                   # originally TisTerritoryCode.n2116
AllTerritoryCode.n2117 = '2117'                   # originally TisTerritoryCode.n2117
AllTerritoryCode.n2118 = '2118'                   # originally TisTerritoryCode.n2118
AllTerritoryCode.n2119 = '2119'                   # originally TisTerritoryCode.n2119
AllTerritoryCode.n2120 = '2120'                   # originally TisTerritoryCode.n2120
AllTerritoryCode.n2121 = '2121'                   # originally TisTerritoryCode.n2121
AllTerritoryCode.n2122 = '2122'                   # originally TisTerritoryCode.n2122
AllTerritoryCode.n2123 = '2123'                   # originally TisTerritoryCode.n2123
AllTerritoryCode.n2124 = '2124'                   # originally TisTerritoryCode.n2124
AllTerritoryCode.n2125 = '2125'                   # originally TisTerritoryCode.n2125
AllTerritoryCode.n2126 = '2126'                   # originally TisTerritoryCode.n2126
AllTerritoryCode.n2127 = '2127'                   # originally TisTerritoryCode.n2127
AllTerritoryCode.n2128 = '2128'                   # originally TisTerritoryCode.n2128
AllTerritoryCode.n2129 = '2129'                   # originally TisTerritoryCode.n2129
AllTerritoryCode.n2130 = '2130'                   # originally TisTerritoryCode.n2130
AllTerritoryCode.n2131 = '2131'                   # originally TisTerritoryCode.n2131
AllTerritoryCode.n2132 = '2132'                   # originally TisTerritoryCode.n2132
AllTerritoryCode.n2133 = '2133'                   # originally TisTerritoryCode.n2133
AllTerritoryCode.n2134 = '2134'                   # originally TisTerritoryCode.n2134
AllTerritoryCode.n2136 = '2136'                   # originally TisTerritoryCode.n2136
AllTerritoryCode.Worldwide = 'Worldwide'          # originally DdexTerritoryCode.Worldwide
AllTerritoryCode.AIDJ = 'AIDJ'                    # originally DeprecatedIsoTerritoryCode.AIDJ
AllTerritoryCode.ANHH = 'ANHH'                    # originally DeprecatedIsoTerritoryCode.ANHH
AllTerritoryCode.BQAQ = 'BQAQ'                    # originally DeprecatedIsoTerritoryCode.BQAQ
AllTerritoryCode.BUMM = 'BUMM'                    # originally DeprecatedIsoTerritoryCode.BUMM
AllTerritoryCode.BYAA = 'BYAA'                    # originally DeprecatedIsoTerritoryCode.BYAA
AllTerritoryCode.CSHH = 'CSHH'                    # originally DeprecatedIsoTerritoryCode.CSHH
AllTerritoryCode.CSXX = 'CSXX'                    # originally DeprecatedIsoTerritoryCode.CSXX
AllTerritoryCode.CTKI = 'CTKI'                    # originally DeprecatedIsoTerritoryCode.CTKI
AllTerritoryCode.DDDE = 'DDDE'                    # originally DeprecatedIsoTerritoryCode.DDDE
AllTerritoryCode.DYBJ = 'DYBJ'                    # originally DeprecatedIsoTerritoryCode.DYBJ
AllTerritoryCode.FQHH = 'FQHH'                    # originally DeprecatedIsoTerritoryCode.FQHH
AllTerritoryCode.FXFR = 'FXFR'                    # originally DeprecatedIsoTerritoryCode.FXFR
AllTerritoryCode.GEHH = 'GEHH'                    # originally DeprecatedIsoTerritoryCode.GEHH
AllTerritoryCode.HVBF = 'HVBF'                    # originally DeprecatedIsoTerritoryCode.HVBF
AllTerritoryCode.JTUM = 'JTUM'                    # originally DeprecatedIsoTerritoryCode.JTUM
AllTerritoryCode.MIUM = 'MIUM'                    # originally DeprecatedIsoTerritoryCode.MIUM
AllTerritoryCode.NHVU = 'NHVU'                    # originally DeprecatedIsoTerritoryCode.NHVU
AllTerritoryCode.NQAQ = 'NQAQ'                    # originally DeprecatedIsoTerritoryCode.NQAQ
AllTerritoryCode.NTHH = 'NTHH'                    # originally DeprecatedIsoTerritoryCode.NTHH
AllTerritoryCode.PCHH = 'PCHH'                    # originally DeprecatedIsoTerritoryCode.PCHH
AllTerritoryCode.PUUM = 'PUUM'                    # originally DeprecatedIsoTerritoryCode.PUUM
AllTerritoryCode.PZPA = 'PZPA'                    # originally DeprecatedIsoTerritoryCode.PZPA
AllTerritoryCode.RHZW = 'RHZW'                    # originally DeprecatedIsoTerritoryCode.RHZW
AllTerritoryCode.SKIN = 'SKIN'                    # originally DeprecatedIsoTerritoryCode.SKIN
AllTerritoryCode.SUHH = 'SUHH'                    # originally DeprecatedIsoTerritoryCode.SUHH
AllTerritoryCode.TPTL = 'TPTL'                    # originally DeprecatedIsoTerritoryCode.TPTL
AllTerritoryCode.VDVN = 'VDVN'                    # originally DeprecatedIsoTerritoryCode.VDVN
AllTerritoryCode.WKUM = 'WKUM'                    # originally DeprecatedIsoTerritoryCode.WKUM
AllTerritoryCode.YDYE = 'YDYE'                    # originally DeprecatedIsoTerritoryCode.YDYE
AllTerritoryCode.YUCS = 'YUCS'                    # originally DeprecatedIsoTerritoryCode.YUCS
AllTerritoryCode.ZRCD = 'ZRCD'                    # originally DeprecatedIsoTerritoryCode.ZRCD
AllTerritoryCode._InitializeFacetMap(AllTerritoryCode._CF_enumeration,
   AllTerritoryCode._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'AllTerritoryCode', AllTerritoryCode)

# Union simple type: {http://ddex.net/xml/avs/avs}CurrencyCode
# superclasses pyxb.binding.datatypes.anySimpleType
class CurrencyCode (pyxb.binding.basis.STD_union):

    """A code representing a Currency."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CurrencyCode')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 1498, 3)
    _Documentation = 'A code representing a Currency.'

    _MemberTypes = ( IsoCurrencyCode, DeprecatedCurrencyCode, )
CurrencyCode._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CurrencyCode)
CurrencyCode._CF_pattern = pyxb.binding.facets.CF_pattern()
CurrencyCode.AED = 'AED'                          # originally IsoCurrencyCode.AED
CurrencyCode.AFN = 'AFN'                          # originally IsoCurrencyCode.AFN
CurrencyCode.ALL = 'ALL'                          # originally IsoCurrencyCode.ALL
CurrencyCode.AMD = 'AMD'                          # originally IsoCurrencyCode.AMD
CurrencyCode.ANG = 'ANG'                          # originally IsoCurrencyCode.ANG
CurrencyCode.AOA = 'AOA'                          # originally IsoCurrencyCode.AOA
CurrencyCode.ARS = 'ARS'                          # originally IsoCurrencyCode.ARS
CurrencyCode.AUD = 'AUD'                          # originally IsoCurrencyCode.AUD
CurrencyCode.AWG = 'AWG'                          # originally IsoCurrencyCode.AWG
CurrencyCode.AZN = 'AZN'                          # originally IsoCurrencyCode.AZN
CurrencyCode.BAM = 'BAM'                          # originally IsoCurrencyCode.BAM
CurrencyCode.BBD = 'BBD'                          # originally IsoCurrencyCode.BBD
CurrencyCode.BDT = 'BDT'                          # originally IsoCurrencyCode.BDT
CurrencyCode.BGN = 'BGN'                          # originally IsoCurrencyCode.BGN
CurrencyCode.BHD = 'BHD'                          # originally IsoCurrencyCode.BHD
CurrencyCode.BIF = 'BIF'                          # originally IsoCurrencyCode.BIF
CurrencyCode.BMD = 'BMD'                          # originally IsoCurrencyCode.BMD
CurrencyCode.BND = 'BND'                          # originally IsoCurrencyCode.BND
CurrencyCode.BOB = 'BOB'                          # originally IsoCurrencyCode.BOB
CurrencyCode.BOV = 'BOV'                          # originally IsoCurrencyCode.BOV
CurrencyCode.BRL = 'BRL'                          # originally IsoCurrencyCode.BRL
CurrencyCode.BSD = 'BSD'                          # originally IsoCurrencyCode.BSD
CurrencyCode.BTN = 'BTN'                          # originally IsoCurrencyCode.BTN
CurrencyCode.BWP = 'BWP'                          # originally IsoCurrencyCode.BWP
CurrencyCode.BYR = 'BYR'                          # originally IsoCurrencyCode.BYR
CurrencyCode.BZD = 'BZD'                          # originally IsoCurrencyCode.BZD
CurrencyCode.CAD = 'CAD'                          # originally IsoCurrencyCode.CAD
CurrencyCode.CDF = 'CDF'                          # originally IsoCurrencyCode.CDF
CurrencyCode.CHF = 'CHF'                          # originally IsoCurrencyCode.CHF
CurrencyCode.CLF = 'CLF'                          # originally IsoCurrencyCode.CLF
CurrencyCode.CLP = 'CLP'                          # originally IsoCurrencyCode.CLP
CurrencyCode.CNY = 'CNY'                          # originally IsoCurrencyCode.CNY
CurrencyCode.COP = 'COP'                          # originally IsoCurrencyCode.COP
CurrencyCode.COU = 'COU'                          # originally IsoCurrencyCode.COU
CurrencyCode.CRC = 'CRC'                          # originally IsoCurrencyCode.CRC
CurrencyCode.CUC = 'CUC'                          # originally IsoCurrencyCode.CUC
CurrencyCode.CUP = 'CUP'                          # originally IsoCurrencyCode.CUP
CurrencyCode.CVE = 'CVE'                          # originally IsoCurrencyCode.CVE
CurrencyCode.CZK = 'CZK'                          # originally IsoCurrencyCode.CZK
CurrencyCode.DJF = 'DJF'                          # originally IsoCurrencyCode.DJF
CurrencyCode.DKK = 'DKK'                          # originally IsoCurrencyCode.DKK
CurrencyCode.DOP = 'DOP'                          # originally IsoCurrencyCode.DOP
CurrencyCode.DZD = 'DZD'                          # originally IsoCurrencyCode.DZD
CurrencyCode.EGP = 'EGP'                          # originally IsoCurrencyCode.EGP
CurrencyCode.ERN = 'ERN'                          # originally IsoCurrencyCode.ERN
CurrencyCode.ETB = 'ETB'                          # originally IsoCurrencyCode.ETB
CurrencyCode.EUR = 'EUR'                          # originally IsoCurrencyCode.EUR
CurrencyCode.FJD = 'FJD'                          # originally IsoCurrencyCode.FJD
CurrencyCode.FKP = 'FKP'                          # originally IsoCurrencyCode.FKP
CurrencyCode.GBP = 'GBP'                          # originally IsoCurrencyCode.GBP
CurrencyCode.GEL = 'GEL'                          # originally IsoCurrencyCode.GEL
CurrencyCode.GHS = 'GHS'                          # originally IsoCurrencyCode.GHS
CurrencyCode.GIP = 'GIP'                          # originally IsoCurrencyCode.GIP
CurrencyCode.GMD = 'GMD'                          # originally IsoCurrencyCode.GMD
CurrencyCode.GNF = 'GNF'                          # originally IsoCurrencyCode.GNF
CurrencyCode.GTQ = 'GTQ'                          # originally IsoCurrencyCode.GTQ
CurrencyCode.GYD = 'GYD'                          # originally IsoCurrencyCode.GYD
CurrencyCode.HKD = 'HKD'                          # originally IsoCurrencyCode.HKD
CurrencyCode.HNL = 'HNL'                          # originally IsoCurrencyCode.HNL
CurrencyCode.HRK = 'HRK'                          # originally IsoCurrencyCode.HRK
CurrencyCode.HTG = 'HTG'                          # originally IsoCurrencyCode.HTG
CurrencyCode.HUF = 'HUF'                          # originally IsoCurrencyCode.HUF
CurrencyCode.IDR = 'IDR'                          # originally IsoCurrencyCode.IDR
CurrencyCode.ILS = 'ILS'                          # originally IsoCurrencyCode.ILS
CurrencyCode.INR = 'INR'                          # originally IsoCurrencyCode.INR
CurrencyCode.IQD = 'IQD'                          # originally IsoCurrencyCode.IQD
CurrencyCode.IRR = 'IRR'                          # originally IsoCurrencyCode.IRR
CurrencyCode.ISK = 'ISK'                          # originally IsoCurrencyCode.ISK
CurrencyCode.JMD = 'JMD'                          # originally IsoCurrencyCode.JMD
CurrencyCode.JOD = 'JOD'                          # originally IsoCurrencyCode.JOD
CurrencyCode.JPY = 'JPY'                          # originally IsoCurrencyCode.JPY
CurrencyCode.KES = 'KES'                          # originally IsoCurrencyCode.KES
CurrencyCode.KGS = 'KGS'                          # originally IsoCurrencyCode.KGS
CurrencyCode.KHR = 'KHR'                          # originally IsoCurrencyCode.KHR
CurrencyCode.KMF = 'KMF'                          # originally IsoCurrencyCode.KMF
CurrencyCode.KPW = 'KPW'                          # originally IsoCurrencyCode.KPW
CurrencyCode.KRW = 'KRW'                          # originally IsoCurrencyCode.KRW
CurrencyCode.KWD = 'KWD'                          # originally IsoCurrencyCode.KWD
CurrencyCode.KYD = 'KYD'                          # originally IsoCurrencyCode.KYD
CurrencyCode.KZT = 'KZT'                          # originally IsoCurrencyCode.KZT
CurrencyCode.LAK = 'LAK'                          # originally IsoCurrencyCode.LAK
CurrencyCode.LBP = 'LBP'                          # originally IsoCurrencyCode.LBP
CurrencyCode.LKR = 'LKR'                          # originally IsoCurrencyCode.LKR
CurrencyCode.LRD = 'LRD'                          # originally IsoCurrencyCode.LRD
CurrencyCode.LSL = 'LSL'                          # originally IsoCurrencyCode.LSL
CurrencyCode.LTL = 'LTL'                          # originally IsoCurrencyCode.LTL
CurrencyCode.LVL = 'LVL'                          # originally IsoCurrencyCode.LVL
CurrencyCode.LYD = 'LYD'                          # originally IsoCurrencyCode.LYD
CurrencyCode.MAD = 'MAD'                          # originally IsoCurrencyCode.MAD
CurrencyCode.MDL = 'MDL'                          # originally IsoCurrencyCode.MDL
CurrencyCode.MGA = 'MGA'                          # originally IsoCurrencyCode.MGA
CurrencyCode.MKD = 'MKD'                          # originally IsoCurrencyCode.MKD
CurrencyCode.MMK = 'MMK'                          # originally IsoCurrencyCode.MMK
CurrencyCode.MNT = 'MNT'                          # originally IsoCurrencyCode.MNT
CurrencyCode.MOP = 'MOP'                          # originally IsoCurrencyCode.MOP
CurrencyCode.MRO = 'MRO'                          # originally IsoCurrencyCode.MRO
CurrencyCode.MUR = 'MUR'                          # originally IsoCurrencyCode.MUR
CurrencyCode.MVR = 'MVR'                          # originally IsoCurrencyCode.MVR
CurrencyCode.MWK = 'MWK'                          # originally IsoCurrencyCode.MWK
CurrencyCode.MXN = 'MXN'                          # originally IsoCurrencyCode.MXN
CurrencyCode.MXV = 'MXV'                          # originally IsoCurrencyCode.MXV
CurrencyCode.MYR = 'MYR'                          # originally IsoCurrencyCode.MYR
CurrencyCode.MZM = 'MZM'                          # originally IsoCurrencyCode.MZM
CurrencyCode.NAD = 'NAD'                          # originally IsoCurrencyCode.NAD
CurrencyCode.NGN = 'NGN'                          # originally IsoCurrencyCode.NGN
CurrencyCode.NIO = 'NIO'                          # originally IsoCurrencyCode.NIO
CurrencyCode.NOK = 'NOK'                          # originally IsoCurrencyCode.NOK
CurrencyCode.NPR = 'NPR'                          # originally IsoCurrencyCode.NPR
CurrencyCode.NZD = 'NZD'                          # originally IsoCurrencyCode.NZD
CurrencyCode.OMR = 'OMR'                          # originally IsoCurrencyCode.OMR
CurrencyCode.PAB = 'PAB'                          # originally IsoCurrencyCode.PAB
CurrencyCode.PEN = 'PEN'                          # originally IsoCurrencyCode.PEN
CurrencyCode.PGK = 'PGK'                          # originally IsoCurrencyCode.PGK
CurrencyCode.PHP = 'PHP'                          # originally IsoCurrencyCode.PHP
CurrencyCode.PKR = 'PKR'                          # originally IsoCurrencyCode.PKR
CurrencyCode.PLN = 'PLN'                          # originally IsoCurrencyCode.PLN
CurrencyCode.PYG = 'PYG'                          # originally IsoCurrencyCode.PYG
CurrencyCode.QAR = 'QAR'                          # originally IsoCurrencyCode.QAR
CurrencyCode.RON = 'RON'                          # originally IsoCurrencyCode.RON
CurrencyCode.RSD = 'RSD'                          # originally IsoCurrencyCode.RSD
CurrencyCode.RUB = 'RUB'                          # originally IsoCurrencyCode.RUB
CurrencyCode.RWF = 'RWF'                          # originally IsoCurrencyCode.RWF
CurrencyCode.SAR = 'SAR'                          # originally IsoCurrencyCode.SAR
CurrencyCode.SBD = 'SBD'                          # originally IsoCurrencyCode.SBD
CurrencyCode.SCR = 'SCR'                          # originally IsoCurrencyCode.SCR
CurrencyCode.SDG = 'SDG'                          # originally IsoCurrencyCode.SDG
CurrencyCode.SEK = 'SEK'                          # originally IsoCurrencyCode.SEK
CurrencyCode.SGD = 'SGD'                          # originally IsoCurrencyCode.SGD
CurrencyCode.SHP = 'SHP'                          # originally IsoCurrencyCode.SHP
CurrencyCode.SLL = 'SLL'                          # originally IsoCurrencyCode.SLL
CurrencyCode.SOS = 'SOS'                          # originally IsoCurrencyCode.SOS
CurrencyCode.SRD = 'SRD'                          # originally IsoCurrencyCode.SRD
CurrencyCode.STD = 'STD'                          # originally IsoCurrencyCode.STD
CurrencyCode.SVC = 'SVC'                          # originally IsoCurrencyCode.SVC
CurrencyCode.SYP = 'SYP'                          # originally IsoCurrencyCode.SYP
CurrencyCode.SZL = 'SZL'                          # originally IsoCurrencyCode.SZL
CurrencyCode.THB = 'THB'                          # originally IsoCurrencyCode.THB
CurrencyCode.TJS = 'TJS'                          # originally IsoCurrencyCode.TJS
CurrencyCode.TMT = 'TMT'                          # originally IsoCurrencyCode.TMT
CurrencyCode.TND = 'TND'                          # originally IsoCurrencyCode.TND
CurrencyCode.TOP = 'TOP'                          # originally IsoCurrencyCode.TOP
CurrencyCode.TRY = 'TRY'                          # originally IsoCurrencyCode.TRY
CurrencyCode.TTD = 'TTD'                          # originally IsoCurrencyCode.TTD
CurrencyCode.TWD = 'TWD'                          # originally IsoCurrencyCode.TWD
CurrencyCode.TZS = 'TZS'                          # originally IsoCurrencyCode.TZS
CurrencyCode.UAH = 'UAH'                          # originally IsoCurrencyCode.UAH
CurrencyCode.UGX = 'UGX'                          # originally IsoCurrencyCode.UGX
CurrencyCode.USD = 'USD'                          # originally IsoCurrencyCode.USD
CurrencyCode.UYI = 'UYI'                          # originally IsoCurrencyCode.UYI
CurrencyCode.UYU = 'UYU'                          # originally IsoCurrencyCode.UYU
CurrencyCode.UZS = 'UZS'                          # originally IsoCurrencyCode.UZS
CurrencyCode.VEF = 'VEF'                          # originally IsoCurrencyCode.VEF
CurrencyCode.VND = 'VND'                          # originally IsoCurrencyCode.VND
CurrencyCode.VUV = 'VUV'                          # originally IsoCurrencyCode.VUV
CurrencyCode.WST = 'WST'                          # originally IsoCurrencyCode.WST
CurrencyCode.XAF = 'XAF'                          # originally IsoCurrencyCode.XAF
CurrencyCode.XCD = 'XCD'                          # originally IsoCurrencyCode.XCD
CurrencyCode.XOF = 'XOF'                          # originally IsoCurrencyCode.XOF
CurrencyCode.XPF = 'XPF'                          # originally IsoCurrencyCode.XPF
CurrencyCode.YER = 'YER'                          # originally IsoCurrencyCode.YER
CurrencyCode.ZAR = 'ZAR'                          # originally IsoCurrencyCode.ZAR
CurrencyCode.ZMK = 'ZMK'                          # originally IsoCurrencyCode.ZMK
CurrencyCode.ZWL = 'ZWL'                          # originally IsoCurrencyCode.ZWL
CurrencyCode.CYP = 'CYP'                          # originally DeprecatedCurrencyCode.CYP
CurrencyCode.EEK = 'EEK'                          # originally DeprecatedCurrencyCode.EEK
CurrencyCode.MTL = 'MTL'                          # originally DeprecatedCurrencyCode.MTL
CurrencyCode.ROL = 'ROL'                          # originally DeprecatedCurrencyCode.ROL
CurrencyCode.SIT = 'SIT'                          # originally DeprecatedCurrencyCode.SIT
CurrencyCode.SKK = 'SKK'                          # originally DeprecatedCurrencyCode.SKK
CurrencyCode._InitializeFacetMap(CurrencyCode._CF_enumeration,
   CurrencyCode._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'CurrencyCode', CurrencyCode)

# Union simple type: {http://ddex.net/xml/avs/avs}CurrentTerritoryCode
# superclasses pyxb.binding.datatypes.anySimpleType
class CurrentTerritoryCode (pyxb.binding.basis.STD_union):

    """A code representing a Territory. This includes ISO 3166-1 two-letter codes, CISAC TIS codes, plus a code for Worldwide."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CurrentTerritoryCode')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 1504, 3)
    _Documentation = 'A code representing a Territory. This includes ISO 3166-1 two-letter codes, CISAC TIS codes, plus a code for Worldwide.'

    _MemberTypes = ( IsoTerritoryCode, TisTerritoryCode, DdexTerritoryCode, )
CurrentTerritoryCode._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CurrentTerritoryCode)
CurrentTerritoryCode._CF_pattern = pyxb.binding.facets.CF_pattern()
CurrentTerritoryCode.AD = 'AD'                    # originally IsoTerritoryCode.AD
CurrentTerritoryCode.AE = 'AE'                    # originally IsoTerritoryCode.AE
CurrentTerritoryCode.AF = 'AF'                    # originally IsoTerritoryCode.AF
CurrentTerritoryCode.AG = 'AG'                    # originally IsoTerritoryCode.AG
CurrentTerritoryCode.AI = 'AI'                    # originally IsoTerritoryCode.AI
CurrentTerritoryCode.AL = 'AL'                    # originally IsoTerritoryCode.AL
CurrentTerritoryCode.AM = 'AM'                    # originally IsoTerritoryCode.AM
CurrentTerritoryCode.AN = 'AN'                    # originally IsoTerritoryCode.AN
CurrentTerritoryCode.AO = 'AO'                    # originally IsoTerritoryCode.AO
CurrentTerritoryCode.AQ = 'AQ'                    # originally IsoTerritoryCode.AQ
CurrentTerritoryCode.AR = 'AR'                    # originally IsoTerritoryCode.AR
CurrentTerritoryCode.AS = 'AS'                    # originally IsoTerritoryCode.AS
CurrentTerritoryCode.AT = 'AT'                    # originally IsoTerritoryCode.AT
CurrentTerritoryCode.AU = 'AU'                    # originally IsoTerritoryCode.AU
CurrentTerritoryCode.AW = 'AW'                    # originally IsoTerritoryCode.AW
CurrentTerritoryCode.AX = 'AX'                    # originally IsoTerritoryCode.AX
CurrentTerritoryCode.AZ = 'AZ'                    # originally IsoTerritoryCode.AZ
CurrentTerritoryCode.BA = 'BA'                    # originally IsoTerritoryCode.BA
CurrentTerritoryCode.BB = 'BB'                    # originally IsoTerritoryCode.BB
CurrentTerritoryCode.BD = 'BD'                    # originally IsoTerritoryCode.BD
CurrentTerritoryCode.BE = 'BE'                    # originally IsoTerritoryCode.BE
CurrentTerritoryCode.BF = 'BF'                    # originally IsoTerritoryCode.BF
CurrentTerritoryCode.BG = 'BG'                    # originally IsoTerritoryCode.BG
CurrentTerritoryCode.BH = 'BH'                    # originally IsoTerritoryCode.BH
CurrentTerritoryCode.BI = 'BI'                    # originally IsoTerritoryCode.BI
CurrentTerritoryCode.BJ = 'BJ'                    # originally IsoTerritoryCode.BJ
CurrentTerritoryCode.BL = 'BL'                    # originally IsoTerritoryCode.BL
CurrentTerritoryCode.BM = 'BM'                    # originally IsoTerritoryCode.BM
CurrentTerritoryCode.BN = 'BN'                    # originally IsoTerritoryCode.BN
CurrentTerritoryCode.BO = 'BO'                    # originally IsoTerritoryCode.BO
CurrentTerritoryCode.BQ = 'BQ'                    # originally IsoTerritoryCode.BQ
CurrentTerritoryCode.BR = 'BR'                    # originally IsoTerritoryCode.BR
CurrentTerritoryCode.BS = 'BS'                    # originally IsoTerritoryCode.BS
CurrentTerritoryCode.BT = 'BT'                    # originally IsoTerritoryCode.BT
CurrentTerritoryCode.BV = 'BV'                    # originally IsoTerritoryCode.BV
CurrentTerritoryCode.BW = 'BW'                    # originally IsoTerritoryCode.BW
CurrentTerritoryCode.BY = 'BY'                    # originally IsoTerritoryCode.BY
CurrentTerritoryCode.BZ = 'BZ'                    # originally IsoTerritoryCode.BZ
CurrentTerritoryCode.CA = 'CA'                    # originally IsoTerritoryCode.CA
CurrentTerritoryCode.CC = 'CC'                    # originally IsoTerritoryCode.CC
CurrentTerritoryCode.CD = 'CD'                    # originally IsoTerritoryCode.CD
CurrentTerritoryCode.CF = 'CF'                    # originally IsoTerritoryCode.CF
CurrentTerritoryCode.CG = 'CG'                    # originally IsoTerritoryCode.CG
CurrentTerritoryCode.CH = 'CH'                    # originally IsoTerritoryCode.CH
CurrentTerritoryCode.CI = 'CI'                    # originally IsoTerritoryCode.CI
CurrentTerritoryCode.CK = 'CK'                    # originally IsoTerritoryCode.CK
CurrentTerritoryCode.CL = 'CL'                    # originally IsoTerritoryCode.CL
CurrentTerritoryCode.CM = 'CM'                    # originally IsoTerritoryCode.CM
CurrentTerritoryCode.CN = 'CN'                    # originally IsoTerritoryCode.CN
CurrentTerritoryCode.CO = 'CO'                    # originally IsoTerritoryCode.CO
CurrentTerritoryCode.CR = 'CR'                    # originally IsoTerritoryCode.CR
CurrentTerritoryCode.CS = 'CS'                    # originally IsoTerritoryCode.CS
CurrentTerritoryCode.CU = 'CU'                    # originally IsoTerritoryCode.CU
CurrentTerritoryCode.CV = 'CV'                    # originally IsoTerritoryCode.CV
CurrentTerritoryCode.CW = 'CW'                    # originally IsoTerritoryCode.CW
CurrentTerritoryCode.CX = 'CX'                    # originally IsoTerritoryCode.CX
CurrentTerritoryCode.CY = 'CY'                    # originally IsoTerritoryCode.CY
CurrentTerritoryCode.CZ = 'CZ'                    # originally IsoTerritoryCode.CZ
CurrentTerritoryCode.DE = 'DE'                    # originally IsoTerritoryCode.DE
CurrentTerritoryCode.DJ = 'DJ'                    # originally IsoTerritoryCode.DJ
CurrentTerritoryCode.DK = 'DK'                    # originally IsoTerritoryCode.DK
CurrentTerritoryCode.DM = 'DM'                    # originally IsoTerritoryCode.DM
CurrentTerritoryCode.DO = 'DO'                    # originally IsoTerritoryCode.DO
CurrentTerritoryCode.DZ = 'DZ'                    # originally IsoTerritoryCode.DZ
CurrentTerritoryCode.EC = 'EC'                    # originally IsoTerritoryCode.EC
CurrentTerritoryCode.EE = 'EE'                    # originally IsoTerritoryCode.EE
CurrentTerritoryCode.EG = 'EG'                    # originally IsoTerritoryCode.EG
CurrentTerritoryCode.EH = 'EH'                    # originally IsoTerritoryCode.EH
CurrentTerritoryCode.ER = 'ER'                    # originally IsoTerritoryCode.ER
CurrentTerritoryCode.ES = 'ES'                    # originally IsoTerritoryCode.ES
CurrentTerritoryCode.ET = 'ET'                    # originally IsoTerritoryCode.ET
CurrentTerritoryCode.FI = 'FI'                    # originally IsoTerritoryCode.FI
CurrentTerritoryCode.FJ = 'FJ'                    # originally IsoTerritoryCode.FJ
CurrentTerritoryCode.FK = 'FK'                    # originally IsoTerritoryCode.FK
CurrentTerritoryCode.FM = 'FM'                    # originally IsoTerritoryCode.FM
CurrentTerritoryCode.FO = 'FO'                    # originally IsoTerritoryCode.FO
CurrentTerritoryCode.FR = 'FR'                    # originally IsoTerritoryCode.FR
CurrentTerritoryCode.GA = 'GA'                    # originally IsoTerritoryCode.GA
CurrentTerritoryCode.GB = 'GB'                    # originally IsoTerritoryCode.GB
CurrentTerritoryCode.GD = 'GD'                    # originally IsoTerritoryCode.GD
CurrentTerritoryCode.GE = 'GE'                    # originally IsoTerritoryCode.GE
CurrentTerritoryCode.GF = 'GF'                    # originally IsoTerritoryCode.GF
CurrentTerritoryCode.GG = 'GG'                    # originally IsoTerritoryCode.GG
CurrentTerritoryCode.GH = 'GH'                    # originally IsoTerritoryCode.GH
CurrentTerritoryCode.GI = 'GI'                    # originally IsoTerritoryCode.GI
CurrentTerritoryCode.GL = 'GL'                    # originally IsoTerritoryCode.GL
CurrentTerritoryCode.GM = 'GM'                    # originally IsoTerritoryCode.GM
CurrentTerritoryCode.GN = 'GN'                    # originally IsoTerritoryCode.GN
CurrentTerritoryCode.GP = 'GP'                    # originally IsoTerritoryCode.GP
CurrentTerritoryCode.GQ = 'GQ'                    # originally IsoTerritoryCode.GQ
CurrentTerritoryCode.GR = 'GR'                    # originally IsoTerritoryCode.GR
CurrentTerritoryCode.GS = 'GS'                    # originally IsoTerritoryCode.GS
CurrentTerritoryCode.GT = 'GT'                    # originally IsoTerritoryCode.GT
CurrentTerritoryCode.GU = 'GU'                    # originally IsoTerritoryCode.GU
CurrentTerritoryCode.GW = 'GW'                    # originally IsoTerritoryCode.GW
CurrentTerritoryCode.GY = 'GY'                    # originally IsoTerritoryCode.GY
CurrentTerritoryCode.HK = 'HK'                    # originally IsoTerritoryCode.HK
CurrentTerritoryCode.HM = 'HM'                    # originally IsoTerritoryCode.HM
CurrentTerritoryCode.HN = 'HN'                    # originally IsoTerritoryCode.HN
CurrentTerritoryCode.HR = 'HR'                    # originally IsoTerritoryCode.HR
CurrentTerritoryCode.HT = 'HT'                    # originally IsoTerritoryCode.HT
CurrentTerritoryCode.HU = 'HU'                    # originally IsoTerritoryCode.HU
CurrentTerritoryCode.ID = 'ID'                    # originally IsoTerritoryCode.ID
CurrentTerritoryCode.IE = 'IE'                    # originally IsoTerritoryCode.IE
CurrentTerritoryCode.IL = 'IL'                    # originally IsoTerritoryCode.IL
CurrentTerritoryCode.IM = 'IM'                    # originally IsoTerritoryCode.IM
CurrentTerritoryCode.IN = 'IN'                    # originally IsoTerritoryCode.IN
CurrentTerritoryCode.IO = 'IO'                    # originally IsoTerritoryCode.IO
CurrentTerritoryCode.IQ = 'IQ'                    # originally IsoTerritoryCode.IQ
CurrentTerritoryCode.IR = 'IR'                    # originally IsoTerritoryCode.IR
CurrentTerritoryCode.IS = 'IS'                    # originally IsoTerritoryCode.IS
CurrentTerritoryCode.IT = 'IT'                    # originally IsoTerritoryCode.IT
CurrentTerritoryCode.JE = 'JE'                    # originally IsoTerritoryCode.JE
CurrentTerritoryCode.JM = 'JM'                    # originally IsoTerritoryCode.JM
CurrentTerritoryCode.JO = 'JO'                    # originally IsoTerritoryCode.JO
CurrentTerritoryCode.JP = 'JP'                    # originally IsoTerritoryCode.JP
CurrentTerritoryCode.KE = 'KE'                    # originally IsoTerritoryCode.KE
CurrentTerritoryCode.KG = 'KG'                    # originally IsoTerritoryCode.KG
CurrentTerritoryCode.KH = 'KH'                    # originally IsoTerritoryCode.KH
CurrentTerritoryCode.KI = 'KI'                    # originally IsoTerritoryCode.KI
CurrentTerritoryCode.KM = 'KM'                    # originally IsoTerritoryCode.KM
CurrentTerritoryCode.KN = 'KN'                    # originally IsoTerritoryCode.KN
CurrentTerritoryCode.KP = 'KP'                    # originally IsoTerritoryCode.KP
CurrentTerritoryCode.KR = 'KR'                    # originally IsoTerritoryCode.KR
CurrentTerritoryCode.KW = 'KW'                    # originally IsoTerritoryCode.KW
CurrentTerritoryCode.KY = 'KY'                    # originally IsoTerritoryCode.KY
CurrentTerritoryCode.KZ = 'KZ'                    # originally IsoTerritoryCode.KZ
CurrentTerritoryCode.LA = 'LA'                    # originally IsoTerritoryCode.LA
CurrentTerritoryCode.LB = 'LB'                    # originally IsoTerritoryCode.LB
CurrentTerritoryCode.LC = 'LC'                    # originally IsoTerritoryCode.LC
CurrentTerritoryCode.LI = 'LI'                    # originally IsoTerritoryCode.LI
CurrentTerritoryCode.LK = 'LK'                    # originally IsoTerritoryCode.LK
CurrentTerritoryCode.LR = 'LR'                    # originally IsoTerritoryCode.LR
CurrentTerritoryCode.LS = 'LS'                    # originally IsoTerritoryCode.LS
CurrentTerritoryCode.LT = 'LT'                    # originally IsoTerritoryCode.LT
CurrentTerritoryCode.LU = 'LU'                    # originally IsoTerritoryCode.LU
CurrentTerritoryCode.LV = 'LV'                    # originally IsoTerritoryCode.LV
CurrentTerritoryCode.LY = 'LY'                    # originally IsoTerritoryCode.LY
CurrentTerritoryCode.MA = 'MA'                    # originally IsoTerritoryCode.MA
CurrentTerritoryCode.MC = 'MC'                    # originally IsoTerritoryCode.MC
CurrentTerritoryCode.MD = 'MD'                    # originally IsoTerritoryCode.MD
CurrentTerritoryCode.ME = 'ME'                    # originally IsoTerritoryCode.ME
CurrentTerritoryCode.MF = 'MF'                    # originally IsoTerritoryCode.MF
CurrentTerritoryCode.MG = 'MG'                    # originally IsoTerritoryCode.MG
CurrentTerritoryCode.MH = 'MH'                    # originally IsoTerritoryCode.MH
CurrentTerritoryCode.MK = 'MK'                    # originally IsoTerritoryCode.MK
CurrentTerritoryCode.ML = 'ML'                    # originally IsoTerritoryCode.ML
CurrentTerritoryCode.MM = 'MM'                    # originally IsoTerritoryCode.MM
CurrentTerritoryCode.MN = 'MN'                    # originally IsoTerritoryCode.MN
CurrentTerritoryCode.MO = 'MO'                    # originally IsoTerritoryCode.MO
CurrentTerritoryCode.MP = 'MP'                    # originally IsoTerritoryCode.MP
CurrentTerritoryCode.MQ = 'MQ'                    # originally IsoTerritoryCode.MQ
CurrentTerritoryCode.MR = 'MR'                    # originally IsoTerritoryCode.MR
CurrentTerritoryCode.MS = 'MS'                    # originally IsoTerritoryCode.MS
CurrentTerritoryCode.MT = 'MT'                    # originally IsoTerritoryCode.MT
CurrentTerritoryCode.MU = 'MU'                    # originally IsoTerritoryCode.MU
CurrentTerritoryCode.MV = 'MV'                    # originally IsoTerritoryCode.MV
CurrentTerritoryCode.MW = 'MW'                    # originally IsoTerritoryCode.MW
CurrentTerritoryCode.MX = 'MX'                    # originally IsoTerritoryCode.MX
CurrentTerritoryCode.MY = 'MY'                    # originally IsoTerritoryCode.MY
CurrentTerritoryCode.MZ = 'MZ'                    # originally IsoTerritoryCode.MZ
CurrentTerritoryCode.NA = 'NA'                    # originally IsoTerritoryCode.NA
CurrentTerritoryCode.NC = 'NC'                    # originally IsoTerritoryCode.NC
CurrentTerritoryCode.NE = 'NE'                    # originally IsoTerritoryCode.NE
CurrentTerritoryCode.NF = 'NF'                    # originally IsoTerritoryCode.NF
CurrentTerritoryCode.NG = 'NG'                    # originally IsoTerritoryCode.NG
CurrentTerritoryCode.NI = 'NI'                    # originally IsoTerritoryCode.NI
CurrentTerritoryCode.NL = 'NL'                    # originally IsoTerritoryCode.NL
CurrentTerritoryCode.NO = 'NO'                    # originally IsoTerritoryCode.NO
CurrentTerritoryCode.NP = 'NP'                    # originally IsoTerritoryCode.NP
CurrentTerritoryCode.NR = 'NR'                    # originally IsoTerritoryCode.NR
CurrentTerritoryCode.NU = 'NU'                    # originally IsoTerritoryCode.NU
CurrentTerritoryCode.NZ = 'NZ'                    # originally IsoTerritoryCode.NZ
CurrentTerritoryCode.OM = 'OM'                    # originally IsoTerritoryCode.OM
CurrentTerritoryCode.PA = 'PA'                    # originally IsoTerritoryCode.PA
CurrentTerritoryCode.PE = 'PE'                    # originally IsoTerritoryCode.PE
CurrentTerritoryCode.PF = 'PF'                    # originally IsoTerritoryCode.PF
CurrentTerritoryCode.PG = 'PG'                    # originally IsoTerritoryCode.PG
CurrentTerritoryCode.PH = 'PH'                    # originally IsoTerritoryCode.PH
CurrentTerritoryCode.PK = 'PK'                    # originally IsoTerritoryCode.PK
CurrentTerritoryCode.PL = 'PL'                    # originally IsoTerritoryCode.PL
CurrentTerritoryCode.PM = 'PM'                    # originally IsoTerritoryCode.PM
CurrentTerritoryCode.PN = 'PN'                    # originally IsoTerritoryCode.PN
CurrentTerritoryCode.PR = 'PR'                    # originally IsoTerritoryCode.PR
CurrentTerritoryCode.PS = 'PS'                    # originally IsoTerritoryCode.PS
CurrentTerritoryCode.PT = 'PT'                    # originally IsoTerritoryCode.PT
CurrentTerritoryCode.PW = 'PW'                    # originally IsoTerritoryCode.PW
CurrentTerritoryCode.PY = 'PY'                    # originally IsoTerritoryCode.PY
CurrentTerritoryCode.QA = 'QA'                    # originally IsoTerritoryCode.QA
CurrentTerritoryCode.RE = 'RE'                    # originally IsoTerritoryCode.RE
CurrentTerritoryCode.RO = 'RO'                    # originally IsoTerritoryCode.RO
CurrentTerritoryCode.RS = 'RS'                    # originally IsoTerritoryCode.RS
CurrentTerritoryCode.RU = 'RU'                    # originally IsoTerritoryCode.RU
CurrentTerritoryCode.RW = 'RW'                    # originally IsoTerritoryCode.RW
CurrentTerritoryCode.SA = 'SA'                    # originally IsoTerritoryCode.SA
CurrentTerritoryCode.SB = 'SB'                    # originally IsoTerritoryCode.SB
CurrentTerritoryCode.SC = 'SC'                    # originally IsoTerritoryCode.SC
CurrentTerritoryCode.SD = 'SD'                    # originally IsoTerritoryCode.SD
CurrentTerritoryCode.SE = 'SE'                    # originally IsoTerritoryCode.SE
CurrentTerritoryCode.SG = 'SG'                    # originally IsoTerritoryCode.SG
CurrentTerritoryCode.SH = 'SH'                    # originally IsoTerritoryCode.SH
CurrentTerritoryCode.SI = 'SI'                    # originally IsoTerritoryCode.SI
CurrentTerritoryCode.SJ = 'SJ'                    # originally IsoTerritoryCode.SJ
CurrentTerritoryCode.SK = 'SK'                    # originally IsoTerritoryCode.SK
CurrentTerritoryCode.SL = 'SL'                    # originally IsoTerritoryCode.SL
CurrentTerritoryCode.SM = 'SM'                    # originally IsoTerritoryCode.SM
CurrentTerritoryCode.SN = 'SN'                    # originally IsoTerritoryCode.SN
CurrentTerritoryCode.SO = 'SO'                    # originally IsoTerritoryCode.SO
CurrentTerritoryCode.SR = 'SR'                    # originally IsoTerritoryCode.SR
CurrentTerritoryCode.SS = 'SS'                    # originally IsoTerritoryCode.SS
CurrentTerritoryCode.ST = 'ST'                    # originally IsoTerritoryCode.ST
CurrentTerritoryCode.SV = 'SV'                    # originally IsoTerritoryCode.SV
CurrentTerritoryCode.SX = 'SX'                    # originally IsoTerritoryCode.SX
CurrentTerritoryCode.SY = 'SY'                    # originally IsoTerritoryCode.SY
CurrentTerritoryCode.SZ = 'SZ'                    # originally IsoTerritoryCode.SZ
CurrentTerritoryCode.TC = 'TC'                    # originally IsoTerritoryCode.TC
CurrentTerritoryCode.TD = 'TD'                    # originally IsoTerritoryCode.TD
CurrentTerritoryCode.TF = 'TF'                    # originally IsoTerritoryCode.TF
CurrentTerritoryCode.TG = 'TG'                    # originally IsoTerritoryCode.TG
CurrentTerritoryCode.TH = 'TH'                    # originally IsoTerritoryCode.TH
CurrentTerritoryCode.TJ = 'TJ'                    # originally IsoTerritoryCode.TJ
CurrentTerritoryCode.TK = 'TK'                    # originally IsoTerritoryCode.TK
CurrentTerritoryCode.TL = 'TL'                    # originally IsoTerritoryCode.TL
CurrentTerritoryCode.TM = 'TM'                    # originally IsoTerritoryCode.TM
CurrentTerritoryCode.TN = 'TN'                    # originally IsoTerritoryCode.TN
CurrentTerritoryCode.TO = 'TO'                    # originally IsoTerritoryCode.TO
CurrentTerritoryCode.TR = 'TR'                    # originally IsoTerritoryCode.TR
CurrentTerritoryCode.TT = 'TT'                    # originally IsoTerritoryCode.TT
CurrentTerritoryCode.TV = 'TV'                    # originally IsoTerritoryCode.TV
CurrentTerritoryCode.TW = 'TW'                    # originally IsoTerritoryCode.TW
CurrentTerritoryCode.TZ = 'TZ'                    # originally IsoTerritoryCode.TZ
CurrentTerritoryCode.UA = 'UA'                    # originally IsoTerritoryCode.UA
CurrentTerritoryCode.UG = 'UG'                    # originally IsoTerritoryCode.UG
CurrentTerritoryCode.UM = 'UM'                    # originally IsoTerritoryCode.UM
CurrentTerritoryCode.US = 'US'                    # originally IsoTerritoryCode.US
CurrentTerritoryCode.UY = 'UY'                    # originally IsoTerritoryCode.UY
CurrentTerritoryCode.UZ = 'UZ'                    # originally IsoTerritoryCode.UZ
CurrentTerritoryCode.VA = 'VA'                    # originally IsoTerritoryCode.VA
CurrentTerritoryCode.VC = 'VC'                    # originally IsoTerritoryCode.VC
CurrentTerritoryCode.VE = 'VE'                    # originally IsoTerritoryCode.VE
CurrentTerritoryCode.VG = 'VG'                    # originally IsoTerritoryCode.VG
CurrentTerritoryCode.VI = 'VI'                    # originally IsoTerritoryCode.VI
CurrentTerritoryCode.VN = 'VN'                    # originally IsoTerritoryCode.VN
CurrentTerritoryCode.VU = 'VU'                    # originally IsoTerritoryCode.VU
CurrentTerritoryCode.WF = 'WF'                    # originally IsoTerritoryCode.WF
CurrentTerritoryCode.WS = 'WS'                    # originally IsoTerritoryCode.WS
CurrentTerritoryCode.YE = 'YE'                    # originally IsoTerritoryCode.YE
CurrentTerritoryCode.YT = 'YT'                    # originally IsoTerritoryCode.YT
CurrentTerritoryCode.ZA = 'ZA'                    # originally IsoTerritoryCode.ZA
CurrentTerritoryCode.ZM = 'ZM'                    # originally IsoTerritoryCode.ZM
CurrentTerritoryCode.ZW = 'ZW'                    # originally IsoTerritoryCode.ZW
CurrentTerritoryCode.n4 = '4'                     # originally TisTerritoryCode.n4
CurrentTerritoryCode.n8 = '8'                     # originally TisTerritoryCode.n8
CurrentTerritoryCode.n12 = '12'                   # originally TisTerritoryCode.n12
CurrentTerritoryCode.n20 = '20'                   # originally TisTerritoryCode.n20
CurrentTerritoryCode.n24 = '24'                   # originally TisTerritoryCode.n24
CurrentTerritoryCode.n28 = '28'                   # originally TisTerritoryCode.n28
CurrentTerritoryCode.n31 = '31'                   # originally TisTerritoryCode.n31
CurrentTerritoryCode.n32 = '32'                   # originally TisTerritoryCode.n32
CurrentTerritoryCode.n36 = '36'                   # originally TisTerritoryCode.n36
CurrentTerritoryCode.n40 = '40'                   # originally TisTerritoryCode.n40
CurrentTerritoryCode.n44 = '44'                   # originally TisTerritoryCode.n44
CurrentTerritoryCode.n48 = '48'                   # originally TisTerritoryCode.n48
CurrentTerritoryCode.n50 = '50'                   # originally TisTerritoryCode.n50
CurrentTerritoryCode.n51 = '51'                   # originally TisTerritoryCode.n51
CurrentTerritoryCode.n52 = '52'                   # originally TisTerritoryCode.n52
CurrentTerritoryCode.n56 = '56'                   # originally TisTerritoryCode.n56
CurrentTerritoryCode.n64 = '64'                   # originally TisTerritoryCode.n64
CurrentTerritoryCode.n68 = '68'                   # originally TisTerritoryCode.n68
CurrentTerritoryCode.n70 = '70'                   # originally TisTerritoryCode.n70
CurrentTerritoryCode.n72 = '72'                   # originally TisTerritoryCode.n72
CurrentTerritoryCode.n76 = '76'                   # originally TisTerritoryCode.n76
CurrentTerritoryCode.n84 = '84'                   # originally TisTerritoryCode.n84
CurrentTerritoryCode.n90 = '90'                   # originally TisTerritoryCode.n90
CurrentTerritoryCode.n96 = '96'                   # originally TisTerritoryCode.n96
CurrentTerritoryCode.n100 = '100'                 # originally TisTerritoryCode.n100
CurrentTerritoryCode.n104 = '104'                 # originally TisTerritoryCode.n104
CurrentTerritoryCode.n108 = '108'                 # originally TisTerritoryCode.n108
CurrentTerritoryCode.n112 = '112'                 # originally TisTerritoryCode.n112
CurrentTerritoryCode.n116 = '116'                 # originally TisTerritoryCode.n116
CurrentTerritoryCode.n120 = '120'                 # originally TisTerritoryCode.n120
CurrentTerritoryCode.n124 = '124'                 # originally TisTerritoryCode.n124
CurrentTerritoryCode.n132 = '132'                 # originally TisTerritoryCode.n132
CurrentTerritoryCode.n140 = '140'                 # originally TisTerritoryCode.n140
CurrentTerritoryCode.n144 = '144'                 # originally TisTerritoryCode.n144
CurrentTerritoryCode.n148 = '148'                 # originally TisTerritoryCode.n148
CurrentTerritoryCode.n152 = '152'                 # originally TisTerritoryCode.n152
CurrentTerritoryCode.n156 = '156'                 # originally TisTerritoryCode.n156
CurrentTerritoryCode.n158 = '158'                 # originally TisTerritoryCode.n158
CurrentTerritoryCode.n170 = '170'                 # originally TisTerritoryCode.n170
CurrentTerritoryCode.n174 = '174'                 # originally TisTerritoryCode.n174
CurrentTerritoryCode.n178 = '178'                 # originally TisTerritoryCode.n178
CurrentTerritoryCode.n180 = '180'                 # originally TisTerritoryCode.n180
CurrentTerritoryCode.n188 = '188'                 # originally TisTerritoryCode.n188
CurrentTerritoryCode.n191 = '191'                 # originally TisTerritoryCode.n191
CurrentTerritoryCode.n192 = '192'                 # originally TisTerritoryCode.n192
CurrentTerritoryCode.n196 = '196'                 # originally TisTerritoryCode.n196
CurrentTerritoryCode.n200 = '200'                 # originally TisTerritoryCode.n200
CurrentTerritoryCode.n203 = '203'                 # originally TisTerritoryCode.n203
CurrentTerritoryCode.n204 = '204'                 # originally TisTerritoryCode.n204
CurrentTerritoryCode.n208 = '208'                 # originally TisTerritoryCode.n208
CurrentTerritoryCode.n212 = '212'                 # originally TisTerritoryCode.n212
CurrentTerritoryCode.n214 = '214'                 # originally TisTerritoryCode.n214
CurrentTerritoryCode.n218 = '218'                 # originally TisTerritoryCode.n218
CurrentTerritoryCode.n222 = '222'                 # originally TisTerritoryCode.n222
CurrentTerritoryCode.n226 = '226'                 # originally TisTerritoryCode.n226
CurrentTerritoryCode.n230 = '230'                 # originally TisTerritoryCode.n230
CurrentTerritoryCode.n231 = '231'                 # originally TisTerritoryCode.n231
CurrentTerritoryCode.n232 = '232'                 # originally TisTerritoryCode.n232
CurrentTerritoryCode.n233 = '233'                 # originally TisTerritoryCode.n233
CurrentTerritoryCode.n242 = '242'                 # originally TisTerritoryCode.n242
CurrentTerritoryCode.n246 = '246'                 # originally TisTerritoryCode.n246
CurrentTerritoryCode.n250 = '250'                 # originally TisTerritoryCode.n250
CurrentTerritoryCode.n258 = '258'                 # originally TisTerritoryCode.n258
CurrentTerritoryCode.n262 = '262'                 # originally TisTerritoryCode.n262
CurrentTerritoryCode.n266 = '266'                 # originally TisTerritoryCode.n266
CurrentTerritoryCode.n268 = '268'                 # originally TisTerritoryCode.n268
CurrentTerritoryCode.n270 = '270'                 # originally TisTerritoryCode.n270
CurrentTerritoryCode.n276 = '276'                 # originally TisTerritoryCode.n276
CurrentTerritoryCode.n278 = '278'                 # originally TisTerritoryCode.n278
CurrentTerritoryCode.n280 = '280'                 # originally TisTerritoryCode.n280
CurrentTerritoryCode.n288 = '288'                 # originally TisTerritoryCode.n288
CurrentTerritoryCode.n296 = '296'                 # originally TisTerritoryCode.n296
CurrentTerritoryCode.n300 = '300'                 # originally TisTerritoryCode.n300
CurrentTerritoryCode.n308 = '308'                 # originally TisTerritoryCode.n308
CurrentTerritoryCode.n320 = '320'                 # originally TisTerritoryCode.n320
CurrentTerritoryCode.n324 = '324'                 # originally TisTerritoryCode.n324
CurrentTerritoryCode.n328 = '328'                 # originally TisTerritoryCode.n328
CurrentTerritoryCode.n332 = '332'                 # originally TisTerritoryCode.n332
CurrentTerritoryCode.n336 = '336'                 # originally TisTerritoryCode.n336
CurrentTerritoryCode.n340 = '340'                 # originally TisTerritoryCode.n340
CurrentTerritoryCode.n344 = '344'                 # originally TisTerritoryCode.n344
CurrentTerritoryCode.n348 = '348'                 # originally TisTerritoryCode.n348
CurrentTerritoryCode.n352 = '352'                 # originally TisTerritoryCode.n352
CurrentTerritoryCode.n356 = '356'                 # originally TisTerritoryCode.n356
CurrentTerritoryCode.n360 = '360'                 # originally TisTerritoryCode.n360
CurrentTerritoryCode.n364 = '364'                 # originally TisTerritoryCode.n364
CurrentTerritoryCode.n368 = '368'                 # originally TisTerritoryCode.n368
CurrentTerritoryCode.n372 = '372'                 # originally TisTerritoryCode.n372
CurrentTerritoryCode.n376 = '376'                 # originally TisTerritoryCode.n376
CurrentTerritoryCode.n380 = '380'                 # originally TisTerritoryCode.n380
CurrentTerritoryCode.n384 = '384'                 # originally TisTerritoryCode.n384
CurrentTerritoryCode.n388 = '388'                 # originally TisTerritoryCode.n388
CurrentTerritoryCode.n392 = '392'                 # originally TisTerritoryCode.n392
CurrentTerritoryCode.n398 = '398'                 # originally TisTerritoryCode.n398
CurrentTerritoryCode.n400 = '400'                 # originally TisTerritoryCode.n400
CurrentTerritoryCode.n404 = '404'                 # originally TisTerritoryCode.n404
CurrentTerritoryCode.n408 = '408'                 # originally TisTerritoryCode.n408
CurrentTerritoryCode.n410 = '410'                 # originally TisTerritoryCode.n410
CurrentTerritoryCode.n414 = '414'                 # originally TisTerritoryCode.n414
CurrentTerritoryCode.n417 = '417'                 # originally TisTerritoryCode.n417
CurrentTerritoryCode.n418 = '418'                 # originally TisTerritoryCode.n418
CurrentTerritoryCode.n422 = '422'                 # originally TisTerritoryCode.n422
CurrentTerritoryCode.n426 = '426'                 # originally TisTerritoryCode.n426
CurrentTerritoryCode.n428 = '428'                 # originally TisTerritoryCode.n428
CurrentTerritoryCode.n430 = '430'                 # originally TisTerritoryCode.n430
CurrentTerritoryCode.n434 = '434'                 # originally TisTerritoryCode.n434
CurrentTerritoryCode.n438 = '438'                 # originally TisTerritoryCode.n438
CurrentTerritoryCode.n440 = '440'                 # originally TisTerritoryCode.n440
CurrentTerritoryCode.n442 = '442'                 # originally TisTerritoryCode.n442
CurrentTerritoryCode.n450 = '450'                 # originally TisTerritoryCode.n450
CurrentTerritoryCode.n454 = '454'                 # originally TisTerritoryCode.n454
CurrentTerritoryCode.n458 = '458'                 # originally TisTerritoryCode.n458
CurrentTerritoryCode.n462 = '462'                 # originally TisTerritoryCode.n462
CurrentTerritoryCode.n466 = '466'                 # originally TisTerritoryCode.n466
CurrentTerritoryCode.n470 = '470'                 # originally TisTerritoryCode.n470
CurrentTerritoryCode.n478 = '478'                 # originally TisTerritoryCode.n478
CurrentTerritoryCode.n480 = '480'                 # originally TisTerritoryCode.n480
CurrentTerritoryCode.n484 = '484'                 # originally TisTerritoryCode.n484
CurrentTerritoryCode.n492 = '492'                 # originally TisTerritoryCode.n492
CurrentTerritoryCode.n496 = '496'                 # originally TisTerritoryCode.n496
CurrentTerritoryCode.n498 = '498'                 # originally TisTerritoryCode.n498
CurrentTerritoryCode.n499 = '499'                 # originally TisTerritoryCode.n499
CurrentTerritoryCode.n504 = '504'                 # originally TisTerritoryCode.n504
CurrentTerritoryCode.n508 = '508'                 # originally TisTerritoryCode.n508
CurrentTerritoryCode.n512 = '512'                 # originally TisTerritoryCode.n512
CurrentTerritoryCode.n516 = '516'                 # originally TisTerritoryCode.n516
CurrentTerritoryCode.n520 = '520'                 # originally TisTerritoryCode.n520
CurrentTerritoryCode.n524 = '524'                 # originally TisTerritoryCode.n524
CurrentTerritoryCode.n528 = '528'                 # originally TisTerritoryCode.n528
CurrentTerritoryCode.n540 = '540'                 # originally TisTerritoryCode.n540
CurrentTerritoryCode.n548 = '548'                 # originally TisTerritoryCode.n548
CurrentTerritoryCode.n554 = '554'                 # originally TisTerritoryCode.n554
CurrentTerritoryCode.n558 = '558'                 # originally TisTerritoryCode.n558
CurrentTerritoryCode.n562 = '562'                 # originally TisTerritoryCode.n562
CurrentTerritoryCode.n566 = '566'                 # originally TisTerritoryCode.n566
CurrentTerritoryCode.n578 = '578'                 # originally TisTerritoryCode.n578
CurrentTerritoryCode.n583 = '583'                 # originally TisTerritoryCode.n583
CurrentTerritoryCode.n584 = '584'                 # originally TisTerritoryCode.n584
CurrentTerritoryCode.n585 = '585'                 # originally TisTerritoryCode.n585
CurrentTerritoryCode.n586 = '586'                 # originally TisTerritoryCode.n586
CurrentTerritoryCode.n591 = '591'                 # originally TisTerritoryCode.n591
CurrentTerritoryCode.n598 = '598'                 # originally TisTerritoryCode.n598
CurrentTerritoryCode.n600 = '600'                 # originally TisTerritoryCode.n600
CurrentTerritoryCode.n604 = '604'                 # originally TisTerritoryCode.n604
CurrentTerritoryCode.n608 = '608'                 # originally TisTerritoryCode.n608
CurrentTerritoryCode.n616 = '616'                 # originally TisTerritoryCode.n616
CurrentTerritoryCode.n620 = '620'                 # originally TisTerritoryCode.n620
CurrentTerritoryCode.n624 = '624'                 # originally TisTerritoryCode.n624
CurrentTerritoryCode.n626 = '626'                 # originally TisTerritoryCode.n626
CurrentTerritoryCode.n630 = '630'                 # originally TisTerritoryCode.n630
CurrentTerritoryCode.n634 = '634'                 # originally TisTerritoryCode.n634
CurrentTerritoryCode.n642 = '642'                 # originally TisTerritoryCode.n642
CurrentTerritoryCode.n643 = '643'                 # originally TisTerritoryCode.n643
CurrentTerritoryCode.n646 = '646'                 # originally TisTerritoryCode.n646
CurrentTerritoryCode.n659 = '659'                 # originally TisTerritoryCode.n659
CurrentTerritoryCode.n662 = '662'                 # originally TisTerritoryCode.n662
CurrentTerritoryCode.n670 = '670'                 # originally TisTerritoryCode.n670
CurrentTerritoryCode.n674 = '674'                 # originally TisTerritoryCode.n674
CurrentTerritoryCode.n678 = '678'                 # originally TisTerritoryCode.n678
CurrentTerritoryCode.n682 = '682'                 # originally TisTerritoryCode.n682
CurrentTerritoryCode.n686 = '686'                 # originally TisTerritoryCode.n686
CurrentTerritoryCode.n688 = '688'                 # originally TisTerritoryCode.n688
CurrentTerritoryCode.n690 = '690'                 # originally TisTerritoryCode.n690
CurrentTerritoryCode.n694 = '694'                 # originally TisTerritoryCode.n694
CurrentTerritoryCode.n702 = '702'                 # originally TisTerritoryCode.n702
CurrentTerritoryCode.n703 = '703'                 # originally TisTerritoryCode.n703
CurrentTerritoryCode.n704 = '704'                 # originally TisTerritoryCode.n704
CurrentTerritoryCode.n705 = '705'                 # originally TisTerritoryCode.n705
CurrentTerritoryCode.n706 = '706'                 # originally TisTerritoryCode.n706
CurrentTerritoryCode.n710 = '710'                 # originally TisTerritoryCode.n710
CurrentTerritoryCode.n716 = '716'                 # originally TisTerritoryCode.n716
CurrentTerritoryCode.n720 = '720'                 # originally TisTerritoryCode.n720
CurrentTerritoryCode.n724 = '724'                 # originally TisTerritoryCode.n724
CurrentTerritoryCode.n728 = '728'                 # originally TisTerritoryCode.n728
CurrentTerritoryCode.n729 = '729'                 # originally TisTerritoryCode.n729
CurrentTerritoryCode.n732 = '732'                 # originally TisTerritoryCode.n732
CurrentTerritoryCode.n736 = '736'                 # originally TisTerritoryCode.n736
CurrentTerritoryCode.n740 = '740'                 # originally TisTerritoryCode.n740
CurrentTerritoryCode.n748 = '748'                 # originally TisTerritoryCode.n748
CurrentTerritoryCode.n752 = '752'                 # originally TisTerritoryCode.n752
CurrentTerritoryCode.n756 = '756'                 # originally TisTerritoryCode.n756
CurrentTerritoryCode.n760 = '760'                 # originally TisTerritoryCode.n760
CurrentTerritoryCode.n762 = '762'                 # originally TisTerritoryCode.n762
CurrentTerritoryCode.n764 = '764'                 # originally TisTerritoryCode.n764
CurrentTerritoryCode.n768 = '768'                 # originally TisTerritoryCode.n768
CurrentTerritoryCode.n776 = '776'                 # originally TisTerritoryCode.n776
CurrentTerritoryCode.n780 = '780'                 # originally TisTerritoryCode.n780
CurrentTerritoryCode.n784 = '784'                 # originally TisTerritoryCode.n784
CurrentTerritoryCode.n788 = '788'                 # originally TisTerritoryCode.n788
CurrentTerritoryCode.n792 = '792'                 # originally TisTerritoryCode.n792
CurrentTerritoryCode.n795 = '795'                 # originally TisTerritoryCode.n795
CurrentTerritoryCode.n798 = '798'                 # originally TisTerritoryCode.n798
CurrentTerritoryCode.n800 = '800'                 # originally TisTerritoryCode.n800
CurrentTerritoryCode.n804 = '804'                 # originally TisTerritoryCode.n804
CurrentTerritoryCode.n807 = '807'                 # originally TisTerritoryCode.n807
CurrentTerritoryCode.n810 = '810'                 # originally TisTerritoryCode.n810
CurrentTerritoryCode.n818 = '818'                 # originally TisTerritoryCode.n818
CurrentTerritoryCode.n826 = '826'                 # originally TisTerritoryCode.n826
CurrentTerritoryCode.n834 = '834'                 # originally TisTerritoryCode.n834
CurrentTerritoryCode.n840 = '840'                 # originally TisTerritoryCode.n840
CurrentTerritoryCode.n854 = '854'                 # originally TisTerritoryCode.n854
CurrentTerritoryCode.n858 = '858'                 # originally TisTerritoryCode.n858
CurrentTerritoryCode.n860 = '860'                 # originally TisTerritoryCode.n860
CurrentTerritoryCode.n862 = '862'                 # originally TisTerritoryCode.n862
CurrentTerritoryCode.n882 = '882'                 # originally TisTerritoryCode.n882
CurrentTerritoryCode.n886 = '886'                 # originally TisTerritoryCode.n886
CurrentTerritoryCode.n887 = '887'                 # originally TisTerritoryCode.n887
CurrentTerritoryCode.n890 = '890'                 # originally TisTerritoryCode.n890
CurrentTerritoryCode.n891 = '891'                 # originally TisTerritoryCode.n891
CurrentTerritoryCode.n894 = '894'                 # originally TisTerritoryCode.n894
CurrentTerritoryCode.n2100 = '2100'               # originally TisTerritoryCode.n2100
CurrentTerritoryCode.n2101 = '2101'               # originally TisTerritoryCode.n2101
CurrentTerritoryCode.n2102 = '2102'               # originally TisTerritoryCode.n2102
CurrentTerritoryCode.n2103 = '2103'               # originally TisTerritoryCode.n2103
CurrentTerritoryCode.n2104 = '2104'               # originally TisTerritoryCode.n2104
CurrentTerritoryCode.n2105 = '2105'               # originally TisTerritoryCode.n2105
CurrentTerritoryCode.n2106 = '2106'               # originally TisTerritoryCode.n2106
CurrentTerritoryCode.n2107 = '2107'               # originally TisTerritoryCode.n2107
CurrentTerritoryCode.n2108 = '2108'               # originally TisTerritoryCode.n2108
CurrentTerritoryCode.n2109 = '2109'               # originally TisTerritoryCode.n2109
CurrentTerritoryCode.n2110 = '2110'               # originally TisTerritoryCode.n2110
CurrentTerritoryCode.n2111 = '2111'               # originally TisTerritoryCode.n2111
CurrentTerritoryCode.n2112 = '2112'               # originally TisTerritoryCode.n2112
CurrentTerritoryCode.n2113 = '2113'               # originally TisTerritoryCode.n2113
CurrentTerritoryCode.n2114 = '2114'               # originally TisTerritoryCode.n2114
CurrentTerritoryCode.n2115 = '2115'               # originally TisTerritoryCode.n2115
CurrentTerritoryCode.n2116 = '2116'               # originally TisTerritoryCode.n2116
CurrentTerritoryCode.n2117 = '2117'               # originally TisTerritoryCode.n2117
CurrentTerritoryCode.n2118 = '2118'               # originally TisTerritoryCode.n2118
CurrentTerritoryCode.n2119 = '2119'               # originally TisTerritoryCode.n2119
CurrentTerritoryCode.n2120 = '2120'               # originally TisTerritoryCode.n2120
CurrentTerritoryCode.n2121 = '2121'               # originally TisTerritoryCode.n2121
CurrentTerritoryCode.n2122 = '2122'               # originally TisTerritoryCode.n2122
CurrentTerritoryCode.n2123 = '2123'               # originally TisTerritoryCode.n2123
CurrentTerritoryCode.n2124 = '2124'               # originally TisTerritoryCode.n2124
CurrentTerritoryCode.n2125 = '2125'               # originally TisTerritoryCode.n2125
CurrentTerritoryCode.n2126 = '2126'               # originally TisTerritoryCode.n2126
CurrentTerritoryCode.n2127 = '2127'               # originally TisTerritoryCode.n2127
CurrentTerritoryCode.n2128 = '2128'               # originally TisTerritoryCode.n2128
CurrentTerritoryCode.n2129 = '2129'               # originally TisTerritoryCode.n2129
CurrentTerritoryCode.n2130 = '2130'               # originally TisTerritoryCode.n2130
CurrentTerritoryCode.n2131 = '2131'               # originally TisTerritoryCode.n2131
CurrentTerritoryCode.n2132 = '2132'               # originally TisTerritoryCode.n2132
CurrentTerritoryCode.n2133 = '2133'               # originally TisTerritoryCode.n2133
CurrentTerritoryCode.n2134 = '2134'               # originally TisTerritoryCode.n2134
CurrentTerritoryCode.n2136 = '2136'               # originally TisTerritoryCode.n2136
CurrentTerritoryCode.Worldwide = 'Worldwide'      # originally DdexTerritoryCode.Worldwide
CurrentTerritoryCode._InitializeFacetMap(CurrentTerritoryCode._CF_enumeration,
   CurrentTerritoryCode._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'CurrentTerritoryCode', CurrentTerritoryCode)

# Union simple type: {http://ddex.net/xml/avs/avs}MusicalWorkContributorRole
# superclasses pyxb.binding.datatypes.anySimpleType
class MusicalWorkContributorRole (pyxb.binding.basis.STD_union):

    """A role played by a Contributor in relation to a MusicalWork."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MusicalWorkContributorRole')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 6271, 3)
    _Documentation = 'A role played by a Contributor in relation to a MusicalWork.'

    _MemberTypes = ( CreativeContributorRole, BusinessContributorRole, )
MusicalWorkContributorRole._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MusicalWorkContributorRole)
MusicalWorkContributorRole._CF_pattern = pyxb.binding.facets.CF_pattern()
MusicalWorkContributorRole.Adapter = 'Adapter'    # originally CreativeContributorRole.Adapter
MusicalWorkContributorRole.Arranger = 'Arranger'  # originally CreativeContributorRole.Arranger
MusicalWorkContributorRole.AssociatedPerformer = 'AssociatedPerformer'# originally CreativeContributorRole.AssociatedPerformer
MusicalWorkContributorRole.Author = 'Author'      # originally CreativeContributorRole.Author
MusicalWorkContributorRole.Composer = 'Composer'  # originally CreativeContributorRole.Composer
MusicalWorkContributorRole.ComposerLyricist = 'ComposerLyricist'# originally CreativeContributorRole.ComposerLyricist
MusicalWorkContributorRole.Librettist = 'Librettist'# originally CreativeContributorRole.Librettist
MusicalWorkContributorRole.Lyricist = 'Lyricist'  # originally CreativeContributorRole.Lyricist
MusicalWorkContributorRole.NonLyricAuthor = 'NonLyricAuthor'# originally CreativeContributorRole.NonLyricAuthor
MusicalWorkContributorRole.SubArranger = 'SubArranger'# originally CreativeContributorRole.SubArranger
MusicalWorkContributorRole.SubLyricist = 'SubLyricist'# originally CreativeContributorRole.SubLyricist
MusicalWorkContributorRole.Translator = 'Translator'# originally CreativeContributorRole.Translator
MusicalWorkContributorRole.Contributor = 'Contributor'# originally BusinessContributorRole.Contributor
MusicalWorkContributorRole.MusicPublisher = 'MusicPublisher'# originally BusinessContributorRole.MusicPublisher
MusicalWorkContributorRole.OriginalPublisher = 'OriginalPublisher'# originally BusinessContributorRole.OriginalPublisher
MusicalWorkContributorRole.SubPublisher = 'SubPublisher'# originally BusinessContributorRole.SubPublisher
MusicalWorkContributorRole.SubstitutedPublisher = 'SubstitutedPublisher'# originally BusinessContributorRole.SubstitutedPublisher
MusicalWorkContributorRole.Unknown = 'Unknown'    # originally BusinessContributorRole.Unknown
MusicalWorkContributorRole.UserDefined = 'UserDefined'# originally BusinessContributorRole.UserDefined
MusicalWorkContributorRole._InitializeFacetMap(MusicalWorkContributorRole._CF_enumeration,
   MusicalWorkContributorRole._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'MusicalWorkContributorRole', MusicalWorkContributorRole)

# Union simple type: {http://ddex.net/xml/avs/avs}TerritoryCode
# superclasses pyxb.binding.datatypes.anySimpleType
class TerritoryCode (pyxb.binding.basis.STD_union):

    """A code representing a Territory. This includes ISO 3166-1 two-letter codes plus a code for Worldwide (This list is included here for compatibility reasons. Current standards use other TerritoryCode lists)."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TerritoryCode')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/avs/avs.xsd', 11251, 3)
    _Documentation = 'A code representing a Territory. This includes ISO 3166-1 two-letter codes plus a code for Worldwide (This list is included here for compatibility reasons. Current standards use other TerritoryCode lists).'

    _MemberTypes = ( IsoTerritoryCode, DdexTerritoryCode, )
TerritoryCode._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TerritoryCode)
TerritoryCode._CF_pattern = pyxb.binding.facets.CF_pattern()
TerritoryCode.AD = 'AD'                           # originally IsoTerritoryCode.AD
TerritoryCode.AE = 'AE'                           # originally IsoTerritoryCode.AE
TerritoryCode.AF = 'AF'                           # originally IsoTerritoryCode.AF
TerritoryCode.AG = 'AG'                           # originally IsoTerritoryCode.AG
TerritoryCode.AI = 'AI'                           # originally IsoTerritoryCode.AI
TerritoryCode.AL = 'AL'                           # originally IsoTerritoryCode.AL
TerritoryCode.AM = 'AM'                           # originally IsoTerritoryCode.AM
TerritoryCode.AN = 'AN'                           # originally IsoTerritoryCode.AN
TerritoryCode.AO = 'AO'                           # originally IsoTerritoryCode.AO
TerritoryCode.AQ = 'AQ'                           # originally IsoTerritoryCode.AQ
TerritoryCode.AR = 'AR'                           # originally IsoTerritoryCode.AR
TerritoryCode.AS = 'AS'                           # originally IsoTerritoryCode.AS
TerritoryCode.AT = 'AT'                           # originally IsoTerritoryCode.AT
TerritoryCode.AU = 'AU'                           # originally IsoTerritoryCode.AU
TerritoryCode.AW = 'AW'                           # originally IsoTerritoryCode.AW
TerritoryCode.AX = 'AX'                           # originally IsoTerritoryCode.AX
TerritoryCode.AZ = 'AZ'                           # originally IsoTerritoryCode.AZ
TerritoryCode.BA = 'BA'                           # originally IsoTerritoryCode.BA
TerritoryCode.BB = 'BB'                           # originally IsoTerritoryCode.BB
TerritoryCode.BD = 'BD'                           # originally IsoTerritoryCode.BD
TerritoryCode.BE = 'BE'                           # originally IsoTerritoryCode.BE
TerritoryCode.BF = 'BF'                           # originally IsoTerritoryCode.BF
TerritoryCode.BG = 'BG'                           # originally IsoTerritoryCode.BG
TerritoryCode.BH = 'BH'                           # originally IsoTerritoryCode.BH
TerritoryCode.BI = 'BI'                           # originally IsoTerritoryCode.BI
TerritoryCode.BJ = 'BJ'                           # originally IsoTerritoryCode.BJ
TerritoryCode.BL = 'BL'                           # originally IsoTerritoryCode.BL
TerritoryCode.BM = 'BM'                           # originally IsoTerritoryCode.BM
TerritoryCode.BN = 'BN'                           # originally IsoTerritoryCode.BN
TerritoryCode.BO = 'BO'                           # originally IsoTerritoryCode.BO
TerritoryCode.BQ = 'BQ'                           # originally IsoTerritoryCode.BQ
TerritoryCode.BR = 'BR'                           # originally IsoTerritoryCode.BR
TerritoryCode.BS = 'BS'                           # originally IsoTerritoryCode.BS
TerritoryCode.BT = 'BT'                           # originally IsoTerritoryCode.BT
TerritoryCode.BV = 'BV'                           # originally IsoTerritoryCode.BV
TerritoryCode.BW = 'BW'                           # originally IsoTerritoryCode.BW
TerritoryCode.BY = 'BY'                           # originally IsoTerritoryCode.BY
TerritoryCode.BZ = 'BZ'                           # originally IsoTerritoryCode.BZ
TerritoryCode.CA = 'CA'                           # originally IsoTerritoryCode.CA
TerritoryCode.CC = 'CC'                           # originally IsoTerritoryCode.CC
TerritoryCode.CD = 'CD'                           # originally IsoTerritoryCode.CD
TerritoryCode.CF = 'CF'                           # originally IsoTerritoryCode.CF
TerritoryCode.CG = 'CG'                           # originally IsoTerritoryCode.CG
TerritoryCode.CH = 'CH'                           # originally IsoTerritoryCode.CH
TerritoryCode.CI = 'CI'                           # originally IsoTerritoryCode.CI
TerritoryCode.CK = 'CK'                           # originally IsoTerritoryCode.CK
TerritoryCode.CL = 'CL'                           # originally IsoTerritoryCode.CL
TerritoryCode.CM = 'CM'                           # originally IsoTerritoryCode.CM
TerritoryCode.CN = 'CN'                           # originally IsoTerritoryCode.CN
TerritoryCode.CO = 'CO'                           # originally IsoTerritoryCode.CO
TerritoryCode.CR = 'CR'                           # originally IsoTerritoryCode.CR
TerritoryCode.CS = 'CS'                           # originally IsoTerritoryCode.CS
TerritoryCode.CU = 'CU'                           # originally IsoTerritoryCode.CU
TerritoryCode.CV = 'CV'                           # originally IsoTerritoryCode.CV
TerritoryCode.CW = 'CW'                           # originally IsoTerritoryCode.CW
TerritoryCode.CX = 'CX'                           # originally IsoTerritoryCode.CX
TerritoryCode.CY = 'CY'                           # originally IsoTerritoryCode.CY
TerritoryCode.CZ = 'CZ'                           # originally IsoTerritoryCode.CZ
TerritoryCode.DE = 'DE'                           # originally IsoTerritoryCode.DE
TerritoryCode.DJ = 'DJ'                           # originally IsoTerritoryCode.DJ
TerritoryCode.DK = 'DK'                           # originally IsoTerritoryCode.DK
TerritoryCode.DM = 'DM'                           # originally IsoTerritoryCode.DM
TerritoryCode.DO = 'DO'                           # originally IsoTerritoryCode.DO
TerritoryCode.DZ = 'DZ'                           # originally IsoTerritoryCode.DZ
TerritoryCode.EC = 'EC'                           # originally IsoTerritoryCode.EC
TerritoryCode.EE = 'EE'                           # originally IsoTerritoryCode.EE
TerritoryCode.EG = 'EG'                           # originally IsoTerritoryCode.EG
TerritoryCode.EH = 'EH'                           # originally IsoTerritoryCode.EH
TerritoryCode.ER = 'ER'                           # originally IsoTerritoryCode.ER
TerritoryCode.ES = 'ES'                           # originally IsoTerritoryCode.ES
TerritoryCode.ET = 'ET'                           # originally IsoTerritoryCode.ET
TerritoryCode.FI = 'FI'                           # originally IsoTerritoryCode.FI
TerritoryCode.FJ = 'FJ'                           # originally IsoTerritoryCode.FJ
TerritoryCode.FK = 'FK'                           # originally IsoTerritoryCode.FK
TerritoryCode.FM = 'FM'                           # originally IsoTerritoryCode.FM
TerritoryCode.FO = 'FO'                           # originally IsoTerritoryCode.FO
TerritoryCode.FR = 'FR'                           # originally IsoTerritoryCode.FR
TerritoryCode.GA = 'GA'                           # originally IsoTerritoryCode.GA
TerritoryCode.GB = 'GB'                           # originally IsoTerritoryCode.GB
TerritoryCode.GD = 'GD'                           # originally IsoTerritoryCode.GD
TerritoryCode.GE = 'GE'                           # originally IsoTerritoryCode.GE
TerritoryCode.GF = 'GF'                           # originally IsoTerritoryCode.GF
TerritoryCode.GG = 'GG'                           # originally IsoTerritoryCode.GG
TerritoryCode.GH = 'GH'                           # originally IsoTerritoryCode.GH
TerritoryCode.GI = 'GI'                           # originally IsoTerritoryCode.GI
TerritoryCode.GL = 'GL'                           # originally IsoTerritoryCode.GL
TerritoryCode.GM = 'GM'                           # originally IsoTerritoryCode.GM
TerritoryCode.GN = 'GN'                           # originally IsoTerritoryCode.GN
TerritoryCode.GP = 'GP'                           # originally IsoTerritoryCode.GP
TerritoryCode.GQ = 'GQ'                           # originally IsoTerritoryCode.GQ
TerritoryCode.GR = 'GR'                           # originally IsoTerritoryCode.GR
TerritoryCode.GS = 'GS'                           # originally IsoTerritoryCode.GS
TerritoryCode.GT = 'GT'                           # originally IsoTerritoryCode.GT
TerritoryCode.GU = 'GU'                           # originally IsoTerritoryCode.GU
TerritoryCode.GW = 'GW'                           # originally IsoTerritoryCode.GW
TerritoryCode.GY = 'GY'                           # originally IsoTerritoryCode.GY
TerritoryCode.HK = 'HK'                           # originally IsoTerritoryCode.HK
TerritoryCode.HM = 'HM'                           # originally IsoTerritoryCode.HM
TerritoryCode.HN = 'HN'                           # originally IsoTerritoryCode.HN
TerritoryCode.HR = 'HR'                           # originally IsoTerritoryCode.HR
TerritoryCode.HT = 'HT'                           # originally IsoTerritoryCode.HT
TerritoryCode.HU = 'HU'                           # originally IsoTerritoryCode.HU
TerritoryCode.ID = 'ID'                           # originally IsoTerritoryCode.ID
TerritoryCode.IE = 'IE'                           # originally IsoTerritoryCode.IE
TerritoryCode.IL = 'IL'                           # originally IsoTerritoryCode.IL
TerritoryCode.IM = 'IM'                           # originally IsoTerritoryCode.IM
TerritoryCode.IN = 'IN'                           # originally IsoTerritoryCode.IN
TerritoryCode.IO = 'IO'                           # originally IsoTerritoryCode.IO
TerritoryCode.IQ = 'IQ'                           # originally IsoTerritoryCode.IQ
TerritoryCode.IR = 'IR'                           # originally IsoTerritoryCode.IR
TerritoryCode.IS = 'IS'                           # originally IsoTerritoryCode.IS
TerritoryCode.IT = 'IT'                           # originally IsoTerritoryCode.IT
TerritoryCode.JE = 'JE'                           # originally IsoTerritoryCode.JE
TerritoryCode.JM = 'JM'                           # originally IsoTerritoryCode.JM
TerritoryCode.JO = 'JO'                           # originally IsoTerritoryCode.JO
TerritoryCode.JP = 'JP'                           # originally IsoTerritoryCode.JP
TerritoryCode.KE = 'KE'                           # originally IsoTerritoryCode.KE
TerritoryCode.KG = 'KG'                           # originally IsoTerritoryCode.KG
TerritoryCode.KH = 'KH'                           # originally IsoTerritoryCode.KH
TerritoryCode.KI = 'KI'                           # originally IsoTerritoryCode.KI
TerritoryCode.KM = 'KM'                           # originally IsoTerritoryCode.KM
TerritoryCode.KN = 'KN'                           # originally IsoTerritoryCode.KN
TerritoryCode.KP = 'KP'                           # originally IsoTerritoryCode.KP
TerritoryCode.KR = 'KR'                           # originally IsoTerritoryCode.KR
TerritoryCode.KW = 'KW'                           # originally IsoTerritoryCode.KW
TerritoryCode.KY = 'KY'                           # originally IsoTerritoryCode.KY
TerritoryCode.KZ = 'KZ'                           # originally IsoTerritoryCode.KZ
TerritoryCode.LA = 'LA'                           # originally IsoTerritoryCode.LA
TerritoryCode.LB = 'LB'                           # originally IsoTerritoryCode.LB
TerritoryCode.LC = 'LC'                           # originally IsoTerritoryCode.LC
TerritoryCode.LI = 'LI'                           # originally IsoTerritoryCode.LI
TerritoryCode.LK = 'LK'                           # originally IsoTerritoryCode.LK
TerritoryCode.LR = 'LR'                           # originally IsoTerritoryCode.LR
TerritoryCode.LS = 'LS'                           # originally IsoTerritoryCode.LS
TerritoryCode.LT = 'LT'                           # originally IsoTerritoryCode.LT
TerritoryCode.LU = 'LU'                           # originally IsoTerritoryCode.LU
TerritoryCode.LV = 'LV'                           # originally IsoTerritoryCode.LV
TerritoryCode.LY = 'LY'                           # originally IsoTerritoryCode.LY
TerritoryCode.MA = 'MA'                           # originally IsoTerritoryCode.MA
TerritoryCode.MC = 'MC'                           # originally IsoTerritoryCode.MC
TerritoryCode.MD = 'MD'                           # originally IsoTerritoryCode.MD
TerritoryCode.ME = 'ME'                           # originally IsoTerritoryCode.ME
TerritoryCode.MF = 'MF'                           # originally IsoTerritoryCode.MF
TerritoryCode.MG = 'MG'                           # originally IsoTerritoryCode.MG
TerritoryCode.MH = 'MH'                           # originally IsoTerritoryCode.MH
TerritoryCode.MK = 'MK'                           # originally IsoTerritoryCode.MK
TerritoryCode.ML = 'ML'                           # originally IsoTerritoryCode.ML
TerritoryCode.MM = 'MM'                           # originally IsoTerritoryCode.MM
TerritoryCode.MN = 'MN'                           # originally IsoTerritoryCode.MN
TerritoryCode.MO = 'MO'                           # originally IsoTerritoryCode.MO
TerritoryCode.MP = 'MP'                           # originally IsoTerritoryCode.MP
TerritoryCode.MQ = 'MQ'                           # originally IsoTerritoryCode.MQ
TerritoryCode.MR = 'MR'                           # originally IsoTerritoryCode.MR
TerritoryCode.MS = 'MS'                           # originally IsoTerritoryCode.MS
TerritoryCode.MT = 'MT'                           # originally IsoTerritoryCode.MT
TerritoryCode.MU = 'MU'                           # originally IsoTerritoryCode.MU
TerritoryCode.MV = 'MV'                           # originally IsoTerritoryCode.MV
TerritoryCode.MW = 'MW'                           # originally IsoTerritoryCode.MW
TerritoryCode.MX = 'MX'                           # originally IsoTerritoryCode.MX
TerritoryCode.MY = 'MY'                           # originally IsoTerritoryCode.MY
TerritoryCode.MZ = 'MZ'                           # originally IsoTerritoryCode.MZ
TerritoryCode.NA = 'NA'                           # originally IsoTerritoryCode.NA
TerritoryCode.NC = 'NC'                           # originally IsoTerritoryCode.NC
TerritoryCode.NE = 'NE'                           # originally IsoTerritoryCode.NE
TerritoryCode.NF = 'NF'                           # originally IsoTerritoryCode.NF
TerritoryCode.NG = 'NG'                           # originally IsoTerritoryCode.NG
TerritoryCode.NI = 'NI'                           # originally IsoTerritoryCode.NI
TerritoryCode.NL = 'NL'                           # originally IsoTerritoryCode.NL
TerritoryCode.NO = 'NO'                           # originally IsoTerritoryCode.NO
TerritoryCode.NP = 'NP'                           # originally IsoTerritoryCode.NP
TerritoryCode.NR = 'NR'                           # originally IsoTerritoryCode.NR
TerritoryCode.NU = 'NU'                           # originally IsoTerritoryCode.NU
TerritoryCode.NZ = 'NZ'                           # originally IsoTerritoryCode.NZ
TerritoryCode.OM = 'OM'                           # originally IsoTerritoryCode.OM
TerritoryCode.PA = 'PA'                           # originally IsoTerritoryCode.PA
TerritoryCode.PE = 'PE'                           # originally IsoTerritoryCode.PE
TerritoryCode.PF = 'PF'                           # originally IsoTerritoryCode.PF
TerritoryCode.PG = 'PG'                           # originally IsoTerritoryCode.PG
TerritoryCode.PH = 'PH'                           # originally IsoTerritoryCode.PH
TerritoryCode.PK = 'PK'                           # originally IsoTerritoryCode.PK
TerritoryCode.PL = 'PL'                           # originally IsoTerritoryCode.PL
TerritoryCode.PM = 'PM'                           # originally IsoTerritoryCode.PM
TerritoryCode.PN = 'PN'                           # originally IsoTerritoryCode.PN
TerritoryCode.PR = 'PR'                           # originally IsoTerritoryCode.PR
TerritoryCode.PS = 'PS'                           # originally IsoTerritoryCode.PS
TerritoryCode.PT = 'PT'                           # originally IsoTerritoryCode.PT
TerritoryCode.PW = 'PW'                           # originally IsoTerritoryCode.PW
TerritoryCode.PY = 'PY'                           # originally IsoTerritoryCode.PY
TerritoryCode.QA = 'QA'                           # originally IsoTerritoryCode.QA
TerritoryCode.RE = 'RE'                           # originally IsoTerritoryCode.RE
TerritoryCode.RO = 'RO'                           # originally IsoTerritoryCode.RO
TerritoryCode.RS = 'RS'                           # originally IsoTerritoryCode.RS
TerritoryCode.RU = 'RU'                           # originally IsoTerritoryCode.RU
TerritoryCode.RW = 'RW'                           # originally IsoTerritoryCode.RW
TerritoryCode.SA = 'SA'                           # originally IsoTerritoryCode.SA
TerritoryCode.SB = 'SB'                           # originally IsoTerritoryCode.SB
TerritoryCode.SC = 'SC'                           # originally IsoTerritoryCode.SC
TerritoryCode.SD = 'SD'                           # originally IsoTerritoryCode.SD
TerritoryCode.SE = 'SE'                           # originally IsoTerritoryCode.SE
TerritoryCode.SG = 'SG'                           # originally IsoTerritoryCode.SG
TerritoryCode.SH = 'SH'                           # originally IsoTerritoryCode.SH
TerritoryCode.SI = 'SI'                           # originally IsoTerritoryCode.SI
TerritoryCode.SJ = 'SJ'                           # originally IsoTerritoryCode.SJ
TerritoryCode.SK = 'SK'                           # originally IsoTerritoryCode.SK
TerritoryCode.SL = 'SL'                           # originally IsoTerritoryCode.SL
TerritoryCode.SM = 'SM'                           # originally IsoTerritoryCode.SM
TerritoryCode.SN = 'SN'                           # originally IsoTerritoryCode.SN
TerritoryCode.SO = 'SO'                           # originally IsoTerritoryCode.SO
TerritoryCode.SR = 'SR'                           # originally IsoTerritoryCode.SR
TerritoryCode.SS = 'SS'                           # originally IsoTerritoryCode.SS
TerritoryCode.ST = 'ST'                           # originally IsoTerritoryCode.ST
TerritoryCode.SV = 'SV'                           # originally IsoTerritoryCode.SV
TerritoryCode.SX = 'SX'                           # originally IsoTerritoryCode.SX
TerritoryCode.SY = 'SY'                           # originally IsoTerritoryCode.SY
TerritoryCode.SZ = 'SZ'                           # originally IsoTerritoryCode.SZ
TerritoryCode.TC = 'TC'                           # originally IsoTerritoryCode.TC
TerritoryCode.TD = 'TD'                           # originally IsoTerritoryCode.TD
TerritoryCode.TF = 'TF'                           # originally IsoTerritoryCode.TF
TerritoryCode.TG = 'TG'                           # originally IsoTerritoryCode.TG
TerritoryCode.TH = 'TH'                           # originally IsoTerritoryCode.TH
TerritoryCode.TJ = 'TJ'                           # originally IsoTerritoryCode.TJ
TerritoryCode.TK = 'TK'                           # originally IsoTerritoryCode.TK
TerritoryCode.TL = 'TL'                           # originally IsoTerritoryCode.TL
TerritoryCode.TM = 'TM'                           # originally IsoTerritoryCode.TM
TerritoryCode.TN = 'TN'                           # originally IsoTerritoryCode.TN
TerritoryCode.TO = 'TO'                           # originally IsoTerritoryCode.TO
TerritoryCode.TR = 'TR'                           # originally IsoTerritoryCode.TR
TerritoryCode.TT = 'TT'                           # originally IsoTerritoryCode.TT
TerritoryCode.TV = 'TV'                           # originally IsoTerritoryCode.TV
TerritoryCode.TW = 'TW'                           # originally IsoTerritoryCode.TW
TerritoryCode.TZ = 'TZ'                           # originally IsoTerritoryCode.TZ
TerritoryCode.UA = 'UA'                           # originally IsoTerritoryCode.UA
TerritoryCode.UG = 'UG'                           # originally IsoTerritoryCode.UG
TerritoryCode.UM = 'UM'                           # originally IsoTerritoryCode.UM
TerritoryCode.US = 'US'                           # originally IsoTerritoryCode.US
TerritoryCode.UY = 'UY'                           # originally IsoTerritoryCode.UY
TerritoryCode.UZ = 'UZ'                           # originally IsoTerritoryCode.UZ
TerritoryCode.VA = 'VA'                           # originally IsoTerritoryCode.VA
TerritoryCode.VC = 'VC'                           # originally IsoTerritoryCode.VC
TerritoryCode.VE = 'VE'                           # originally IsoTerritoryCode.VE
TerritoryCode.VG = 'VG'                           # originally IsoTerritoryCode.VG
TerritoryCode.VI = 'VI'                           # originally IsoTerritoryCode.VI
TerritoryCode.VN = 'VN'                           # originally IsoTerritoryCode.VN
TerritoryCode.VU = 'VU'                           # originally IsoTerritoryCode.VU
TerritoryCode.WF = 'WF'                           # originally IsoTerritoryCode.WF
TerritoryCode.WS = 'WS'                           # originally IsoTerritoryCode.WS
TerritoryCode.YE = 'YE'                           # originally IsoTerritoryCode.YE
TerritoryCode.YT = 'YT'                           # originally IsoTerritoryCode.YT
TerritoryCode.ZA = 'ZA'                           # originally IsoTerritoryCode.ZA
TerritoryCode.ZM = 'ZM'                           # originally IsoTerritoryCode.ZM
TerritoryCode.ZW = 'ZW'                           # originally IsoTerritoryCode.ZW
TerritoryCode.Worldwide = 'Worldwide'             # originally DdexTerritoryCode.Worldwide
TerritoryCode._InitializeFacetMap(TerritoryCode._CF_enumeration,
   TerritoryCode._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'TerritoryCode', TerritoryCode)
