# ./_ddex.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:4138b5908ba26e50550d431f0873fd623feecf75
# Generated 2015-07-06 15:43:13.583236 by PyXB version 1.2.4 using Python 2.7.6.final.0
# Namespace http://ddex.net/xml/20110630/ddex [xmlns:ddex]

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:a4a9bd6c-23f5-11e5-814c-080027960975')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://ddex.net/xml/20110630/ddex', create_if_missing=True)
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


# Atomic simple type: {http://ddex.net/xml/20110630/ddex}AccessLimitation
class AccessLimitation (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of limitation on the access of a site."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AccessLimitation')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 18, 4)
    _Documentation = 'A Type of limitation on the access of a site.'
AccessLimitation._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=AccessLimitation, enum_prefix=None)
AccessLimitation.NoLimitation = AccessLimitation._CF_enumeration.addEnumeration(unicode_value='NoLimitation', tag='NoLimitation')
AccessLimitation.PrivateAccessOnly = AccessLimitation._CF_enumeration.addEnumeration(unicode_value='PrivateAccessOnly', tag='PrivateAccessOnly')
AccessLimitation._InitializeFacetMap(AccessLimitation._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'AccessLimitation', AccessLimitation)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}AdministratingRecordCompanyRole
class AdministratingRecordCompanyRole (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A role played by a Party responsible for administering Rights in a
                Resource or a Release."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AdministratingRecordCompanyRole')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 27, 4)
    _Documentation = 'A role played by a Party responsible for administering Rights in a\n                Resource or a Release.'
AdministratingRecordCompanyRole._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=AdministratingRecordCompanyRole, enum_prefix=None)
AdministratingRecordCompanyRole.DesignatedDsrMessageRecipient = AdministratingRecordCompanyRole._CF_enumeration.addEnumeration(unicode_value='DesignatedDsrMessageRecipient', tag='DesignatedDsrMessageRecipient')
AdministratingRecordCompanyRole.RightsAdministrator = AdministratingRecordCompanyRole._CF_enumeration.addEnumeration(unicode_value='RightsAdministrator', tag='RightsAdministrator')
AdministratingRecordCompanyRole.RoyaltyAdministrator = AdministratingRecordCompanyRole._CF_enumeration.addEnumeration(unicode_value='RoyaltyAdministrator', tag='RoyaltyAdministrator')
AdministratingRecordCompanyRole.Unknown = AdministratingRecordCompanyRole._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
AdministratingRecordCompanyRole._InitializeFacetMap(AdministratingRecordCompanyRole._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'AdministratingRecordCompanyRole', AdministratingRecordCompanyRole)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}ArtistRole
class ArtistRole (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A role of a principal Contributor in relation to a Performance or a
                Fixation."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ArtistRole')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 39, 4)
    _Documentation = 'A role of a principal Contributor in relation to a Performance or a\n                Fixation.'
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
ArtistRole.StudioMusician = ArtistRole._CF_enumeration.addEnumeration(unicode_value='StudioMusician', tag='StudioMusician')
ArtistRole.StudioPersonnel = ArtistRole._CF_enumeration.addEnumeration(unicode_value='StudioPersonnel', tag='StudioPersonnel')
ArtistRole.SubArranger = ArtistRole._CF_enumeration.addEnumeration(unicode_value='SubArranger', tag='SubArranger')
ArtistRole.SubPublisher = ArtistRole._CF_enumeration.addEnumeration(unicode_value='SubPublisher', tag='SubPublisher')
ArtistRole.SubstitutedPublisher = ArtistRole._CF_enumeration.addEnumeration(unicode_value='SubstitutedPublisher', tag='SubstitutedPublisher')
ArtistRole.Translator = ArtistRole._CF_enumeration.addEnumeration(unicode_value='Translator', tag='Translator')
ArtistRole.Unknown = ArtistRole._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
ArtistRole.UserDefined = ArtistRole._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
ArtistRole._InitializeFacetMap(ArtistRole._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ArtistRole', ArtistRole)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}AudioCodecType
class AudioCodecType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of AudioCodec."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AudioCodecType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 96, 4)
    _Documentation = 'A Type of AudioCodec.'
AudioCodecType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=AudioCodecType, enum_prefix=None)
AudioCodecType.AAC = AudioCodecType._CF_enumeration.addEnumeration(unicode_value='AAC', tag='AAC')
AudioCodecType.ADPCM = AudioCodecType._CF_enumeration.addEnumeration(unicode_value='ADPCM', tag='ADPCM')
AudioCodecType.ALaw = AudioCodecType._CF_enumeration.addEnumeration(unicode_value='ALaw', tag='ALaw')
AudioCodecType.AMR_NB = AudioCodecType._CF_enumeration.addEnumeration(unicode_value='AMR-NB', tag='AMR_NB')
AudioCodecType.AMR_WB = AudioCodecType._CF_enumeration.addEnumeration(unicode_value='AMR-WB', tag='AMR_WB')
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

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}CalculationType
class CalculationType (pyxb.binding.datatypes.string):

    """A Type of Calculation used to determine an actual Amount
                paid."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CalculationType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 120, 4)
    _Documentation = 'A Type of Calculation used to determine an actual Amount\n                paid.'
CalculationType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'CalculationType', CalculationType)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}CamlMessageInBatchType
class CamlMessageInBatchType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Message in a batch in the CAML
                DdexMessageSuite."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CamlMessageInBatchType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 127, 4)
    _Documentation = 'A Type of Message in a batch in the CAML\n                DdexMessageSuite.'
CamlMessageInBatchType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CamlMessageInBatchType, enum_prefix=None)
CamlMessageInBatchType.LicenseOrClaimRequestMessage = CamlMessageInBatchType._CF_enumeration.addEnumeration(unicode_value='LicenseOrClaimRequestMessage', tag='LicenseOrClaimRequestMessage')
CamlMessageInBatchType.LicenseOrClaimMessage = CamlMessageInBatchType._CF_enumeration.addEnumeration(unicode_value='LicenseOrClaimMessage', tag='LicenseOrClaimMessage')
CamlMessageInBatchType.LicensingInformationRequestMessage = CamlMessageInBatchType._CF_enumeration.addEnumeration(unicode_value='LicensingInformationRequestMessage', tag='LicensingInformationRequestMessage')
CamlMessageInBatchType.LicenseOrClaimConfirmationMessage = CamlMessageInBatchType._CF_enumeration.addEnumeration(unicode_value='LicenseOrClaimConfirmationMessage', tag='LicenseOrClaimConfirmationMessage')
CamlMessageInBatchType.NewReleaseMessage = CamlMessageInBatchType._CF_enumeration.addEnumeration(unicode_value='NewReleaseMessage', tag='NewReleaseMessage')
CamlMessageInBatchType.ContractDeliveryMessage = CamlMessageInBatchType._CF_enumeration.addEnumeration(unicode_value='ContractDeliveryMessage', tag='ContractDeliveryMessage')
CamlMessageInBatchType.ProductDeletionMessage = CamlMessageInBatchType._CF_enumeration.addEnumeration(unicode_value='ProductDeletionMessage', tag='ProductDeletionMessage')
CamlMessageInBatchType._InitializeFacetMap(CamlMessageInBatchType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CamlMessageInBatchType', CamlMessageInBatchType)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}CarrierType
class CarrierType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Carrier used for a Fixation."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CarrierType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 142, 4)
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

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}CatalogReleaseReference
class CatalogReleaseReference (pyxb.binding.datatypes.IDREF):

    """A Reference to a Release which is contained within a specific
                Catalog."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CatalogReleaseReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 257, 4)
    _Documentation = 'A Reference to a Release which is contained within a specific\n                Catalog.'
CatalogReleaseReference._CF_pattern = pyxb.binding.facets.CF_pattern()
CatalogReleaseReference._CF_pattern.addPattern(pattern='R[\\d\\-_a-zA-Z]+')
CatalogReleaseReference._InitializeFacetMap(CatalogReleaseReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'CatalogReleaseReference', CatalogReleaseReference)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}CdProtectionType
class CdProtectionType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of CD protection."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CdProtectionType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 266, 4)
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

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}CodingType
class CodingType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of coding used to encode a Resource."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CodingType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 281, 4)
    _Documentation = 'A Type of coding used to encode a Resource.'
CodingType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CodingType, enum_prefix=None)
CodingType.Lossless = CodingType._CF_enumeration.addEnumeration(unicode_value='Lossless', tag='Lossless')
CodingType.Lossy = CodingType._CF_enumeration.addEnumeration(unicode_value='Lossy', tag='Lossy')
CodingType._InitializeFacetMap(CodingType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CodingType', CodingType)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}CollectionCollectionReference
class CollectionCollectionReference (pyxb.binding.datatypes.IDREF):

    """A Reference to a Collection which is contained within a specific
                Collection."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CollectionCollectionReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 290, 4)
    _Documentation = 'A Reference to a Collection which is contained within a specific\n                Collection.'
CollectionCollectionReference._CF_pattern = pyxb.binding.facets.CF_pattern()
CollectionCollectionReference._CF_pattern.addPattern(pattern='X[\\d\\-_a-zA-Z]+')
CollectionCollectionReference._InitializeFacetMap(CollectionCollectionReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'CollectionCollectionReference', CollectionCollectionReference)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}CollectionReference
class CollectionReference (pyxb.binding.datatypes.ID):

    """A Reference to a Collection."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CollectionReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 299, 4)
    _Documentation = 'A Reference to a Collection.'
CollectionReference._CF_pattern = pyxb.binding.facets.CF_pattern()
CollectionReference._CF_pattern.addPattern(pattern='X[\\d\\-_a-zA-Z]+')
CollectionReference._InitializeFacetMap(CollectionReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'CollectionReference', CollectionReference)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}CollectionResourceReference
class CollectionResourceReference (pyxb.binding.datatypes.IDREF):

    """A Reference to a Resource which is contained within a specific
                Collection."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CollectionResourceReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 307, 4)
    _Documentation = 'A Reference to a Resource which is contained within a specific\n                Collection.'
CollectionResourceReference._CF_pattern = pyxb.binding.facets.CF_pattern()
CollectionResourceReference._CF_pattern.addPattern(pattern='A[\\d\\-_a-zA-Z]+')
CollectionResourceReference._InitializeFacetMap(CollectionResourceReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'CollectionResourceReference', CollectionResourceReference)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}CollectionType
class CollectionType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Collection."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CollectionType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 316, 4)
    _Documentation = 'A Type of Collection.'
CollectionType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CollectionType, enum_prefix=None)
CollectionType.AudioChapter = CollectionType._CF_enumeration.addEnumeration(unicode_value='AudioChapter', tag='AudioChapter')
CollectionType.Episode = CollectionType._CF_enumeration.addEnumeration(unicode_value='Episode', tag='Episode')
CollectionType.MedleySegment = CollectionType._CF_enumeration.addEnumeration(unicode_value='MedleySegment', tag='MedleySegment')
CollectionType.PotpourriSegment = CollectionType._CF_enumeration.addEnumeration(unicode_value='PotpourriSegment', tag='PotpourriSegment')
CollectionType.Season = CollectionType._CF_enumeration.addEnumeration(unicode_value='Season', tag='Season')
CollectionType.Series = CollectionType._CF_enumeration.addEnumeration(unicode_value='Series', tag='Series')
CollectionType.VideoChapter = CollectionType._CF_enumeration.addEnumeration(unicode_value='VideoChapter', tag='VideoChapter')
CollectionType._InitializeFacetMap(CollectionType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CollectionType', CollectionType)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}CollectionWorkReference
class CollectionWorkReference (pyxb.binding.datatypes.IDREF):

    """A Reference to a Work which is contained within a specific
                Collection."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CollectionWorkReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 330, 4)
    _Documentation = 'A Reference to a Work which is contained within a specific\n                Collection.'
CollectionWorkReference._CF_pattern = pyxb.binding.facets.CF_pattern()
CollectionWorkReference._CF_pattern.addPattern(pattern='W[\\d\\-_a-zA-Z]+')
CollectionWorkReference._InitializeFacetMap(CollectionWorkReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'CollectionWorkReference', CollectionWorkReference)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}CommercialModelType
class CommercialModelType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of CommercialModel (e.g. SubscriptionModel and
                PayAsYouGoModel). The CommercialModelType indicates how a Consumer pays for a
                Service or Release."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CommercialModelType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 339, 4)
    _Documentation = 'A Type of CommercialModel (e.g. SubscriptionModel and\n                PayAsYouGoModel). The CommercialModelType indicates how a Consumer pays for a\n                Service or Release.'
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

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}CompilationType
class CompilationType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Compilation."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CompilationType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 355, 4)
    _Documentation = 'A Type of Compilation.'
CompilationType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CompilationType, enum_prefix=None)
CompilationType.InternalCompilation = CompilationType._CF_enumeration.addEnumeration(unicode_value='InternalCompilation', tag='InternalCompilation')
CompilationType.NonInternalCompilation = CompilationType._CF_enumeration.addEnumeration(unicode_value='NonInternalCompilation', tag='NonInternalCompilation')
CompilationType.NotCompiled = CompilationType._CF_enumeration.addEnumeration(unicode_value='NotCompiled', tag='NotCompiled')
CompilationType._InitializeFacetMap(CompilationType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CompilationType', CompilationType)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}ContainerFormat
class ContainerFormat (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of container according to its FileFormat."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ContainerFormat')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 365, 4)
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

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}ControlledCompositionStatus
class ControlledCompositionStatus (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A status of controlled composition clause in terms of its
                effectiveness."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ControlledCompositionStatus')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 381, 4)
    _Documentation = 'A status of controlled composition clause in terms of its\n                effectiveness.'
ControlledCompositionStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ControlledCompositionStatus, enum_prefix=None)
ControlledCompositionStatus.Active = ControlledCompositionStatus._CF_enumeration.addEnumeration(unicode_value='Active', tag='Active')
ControlledCompositionStatus.Refused = ControlledCompositionStatus._CF_enumeration.addEnumeration(unicode_value='Refused', tag='Refused')
ControlledCompositionStatus._InitializeFacetMap(ControlledCompositionStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ControlledCompositionStatus', ControlledCompositionStatus)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}ControlledCompositionType
class ControlledCompositionType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A type of a controlled composition clause."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ControlledCompositionType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 391, 4)
    _Documentation = 'A type of a controlled composition clause.'
ControlledCompositionType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ControlledCompositionType, enum_prefix=None)
ControlledCompositionType.ControlledCompositionAgreement = ControlledCompositionType._CF_enumeration.addEnumeration(unicode_value='ControlledCompositionAgreement', tag='ControlledCompositionAgreement')
ControlledCompositionType.CsiRoyaltyRateModification = ControlledCompositionType._CF_enumeration.addEnumeration(unicode_value='CsiRoyaltyRateModification', tag='CsiRoyaltyRateModification')
ControlledCompositionType.PublisherReducedRoyaltyRateModification = ControlledCompositionType._CF_enumeration.addEnumeration(unicode_value='PublisherReducedRoyaltyRateModification', tag='PublisherReducedRoyaltyRateModification')
ControlledCompositionType._InitializeFacetMap(ControlledCompositionType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ControlledCompositionType', ControlledCompositionType)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}CreationType
class CreationType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Creation."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CreationType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 401, 4)
    _Documentation = 'A Type of Creation.'
CreationType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CreationType, enum_prefix=None)
CreationType.MusicalWork = CreationType._CF_enumeration.addEnumeration(unicode_value='MusicalWork', tag='MusicalWork')
CreationType.Release = CreationType._CF_enumeration.addEnumeration(unicode_value='Release', tag='Release')
CreationType.Resource = CreationType._CF_enumeration.addEnumeration(unicode_value='Resource', tag='Resource')
CreationType._InitializeFacetMap(CreationType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CreationType', CreationType)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}CueOrigin
class CueOrigin (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Cue according to its origin."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CueOrigin')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 411, 4)
    _Documentation = 'A Type of Cue according to its origin.'
CueOrigin._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CueOrigin, enum_prefix=None)
CueOrigin.LibraryMusic = CueOrigin._CF_enumeration.addEnumeration(unicode_value='LibraryMusic', tag='LibraryMusic')
CueOrigin.PreexistingMusic = CueOrigin._CF_enumeration.addEnumeration(unicode_value='PreexistingMusic', tag='PreexistingMusic')
CueOrigin.SpeciallyCommissionedMusic = CueOrigin._CF_enumeration.addEnumeration(unicode_value='SpeciallyCommissionedMusic', tag='SpeciallyCommissionedMusic')
CueOrigin.Unknown = CueOrigin._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
CueOrigin.UserDefined = CueOrigin._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
CueOrigin._InitializeFacetMap(CueOrigin._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CueOrigin', CueOrigin)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}CueResourceReference
class CueResourceReference (pyxb.binding.datatypes.IDREF):

    """A Reference to a Resource which is contained within a specific
                Cue."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CueResourceReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 423, 4)
    _Documentation = 'A Reference to a Resource which is contained within a specific\n                Cue.'
CueResourceReference._CF_pattern = pyxb.binding.facets.CF_pattern()
CueResourceReference._CF_pattern.addPattern(pattern='A[\\d\\-_a-zA-Z]+')
CueResourceReference._InitializeFacetMap(CueResourceReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'CueResourceReference', CueResourceReference)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}CueSheetReference
class CueSheetReference (pyxb.binding.datatypes.ID):

    """A Reference to a CueSheet."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CueSheetReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 432, 4)
    _Documentation = 'A Reference to a CueSheet.'
CueSheetReference._CF_pattern = pyxb.binding.facets.CF_pattern()
CueSheetReference._CF_pattern.addPattern(pattern='Q[\\d\\-_a-zA-Z]+')
CueSheetReference._InitializeFacetMap(CueSheetReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'CueSheetReference', CueSheetReference)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}CueSheetType
class CueSheetType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of CueSheet."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CueSheetType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 440, 4)
    _Documentation = 'A Type of CueSheet.'
CueSheetType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CueSheetType, enum_prefix=None)
CueSheetType.AverageCueSheet = CueSheetType._CF_enumeration.addEnumeration(unicode_value='AverageCueSheet', tag='AverageCueSheet')
CueSheetType.CompositeCueSheet = CueSheetType._CF_enumeration.addEnumeration(unicode_value='CompositeCueSheet', tag='CompositeCueSheet')
CueSheetType.StandardCueSheet = CueSheetType._CF_enumeration.addEnumeration(unicode_value='StandardCueSheet', tag='StandardCueSheet')
CueSheetType.SummarisedCueSheet = CueSheetType._CF_enumeration.addEnumeration(unicode_value='SummarisedCueSheet', tag='SummarisedCueSheet')
CueSheetType.SurrogateCueSheet = CueSheetType._CF_enumeration.addEnumeration(unicode_value='SurrogateCueSheet', tag='SurrogateCueSheet')
CueSheetType._InitializeFacetMap(CueSheetType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CueSheetType', CueSheetType)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}CueUseType
class CueUseType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of use of a Cue."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CueUseType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 452, 4)
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

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}CueWorkReference
class CueWorkReference (pyxb.binding.datatypes.IDREF):

    """A Reference to a Work which is contained within a specific
                Cue."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CueWorkReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 469, 4)
    _Documentation = 'A Reference to a Work which is contained within a specific\n                Cue.'
CueWorkReference._CF_pattern = pyxb.binding.facets.CF_pattern()
CueWorkReference._CF_pattern.addPattern(pattern='W[\\d\\-_a-zA-Z]+')
CueWorkReference._InitializeFacetMap(CueWorkReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'CueWorkReference', CueWorkReference)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}DataMismatchResponseType
class DataMismatchResponseType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of action that is a response to a
                DataMismatch."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DataMismatchResponseType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 478, 4)
    _Documentation = 'A Type of action that is a response to a\n                DataMismatch.'
DataMismatchResponseType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DataMismatchResponseType, enum_prefix=None)
DataMismatchResponseType.AdditionalInformationOnly = DataMismatchResponseType._CF_enumeration.addEnumeration(unicode_value='AdditionalInformationOnly', tag='AdditionalInformationOnly')
DataMismatchResponseType.DataMismatchConfirmation = DataMismatchResponseType._CF_enumeration.addEnumeration(unicode_value='DataMismatchConfirmation', tag='DataMismatchConfirmation')
DataMismatchResponseType.DataMismatchOutOfScope = DataMismatchResponseType._CF_enumeration.addEnumeration(unicode_value='DataMismatchOutOfScope', tag='DataMismatchOutOfScope')
DataMismatchResponseType.DataMismatchRaisedCommercialDispute = DataMismatchResponseType._CF_enumeration.addEnumeration(unicode_value='DataMismatchRaisedCommercialDispute', tag='DataMismatchRaisedCommercialDispute')
DataMismatchResponseType.NoReaction = DataMismatchResponseType._CF_enumeration.addEnumeration(unicode_value='NoReaction', tag='NoReaction')
DataMismatchResponseType.UserDefined = DataMismatchResponseType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
DataMismatchResponseType._InitializeFacetMap(DataMismatchResponseType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DataMismatchResponseType', DataMismatchResponseType)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}DataMismatchStatus
class DataMismatchStatus (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A status of a DataMismatch."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DataMismatchStatus')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 492, 4)
    _Documentation = 'A status of a DataMismatch.'
DataMismatchStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DataMismatchStatus, enum_prefix=None)
DataMismatchStatus.AdditionalInformationOnly = DataMismatchStatus._CF_enumeration.addEnumeration(unicode_value='AdditionalInformationOnly', tag='AdditionalInformationOnly')
DataMismatchStatus.Corrected = DataMismatchStatus._CF_enumeration.addEnumeration(unicode_value='Corrected', tag='Corrected')
DataMismatchStatus.Fatal = DataMismatchStatus._CF_enumeration.addEnumeration(unicode_value='Fatal', tag='Fatal')
DataMismatchStatus.NotCorrected = DataMismatchStatus._CF_enumeration.addEnumeration(unicode_value='NotCorrected', tag='NotCorrected')
DataMismatchStatus.UserDefined = DataMismatchStatus._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
DataMismatchStatus._InitializeFacetMap(DataMismatchStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DataMismatchStatus', DataMismatchStatus)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}DataMismatchType
class DataMismatchType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of DataMismatch."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DataMismatchType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 504, 4)
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

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}DdexPartyId
class DdexPartyId (pyxb.binding.datatypes.string):

    """An Identifier of a Party according to the DdexPartyId standard
                DDEX-DPID."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DdexPartyId')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 532, 4)
    _Documentation = 'An Identifier of a Party according to the DdexPartyId standard\n                DDEX-DPID.'
DdexPartyId._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'DdexPartyId', DdexPartyId)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}DealReleaseReference
class DealReleaseReference (pyxb.binding.datatypes.IDREF):

    """A Reference to a Release which is included in a specific
                Deal."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DealReleaseReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 539, 4)
    _Documentation = 'A Reference to a Release which is included in a specific\n                Deal.'
DealReleaseReference._CF_pattern = pyxb.binding.facets.CF_pattern()
DealReleaseReference._CF_pattern.addPattern(pattern='R[\\d\\-_a-zA-Z]+')
DealReleaseReference._InitializeFacetMap(DealReleaseReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'DealReleaseReference', DealReleaseReference)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}DealResourceReference
class DealResourceReference (pyxb.binding.datatypes.IDREF):

    """A Reference to a Resource which is contained within a specific
                Deal."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DealResourceReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 548, 4)
    _Documentation = 'A Reference to a Resource which is contained within a specific\n                Deal.'
DealResourceReference._CF_pattern = pyxb.binding.facets.CF_pattern()
DealResourceReference._CF_pattern.addPattern(pattern='A[\\d\\-_a-zA-Z]+')
DealResourceReference._InitializeFacetMap(DealResourceReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'DealResourceReference', DealResourceReference)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}DealTechnicalResourceDetailsReference
class DealTechnicalResourceDetailsReference (pyxb.binding.datatypes.IDREF):

    """A Reference to a Resource which is contained within a specific
                Deal."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DealTechnicalResourceDetailsReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 557, 4)
    _Documentation = 'A Reference to a Resource which is contained within a specific\n                Deal.'
DealTechnicalResourceDetailsReference._CF_pattern = pyxb.binding.facets.CF_pattern()
DealTechnicalResourceDetailsReference._CF_pattern.addPattern(pattern='T[\\d\\-_a-zA-Z]+')
DealTechnicalResourceDetailsReference._InitializeFacetMap(DealTechnicalResourceDetailsReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'DealTechnicalResourceDetailsReference', DealTechnicalResourceDetailsReference)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}DeclinationConditionReference
class DeclinationConditionReference (pyxb.binding.datatypes.IDREF):

    """A Reference to a LicenseOrClaimCondition which is contained within a
                specific declination."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DeclinationConditionReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 566, 4)
    _Documentation = 'A Reference to a LicenseOrClaimCondition which is contained within a\n                specific declination.'
DeclinationConditionReference._CF_pattern = pyxb.binding.facets.CF_pattern()
DeclinationConditionReference._CF_pattern.addPattern(pattern='E[\\d\\-_a-zA-Z]+')
DeclinationConditionReference._InitializeFacetMap(DeclinationConditionReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'DeclinationConditionReference', DeclinationConditionReference)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}DeclinationReleaseReference
class DeclinationReleaseReference (pyxb.binding.datatypes.IDREF):

    """A Reference to a Release which is contained within a specific
                declination."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DeclinationReleaseReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 575, 4)
    _Documentation = 'A Reference to a Release which is contained within a specific\n                declination.'
DeclinationReleaseReference._CF_pattern = pyxb.binding.facets.CF_pattern()
DeclinationReleaseReference._CF_pattern.addPattern(pattern='A[\\d\\-_a-zA-Z]+')
DeclinationReleaseReference._InitializeFacetMap(DeclinationReleaseReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'DeclinationReleaseReference', DeclinationReleaseReference)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}DeclinationResourceReference
class DeclinationResourceReference (pyxb.binding.datatypes.IDREF):

    """A Reference to a Resource which is contained within a specific
                declination."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DeclinationResourceReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 584, 4)
    _Documentation = 'A Reference to a Resource which is contained within a specific\n                declination.'
DeclinationResourceReference._CF_pattern = pyxb.binding.facets.CF_pattern()
DeclinationResourceReference._CF_pattern.addPattern(pattern='A[\\d\\-_a-zA-Z]+')
DeclinationResourceReference._InitializeFacetMap(DeclinationResourceReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'DeclinationResourceReference', DeclinationResourceReference)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}DeclinationRightShareReference
class DeclinationRightShareReference (pyxb.binding.datatypes.IDREF):

    """A Reference to a RightShare which is contained within a specific
                declination."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DeclinationRightShareReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 593, 4)
    _Documentation = 'A Reference to a RightShare which is contained within a specific\n                declination.'
DeclinationRightShareReference._CF_pattern = pyxb.binding.facets.CF_pattern()
DeclinationRightShareReference._CF_pattern.addPattern(pattern='S[\\d\\-_a-zA-Z]+')
DeclinationRightShareReference._InitializeFacetMap(DeclinationRightShareReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'DeclinationRightShareReference', DeclinationRightShareReference)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}DeclinationWorkReference
class DeclinationWorkReference (pyxb.binding.datatypes.IDREF):

    """A Reference to a Work which is contained within a specific
                declination."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DeclinationWorkReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 602, 4)
    _Documentation = 'A Reference to a Work which is contained within a specific\n                declination.'
DeclinationWorkReference._CF_pattern = pyxb.binding.facets.CF_pattern()
DeclinationWorkReference._CF_pattern.addPattern(pattern='W[\\d\\-_a-zA-Z]+')
DeclinationWorkReference._InitializeFacetMap(DeclinationWorkReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'DeclinationWorkReference', DeclinationWorkReference)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}DeductionRateType
class DeductionRateType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of DeductionRate."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DeductionRateType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 611, 4)
    _Documentation = 'A Type of DeductionRate.'
DeductionRateType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DeductionRateType, enum_prefix=None)
DeductionRateType.PennyRate = DeductionRateType._CF_enumeration.addEnumeration(unicode_value='PennyRate', tag='PennyRate')
DeductionRateType.PercentageRate = DeductionRateType._CF_enumeration.addEnumeration(unicode_value='PercentageRate', tag='PercentageRate')
DeductionRateType.UserDefined = DeductionRateType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
DeductionRateType._InitializeFacetMap(DeductionRateType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DeductionRateType', DeductionRateType)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}DeliveryActionType
class DeliveryActionType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of action requested for deliveries."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DeliveryActionType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 621, 4)
    _Documentation = 'A Type of action requested for deliveries.'
DeliveryActionType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DeliveryActionType, enum_prefix=None)
DeliveryActionType.ChangeDeliveryLimits = DeliveryActionType._CF_enumeration.addEnumeration(unicode_value='ChangeDeliveryLimits', tag='ChangeDeliveryLimits')
DeliveryActionType.RestartDeliveryWithLimits = DeliveryActionType._CF_enumeration.addEnumeration(unicode_value='RestartDeliveryWithLimits', tag='RestartDeliveryWithLimits')
DeliveryActionType.RestartDeliveryWithPreviousLimits = DeliveryActionType._CF_enumeration.addEnumeration(unicode_value='RestartDeliveryWithPreviousLimits', tag='RestartDeliveryWithPreviousLimits')
DeliveryActionType.StopDelivery = DeliveryActionType._CF_enumeration.addEnumeration(unicode_value='StopDelivery', tag='StopDelivery')
DeliveryActionType._InitializeFacetMap(DeliveryActionType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DeliveryActionType', DeliveryActionType)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}DeliveryMessageType
class DeliveryMessageType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of delivery Message."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DeliveryMessageType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 632, 4)
    _Documentation = 'A Type of delivery Message.'
DeliveryMessageType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DeliveryMessageType, enum_prefix=None)
DeliveryMessageType.NewReleaseMessage = DeliveryMessageType._CF_enumeration.addEnumeration(unicode_value='NewReleaseMessage', tag='NewReleaseMessage')
DeliveryMessageType.NonDdexMessage = DeliveryMessageType._CF_enumeration.addEnumeration(unicode_value='NonDdexMessage', tag='NonDdexMessage')
DeliveryMessageType.Unknown = DeliveryMessageType._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
DeliveryMessageType._InitializeFacetMap(DeliveryMessageType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DeliveryMessageType', DeliveryMessageType)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}DeprecatedCurrencyCode
class DeprecatedCurrencyCode (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A CurrencyCode which is not valid anymore."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DeprecatedCurrencyCode')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 642, 4)
    _Documentation = 'A CurrencyCode which is not valid anymore.'
DeprecatedCurrencyCode._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DeprecatedCurrencyCode, enum_prefix=None)
DeprecatedCurrencyCode.CYP = DeprecatedCurrencyCode._CF_enumeration.addEnumeration(unicode_value='CYP', tag='CYP')
DeprecatedCurrencyCode.MTL = DeprecatedCurrencyCode._CF_enumeration.addEnumeration(unicode_value='MTL', tag='MTL')
DeprecatedCurrencyCode.ROL = DeprecatedCurrencyCode._CF_enumeration.addEnumeration(unicode_value='ROL', tag='ROL')
DeprecatedCurrencyCode.SIT = DeprecatedCurrencyCode._CF_enumeration.addEnumeration(unicode_value='SIT', tag='SIT')
DeprecatedCurrencyCode.SKK = DeprecatedCurrencyCode._CF_enumeration.addEnumeration(unicode_value='SKK', tag='SKK')
DeprecatedCurrencyCode._InitializeFacetMap(DeprecatedCurrencyCode._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DeprecatedCurrencyCode', DeprecatedCurrencyCode)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}DescriptorSyntax
class DescriptorSyntax (pyxb.binding.datatypes.string):

    """A Type of a Descriptor according to how it is defined
                syntactically."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DescriptorSyntax')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 674, 4)
    _Documentation = 'A Type of a Descriptor according to how it is defined\n                syntactically.'
DescriptorSyntax._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'DescriptorSyntax', DescriptorSyntax)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}DigitizationMode
class DigitizationMode (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Digitization mode of a Resource."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DigitizationMode')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 681, 4)
    _Documentation = 'A Digitization mode of a Resource.'
DigitizationMode._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DigitizationMode, enum_prefix=None)
DigitizationMode.AAD = DigitizationMode._CF_enumeration.addEnumeration(unicode_value='AAD', tag='AAD')
DigitizationMode.ADD = DigitizationMode._CF_enumeration.addEnumeration(unicode_value='ADD', tag='ADD')
DigitizationMode.DDD = DigitizationMode._CF_enumeration.addEnumeration(unicode_value='DDD', tag='DDD')
DigitizationMode.Unknown = DigitizationMode._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
DigitizationMode._InitializeFacetMap(DigitizationMode._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DigitizationMode', DigitizationMode)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}DistributionChannelType
class DistributionChannelType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of DistributionChannel used to disseminate a Service or Release
                to a Consumer."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DistributionChannelType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 692, 4)
    _Documentation = 'A Type of DistributionChannel used to disseminate a Service or Release\n                to a Consumer.'
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

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}DrmEnforcementType
class DrmEnforcementType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of DRM enforcement."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DrmEnforcementType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 712, 4)
    _Documentation = 'A Type of DRM enforcement.'
DrmEnforcementType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DrmEnforcementType, enum_prefix=None)
DrmEnforcementType.DrmEnforced = DrmEnforcementType._CF_enumeration.addEnumeration(unicode_value='DrmEnforced', tag='DrmEnforced')
DrmEnforcementType.NotDrmEnforced = DrmEnforcementType._CF_enumeration.addEnumeration(unicode_value='NotDrmEnforced', tag='NotDrmEnforced')
DrmEnforcementType._InitializeFacetMap(DrmEnforcementType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DrmEnforcementType', DrmEnforcementType)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}DrmPlatformType
class DrmPlatformType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of DrmPlatform."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DrmPlatformType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 721, 4)
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

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}DsrMessageType
class DsrMessageType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Message in the DSR DdexMessageSuite."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DsrMessageType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 734, 4)
    _Documentation = 'A Type of Message in the DSR DdexMessageSuite.'
DsrMessageType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DsrMessageType, enum_prefix=None)
DsrMessageType.SalesReportToRecordCompanyMessage = DsrMessageType._CF_enumeration.addEnumeration(unicode_value='SalesReportToRecordCompanyMessage', tag='SalesReportToRecordCompanyMessage')
DsrMessageType.SalesReportToSocietyMessage = DsrMessageType._CF_enumeration.addEnumeration(unicode_value='SalesReportToSocietyMessage', tag='SalesReportToSocietyMessage')
DsrMessageType._InitializeFacetMap(DsrMessageType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DsrMessageType', DsrMessageType)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}ErnMessageType
class ErnMessageType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Message in the ERN DdexMessageSuite."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ErnMessageType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 743, 4)
    _Documentation = 'A Type of Message in the ERN DdexMessageSuite.'
ErnMessageType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ErnMessageType, enum_prefix=None)
ErnMessageType.NewReleaseMessage = ErnMessageType._CF_enumeration.addEnumeration(unicode_value='NewReleaseMessage', tag='NewReleaseMessage')
ErnMessageType._InitializeFacetMap(ErnMessageType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ErnMessageType', ErnMessageType)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}ExpressionType
class ExpressionType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of expression indicating how it should be
                perceived."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ExpressionType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 751, 4)
    _Documentation = 'A Type of expression indicating how it should be\n                perceived.'
ExpressionType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ExpressionType, enum_prefix=None)
ExpressionType.Informative = ExpressionType._CF_enumeration.addEnumeration(unicode_value='Informative', tag='Informative')
ExpressionType.Instructive = ExpressionType._CF_enumeration.addEnumeration(unicode_value='Instructive', tag='Instructive')
ExpressionType._InitializeFacetMap(ExpressionType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ExpressionType', ExpressionType)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}ExternallyLinkedResourceType
class ExternallyLinkedResourceType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Resource pointed to by an ExternalLink."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ExternallyLinkedResourceType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 761, 4)
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

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}FileStatus
class FileStatus (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A status of a File in terms of its validity."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FileStatus')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 775, 4)
    _Documentation = 'A status of a File in terms of its validity.'
FileStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=FileStatus, enum_prefix=None)
FileStatus.FileMissing = FileStatus._CF_enumeration.addEnumeration(unicode_value='FileMissing', tag='FileMissing')
FileStatus.FileOK = FileStatus._CF_enumeration.addEnumeration(unicode_value='FileOK', tag='FileOK')
FileStatus.HashSumWrong = FileStatus._CF_enumeration.addEnumeration(unicode_value='HashSumWrong', tag='HashSumWrong')
FileStatus.SignatureWrong = FileStatus._CF_enumeration.addEnumeration(unicode_value='SignatureWrong', tag='SignatureWrong')
FileStatus._InitializeFacetMap(FileStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'FileStatus', FileStatus)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}FingerprintAlgorithmType
class FingerprintAlgorithmType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of FingerprintAlgorithm."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FingerprintAlgorithmType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 786, 4)
    _Documentation = 'A Type of FingerprintAlgorithm.'
FingerprintAlgorithmType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=FingerprintAlgorithmType, enum_prefix=None)
FingerprintAlgorithmType.UserDefined = FingerprintAlgorithmType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
FingerprintAlgorithmType._InitializeFacetMap(FingerprintAlgorithmType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'FingerprintAlgorithmType', FingerprintAlgorithmType)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}GoverningAgreementType
class GoverningAgreementType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of governing agreement."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GoverningAgreementType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 794, 4)
    _Documentation = 'A Type of governing agreement.'
GoverningAgreementType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=GoverningAgreementType, enum_prefix=None)
GoverningAgreementType.UserDefined = GoverningAgreementType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
GoverningAgreementType._InitializeFacetMap(GoverningAgreementType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'GoverningAgreementType', GoverningAgreementType)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}HashSum
class HashSum (pyxb.binding.datatypes.string):

    """A value calculated from digital data that serves to distinguish it
                from other digital data."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'HashSum')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 802, 4)
    _Documentation = 'A value calculated from digital data that serves to distinguish it\n                from other digital data.'
HashSum._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'HashSum', HashSum)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}HashSumAlgorithmType
class HashSumAlgorithmType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of HashSumAlgorithm."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'HashSumAlgorithmType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 809, 4)
    _Documentation = 'A Type of HashSumAlgorithm.'
HashSumAlgorithmType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=HashSumAlgorithmType, enum_prefix=None)
HashSumAlgorithmType.MD4 = HashSumAlgorithmType._CF_enumeration.addEnumeration(unicode_value='MD4', tag='MD4')
HashSumAlgorithmType.MD5 = HashSumAlgorithmType._CF_enumeration.addEnumeration(unicode_value='MD5', tag='MD5')
HashSumAlgorithmType.SHA = HashSumAlgorithmType._CF_enumeration.addEnumeration(unicode_value='SHA', tag='SHA')
HashSumAlgorithmType.SHA1 = HashSumAlgorithmType._CF_enumeration.addEnumeration(unicode_value='SHA1', tag='SHA1')
HashSumAlgorithmType.UserDefined = HashSumAlgorithmType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
HashSumAlgorithmType._InitializeFacetMap(HashSumAlgorithmType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'HashSumAlgorithmType', HashSumAlgorithmType)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}ImageCodecType
class ImageCodecType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of ImageCodec."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ImageCodecType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 821, 4)
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

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}ImageType
class ImageType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Image."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ImageType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 835, 4)
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

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}InvoiceAvailabilityStatus
class InvoiceAvailabilityStatus (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A status of the availability of a Invoice."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InvoiceAvailabilityStatus')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 856, 4)
    _Documentation = 'A status of the availability of a Invoice.'
InvoiceAvailabilityStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=InvoiceAvailabilityStatus, enum_prefix=None)
InvoiceAvailabilityStatus.InvoiceAvailable = InvoiceAvailabilityStatus._CF_enumeration.addEnumeration(unicode_value='InvoiceAvailable', tag='InvoiceAvailable')
InvoiceAvailabilityStatus.InvoiceNotAvailable = InvoiceAvailabilityStatus._CF_enumeration.addEnumeration(unicode_value='InvoiceNotAvailable', tag='InvoiceNotAvailable')
InvoiceAvailabilityStatus._InitializeFacetMap(InvoiceAvailabilityStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'InvoiceAvailabilityStatus', InvoiceAvailabilityStatus)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}InvoiceSupportInformationLicenseOrClaimReference
class InvoiceSupportInformationLicenseOrClaimReference (pyxb.binding.datatypes.IDREF):

    """A Reference to a License or Claim which is contained within a specific
                InvoiceSupportInformation."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InvoiceSupportInformationLicenseOrClaimReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 865, 4)
    _Documentation = 'A Reference to a License or Claim which is contained within a specific\n                InvoiceSupportInformation.'
InvoiceSupportInformationLicenseOrClaimReference._CF_pattern = pyxb.binding.facets.CF_pattern()
InvoiceSupportInformationLicenseOrClaimReference._CF_pattern.addPattern(pattern='L[\\d\\-_a-zA-Z]+')
InvoiceSupportInformationLicenseOrClaimReference._InitializeFacetMap(InvoiceSupportInformationLicenseOrClaimReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'InvoiceSupportInformationLicenseOrClaimReference', InvoiceSupportInformationLicenseOrClaimReference)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}LicenseOrClaimConditionReference
class LicenseOrClaimConditionReference (pyxb.binding.datatypes.ID):

    """A Reference to a LicenseOrClaimCondition."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LicenseOrClaimConditionReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 874, 4)
    _Documentation = 'A Reference to a LicenseOrClaimCondition.'
LicenseOrClaimConditionReference._CF_pattern = pyxb.binding.facets.CF_pattern()
LicenseOrClaimConditionReference._CF_pattern.addPattern(pattern='E[\\d\\-_a-zA-Z]+')
LicenseOrClaimConditionReference._InitializeFacetMap(LicenseOrClaimConditionReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'LicenseOrClaimConditionReference', LicenseOrClaimConditionReference)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}LicenseOrClaimReference
class LicenseOrClaimReference (pyxb.binding.datatypes.ID):

    """A Reference to a LicenseOrClaim."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LicenseOrClaimReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 882, 4)
    _Documentation = 'A Reference to a LicenseOrClaim.'
LicenseOrClaimReference._CF_pattern = pyxb.binding.facets.CF_pattern()
LicenseOrClaimReference._CF_pattern.addPattern(pattern='L[\\d\\-_a-zA-Z]+')
LicenseOrClaimReference._InitializeFacetMap(LicenseOrClaimReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'LicenseOrClaimReference', LicenseOrClaimReference)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}LicenseOrClaimReferenceToLicenseOrClaimCondition
class LicenseOrClaimReferenceToLicenseOrClaimCondition (pyxb.binding.datatypes.IDREF):

    """A Reference to a LicenseOrClaimCondition which is contained within a
                specific License or Claim."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LicenseOrClaimReferenceToLicenseOrClaimCondition')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 890, 4)
    _Documentation = 'A Reference to a LicenseOrClaimCondition which is contained within a\n                specific License or Claim.'
LicenseOrClaimReferenceToLicenseOrClaimCondition._CF_pattern = pyxb.binding.facets.CF_pattern()
LicenseOrClaimReferenceToLicenseOrClaimCondition._CF_pattern.addPattern(pattern='E[\\d\\-_a-zA-Z]+')
LicenseOrClaimReferenceToLicenseOrClaimCondition._InitializeFacetMap(LicenseOrClaimReferenceToLicenseOrClaimCondition._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'LicenseOrClaimReferenceToLicenseOrClaimCondition', LicenseOrClaimReferenceToLicenseOrClaimCondition)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}LicenseOrClaimRefusalReason
class LicenseOrClaimRefusalReason (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of reason for a refusing a License or Claim."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LicenseOrClaimRefusalReason')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 899, 4)
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
LicenseOrClaimRefusalReason._InitializeFacetMap(LicenseOrClaimRefusalReason._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'LicenseOrClaimRefusalReason', LicenseOrClaimRefusalReason)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}LicenseOrClaimReleaseReference
class LicenseOrClaimReleaseReference (pyxb.binding.datatypes.IDREF):

    """A Reference to a Release which is contained within a specific License
                or Claim."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LicenseOrClaimReleaseReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 944, 4)
    _Documentation = 'A Reference to a Release which is contained within a specific License\n                or Claim.'
LicenseOrClaimReleaseReference._CF_pattern = pyxb.binding.facets.CF_pattern()
LicenseOrClaimReleaseReference._CF_pattern.addPattern(pattern='R[\\d\\-_a-zA-Z]+')
LicenseOrClaimReleaseReference._InitializeFacetMap(LicenseOrClaimReleaseReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'LicenseOrClaimReleaseReference', LicenseOrClaimReleaseReference)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}LicenseOrClaimRequestUpdateReason
class LicenseOrClaimRequestUpdateReason (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of reason for a updating a License request."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LicenseOrClaimRequestUpdateReason')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 953, 4)
    _Documentation = 'A Type of reason for a updating a License request.'
LicenseOrClaimRequestUpdateReason._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=LicenseOrClaimRequestUpdateReason, enum_prefix=None)
LicenseOrClaimRequestUpdateReason.AdditionalInformationProvided = LicenseOrClaimRequestUpdateReason._CF_enumeration.addEnumeration(unicode_value='AdditionalInformationProvided', tag='AdditionalInformationProvided')
LicenseOrClaimRequestUpdateReason.AdditionalInformationProvidedAsRequested = LicenseOrClaimRequestUpdateReason._CF_enumeration.addEnumeration(unicode_value='AdditionalInformationProvidedAsRequested', tag='AdditionalInformationProvidedAsRequested')
LicenseOrClaimRequestUpdateReason.UserDefined = LicenseOrClaimRequestUpdateReason._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
LicenseOrClaimRequestUpdateReason._InitializeFacetMap(LicenseOrClaimRequestUpdateReason._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'LicenseOrClaimRequestUpdateReason', LicenseOrClaimRequestUpdateReason)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}LicenseOrClaimResourceReference
class LicenseOrClaimResourceReference (pyxb.binding.datatypes.IDREF):

    """A Reference to a Resource which is contained within a specific License
                or Claim."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LicenseOrClaimResourceReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 963, 4)
    _Documentation = 'A Reference to a Resource which is contained within a specific License\n                or Claim.'
LicenseOrClaimResourceReference._CF_pattern = pyxb.binding.facets.CF_pattern()
LicenseOrClaimResourceReference._CF_pattern.addPattern(pattern='A[\\d\\-_a-zA-Z]+')
LicenseOrClaimResourceReference._InitializeFacetMap(LicenseOrClaimResourceReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'LicenseOrClaimResourceReference', LicenseOrClaimResourceReference)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}LicenseOrClaimRightShareReference
class LicenseOrClaimRightShareReference (pyxb.binding.datatypes.IDREF):

    """A Reference to a RightShare which is contained within a specific
                License or Claim."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LicenseOrClaimRightShareReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 972, 4)
    _Documentation = 'A Reference to a RightShare which is contained within a specific\n                License or Claim.'
LicenseOrClaimRightShareReference._CF_pattern = pyxb.binding.facets.CF_pattern()
LicenseOrClaimRightShareReference._CF_pattern.addPattern(pattern='S[\\d\\-_a-zA-Z]+')
LicenseOrClaimRightShareReference._InitializeFacetMap(LicenseOrClaimRightShareReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'LicenseOrClaimRightShareReference', LicenseOrClaimRightShareReference)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}LicenseOrClaimUpdateReason
class LicenseOrClaimUpdateReason (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of reason for a updating a License."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LicenseOrClaimUpdateReason')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 981, 4)
    _Documentation = 'A Type of reason for a updating a License.'
LicenseOrClaimUpdateReason._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=LicenseOrClaimUpdateReason, enum_prefix=None)
LicenseOrClaimUpdateReason.NewLicenseIssued = LicenseOrClaimUpdateReason._CF_enumeration.addEnumeration(unicode_value='NewLicenseIssued', tag='NewLicenseIssued')
LicenseOrClaimUpdateReason.NewRightShareIdentified = LicenseOrClaimUpdateReason._CF_enumeration.addEnumeration(unicode_value='NewRightShareIdentified', tag='NewRightShareIdentified')
LicenseOrClaimUpdateReason.NewRightsholderIdentified = LicenseOrClaimUpdateReason._CF_enumeration.addEnumeration(unicode_value='NewRightsholderIdentified', tag='NewRightsholderIdentified')
LicenseOrClaimUpdateReason.NewWorkIdentified = LicenseOrClaimUpdateReason._CF_enumeration.addEnumeration(unicode_value='NewWorkIdentified', tag='NewWorkIdentified')
LicenseOrClaimUpdateReason.Revoked = LicenseOrClaimUpdateReason._CF_enumeration.addEnumeration(unicode_value='Revoked', tag='Revoked')
LicenseOrClaimUpdateReason.UserDefined = LicenseOrClaimUpdateReason._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
LicenseOrClaimUpdateReason._InitializeFacetMap(LicenseOrClaimUpdateReason._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'LicenseOrClaimUpdateReason', LicenseOrClaimUpdateReason)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}LicenseOrClaimWorkReference
class LicenseOrClaimWorkReference (pyxb.binding.datatypes.IDREF):

    """A Reference to a Work which is contained within a specific License or
                Claim."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LicenseOrClaimWorkReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 994, 4)
    _Documentation = 'A Reference to a Work which is contained within a specific License or\n                Claim.'
LicenseOrClaimWorkReference._CF_pattern = pyxb.binding.facets.CF_pattern()
LicenseOrClaimWorkReference._CF_pattern.addPattern(pattern='W[\\d\\-_a-zA-Z]+')
LicenseOrClaimWorkReference._InitializeFacetMap(LicenseOrClaimWorkReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'LicenseOrClaimWorkReference', LicenseOrClaimWorkReference)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}LicenseStatus
class LicenseStatus (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A legal status of a License for a Claim."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LicenseStatus')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1003, 4)
    _Documentation = 'A legal status of a License for a Claim.'
LicenseStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=LicenseStatus, enum_prefix=None)
LicenseStatus.Active = LicenseStatus._CF_enumeration.addEnumeration(unicode_value='Active', tag='Active')
LicenseStatus.Pending = LicenseStatus._CF_enumeration.addEnumeration(unicode_value='Pending', tag='Pending')
LicenseStatus.Revoked = LicenseStatus._CF_enumeration.addEnumeration(unicode_value='Revoked', tag='Revoked')
LicenseStatus._InitializeFacetMap(LicenseStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'LicenseStatus', LicenseStatus)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}LicensingProcessStatus
class LicensingProcessStatus (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An operational status of a licensing process."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LicensingProcessStatus')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1013, 4)
    _Documentation = 'An operational status of a licensing process.'
LicensingProcessStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=LicensingProcessStatus, enum_prefix=None)
LicensingProcessStatus.Pending = LicensingProcessStatus._CF_enumeration.addEnumeration(unicode_value='Pending', tag='Pending')
LicensingProcessStatus.Processed = LicensingProcessStatus._CF_enumeration.addEnumeration(unicode_value='Processed', tag='Processed')
LicensingProcessStatus.ThirdPartyInformationRequested = LicensingProcessStatus._CF_enumeration.addEnumeration(unicode_value='ThirdPartyInformationRequested', tag='ThirdPartyInformationRequested')
LicensingProcessStatus._InitializeFacetMap(LicensingProcessStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'LicensingProcessStatus', LicensingProcessStatus)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}LocalCollectionAnchor
class LocalCollectionAnchor (pyxb.binding.datatypes.ID):

    """A LocalAnchor which acts as a local Identifier of a Collection. This
                LocalAnchor is a string starting with the letter X."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LocalCollectionAnchor')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1023, 4)
    _Documentation = 'A LocalAnchor which acts as a local Identifier of a Collection. This\n                LocalAnchor is a string starting with the letter X.'
LocalCollectionAnchor._CF_pattern = pyxb.binding.facets.CF_pattern()
LocalCollectionAnchor._CF_pattern.addPattern(pattern='X[\\d\\-_a-zA-Z]+')
LocalCollectionAnchor._InitializeFacetMap(LocalCollectionAnchor._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'LocalCollectionAnchor', LocalCollectionAnchor)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}LocalCollectionAnchorReference
class LocalCollectionAnchorReference (pyxb.binding.datatypes.IDREF):

    """A LocalAnchorReference which acts as a reference to a local Identifier
                of a Collection. This LocalAnchorReference is a string starting with the letter
                X."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LocalCollectionAnchorReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1032, 4)
    _Documentation = 'A LocalAnchorReference which acts as a reference to a local Identifier\n                of a Collection. This LocalAnchorReference is a string starting with the letter\n                X.'
LocalCollectionAnchorReference._CF_pattern = pyxb.binding.facets.CF_pattern()
LocalCollectionAnchorReference._CF_pattern.addPattern(pattern='X[\\d\\-_a-zA-Z]+')
LocalCollectionAnchorReference._InitializeFacetMap(LocalCollectionAnchorReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'LocalCollectionAnchorReference', LocalCollectionAnchorReference)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}LocalCueSheetAnchor
class LocalCueSheetAnchor (pyxb.binding.datatypes.ID):

    """A LocalAnchor which acts as a local Identifier of a CueSheet. This
                LocalAnchor is a string starting with the letter Q."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LocalCueSheetAnchor')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1042, 4)
    _Documentation = 'A LocalAnchor which acts as a local Identifier of a CueSheet. This\n                LocalAnchor is a string starting with the letter Q.'
LocalCueSheetAnchor._CF_pattern = pyxb.binding.facets.CF_pattern()
LocalCueSheetAnchor._CF_pattern.addPattern(pattern='Q[\\d\\-_a-zA-Z]+')
LocalCueSheetAnchor._InitializeFacetMap(LocalCueSheetAnchor._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'LocalCueSheetAnchor', LocalCueSheetAnchor)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}LocalCueSheetAnchorReference
class LocalCueSheetAnchorReference (pyxb.binding.datatypes.IDREF):

    """A LocalAnchorReference which acts as a reference to a local Identifier
                of a CueSheet. This LocalAnchorReference is a string starting with the letter
                Q."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LocalCueSheetAnchorReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1051, 4)
    _Documentation = 'A LocalAnchorReference which acts as a reference to a local Identifier\n                of a CueSheet. This LocalAnchorReference is a string starting with the letter\n                Q.'
LocalCueSheetAnchorReference._CF_pattern = pyxb.binding.facets.CF_pattern()
LocalCueSheetAnchorReference._CF_pattern.addPattern(pattern='Q[\\d\\-_a-zA-Z]+')
LocalCueSheetAnchorReference._InitializeFacetMap(LocalCueSheetAnchorReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'LocalCueSheetAnchorReference', LocalCueSheetAnchorReference)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}LocalLicenseOrClaimAnchor
class LocalLicenseOrClaimAnchor (pyxb.binding.datatypes.ID):

    """A LocalAnchor which acts as a local Identifier of a LicenseOrClaim.
                This LocalAnchor is a string starting with the letter L."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LocalLicenseOrClaimAnchor')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1061, 4)
    _Documentation = 'A LocalAnchor which acts as a local Identifier of a LicenseOrClaim.\n                This LocalAnchor is a string starting with the letter L.'
LocalLicenseOrClaimAnchor._CF_pattern = pyxb.binding.facets.CF_pattern()
LocalLicenseOrClaimAnchor._CF_pattern.addPattern(pattern='L[\\d\\-_a-zA-Z]+')
LocalLicenseOrClaimAnchor._InitializeFacetMap(LocalLicenseOrClaimAnchor._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'LocalLicenseOrClaimAnchor', LocalLicenseOrClaimAnchor)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}LocalLicenseOrClaimAnchorReference
class LocalLicenseOrClaimAnchorReference (pyxb.binding.datatypes.IDREF):

    """A LocalAnchorReference which acts as a reference to a local Identifier
                of a LicenseOrClaim. This LocalAnchorReference is a string starting with the letter
                L."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LocalLicenseOrClaimAnchorReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1070, 4)
    _Documentation = 'A LocalAnchorReference which acts as a reference to a local Identifier\n                of a LicenseOrClaim. This LocalAnchorReference is a string starting with the letter\n                L.'
LocalLicenseOrClaimAnchorReference._CF_pattern = pyxb.binding.facets.CF_pattern()
LocalLicenseOrClaimAnchorReference._CF_pattern.addPattern(pattern='L[\\d\\-_a-zA-Z]+')
LocalLicenseOrClaimAnchorReference._InitializeFacetMap(LocalLicenseOrClaimAnchorReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'LocalLicenseOrClaimAnchorReference', LocalLicenseOrClaimAnchorReference)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}LocalLicenseOrClaimConditionAnchor
class LocalLicenseOrClaimConditionAnchor (pyxb.binding.datatypes.ID):

    """A LocalAnchor which acts as a local Identifier of a
                LicenseOrClaimCondition. This LocalAnchor is a string starting with the letter
                E."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LocalLicenseOrClaimConditionAnchor')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1080, 4)
    _Documentation = 'A LocalAnchor which acts as a local Identifier of a\n                LicenseOrClaimCondition. This LocalAnchor is a string starting with the letter\n                E.'
LocalLicenseOrClaimConditionAnchor._CF_pattern = pyxb.binding.facets.CF_pattern()
LocalLicenseOrClaimConditionAnchor._CF_pattern.addPattern(pattern='E[\\d\\-_a-zA-Z]+')
LocalLicenseOrClaimConditionAnchor._InitializeFacetMap(LocalLicenseOrClaimConditionAnchor._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'LocalLicenseOrClaimConditionAnchor', LocalLicenseOrClaimConditionAnchor)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}LocalLicenseOrClaimConditionAnchorReference
class LocalLicenseOrClaimConditionAnchorReference (pyxb.binding.datatypes.IDREF):

    """A LocalAnchorReference which acts as a reference to a local Identifier
                of a LicenseOrClaimCondition. This LocalAnchorReference is a string starting with
                the letter E."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LocalLicenseOrClaimConditionAnchorReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1090, 4)
    _Documentation = 'A LocalAnchorReference which acts as a reference to a local Identifier\n                of a LicenseOrClaimCondition. This LocalAnchorReference is a string starting with\n                the letter E.'
LocalLicenseOrClaimConditionAnchorReference._CF_pattern = pyxb.binding.facets.CF_pattern()
LocalLicenseOrClaimConditionAnchorReference._CF_pattern.addPattern(pattern='E[\\d\\-_a-zA-Z]+')
LocalLicenseOrClaimConditionAnchorReference._InitializeFacetMap(LocalLicenseOrClaimConditionAnchorReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'LocalLicenseOrClaimConditionAnchorReference', LocalLicenseOrClaimConditionAnchorReference)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}LocalMusicalWorkAnchor
class LocalMusicalWorkAnchor (pyxb.binding.datatypes.ID):

    """A LocalAnchor which acts as a local Identifier of a MusicalWork. This
                LocalAnchor is a string starting with the letter W."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LocalMusicalWorkAnchor')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1100, 4)
    _Documentation = 'A LocalAnchor which acts as a local Identifier of a MusicalWork. This\n                LocalAnchor is a string starting with the letter W.'
LocalMusicalWorkAnchor._CF_pattern = pyxb.binding.facets.CF_pattern()
LocalMusicalWorkAnchor._CF_pattern.addPattern(pattern='W[\\d\\-_a-zA-Z]+')
LocalMusicalWorkAnchor._InitializeFacetMap(LocalMusicalWorkAnchor._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'LocalMusicalWorkAnchor', LocalMusicalWorkAnchor)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}LocalMusicalWorkAnchorReference
class LocalMusicalWorkAnchorReference (pyxb.binding.datatypes.IDREF):

    """A LocalAnchorReference which acts as a reference to a local Identifier
                of a MusicalWork. This LocalAnchorReference is a string starting with the letter
                W."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LocalMusicalWorkAnchorReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1109, 4)
    _Documentation = 'A LocalAnchorReference which acts as a reference to a local Identifier\n                of a MusicalWork. This LocalAnchorReference is a string starting with the letter\n                W.'
LocalMusicalWorkAnchorReference._CF_pattern = pyxb.binding.facets.CF_pattern()
LocalMusicalWorkAnchorReference._CF_pattern.addPattern(pattern='W[\\d\\-_a-zA-Z]+')
LocalMusicalWorkAnchorReference._InitializeFacetMap(LocalMusicalWorkAnchorReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'LocalMusicalWorkAnchorReference', LocalMusicalWorkAnchorReference)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}LocalReleaseAnchor
class LocalReleaseAnchor (pyxb.binding.datatypes.ID):

    """A LocalAnchor which acts as a local Identifier of a Release. This
                LocalAnchor is a string starting with the letter R."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LocalReleaseAnchor')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1119, 4)
    _Documentation = 'A LocalAnchor which acts as a local Identifier of a Release. This\n                LocalAnchor is a string starting with the letter R.'
LocalReleaseAnchor._CF_pattern = pyxb.binding.facets.CF_pattern()
LocalReleaseAnchor._CF_pattern.addPattern(pattern='R[\\d\\-_a-zA-Z]+')
LocalReleaseAnchor._InitializeFacetMap(LocalReleaseAnchor._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'LocalReleaseAnchor', LocalReleaseAnchor)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}LocalReleaseAnchorReference
class LocalReleaseAnchorReference (pyxb.binding.datatypes.IDREF):

    """A LocalAnchorReference which acts as a reference to a local Identifier
                of a Release. This LocalAnchorReference is a string starting with the letter
                R."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LocalReleaseAnchorReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1128, 4)
    _Documentation = 'A LocalAnchorReference which acts as a reference to a local Identifier\n                of a Release. This LocalAnchorReference is a string starting with the letter\n                R.'
LocalReleaseAnchorReference._CF_pattern = pyxb.binding.facets.CF_pattern()
LocalReleaseAnchorReference._CF_pattern.addPattern(pattern='R[\\d\\-_a-zA-Z]+')
LocalReleaseAnchorReference._InitializeFacetMap(LocalReleaseAnchorReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'LocalReleaseAnchorReference', LocalReleaseAnchorReference)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}LocalResourceAnchor
class LocalResourceAnchor (pyxb.binding.datatypes.ID):

    """A LocalAnchor which acts as a local Identifier of a Resource. This
                LocalAnchor is a string starting with the letter A."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LocalResourceAnchor')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1138, 4)
    _Documentation = 'A LocalAnchor which acts as a local Identifier of a Resource. This\n                LocalAnchor is a string starting with the letter A.'
LocalResourceAnchor._CF_pattern = pyxb.binding.facets.CF_pattern()
LocalResourceAnchor._CF_pattern.addPattern(pattern='A[\\d\\-_a-zA-Z]+')
LocalResourceAnchor._InitializeFacetMap(LocalResourceAnchor._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'LocalResourceAnchor', LocalResourceAnchor)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}LocalResourceAnchorReference
class LocalResourceAnchorReference (pyxb.binding.datatypes.IDREF):

    """A LocalAnchorReference which acts as a reference to a local Identifier
                of a Resource. This LocalAnchorReference is a string starting with the letter
                A."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LocalResourceAnchorReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1147, 4)
    _Documentation = 'A LocalAnchorReference which acts as a reference to a local Identifier\n                of a Resource. This LocalAnchorReference is a string starting with the letter\n                A.'
LocalResourceAnchorReference._CF_pattern = pyxb.binding.facets.CF_pattern()
LocalResourceAnchorReference._CF_pattern.addPattern(pattern='A[\\d\\-_a-zA-Z]+')
LocalResourceAnchorReference._InitializeFacetMap(LocalResourceAnchorReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'LocalResourceAnchorReference', LocalResourceAnchorReference)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}LocalRightShareAnchor
class LocalRightShareAnchor (pyxb.binding.datatypes.ID):

    """A LocalAnchor which acts as a local Identifier of a RightShare. This
                LocalAnchor is a string starting with the letter S."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LocalRightShareAnchor')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1157, 4)
    _Documentation = 'A LocalAnchor which acts as a local Identifier of a RightShare. This\n                LocalAnchor is a string starting with the letter S.'
LocalRightShareAnchor._CF_pattern = pyxb.binding.facets.CF_pattern()
LocalRightShareAnchor._CF_pattern.addPattern(pattern='S[\\d\\-_a-zA-Z]+')
LocalRightShareAnchor._InitializeFacetMap(LocalRightShareAnchor._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'LocalRightShareAnchor', LocalRightShareAnchor)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}LocalRightShareAnchorReference
class LocalRightShareAnchorReference (pyxb.binding.datatypes.IDREF):

    """A LocalAnchorReference which acts as a reference to a local Identifier
                of a RightShare. This LocalAnchorReference is a string starting with the letter
                S."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LocalRightShareAnchorReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1166, 4)
    _Documentation = 'A LocalAnchorReference which acts as a reference to a local Identifier\n                of a RightShare. This LocalAnchorReference is a string starting with the letter\n                S.'
LocalRightShareAnchorReference._CF_pattern = pyxb.binding.facets.CF_pattern()
LocalRightShareAnchorReference._CF_pattern.addPattern(pattern='S[\\d\\-_a-zA-Z]+')
LocalRightShareAnchorReference._InitializeFacetMap(LocalRightShareAnchorReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'LocalRightShareAnchorReference', LocalRightShareAnchorReference)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}LocalTechnicalResourceDetailsAnchor
class LocalTechnicalResourceDetailsAnchor (pyxb.binding.datatypes.ID):

    """A LocalAnchor which acts as a local Identifier of a
                TechnicalResourceDetails Composite. This LocalAnchor is a string starting with the
                letter T."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LocalTechnicalResourceDetailsAnchor')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1176, 4)
    _Documentation = 'A LocalAnchor which acts as a local Identifier of a\n                TechnicalResourceDetails Composite. This LocalAnchor is a string starting with the\n                letter T.'
LocalTechnicalResourceDetailsAnchor._CF_pattern = pyxb.binding.facets.CF_pattern()
LocalTechnicalResourceDetailsAnchor._CF_pattern.addPattern(pattern='T[\\d\\-_a-zA-Z]+')
LocalTechnicalResourceDetailsAnchor._InitializeFacetMap(LocalTechnicalResourceDetailsAnchor._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'LocalTechnicalResourceDetailsAnchor', LocalTechnicalResourceDetailsAnchor)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}LocalTechnicalResourceDetailsAnchorReference
class LocalTechnicalResourceDetailsAnchorReference (pyxb.binding.datatypes.IDREF):

    """A LocalAnchorReference which acts as a reference to a local Identifier
                of a TechnicalResourceDetails Composite. This LocalAnchorReference is a string
                starting with the letter T."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LocalTechnicalResourceDetailsAnchorReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1186, 4)
    _Documentation = 'A LocalAnchorReference which acts as a reference to a local Identifier\n                of a TechnicalResourceDetails Composite. This LocalAnchorReference is a string\n                starting with the letter T.'
LocalTechnicalResourceDetailsAnchorReference._CF_pattern = pyxb.binding.facets.CF_pattern()
LocalTechnicalResourceDetailsAnchorReference._CF_pattern.addPattern(pattern='T[\\d\\-_a-zA-Z]+')
LocalTechnicalResourceDetailsAnchorReference._InitializeFacetMap(LocalTechnicalResourceDetailsAnchorReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'LocalTechnicalResourceDetailsAnchorReference', LocalTechnicalResourceDetailsAnchorReference)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}MembershipType
class MembershipType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of membership."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MembershipType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1196, 4)
    _Documentation = 'A Type of membership.'
MembershipType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MembershipType, enum_prefix=None)
MembershipType.NationalMember = MembershipType._CF_enumeration.addEnumeration(unicode_value='NationalMember', tag='NationalMember')
MembershipType.RegionalMember = MembershipType._CF_enumeration.addEnumeration(unicode_value='RegionalMember', tag='RegionalMember')
MembershipType.WorldwideMember = MembershipType._CF_enumeration.addEnumeration(unicode_value='WorldwideMember', tag='WorldwideMember')
MembershipType._InitializeFacetMap(MembershipType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MembershipType', MembershipType)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}MessageActionType
class MessageActionType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of action requested in a Message."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MessageActionType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1206, 4)
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

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}MessageContentRevenueType
class MessageContentRevenueType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of revenue to which the content of the Message
                relates."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MessageContentRevenueType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1219, 4)
    _Documentation = 'A Type of revenue to which the content of the Message\n                relates.'
MessageContentRevenueType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MessageContentRevenueType, enum_prefix=None)
MessageContentRevenueType.NonTransactionalRevenue = MessageContentRevenueType._CF_enumeration.addEnumeration(unicode_value='NonTransactionalRevenue', tag='NonTransactionalRevenue')
MessageContentRevenueType.TransactionalRevenue = MessageContentRevenueType._CF_enumeration.addEnumeration(unicode_value='TransactionalRevenue', tag='TransactionalRevenue')
MessageContentRevenueType.UserDefined = MessageContentRevenueType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
MessageContentRevenueType._InitializeFacetMap(MessageContentRevenueType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MessageContentRevenueType', MessageContentRevenueType)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}MessageControlType
class MessageControlType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Message according to its operational
                status."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MessageControlType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1230, 4)
    _Documentation = 'A Type of Message according to its operational\n                status.'
MessageControlType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MessageControlType, enum_prefix=None)
MessageControlType.LiveMessage = MessageControlType._CF_enumeration.addEnumeration(unicode_value='LiveMessage', tag='LiveMessage')
MessageControlType.TestMessage = MessageControlType._CF_enumeration.addEnumeration(unicode_value='TestMessage', tag='TestMessage')
MessageControlType._InitializeFacetMap(MessageControlType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MessageControlType', MessageControlType)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}MessageType
class MessageType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Message in a DDEX namespace."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MessageType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1240, 4)
    _Documentation = 'A Type of Message in a DDEX namespace.'
MessageType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MessageType, enum_prefix=None)
MessageType.SalesReportToRecordCompanyMessage = MessageType._CF_enumeration.addEnumeration(unicode_value='SalesReportToRecordCompanyMessage', tag='SalesReportToRecordCompanyMessage')
MessageType.SalesReportToSocietyMessage = MessageType._CF_enumeration.addEnumeration(unicode_value='SalesReportToSocietyMessage', tag='SalesReportToSocietyMessage')
MessageType.InvoiceMessage = MessageType._CF_enumeration.addEnumeration(unicode_value='InvoiceMessage', tag='InvoiceMessage')
MessageType.NewReleaseMessage = MessageType._CF_enumeration.addEnumeration(unicode_value='NewReleaseMessage', tag='NewReleaseMessage')
MessageType.CatalogListMessage = MessageType._CF_enumeration.addEnumeration(unicode_value='CatalogListMessage', tag='CatalogListMessage')
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
MessageType.SalesReportMessage = MessageType._CF_enumeration.addEnumeration(unicode_value='SalesReportMessage', tag='SalesReportMessage')
MessageType.WsAcknowledgementMessage = MessageType._CF_enumeration.addEnumeration(unicode_value='WsAcknowledgementMessage', tag='WsAcknowledgementMessage')
MessageType.FtpAcknowledgementMessage_ = MessageType._CF_enumeration.addEnumeration(unicode_value='FtpAcknowledgementMessage', tag='FtpAcknowledgementMessage_')
MessageType.ManifestMessage = MessageType._CF_enumeration.addEnumeration(unicode_value='ManifestMessage', tag='ManifestMessage')
MessageType.ReleaseStatusInformationMessage = MessageType._CF_enumeration.addEnumeration(unicode_value='ReleaseStatusInformationMessage', tag='ReleaseStatusInformationMessage')
MessageType.OrderedReleaseInQueueRequestMessage = MessageType._CF_enumeration.addEnumeration(unicode_value='OrderedReleaseInQueueRequestMessage', tag='OrderedReleaseInQueueRequestMessage')
MessageType.RedeliveryRequestMessage = MessageType._CF_enumeration.addEnumeration(unicode_value='RedeliveryRequestMessage', tag='RedeliveryRequestMessage')
MessageType.SupplyChainStatusMessage = MessageType._CF_enumeration.addEnumeration(unicode_value='SupplyChainStatusMessage', tag='SupplyChainStatusMessage')
MessageType.ReleaseAvailabilityMessage = MessageType._CF_enumeration.addEnumeration(unicode_value='ReleaseAvailabilityMessage', tag='ReleaseAvailabilityMessage')
MessageType.InformationAboutDeliveredAndAvailableReleasesRequestMessage = MessageType._CF_enumeration.addEnumeration(unicode_value='InformationAboutDeliveredAndAvailableReleasesRequestMessage', tag='InformationAboutDeliveredAndAvailableReleasesRequestMessage')
MessageType.DeliveryFrequencyChangeRequestMessage = MessageType._CF_enumeration.addEnumeration(unicode_value='DeliveryFrequencyChangeRequestMessage', tag='DeliveryFrequencyChangeRequestMessage')
MessageType.ReportRequestMessage = MessageType._CF_enumeration.addEnumeration(unicode_value='ReportRequestMessage', tag='ReportRequestMessage')
MessageType.ReportDeliveryMessage = MessageType._CF_enumeration.addEnumeration(unicode_value='ReportDeliveryMessage', tag='ReportDeliveryMessage')
MessageType.ReleaseAvailabilityResponseMessage = MessageType._CF_enumeration.addEnumeration(unicode_value='ReleaseAvailabilityResponseMessage', tag='ReleaseAvailabilityResponseMessage')
MessageType.OrderedReleaseInQueueResponseMessage = MessageType._CF_enumeration.addEnumeration(unicode_value='OrderedReleaseInQueueResponseMessage', tag='OrderedReleaseInQueueResponseMessage')
MessageType.RedeliveryResponseMessage = MessageType._CF_enumeration.addEnumeration(unicode_value='RedeliveryResponseMessage', tag='RedeliveryResponseMessage')
MessageType.InformationAboutDeliveredAndAvailableReleasesResponseMessage = MessageType._CF_enumeration.addEnumeration(unicode_value='InformationAboutDeliveredAndAvailableReleasesResponseMessage', tag='InformationAboutDeliveredAndAvailableReleasesResponseMessage')
MessageType.DeliveryFrequencyChangeResponseMessage = MessageType._CF_enumeration.addEnumeration(unicode_value='DeliveryFrequencyChangeResponseMessage', tag='DeliveryFrequencyChangeResponseMessage')
MessageType.ReportResponseMessage = MessageType._CF_enumeration.addEnumeration(unicode_value='ReportResponseMessage', tag='ReportResponseMessage')
MessageType.ReleaseAvailabilityRequestMessage = MessageType._CF_enumeration.addEnumeration(unicode_value='ReleaseAvailabilityRequestMessage', tag='ReleaseAvailabilityRequestMessage')
MessageType.ReleaseStatusRequestMessage = MessageType._CF_enumeration.addEnumeration(unicode_value='ReleaseStatusRequestMessage', tag='ReleaseStatusRequestMessage')
MessageType.ReleaseSupplyChainStatusRequestMessage = MessageType._CF_enumeration.addEnumeration(unicode_value='ReleaseSupplyChainStatusRequestMessage', tag='ReleaseSupplyChainStatusRequestMessage')
MessageType.ReleaseSupplyChainStatusResponseMessage = MessageType._CF_enumeration.addEnumeration(unicode_value='ReleaseSupplyChainStatusResponseMessage', tag='ReleaseSupplyChainStatusResponseMessage')
MessageType.ReleaseAvailabilityResponseMessage_ = MessageType._CF_enumeration.addEnumeration(unicode_value='ReleaseAvailabilityResponseMessage', tag='ReleaseAvailabilityResponseMessage_')
MessageType.OrderedReleaseInQueueResponseMessage_ = MessageType._CF_enumeration.addEnumeration(unicode_value='OrderedReleaseInQueueResponseMessage', tag='OrderedReleaseInQueueResponseMessage_')
MessageType.RedeliveryResponseMessage_ = MessageType._CF_enumeration.addEnumeration(unicode_value='RedeliveryResponseMessage', tag='RedeliveryResponseMessage_')
MessageType.InformationAboutDeliveredAndAvailableReleasesResponseMessage_ = MessageType._CF_enumeration.addEnumeration(unicode_value='InformationAboutDeliveredAndAvailableReleasesResponseMessage', tag='InformationAboutDeliveredAndAvailableReleasesResponseMessage_')
MessageType.DeliveryFrequencyChangeResponseMessage_ = MessageType._CF_enumeration.addEnumeration(unicode_value='DeliveryFrequencyChangeResponseMessage', tag='DeliveryFrequencyChangeResponseMessage_')
MessageType.ReportResponseMessage_ = MessageType._CF_enumeration.addEnumeration(unicode_value='ReportResponseMessage', tag='ReportResponseMessage_')
MessageType.ReleaseAvailabilityRequestMessage_ = MessageType._CF_enumeration.addEnumeration(unicode_value='ReleaseAvailabilityRequestMessage', tag='ReleaseAvailabilityRequestMessage_')
MessageType.ReleaseStatusRequestMessage_ = MessageType._CF_enumeration.addEnumeration(unicode_value='ReleaseStatusRequestMessage', tag='ReleaseStatusRequestMessage_')
MessageType.ReleaseSupplyChainStatusRequestMessage_ = MessageType._CF_enumeration.addEnumeration(unicode_value='ReleaseSupplyChainStatusRequestMessage', tag='ReleaseSupplyChainStatusRequestMessage_')
MessageType.ReleaseSupplyChainStatusResponseMessage_ = MessageType._CF_enumeration.addEnumeration(unicode_value='ReleaseSupplyChainStatusResponseMessage', tag='ReleaseSupplyChainStatusResponseMessage_')
MessageType.InformationAboutDeliveredAndAvailableReleasesReportMessage = MessageType._CF_enumeration.addEnumeration(unicode_value='InformationAboutDeliveredAndAvailableReleasesReportMessage', tag='InformationAboutDeliveredAndAvailableReleasesReportMessage')
MessageType.ReleasesInQueueReportMessage = MessageType._CF_enumeration.addEnumeration(unicode_value='ReleasesInQueueReportMessage', tag='ReleasesInQueueReportMessage')
MessageType.ManifestMessage_ = MessageType._CF_enumeration.addEnumeration(unicode_value='ManifestMessage', tag='ManifestMessage_')
MessageType.ManifestMessage_2 = MessageType._CF_enumeration.addEnumeration(unicode_value='ManifestMessage', tag='ManifestMessage_2')
MessageType.SalesReportDeliveryMessage = MessageType._CF_enumeration.addEnumeration(unicode_value='SalesReportDeliveryMessage', tag='SalesReportDeliveryMessage')
MessageType.InvoiceDeliveryMessage = MessageType._CF_enumeration.addEnumeration(unicode_value='InvoiceDeliveryMessage', tag='InvoiceDeliveryMessage')
MessageType.SalesReportRequestMessage = MessageType._CF_enumeration.addEnumeration(unicode_value='SalesReportRequestMessage', tag='SalesReportRequestMessage')
MessageType.InvoiceRequestMessage = MessageType._CF_enumeration.addEnumeration(unicode_value='InvoiceRequestMessage', tag='InvoiceRequestMessage')
MessageType.InvoiceAcknowledgementRequestMessage = MessageType._CF_enumeration.addEnumeration(unicode_value='InvoiceAcknowledgementRequestMessage', tag='InvoiceAcknowledgementRequestMessage')
MessageType.SalesReportDeliveryAcknowledgementMessage = MessageType._CF_enumeration.addEnumeration(unicode_value='SalesReportDeliveryAcknowledgementMessage', tag='SalesReportDeliveryAcknowledgementMessage')
MessageType.InvoiceDeliveryAcknowledgementMessage = MessageType._CF_enumeration.addEnumeration(unicode_value='InvoiceDeliveryAcknowledgementMessage', tag='InvoiceDeliveryAcknowledgementMessage')
MessageType.ManifestMessage_3 = MessageType._CF_enumeration.addEnumeration(unicode_value='ManifestMessage', tag='ManifestMessage_3')
MessageType.ContractDeliveryMessage = MessageType._CF_enumeration.addEnumeration(unicode_value='ContractDeliveryMessage', tag='ContractDeliveryMessage')
MessageType.ProductDeletionMessage = MessageType._CF_enumeration.addEnumeration(unicode_value='ProductDeletionMessage', tag='ProductDeletionMessage')
MessageType.DeclarationOfSoundRecordingRightsClaimMessage = MessageType._CF_enumeration.addEnumeration(unicode_value='DeclarationOfSoundRecordingRightsClaimMessage', tag='DeclarationOfSoundRecordingRightsClaimMessage')
MessageType.RequestSoundRecordingInformationMessage = MessageType._CF_enumeration.addEnumeration(unicode_value='RequestSoundRecordingInformationMessage', tag='RequestSoundRecordingInformationMessage')
MessageType.RevokeSoundRecordingRightsClaimMessage = MessageType._CF_enumeration.addEnumeration(unicode_value='RevokeSoundRecordingRightsClaimMessage', tag='RevokeSoundRecordingRightsClaimMessage')
MessageType.SalesReportMessage_ = MessageType._CF_enumeration.addEnumeration(unicode_value='SalesReportMessage', tag='SalesReportMessage_')
MessageType.DeclarationOfRevenueMessage = MessageType._CF_enumeration.addEnumeration(unicode_value='DeclarationOfRevenueMessage', tag='DeclarationOfRevenueMessage')
MessageType.ManifestMessage_4 = MessageType._CF_enumeration.addEnumeration(unicode_value='ManifestMessage', tag='ManifestMessage_4')
MessageType._InitializeFacetMap(MessageType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MessageType', MessageType)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}MidiType
class MidiType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of MIDI."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MidiType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1317, 4)
    _Documentation = 'A Type of MIDI.'
MidiType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MidiType, enum_prefix=None)
MidiType.MonophonicMidi = MidiType._CF_enumeration.addEnumeration(unicode_value='MonophonicMidi', tag='MonophonicMidi')
MidiType.PolyphonicMidi = MidiType._CF_enumeration.addEnumeration(unicode_value='PolyphonicMidi', tag='PolyphonicMidi')
MidiType.Unknown = MidiType._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
MidiType.UserDefined = MidiType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
MidiType._InitializeFacetMap(MidiType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MidiType', MidiType)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}MlcmMessageType
class MlcmMessageType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Message in the Music Licensing Company Message
                Suite."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MlcmMessageType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1328, 4)
    _Documentation = 'A Type of Message in the Music Licensing Company Message\n                Suite.'
MlcmMessageType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MlcmMessageType, enum_prefix=None)
MlcmMessageType.DeclarationOfSoundRecordingRightsClaimMessage = MlcmMessageType._CF_enumeration.addEnumeration(unicode_value='DeclarationOfSoundRecordingRightsClaimMessage', tag='DeclarationOfSoundRecordingRightsClaimMessage')
MlcmMessageType.RequestSoundRecordingInformationMessage = MlcmMessageType._CF_enumeration.addEnumeration(unicode_value='RequestSoundRecordingInformationMessage', tag='RequestSoundRecordingInformationMessage')
MlcmMessageType.RevokeSoundRecordingRightsClaimMessage = MlcmMessageType._CF_enumeration.addEnumeration(unicode_value='RevokeSoundRecordingRightsClaimMessage', tag='RevokeSoundRecordingRightsClaimMessage')
MlcmMessageType.SalesReportMessage = MlcmMessageType._CF_enumeration.addEnumeration(unicode_value='SalesReportMessage', tag='SalesReportMessage')
MlcmMessageType.DeclarationOfRevenueMessage = MlcmMessageType._CF_enumeration.addEnumeration(unicode_value='DeclarationOfRevenueMessage', tag='DeclarationOfRevenueMessage')
MlcmMessageType._InitializeFacetMap(MlcmMessageType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MlcmMessageType', MlcmMessageType)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}MusicalWorkContributorRole
class MusicalWorkContributorRole (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A role played by a Contributor in relation to a
                MusicalWork."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MusicalWorkContributorRole')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1341, 4)
    _Documentation = 'A role played by a Contributor in relation to a\n                MusicalWork.'
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

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}MusicalWorkReference
class MusicalWorkReference (pyxb.binding.datatypes.ID):

    """A Reference to a MusicalWork."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MusicalWorkReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1367, 4)
    _Documentation = 'A Reference to a MusicalWork.'
MusicalWorkReference._CF_pattern = pyxb.binding.facets.CF_pattern()
MusicalWorkReference._CF_pattern.addPattern(pattern='W[\\d\\-_a-zA-Z]+')
MusicalWorkReference._InitializeFacetMap(MusicalWorkReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'MusicalWorkReference', MusicalWorkReference)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}MusicalWorkRightsClaimType
class MusicalWorkRightsClaimType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of RightsClaim related to a MusicalWork."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MusicalWorkRightsClaimType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1375, 4)
    _Documentation = 'A Type of RightsClaim related to a MusicalWork.'
MusicalWorkRightsClaimType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MusicalWorkRightsClaimType, enum_prefix=None)
MusicalWorkRightsClaimType.CopyrightControl = MusicalWorkRightsClaimType._CF_enumeration.addEnumeration(unicode_value='CopyrightControl', tag='CopyrightControl')
MusicalWorkRightsClaimType.NonMemberClaim = MusicalWorkRightsClaimType._CF_enumeration.addEnumeration(unicode_value='NonMemberClaim', tag='NonMemberClaim')
MusicalWorkRightsClaimType.PublicDomain = MusicalWorkRightsClaimType._CF_enumeration.addEnumeration(unicode_value='PublicDomain', tag='PublicDomain')
MusicalWorkRightsClaimType.SocietyClaim = MusicalWorkRightsClaimType._CF_enumeration.addEnumeration(unicode_value='SocietyClaim', tag='SocietyClaim')
MusicalWorkRightsClaimType.Unknown = MusicalWorkRightsClaimType._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
MusicalWorkRightsClaimType._InitializeFacetMap(MusicalWorkRightsClaimType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MusicalWorkRightsClaimType', MusicalWorkRightsClaimType)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}MusicalWorkType
class MusicalWorkType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of MusicalWork."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MusicalWorkType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1387, 4)
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

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}NewReleaseMessageStatus
class NewReleaseMessageStatus (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A status of a NewReleaseMessage."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NewReleaseMessageStatus')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1423, 4)
    _Documentation = 'A status of a NewReleaseMessage.'
NewReleaseMessageStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=NewReleaseMessageStatus, enum_prefix=None)
NewReleaseMessageStatus.NewReleaseMessageNotProvided = NewReleaseMessageStatus._CF_enumeration.addEnumeration(unicode_value='NewReleaseMessageNotProvided', tag='NewReleaseMessageNotProvided')
NewReleaseMessageStatus.NewReleaseMessageProvided = NewReleaseMessageStatus._CF_enumeration.addEnumeration(unicode_value='NewReleaseMessageProvided', tag='NewReleaseMessageProvided')
NewReleaseMessageStatus._InitializeFacetMap(NewReleaseMessageStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'NewReleaseMessageStatus', NewReleaseMessageStatus)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}NonIsoTerritoryCode
class NonIsoTerritoryCode (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A TerritoryId which is not a TerritoryId according to the ISO 3166-1
                standard."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NonIsoTerritoryCode')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1432, 4)
    _Documentation = 'A TerritoryId which is not a TerritoryId according to the ISO 3166-1\n                standard.'
NonIsoTerritoryCode._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=NonIsoTerritoryCode, enum_prefix=None)
NonIsoTerritoryCode.Worldwide = NonIsoTerritoryCode._CF_enumeration.addEnumeration(unicode_value='Worldwide', tag='Worldwide')
NonIsoTerritoryCode._InitializeFacetMap(NonIsoTerritoryCode._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'NonIsoTerritoryCode', NonIsoTerritoryCode)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}NumberOfDisks
class NumberOfDisks (pyxb.binding.datatypes.string):

    """A number of disks."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NumberOfDisks')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1446, 4)
    _Documentation = 'A number of disks.'
NumberOfDisks._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'NumberOfDisks', NumberOfDisks)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}NumberOfResources
class NumberOfResources (pyxb.binding.datatypes.integer):

    """A number of Resources."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NumberOfResources')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1452, 4)
    _Documentation = 'A number of Resources.'
NumberOfResources._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'NumberOfResources', NumberOfResources)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}OperatingSystemType
class OperatingSystemType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of OperatingSystem."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OperatingSystemType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1458, 4)
    _Documentation = 'A Type of OperatingSystem.'
OperatingSystemType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=OperatingSystemType, enum_prefix=None)
OperatingSystemType.MacOS = OperatingSystemType._CF_enumeration.addEnumeration(unicode_value='MacOS', tag='MacOS')
OperatingSystemType.MsWindows = OperatingSystemType._CF_enumeration.addEnumeration(unicode_value='MsWindows', tag='MsWindows')
OperatingSystemType.Symbian = OperatingSystemType._CF_enumeration.addEnumeration(unicode_value='Symbian', tag='Symbian')
OperatingSystemType.Unknown = OperatingSystemType._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
OperatingSystemType._InitializeFacetMap(OperatingSystemType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'OperatingSystemType', OperatingSystemType)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}OrderType
class OrderType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of order."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OrderType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1469, 4)
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

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}ParentalWarningType
class ParentalWarningType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Creation according to advice which it carries about the
                level of explicitness or offensiveness of its content."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ParentalWarningType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1486, 4)
    _Documentation = 'A Type of Creation according to advice which it carries about the\n                level of explicitness or offensiveness of its content.'
ParentalWarningType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ParentalWarningType, enum_prefix=None)
ParentalWarningType.Explicit = ParentalWarningType._CF_enumeration.addEnumeration(unicode_value='Explicit', tag='Explicit')
ParentalWarningType.ExplicitContentEdited = ParentalWarningType._CF_enumeration.addEnumeration(unicode_value='ExplicitContentEdited', tag='ExplicitContentEdited')
ParentalWarningType.NoAdviceAvailable = ParentalWarningType._CF_enumeration.addEnumeration(unicode_value='NoAdviceAvailable', tag='NoAdviceAvailable')
ParentalWarningType.NotExplicit = ParentalWarningType._CF_enumeration.addEnumeration(unicode_value='NotExplicit', tag='NotExplicit')
ParentalWarningType.Unknown = ParentalWarningType._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
ParentalWarningType.UserDefined = ParentalWarningType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
ParentalWarningType._InitializeFacetMap(ParentalWarningType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ParentalWarningType', ParentalWarningType)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}PartyName
class PartyName (pyxb.binding.datatypes.string):

    """A Name of a Party."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PartyName')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1500, 4)
    _Documentation = 'A Name of a Party.'
PartyName._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'PartyName', PartyName)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}PercentageType
class PercentageType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of PercentageRate."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PercentageType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1506, 4)
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

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}PLineType
class PLineType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of PLine."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PLineType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1519, 4)
    _Documentation = 'A Type of PLine.'
PLineType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PLineType, enum_prefix=None)
PLineType.OriginalPLine = PLineType._CF_enumeration.addEnumeration(unicode_value='OriginalPLine', tag='OriginalPLine')
PLineType.RemasteringPLine = PLineType._CF_enumeration.addEnumeration(unicode_value='RemasteringPLine', tag='RemasteringPLine')
PLineType._InitializeFacetMap(PLineType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'PLineType', PLineType)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}PriceRangeType
class PriceRangeType (pyxb.binding.datatypes.string):

    """A Type of Price according to its value range."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PriceRangeType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1528, 4)
    _Documentation = 'A Type of Price according to its value range.'
PriceRangeType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'PriceRangeType', PriceRangeType)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}PriceType
class PriceType (pyxb.binding.datatypes.string):

    """A Type of Price."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PriceType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1534, 4)
    _Documentation = 'A Type of Price.'
PriceType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'PriceType', PriceType)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}Priority
class Priority (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of priority."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Priority')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1540, 4)
    _Documentation = 'A Type of priority.'
Priority._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Priority, enum_prefix=None)
Priority.High = Priority._CF_enumeration.addEnumeration(unicode_value='High', tag='High')
Priority.Low = Priority._CF_enumeration.addEnumeration(unicode_value='Low', tag='Low')
Priority.Normal = Priority._CF_enumeration.addEnumeration(unicode_value='Normal', tag='Normal')
Priority._InitializeFacetMap(Priority._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'Priority', Priority)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}ProductType
class ProductType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Product."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ProductType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1550, 4)
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

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}Purpose
class Purpose (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of use that is the purpose of an action."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Purpose')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1563, 4)
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

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}RatingAgency
class RatingAgency (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An Organization that issues ParentalWarnings."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RatingAgency')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1577, 4)
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

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}ReasonType
class ReasonType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of reason."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReasonType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1627, 4)
    _Documentation = 'A Type of reason.'
ReasonType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ReasonType, enum_prefix=None)
ReasonType.ChartReporting = ReasonType._CF_enumeration.addEnumeration(unicode_value='ChartReporting', tag='ChartReporting')
ReasonType.RoyaltyReporting = ReasonType._CF_enumeration.addEnumeration(unicode_value='RoyaltyReporting', tag='RoyaltyReporting')
ReasonType.UserDefined = ReasonType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
ReasonType._InitializeFacetMap(ReasonType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ReasonType', ReasonType)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}RecipientRevenueType
class RecipientRevenueType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of revenue according to the recipient of the
                payment."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RecipientRevenueType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1637, 4)
    _Documentation = 'A Type of revenue according to the recipient of the\n                payment.'
RecipientRevenueType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=RecipientRevenueType, enum_prefix=None)
RecipientRevenueType.PerformerAndProducerRevenue = RecipientRevenueType._CF_enumeration.addEnumeration(unicode_value='PerformerAndProducerRevenue', tag='PerformerAndProducerRevenue')
RecipientRevenueType.PerformerRevenue = RecipientRevenueType._CF_enumeration.addEnumeration(unicode_value='PerformerRevenue', tag='PerformerRevenue')
RecipientRevenueType.ProducerRevenue = RecipientRevenueType._CF_enumeration.addEnumeration(unicode_value='ProducerRevenue', tag='ProducerRevenue')
RecipientRevenueType._InitializeFacetMap(RecipientRevenueType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'RecipientRevenueType', RecipientRevenueType)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}RecordingMode
class RecordingMode (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A mode of a Recording."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RecordingMode')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1648, 4)
    _Documentation = 'A mode of a Recording.'
RecordingMode._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=RecordingMode, enum_prefix=None)
RecordingMode.Mono = RecordingMode._CF_enumeration.addEnumeration(unicode_value='Mono', tag='Mono')
RecordingMode.MultichannelAudio = RecordingMode._CF_enumeration.addEnumeration(unicode_value='MultichannelAudio', tag='MultichannelAudio')
RecordingMode.Stereo = RecordingMode._CF_enumeration.addEnumeration(unicode_value='Stereo', tag='Stereo')
RecordingMode.Unknown = RecordingMode._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
RecordingMode._InitializeFacetMap(RecordingMode._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'RecordingMode', RecordingMode)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}RedeliveryReasonType
class RedeliveryReasonType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A reason for a redelivery."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RedeliveryReasonType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1659, 4)
    _Documentation = 'A reason for a redelivery.'
RedeliveryReasonType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=RedeliveryReasonType, enum_prefix=None)
RedeliveryReasonType.BinaryCorrupted = RedeliveryReasonType._CF_enumeration.addEnumeration(unicode_value='BinaryCorrupted', tag='BinaryCorrupted')
RedeliveryReasonType.MetadataInadequate = RedeliveryReasonType._CF_enumeration.addEnumeration(unicode_value='MetadataInadequate', tag='MetadataInadequate')
RedeliveryReasonType.PackageIncomplete = RedeliveryReasonType._CF_enumeration.addEnumeration(unicode_value='PackageIncomplete', tag='PackageIncomplete')
RedeliveryReasonType.ProcessingErrorAtReleaseDistributor = RedeliveryReasonType._CF_enumeration.addEnumeration(unicode_value='ProcessingErrorAtReleaseDistributor', tag='ProcessingErrorAtReleaseDistributor')
RedeliveryReasonType.UserDefined = RedeliveryReasonType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
RedeliveryReasonType._InitializeFacetMap(RedeliveryReasonType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'RedeliveryReasonType', RedeliveryReasonType)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}ReferenceUnit
class ReferenceUnit (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A unit to which a Quantity refers."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReferenceUnit')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1671, 4)
    _Documentation = 'A unit to which a Quantity refers.'
ReferenceUnit._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ReferenceUnit, enum_prefix=None)
ReferenceUnit.PerLicense = ReferenceUnit._CF_enumeration.addEnumeration(unicode_value='PerLicense', tag='PerLicense')
ReferenceUnit.PerUse = ReferenceUnit._CF_enumeration.addEnumeration(unicode_value='PerUse', tag='PerUse')
ReferenceUnit._InitializeFacetMap(ReferenceUnit._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ReferenceUnit', ReferenceUnit)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}RelationalRelator
class RelationalRelator (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Relator between two Entities expressing a measurable
                relationship."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RelationalRelator')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1680, 4)
    _Documentation = 'A Relator between two Entities expressing a measurable\n                relationship.'
RelationalRelator._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=RelationalRelator, enum_prefix=None)
RelationalRelator.EqualTo = RelationalRelator._CF_enumeration.addEnumeration(unicode_value='EqualTo', tag='EqualTo')
RelationalRelator.LessThan = RelationalRelator._CF_enumeration.addEnumeration(unicode_value='LessThan', tag='LessThan')
RelationalRelator.LessThanOrEqualTo = RelationalRelator._CF_enumeration.addEnumeration(unicode_value='LessThanOrEqualTo', tag='LessThanOrEqualTo')
RelationalRelator.MoreThan = RelationalRelator._CF_enumeration.addEnumeration(unicode_value='MoreThan', tag='MoreThan')
RelationalRelator.MoreThanOrEqualTo = RelationalRelator._CF_enumeration.addEnumeration(unicode_value='MoreThanOrEqualTo', tag='MoreThanOrEqualTo')
RelationalRelator.NotEqualTo = RelationalRelator._CF_enumeration.addEnumeration(unicode_value='NotEqualTo', tag='NotEqualTo')
RelationalRelator._InitializeFacetMap(RelationalRelator._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'RelationalRelator', RelationalRelator)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}ReleaseAvailabilityStatus
class ReleaseAvailabilityStatus (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A status of the availability of a Release."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReleaseAvailabilityStatus')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1694, 4)
    _Documentation = 'A status of the availability of a Release.'
ReleaseAvailabilityStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ReleaseAvailabilityStatus, enum_prefix=None)
ReleaseAvailabilityStatus.AvailableForDSP = ReleaseAvailabilityStatus._CF_enumeration.addEnumeration(unicode_value='AvailableForDSP', tag='AvailableForDSP')
ReleaseAvailabilityStatus.NotAvailableForDSP = ReleaseAvailabilityStatus._CF_enumeration.addEnumeration(unicode_value='NotAvailableForDSP', tag='NotAvailableForDSP')
ReleaseAvailabilityStatus.NotClearedForDSP = ReleaseAvailabilityStatus._CF_enumeration.addEnumeration(unicode_value='NotClearedForDSP', tag='NotClearedForDSP')
ReleaseAvailabilityStatus.NotClearedForTerritory = ReleaseAvailabilityStatus._CF_enumeration.addEnumeration(unicode_value='NotClearedForTerritory', tag='NotClearedForTerritory')
ReleaseAvailabilityStatus.NotYetPrepared = ReleaseAvailabilityStatus._CF_enumeration.addEnumeration(unicode_value='NotYetPrepared', tag='NotYetPrepared')
ReleaseAvailabilityStatus.UserDefined = ReleaseAvailabilityStatus._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
ReleaseAvailabilityStatus._InitializeFacetMap(ReleaseAvailabilityStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ReleaseAvailabilityStatus', ReleaseAvailabilityStatus)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}ReleaseReference
class ReleaseReference (pyxb.binding.datatypes.ID):

    """An Identifier of a Release which is specific to a
                DdexMessage."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReleaseReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1707, 4)
    _Documentation = 'An Identifier of a Release which is specific to a\n                DdexMessage.'
ReleaseReference._CF_pattern = pyxb.binding.facets.CF_pattern()
ReleaseReference._CF_pattern.addPattern(pattern='R[\\d\\-_a-zA-Z]+')
ReleaseReference._InitializeFacetMap(ReleaseReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'ReleaseReference', ReleaseReference)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}ReleaseRelationshipType
class ReleaseRelationshipType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of relationship between two Releases."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReleaseRelationshipType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1716, 4)
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

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}ReleaseResourceType
class ReleaseResourceType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Resource in the context of a Release."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReleaseResourceType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1741, 4)
    _Documentation = 'A Type of Resource in the context of a Release.'
ReleaseResourceType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ReleaseResourceType, enum_prefix=None)
ReleaseResourceType.PrimaryResource = ReleaseResourceType._CF_enumeration.addEnumeration(unicode_value='PrimaryResource', tag='PrimaryResource')
ReleaseResourceType.SecondaryResource = ReleaseResourceType._CF_enumeration.addEnumeration(unicode_value='SecondaryResource', tag='SecondaryResource')
ReleaseResourceType._InitializeFacetMap(ReleaseResourceType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ReleaseResourceType', ReleaseResourceType)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}ReleaseType
class ReleaseType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Release according to its content, Duration and/or number of
                components. Note: a ReleaseType is the form in which a ReleaseCreator anticipates
                offering a Release to Consumers."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReleaseType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1750, 4)
    _Documentation = 'A Type of Release according to its content, Duration and/or number of\n                components. Note: a ReleaseType is the form in which a ReleaseCreator anticipates\n                offering a Release to Consumers.'
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
ReleaseType.VideoAlbum = ReleaseType._CF_enumeration.addEnumeration(unicode_value='VideoAlbum', tag='VideoAlbum')
ReleaseType.VideoChapterRelease = ReleaseType._CF_enumeration.addEnumeration(unicode_value='VideoChapterRelease', tag='VideoChapterRelease')
ReleaseType.VideoClipRelease = ReleaseType._CF_enumeration.addEnumeration(unicode_value='VideoClipRelease', tag='VideoClipRelease')
ReleaseType.VideoScreenCaptureRelease = ReleaseType._CF_enumeration.addEnumeration(unicode_value='VideoScreenCaptureRelease', tag='VideoScreenCaptureRelease')
ReleaseType.VideoSingle = ReleaseType._CF_enumeration.addEnumeration(unicode_value='VideoSingle', tag='VideoSingle')
ReleaseType.VideoTrackRelease = ReleaseType._CF_enumeration.addEnumeration(unicode_value='VideoTrackRelease', tag='VideoTrackRelease')
ReleaseType.WallpaperRelease = ReleaseType._CF_enumeration.addEnumeration(unicode_value='WallpaperRelease', tag='WallpaperRelease')
ReleaseType._InitializeFacetMap(ReleaseType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ReleaseType', ReleaseType)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}ReportFormat
class ReportFormat (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Report according to its FileFormat."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReportFormat')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1822, 4)
    _Documentation = 'A Type of Report according to its FileFormat.'
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

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}ReportType
class ReportType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Report."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReportType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1836, 4)
    _Documentation = 'A Type of Report.'
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

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}RepresentativeImageReference
class RepresentativeImageReference (pyxb.binding.datatypes.IDREF):

    """A Reference to a Image which is represents a specific Resource
                ."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RepresentativeImageReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1856, 4)
    _Documentation = 'A Reference to a Image which is represents a specific Resource\n                .'
RepresentativeImageReference._CF_pattern = pyxb.binding.facets.CF_pattern()
RepresentativeImageReference._CF_pattern.addPattern(pattern='A[\\d\\-_a-zA-Z]+')
RepresentativeImageReference._InitializeFacetMap(RepresentativeImageReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'RepresentativeImageReference', RepresentativeImageReference)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}RequestConditionReference
class RequestConditionReference (pyxb.binding.datatypes.IDREF):

    """A Reference to a LicenseOrClaimCondition which is contained within a
                specific request."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RequestConditionReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1865, 4)
    _Documentation = 'A Reference to a LicenseOrClaimCondition which is contained within a\n                specific request.'
RequestConditionReference._CF_pattern = pyxb.binding.facets.CF_pattern()
RequestConditionReference._CF_pattern.addPattern(pattern='E[\\d\\-_a-zA-Z]+')
RequestConditionReference._InitializeFacetMap(RequestConditionReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'RequestConditionReference', RequestConditionReference)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}RequestedActionType
class RequestedActionType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of action requested."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RequestedActionType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1874, 4)
    _Documentation = 'A Type of action requested.'
RequestedActionType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=RequestedActionType, enum_prefix=None)
RequestedActionType.AdditionalInformationOnly = RequestedActionType._CF_enumeration.addEnumeration(unicode_value='AdditionalInformationOnly', tag='AdditionalInformationOnly')
RequestedActionType.CorrectAndInform = RequestedActionType._CF_enumeration.addEnumeration(unicode_value='CorrectAndInform', tag='CorrectAndInform')
RequestedActionType.CorrectAndResend = RequestedActionType._CF_enumeration.addEnumeration(unicode_value='CorrectAndResend', tag='CorrectAndResend')
RequestedActionType.NoAction = RequestedActionType._CF_enumeration.addEnumeration(unicode_value='NoAction', tag='NoAction')
RequestedActionType.UserDefined = RequestedActionType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
RequestedActionType._InitializeFacetMap(RequestedActionType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'RequestedActionType', RequestedActionType)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}RequestReleaseReference
class RequestReleaseReference (pyxb.binding.datatypes.IDREF):

    """A Reference to a Release which is contained within a specific
                request."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RequestReleaseReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1886, 4)
    _Documentation = 'A Reference to a Release which is contained within a specific\n                request.'
RequestReleaseReference._CF_pattern = pyxb.binding.facets.CF_pattern()
RequestReleaseReference._CF_pattern.addPattern(pattern='R[\\d\\-_a-zA-Z]+')
RequestReleaseReference._InitializeFacetMap(RequestReleaseReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'RequestReleaseReference', RequestReleaseReference)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}RequestResourceReference
class RequestResourceReference (pyxb.binding.datatypes.IDREF):

    """A Reference to a Resource which is contained within a specific
                request."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RequestResourceReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1895, 4)
    _Documentation = 'A Reference to a Resource which is contained within a specific\n                request.'
RequestResourceReference._CF_pattern = pyxb.binding.facets.CF_pattern()
RequestResourceReference._CF_pattern.addPattern(pattern='A[\\d\\-_a-zA-Z]+')
RequestResourceReference._InitializeFacetMap(RequestResourceReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'RequestResourceReference', RequestResourceReference)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}RequestRightShareReference
class RequestRightShareReference (pyxb.binding.datatypes.IDREF):

    """A Reference to a RightShare which is contained within a specific
                request."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RequestRightShareReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1904, 4)
    _Documentation = 'A Reference to a RightShare which is contained within a specific\n                request.'
RequestRightShareReference._CF_pattern = pyxb.binding.facets.CF_pattern()
RequestRightShareReference._CF_pattern.addPattern(pattern='S[\\d\\-_a-zA-Z]+')
RequestRightShareReference._InitializeFacetMap(RequestRightShareReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'RequestRightShareReference', RequestRightShareReference)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}RequestWorkReference
class RequestWorkReference (pyxb.binding.datatypes.IDREF):

    """A Reference to a Work which is contained within a specific
                request."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RequestWorkReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1913, 4)
    _Documentation = 'A Reference to a Work which is contained within a specific\n                request.'
RequestWorkReference._CF_pattern = pyxb.binding.facets.CF_pattern()
RequestWorkReference._CF_pattern.addPattern(pattern='W[\\d\\-_a-zA-Z]+')
RequestWorkReference._InitializeFacetMap(RequestWorkReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'RequestWorkReference', RequestWorkReference)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}ResourceContainedResourceReference
class ResourceContainedResourceReference (pyxb.binding.datatypes.IDREF):

    """A Reference to a Resource which is contained within a specific
                Resource ."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ResourceContainedResourceReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1922, 4)
    _Documentation = 'A Reference to a Resource which is contained within a specific\n                Resource .'
ResourceContainedResourceReference._CF_pattern = pyxb.binding.facets.CF_pattern()
ResourceContainedResourceReference._CF_pattern.addPattern(pattern='A[\\d\\-_a-zA-Z]+')
ResourceContainedResourceReference._InitializeFacetMap(ResourceContainedResourceReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'ResourceContainedResourceReference', ResourceContainedResourceReference)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}ResourceContributorRole
class ResourceContributorRole (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A role played by a Contributor in relation to a Fixation of an
                abstract Creation."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ResourceContributorRole')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1931, 4)
    _Documentation = 'A role played by a Contributor in relation to a Fixation of an\n                abstract Creation.'
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

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}ResourceGroupResourceReference
class ResourceGroupResourceReference (pyxb.binding.datatypes.IDREF):

    """A Reference to a Resource which is contained within a specific group
                of Resources."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ResourceGroupResourceReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1983, 4)
    _Documentation = 'A Reference to a Resource which is contained within a specific group\n                of Resources.'
ResourceGroupResourceReference._CF_pattern = pyxb.binding.facets.CF_pattern()
ResourceGroupResourceReference._CF_pattern.addPattern(pattern='A[\\d\\-_a-zA-Z]+')
ResourceGroupResourceReference._InitializeFacetMap(ResourceGroupResourceReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'ResourceGroupResourceReference', ResourceGroupResourceReference)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}ResourceMusicalWorkReference
class ResourceMusicalWorkReference (pyxb.binding.datatypes.IDREF):

    """A Reference to a MusicalWork which is contained within a specific
                Resource."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ResourceMusicalWorkReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 1992, 4)
    _Documentation = 'A Reference to a MusicalWork which is contained within a specific\n                Resource.'
ResourceMusicalWorkReference._CF_pattern = pyxb.binding.facets.CF_pattern()
ResourceMusicalWorkReference._CF_pattern.addPattern(pattern='W[\\d\\-_a-zA-Z]+')
ResourceMusicalWorkReference._InitializeFacetMap(ResourceMusicalWorkReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'ResourceMusicalWorkReference', ResourceMusicalWorkReference)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}ResourceOmissionReason
class ResourceOmissionReason (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of reason for a omitting a Resource."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ResourceOmissionReason')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 2001, 4)
    _Documentation = 'A Type of reason for a omitting a Resource.'
ResourceOmissionReason._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ResourceOmissionReason, enum_prefix=None)
ResourceOmissionReason.PassportServiceRelease = ResourceOmissionReason._CF_enumeration.addEnumeration(unicode_value='PassportServiceRelease', tag='PassportServiceRelease')
ResourceOmissionReason.PreRelease = ResourceOmissionReason._CF_enumeration.addEnumeration(unicode_value='PreRelease', tag='PreRelease')
ResourceOmissionReason.UserDefined = ResourceOmissionReason._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
ResourceOmissionReason.VirtualRelease = ResourceOmissionReason._CF_enumeration.addEnumeration(unicode_value='VirtualRelease', tag='VirtualRelease')
ResourceOmissionReason._InitializeFacetMap(ResourceOmissionReason._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ResourceOmissionReason', ResourceOmissionReason)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}ResourceReference
class ResourceReference (pyxb.binding.datatypes.ID):

    """An Identifier of a Resource which is specific to a
                DdexMessage."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ResourceReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 2012, 4)
    _Documentation = 'An Identifier of a Resource which is specific to a\n                DdexMessage.'
ResourceReference._CF_pattern = pyxb.binding.facets.CF_pattern()
ResourceReference._CF_pattern.addPattern(pattern='A[\\d\\-_a-zA-Z]+')
ResourceReference._InitializeFacetMap(ResourceReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'ResourceReference', ResourceReference)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}ResourceReleaseReference
class ResourceReleaseReference (pyxb.binding.datatypes.IDREF):

    """A Reference to a Release which is included in a specific
                Resource."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ResourceReleaseReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 2021, 4)
    _Documentation = 'A Reference to a Release which is included in a specific\n                Resource.'
ResourceReleaseReference._CF_pattern = pyxb.binding.facets.CF_pattern()
ResourceReleaseReference._CF_pattern.addPattern(pattern='R[\\d\\-_a-zA-Z]+')
ResourceReleaseReference._InitializeFacetMap(ResourceReleaseReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'ResourceReleaseReference', ResourceReleaseReference)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}ResourceType
class ResourceType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Resource."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ResourceType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 2030, 4)
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

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}RevenueSourceType
class RevenueSourceType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of revenue earned by the SoundRecording, according to the way
                the revenue is generated."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RevenueSourceType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 2045, 4)
    _Documentation = 'A Type of revenue earned by the SoundRecording, according to the way\n                the revenue is generated.'
RevenueSourceType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=RevenueSourceType, enum_prefix=None)
RevenueSourceType.FinancialRevenue = RevenueSourceType._CF_enumeration.addEnumeration(unicode_value='FinancialRevenue', tag='FinancialRevenue')
RevenueSourceType.IndemnityRevenue = RevenueSourceType._CF_enumeration.addEnumeration(unicode_value='IndemnityRevenue', tag='IndemnityRevenue')
RevenueSourceType.RoyaltyRevenue = RevenueSourceType._CF_enumeration.addEnumeration(unicode_value='RoyaltyRevenue', tag='RoyaltyRevenue')
RevenueSourceType._InitializeFacetMap(RevenueSourceType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'RevenueSourceType', RevenueSourceType)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}RightsControllerRole
class RightsControllerRole (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A role of a RightsController."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RightsControllerRole')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 2056, 4)
    _Documentation = 'A role of a RightsController.'
RightsControllerRole._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=RightsControllerRole, enum_prefix=None)
RightsControllerRole.AdministratingRecordCompany = RightsControllerRole._CF_enumeration.addEnumeration(unicode_value='AdministratingRecordCompany', tag='AdministratingRecordCompany')
RightsControllerRole.RightsAdministrator = RightsControllerRole._CF_enumeration.addEnumeration(unicode_value='RightsAdministrator', tag='RightsAdministrator')
RightsControllerRole.RightsController = RightsControllerRole._CF_enumeration.addEnumeration(unicode_value='RightsController', tag='RightsController')
RightsControllerRole.RoyaltyAdministrator = RightsControllerRole._CF_enumeration.addEnumeration(unicode_value='RoyaltyAdministrator', tag='RoyaltyAdministrator')
RightsControllerRole.Unknown = RightsControllerRole._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
RightsControllerRole._InitializeFacetMap(RightsControllerRole._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'RightsControllerRole', RightsControllerRole)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}RightsCoverage
class RightsCoverage (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Right which is covered."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RightsCoverage')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 2068, 4)
    _Documentation = 'A Type of Right which is covered.'
RightsCoverage._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=RightsCoverage, enum_prefix=None)
RightsCoverage.MakeAvailableRight = RightsCoverage._CF_enumeration.addEnumeration(unicode_value='MakeAvailableRight', tag='MakeAvailableRight')
RightsCoverage.MechanicalRight = RightsCoverage._CF_enumeration.addEnumeration(unicode_value='MechanicalRight', tag='MechanicalRight')
RightsCoverage.PerformingRight = RightsCoverage._CF_enumeration.addEnumeration(unicode_value='PerformingRight', tag='PerformingRight')
RightsCoverage.ReproductionRight = RightsCoverage._CF_enumeration.addEnumeration(unicode_value='ReproductionRight', tag='ReproductionRight')
RightsCoverage.SynchronizationRight = RightsCoverage._CF_enumeration.addEnumeration(unicode_value='SynchronizationRight', tag='SynchronizationRight')
RightsCoverage._InitializeFacetMap(RightsCoverage._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'RightsCoverage', RightsCoverage)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}RightShareReference
class RightShareReference (pyxb.binding.datatypes.ID):

    """A Reference to a RightShare."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RightShareReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 2080, 4)
    _Documentation = 'A Reference to a RightShare.'
RightShareReference._CF_pattern = pyxb.binding.facets.CF_pattern()
RightShareReference._CF_pattern.addPattern(pattern='S[\\d\\-_a-zA-Z]+')
RightShareReference._InitializeFacetMap(RightShareReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'RightShareReference', RightShareReference)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}RightShareReleaseReference
class RightShareReleaseReference (pyxb.binding.datatypes.IDREF):

    """A Reference to a Release which is contained within a specific
                RightShare."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RightShareReleaseReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 2088, 4)
    _Documentation = 'A Reference to a Release which is contained within a specific\n                RightShare.'
RightShareReleaseReference._CF_pattern = pyxb.binding.facets.CF_pattern()
RightShareReleaseReference._CF_pattern.addPattern(pattern='R[\\d\\-_a-zA-Z]+')
RightShareReleaseReference._InitializeFacetMap(RightShareReleaseReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'RightShareReleaseReference', RightShareReleaseReference)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}RightShareResourceReference
class RightShareResourceReference (pyxb.binding.datatypes.IDREF):

    """A Reference to a Resource which is contained within a specific
                RightShare."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RightShareResourceReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 2097, 4)
    _Documentation = 'A Reference to a Resource which is contained within a specific\n                RightShare.'
RightShareResourceReference._CF_pattern = pyxb.binding.facets.CF_pattern()
RightShareResourceReference._CF_pattern.addPattern(pattern='A[\\d\\-_a-zA-Z]+')
RightShareResourceReference._InitializeFacetMap(RightShareResourceReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'RightShareResourceReference', RightShareResourceReference)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}RightShareWorkReference
class RightShareWorkReference (pyxb.binding.datatypes.IDREF):

    """A Reference to a Work which is contained within a specific
                RightShare."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RightShareWorkReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 2106, 4)
    _Documentation = 'A Reference to a Work which is contained within a specific\n                RightShare.'
RightShareWorkReference._CF_pattern = pyxb.binding.facets.CF_pattern()
RightShareWorkReference._CF_pattern.addPattern(pattern='W[\\d\\-_a-zA-Z]+')
RightShareWorkReference._InitializeFacetMap(RightShareWorkReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'RightShareWorkReference', RightShareWorkReference)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}RoyaltyRateCalculationType
class RoyaltyRateCalculationType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of RoyaltyRate according to the calculation
                method."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RoyaltyRateCalculationType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 2115, 4)
    _Documentation = 'A Type of RoyaltyRate according to the calculation\n                method.'
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

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}RoyaltyRateType
class RoyaltyRateType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of RoyaltyRate."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RoyaltyRateType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 2130, 4)
    _Documentation = 'A Type of RoyaltyRate.'
RoyaltyRateType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=RoyaltyRateType, enum_prefix=None)
RoyaltyRateType.PennyRate = RoyaltyRateType._CF_enumeration.addEnumeration(unicode_value='PennyRate', tag='PennyRate')
RoyaltyRateType.PercentageRoyaltyRate = RoyaltyRateType._CF_enumeration.addEnumeration(unicode_value='PercentageRoyaltyRate', tag='PercentageRoyaltyRate')
RoyaltyRateType.UserDefined = RoyaltyRateType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
RoyaltyRateType._InitializeFacetMap(RoyaltyRateType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'RoyaltyRateType', RoyaltyRateType)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}SalesReportAvailabilityStatus
class SalesReportAvailabilityStatus (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A status of the availability of a SalesReport."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SalesReportAvailabilityStatus')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 2140, 4)
    _Documentation = 'A status of the availability of a SalesReport.'
SalesReportAvailabilityStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SalesReportAvailabilityStatus, enum_prefix=None)
SalesReportAvailabilityStatus.SalesReportAvailable = SalesReportAvailabilityStatus._CF_enumeration.addEnumeration(unicode_value='SalesReportAvailable', tag='SalesReportAvailable')
SalesReportAvailabilityStatus.SalesReportNotAvailable = SalesReportAvailabilityStatus._CF_enumeration.addEnumeration(unicode_value='SalesReportNotAvailable', tag='SalesReportNotAvailable')
SalesReportAvailabilityStatus._InitializeFacetMap(SalesReportAvailabilityStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'SalesReportAvailabilityStatus', SalesReportAvailabilityStatus)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}Sex
class Sex (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """The biological sex of a being."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Sex')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 2149, 4)
    _Documentation = 'The biological sex of a being.'
Sex._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Sex, enum_prefix=None)
Sex.Female = Sex._CF_enumeration.addEnumeration(unicode_value='Female', tag='Female')
Sex.Male = Sex._CF_enumeration.addEnumeration(unicode_value='Male', tag='Male')
Sex.Unknown = Sex._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
Sex._InitializeFacetMap(Sex._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'Sex', Sex)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}SheetMusicCodecType
class SheetMusicCodecType (pyxb.binding.datatypes.string):

    """A Type of SheetMusicCodec."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SheetMusicCodecType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 2159, 4)
    _Documentation = 'A Type of SheetMusicCodec.'
SheetMusicCodecType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'SheetMusicCodecType', SheetMusicCodecType)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}SheetMusicType
class SheetMusicType (pyxb.binding.datatypes.string):

    """A Type of SheetMusic."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SheetMusicType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 2165, 4)
    _Documentation = 'A Type of SheetMusic.'
SheetMusicType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'SheetMusicType', SheetMusicType)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}SoftwareType
class SoftwareType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Software."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SoftwareType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 2171, 4)
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

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}SoundProcessorType
class SoundProcessorType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of sound processor."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SoundProcessorType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 2184, 4)
    _Documentation = 'A Type of sound processor.'
SoundProcessorType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SoundProcessorType, enum_prefix=None)
SoundProcessorType.MidiProcessor = SoundProcessorType._CF_enumeration.addEnumeration(unicode_value='MidiProcessor', tag='MidiProcessor')
SoundProcessorType.Unknown = SoundProcessorType._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
SoundProcessorType.UserDefined = SoundProcessorType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
SoundProcessorType._InitializeFacetMap(SoundProcessorType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'SoundProcessorType', SoundProcessorType)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}SoundRecordingCollectionReference
class SoundRecordingCollectionReference (pyxb.binding.datatypes.IDREF):

    """A Reference to a Collection which is contained within a specific
                SoundRecording."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SoundRecordingCollectionReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 2194, 4)
    _Documentation = 'A Reference to a Collection which is contained within a specific\n                SoundRecording.'
SoundRecordingCollectionReference._CF_pattern = pyxb.binding.facets.CF_pattern()
SoundRecordingCollectionReference._CF_pattern.addPattern(pattern='X[\\d\\-_a-zA-Z]+')
SoundRecordingCollectionReference._InitializeFacetMap(SoundRecordingCollectionReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'SoundRecordingCollectionReference', SoundRecordingCollectionReference)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}SoundRecordingType
class SoundRecordingType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of SoundRecording."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SoundRecordingType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 2203, 4)
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

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}SupplyChainStatus
class SupplyChainStatus (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A status of a Release in a supply chain."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SupplyChainStatus')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 2216, 4)
    _Documentation = 'A status of a Release in a supply chain.'
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

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}TaxScope
class TaxScope (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Tax according to its scope."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TaxScope')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 2235, 4)
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

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}TaxType
class TaxType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Tax."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TaxType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 2248, 4)
    _Documentation = 'A Type of Tax.'
TaxType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TaxType, enum_prefix=None)
TaxType.CombinedTax = TaxType._CF_enumeration.addEnumeration(unicode_value='CombinedTax', tag='CombinedTax')
TaxType.SalesTax = TaxType._CF_enumeration.addEnumeration(unicode_value='SalesTax', tag='SalesTax')
TaxType.ServiceTax = TaxType._CF_enumeration.addEnumeration(unicode_value='ServiceTax', tag='ServiceTax')
TaxType.SourceTax = TaxType._CF_enumeration.addEnumeration(unicode_value='SourceTax', tag='SourceTax')
TaxType.UserDefined = TaxType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
TaxType._InitializeFacetMap(TaxType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TaxType', TaxType)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}TechnicalResourceDetailsReference
class TechnicalResourceDetailsReference (pyxb.binding.datatypes.ID):

    """An Identifier of a Composite specifying technical details of a
                Resource which is specific to a DdexMessage."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TechnicalResourceDetailsReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 2260, 4)
    _Documentation = 'An Identifier of a Composite specifying technical details of a\n                Resource which is specific to a DdexMessage.'
TechnicalResourceDetailsReference._CF_pattern = pyxb.binding.facets.CF_pattern()
TechnicalResourceDetailsReference._CF_pattern.addPattern(pattern='T[\\d\\-_a-zA-Z]+')
TechnicalResourceDetailsReference._InitializeFacetMap(TechnicalResourceDetailsReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'TechnicalResourceDetailsReference', TechnicalResourceDetailsReference)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}TextCodecType
class TextCodecType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of TextCodec."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TextCodecType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 2269, 4)
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

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}TextType
class TextType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Text."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TextType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 2283, 4)
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

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}ThemeType
class ThemeType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Theme."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ThemeType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 2297, 4)
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

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}TitleType
class TitleType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Title which defines its origin, form or the function it
                fulfils in relation to a Creation. Note: A Title may fulfil more than one role.
                Example: "Help" may be both the OriginalTitle and the DisplayTitle for the
                well-known Beatles song."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TitleType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 2310, 4)
    _Documentation = 'A Type of Title which defines its origin, form or the function it\n                fulfils in relation to a Creation. Note: A Title may fulfil more than one role.\n                Example: "Help" may be both the OriginalTitle and the DisplayTitle for the\n                well-known Beatles song.'
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

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}UnitOfBitRate
class UnitOfBitRate (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A UnitOfMeasure for a BitRate."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UnitOfBitRate')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 2336, 4)
    _Documentation = 'A UnitOfMeasure for a BitRate.'
UnitOfBitRate._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=UnitOfBitRate, enum_prefix=None)
UnitOfBitRate.bps = UnitOfBitRate._CF_enumeration.addEnumeration(unicode_value='bps', tag='bps')
UnitOfBitRate.Gbps = UnitOfBitRate._CF_enumeration.addEnumeration(unicode_value='Gbps', tag='Gbps')
UnitOfBitRate.kbps = UnitOfBitRate._CF_enumeration.addEnumeration(unicode_value='kbps', tag='kbps')
UnitOfBitRate.Mbps = UnitOfBitRate._CF_enumeration.addEnumeration(unicode_value='Mbps', tag='Mbps')
UnitOfBitRate._InitializeFacetMap(UnitOfBitRate._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'UnitOfBitRate', UnitOfBitRate)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}UnitOfConditionValue
class UnitOfConditionValue (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A UnitOfMeasure for a condition value."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UnitOfConditionValue')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 2347, 4)
    _Documentation = 'A UnitOfMeasure for a condition value.'
UnitOfConditionValue._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=UnitOfConditionValue, enum_prefix=None)
UnitOfConditionValue.Millisecond = UnitOfConditionValue._CF_enumeration.addEnumeration(unicode_value='Millisecond', tag='Millisecond')
UnitOfConditionValue.Minute = UnitOfConditionValue._CF_enumeration.addEnumeration(unicode_value='Minute', tag='Minute')
UnitOfConditionValue.Percent = UnitOfConditionValue._CF_enumeration.addEnumeration(unicode_value='Percent', tag='Percent')
UnitOfConditionValue.Pixel = UnitOfConditionValue._CF_enumeration.addEnumeration(unicode_value='Pixel', tag='Pixel')
UnitOfConditionValue.Second = UnitOfConditionValue._CF_enumeration.addEnumeration(unicode_value='Second', tag='Second')
UnitOfConditionValue._InitializeFacetMap(UnitOfConditionValue._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'UnitOfConditionValue', UnitOfConditionValue)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}UnitOfExtent
class UnitOfExtent (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A UnitOfMeasure for an Extent."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UnitOfExtent')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 2359, 4)
    _Documentation = 'A UnitOfMeasure for an Extent.'
UnitOfExtent._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=UnitOfExtent, enum_prefix=None)
UnitOfExtent.cm = UnitOfExtent._CF_enumeration.addEnumeration(unicode_value='cm', tag='cm')
UnitOfExtent.Inch = UnitOfExtent._CF_enumeration.addEnumeration(unicode_value='Inch', tag='Inch')
UnitOfExtent.mm = UnitOfExtent._CF_enumeration.addEnumeration(unicode_value='mm', tag='mm')
UnitOfExtent.PercentOfScreen = UnitOfExtent._CF_enumeration.addEnumeration(unicode_value='PercentOfScreen', tag='PercentOfScreen')
UnitOfExtent.Pixel = UnitOfExtent._CF_enumeration.addEnumeration(unicode_value='Pixel', tag='Pixel')
UnitOfExtent._InitializeFacetMap(UnitOfExtent._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'UnitOfExtent', UnitOfExtent)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}UnitOfFrameRate
class UnitOfFrameRate (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A UnitOfMeasure for a FrameRate."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UnitOfFrameRate')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 2371, 4)
    _Documentation = 'A UnitOfMeasure for a FrameRate.'
UnitOfFrameRate._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=UnitOfFrameRate, enum_prefix=None)
UnitOfFrameRate.Hzinterlaced = UnitOfFrameRate._CF_enumeration.addEnumeration(unicode_value='Hz(interlaced)', tag='Hzinterlaced')
UnitOfFrameRate.Hznon_interlaced = UnitOfFrameRate._CF_enumeration.addEnumeration(unicode_value='Hz(non-interlaced)', tag='Hznon_interlaced')
UnitOfFrameRate._InitializeFacetMap(UnitOfFrameRate._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'UnitOfFrameRate', UnitOfFrameRate)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}UnitOfFrequency
class UnitOfFrequency (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A UnitOfMeasure for a frequency."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UnitOfFrequency')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 2380, 4)
    _Documentation = 'A UnitOfMeasure for a frequency.'
UnitOfFrequency._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=UnitOfFrequency, enum_prefix=None)
UnitOfFrequency.GHz = UnitOfFrequency._CF_enumeration.addEnumeration(unicode_value='GHz', tag='GHz')
UnitOfFrequency.Hz = UnitOfFrequency._CF_enumeration.addEnumeration(unicode_value='Hz', tag='Hz')
UnitOfFrequency.kHz = UnitOfFrequency._CF_enumeration.addEnumeration(unicode_value='kHz', tag='kHz')
UnitOfFrequency.MHz = UnitOfFrequency._CF_enumeration.addEnumeration(unicode_value='MHz', tag='MHz')
UnitOfFrequency._InitializeFacetMap(UnitOfFrequency._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'UnitOfFrequency', UnitOfFrequency)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}UpdateIndicator
class UpdateIndicator (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Message according to whether the Message contains original
                data or updates to previously sent data."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UpdateIndicator')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 2391, 4)
    _Documentation = 'A Type of Message according to whether the Message contains original\n                data or updates to previously sent data.'
UpdateIndicator._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=UpdateIndicator, enum_prefix=None)
UpdateIndicator.OriginalMessage = UpdateIndicator._CF_enumeration.addEnumeration(unicode_value='OriginalMessage', tag='OriginalMessage')
UpdateIndicator.UpdateMessage = UpdateIndicator._CF_enumeration.addEnumeration(unicode_value='UpdateMessage', tag='UpdateMessage')
UpdateIndicator._InitializeFacetMap(UpdateIndicator._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'UpdateIndicator', UpdateIndicator)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}UserInterfaceType
class UserInterfaceType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of physical interface by which a Consumer uses a Service or
                Release."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UserInterfaceType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 2401, 4)
    _Documentation = 'A Type of physical interface by which a Consumer uses a Service or\n                Release.'
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

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}UseType
class UseType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of a nature of a Service, or a Release, as used by a
                Consumer."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UseType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 2422, 4)
    _Documentation = 'A Type of a nature of a Service, or a Release, as used by a\n                Consumer.'
UseType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=UseType, enum_prefix=None)
UseType.AsPerContract = UseType._CF_enumeration.addEnumeration(unicode_value='AsPerContract', tag='AsPerContract')
UseType.Broadcast = UseType._CF_enumeration.addEnumeration(unicode_value='Broadcast', tag='Broadcast')
UseType.ConditionalDownload = UseType._CF_enumeration.addEnumeration(unicode_value='ConditionalDownload', tag='ConditionalDownload')
UseType.ContentInfluencedStream = UseType._CF_enumeration.addEnumeration(unicode_value='ContentInfluencedStream', tag='ContentInfluencedStream')
UseType.Display = UseType._CF_enumeration.addEnumeration(unicode_value='Display', tag='Display')
UseType.Download = UseType._CF_enumeration.addEnumeration(unicode_value='Download', tag='Download')
UseType.KioskDownload = UseType._CF_enumeration.addEnumeration(unicode_value='KioskDownload', tag='KioskDownload')
UseType.Narrowcast = UseType._CF_enumeration.addEnumeration(unicode_value='Narrowcast', tag='Narrowcast')
UseType.NonInteractiveStream = UseType._CF_enumeration.addEnumeration(unicode_value='NonInteractiveStream', tag='NonInteractiveStream')
UseType.OnDemandStream = UseType._CF_enumeration.addEnumeration(unicode_value='OnDemandStream', tag='OnDemandStream')
UseType.PerformInPublic = UseType._CF_enumeration.addEnumeration(unicode_value='PerformInPublic', tag='PerformInPublic')
UseType.PermanentDownload = UseType._CF_enumeration.addEnumeration(unicode_value='PermanentDownload', tag='PermanentDownload')
UseType.Playback = UseType._CF_enumeration.addEnumeration(unicode_value='Playback', tag='Playback')
UseType.PlayInPublic = UseType._CF_enumeration.addEnumeration(unicode_value='PlayInPublic', tag='PlayInPublic')
UseType.Podcast = UseType._CF_enumeration.addEnumeration(unicode_value='Podcast', tag='Podcast')
UseType.Print = UseType._CF_enumeration.addEnumeration(unicode_value='Print', tag='Print')
UseType.PrivateCopy = UseType._CF_enumeration.addEnumeration(unicode_value='PrivateCopy', tag='PrivateCopy')
UseType.Rent = UseType._CF_enumeration.addEnumeration(unicode_value='Rent', tag='Rent')
UseType.Simulcast = UseType._CF_enumeration.addEnumeration(unicode_value='Simulcast', tag='Simulcast')
UseType.Stream = UseType._CF_enumeration.addEnumeration(unicode_value='Stream', tag='Stream')
UseType.TetheredDownload = UseType._CF_enumeration.addEnumeration(unicode_value='TetheredDownload', tag='TetheredDownload')
UseType.TimeInfluencedStream = UseType._CF_enumeration.addEnumeration(unicode_value='TimeInfluencedStream', tag='TimeInfluencedStream')
UseType.Unknown = UseType._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
UseType.UseAsAlertTone = UseType._CF_enumeration.addEnumeration(unicode_value='UseAsAlertTone', tag='UseAsAlertTone')
UseType.UseAsKaraoke = UseType._CF_enumeration.addEnumeration(unicode_value='UseAsKaraoke', tag='UseAsKaraoke')
UseType.UseAsRingbackTone = UseType._CF_enumeration.addEnumeration(unicode_value='UseAsRingbackTone', tag='UseAsRingbackTone')
UseType.UseAsRingbackTune = UseType._CF_enumeration.addEnumeration(unicode_value='UseAsRingbackTune', tag='UseAsRingbackTune')
UseType.UseAsRingtone = UseType._CF_enumeration.addEnumeration(unicode_value='UseAsRingtone', tag='UseAsRingtone')
UseType.UseAsRingtune = UseType._CF_enumeration.addEnumeration(unicode_value='UseAsRingtune', tag='UseAsRingtune')
UseType.UseAsScreensaver = UseType._CF_enumeration.addEnumeration(unicode_value='UseAsScreensaver', tag='UseAsScreensaver')
UseType.UserDefined = UseType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
UseType.UserMakeAvailableLabelProvided = UseType._CF_enumeration.addEnumeration(unicode_value='UserMakeAvailableLabelProvided', tag='UserMakeAvailableLabelProvided')
UseType.UserMakeAvailableUserProvided = UseType._CF_enumeration.addEnumeration(unicode_value='UserMakeAvailableUserProvided', tag='UserMakeAvailableUserProvided')
UseType.Webcast = UseType._CF_enumeration.addEnumeration(unicode_value='Webcast', tag='Webcast')
UseType._InitializeFacetMap(UseType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'UseType', UseType)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}ValueType
class ValueType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of RoyaltyRate."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ValueType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 2464, 4)
    _Documentation = 'A Type of RoyaltyRate.'
ValueType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ValueType, enum_prefix=None)
ValueType.Calculated = ValueType._CF_enumeration.addEnumeration(unicode_value='Calculated', tag='Calculated')
ValueType.Maximum = ValueType._CF_enumeration.addEnumeration(unicode_value='Maximum', tag='Maximum')
ValueType.Minimum = ValueType._CF_enumeration.addEnumeration(unicode_value='Minimum', tag='Minimum')
ValueType._InitializeFacetMap(ValueType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ValueType', ValueType)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}VideoCodecType
class VideoCodecType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of VideoCodec."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VideoCodecType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 2474, 4)
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

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}VideoCueSheetReference
class VideoCueSheetReference (pyxb.binding.datatypes.IDREF):

    """A Reference to a CueSheet which is contained within a specific
                Video."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VideoCueSheetReference')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 2493, 4)
    _Documentation = 'A Reference to a CueSheet which is contained within a specific\n                Video.'
VideoCueSheetReference._CF_pattern = pyxb.binding.facets.CF_pattern()
VideoCueSheetReference._CF_pattern.addPattern(pattern='Q[\\d\\-_a-zA-Z]+')
VideoCueSheetReference._InitializeFacetMap(VideoCueSheetReference._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'VideoCueSheetReference', VideoCueSheetReference)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}VideoDefinitionType
class VideoDefinitionType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of resolution (or definition) in which a Video is
                provided."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VideoDefinitionType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 2502, 4)
    _Documentation = 'A Type of resolution (or definition) in which a Video is\n                provided.'
VideoDefinitionType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=VideoDefinitionType, enum_prefix=None)
VideoDefinitionType.HighDefinition = VideoDefinitionType._CF_enumeration.addEnumeration(unicode_value='HighDefinition', tag='HighDefinition')
VideoDefinitionType.StandardDefinition = VideoDefinitionType._CF_enumeration.addEnumeration(unicode_value='StandardDefinition', tag='StandardDefinition')
VideoDefinitionType._InitializeFacetMap(VideoDefinitionType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'VideoDefinitionType', VideoDefinitionType)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}VideoType
class VideoType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of Video."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VideoType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 2512, 4)
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

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}VisualPerceptionType
class VisualPerceptionType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of MusicalCreation according to how it is experienced in an
                AudioVisual Creation."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VisualPerceptionType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 2551, 4)
    _Documentation = 'A Type of MusicalCreation according to how it is experienced in an\n                AudioVisual Creation.'
VisualPerceptionType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=VisualPerceptionType, enum_prefix=None)
VisualPerceptionType.Background = VisualPerceptionType._CF_enumeration.addEnumeration(unicode_value='Background', tag='Background')
VisualPerceptionType.UserDefined = VisualPerceptionType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
VisualPerceptionType.Visual = VisualPerceptionType._CF_enumeration.addEnumeration(unicode_value='Visual', tag='Visual')
VisualPerceptionType._InitializeFacetMap(VisualPerceptionType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'VisualPerceptionType', VisualPerceptionType)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}VocalType
class VocalType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A Type of a MusicalCreation according to the occurrence of
                vocals."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VocalType')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 2562, 4)
    _Documentation = 'A Type of a MusicalCreation according to the occurrence of\n                vocals.'
VocalType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=VocalType, enum_prefix=None)
VocalType.Instrumental = VocalType._CF_enumeration.addEnumeration(unicode_value='Instrumental', tag='Instrumental')
VocalType.UserDefined = VocalType._CF_enumeration.addEnumeration(unicode_value='UserDefined', tag='UserDefined')
VocalType.Vocal = VocalType._CF_enumeration.addEnumeration(unicode_value='Vocal', tag='Vocal')
VocalType._InitializeFacetMap(VocalType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'VocalType', VocalType)

# Atomic simple type: {http://ddex.net/xml/20110630/ddex}WsMessageStatus
class WsMessageStatus (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """A status of a WsMessage."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'WsMessageStatus')
    _XSDLocation = pyxb.utils.utility.Location('http://ddex.net/xml/20110630/ddex.xsd', 2573, 4)
    _Documentation = 'A status of a WsMessage.'
WsMessageStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=WsMessageStatus, enum_prefix=None)
WsMessageStatus.BackendProcessingError = WsMessageStatus._CF_enumeration.addEnumeration(unicode_value='BackendProcessingError', tag='BackendProcessingError')
WsMessageStatus.NoValidMessageReceived = WsMessageStatus._CF_enumeration.addEnumeration(unicode_value='NoValidMessageReceived', tag='NoValidMessageReceived')
WsMessageStatus.ValidMessageQueuedForProcessing = WsMessageStatus._CF_enumeration.addEnumeration(unicode_value='ValidMessageQueuedForProcessing', tag='ValidMessageQueuedForProcessing')
WsMessageStatus.ValidMessageReceived = WsMessageStatus._CF_enumeration.addEnumeration(unicode_value='ValidMessageReceived', tag='ValidMessageReceived')
WsMessageStatus._InitializeFacetMap(WsMessageStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'WsMessageStatus', WsMessageStatus)
