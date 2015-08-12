import pyxb
import ern312
import ern32
import ern33
import ern34
import ern341
import ern35
import ern351
import ern36


def open_ddex(path):
    """
    Open an XML from a path and parse it into a DDEX data structure.
    This script automatically finds which ERN version to use.

    Args:
        path (str): path to the XML file.

    Returns:
        A DDEX data structure. The type depends on the ERN version.

    Raises:
        ValueError: No ERN version compatible with this DDEX file.
    """
    with open(path, 'rb') as f:
        xml_data = f.read()

    if 'MessageSchemaVersionId="2010/ern-main/312"' in xml_data:
        return ern312.CreateFromDocument(xml_data)
    elif 'MessageSchemaVersionId="ern/32"' in xml_data:
        return ern32.CreateFromDocument(xml_data)
    elif 'MessageSchemaVersionId="2011/ern-main/33"' in xml_data:
        return ern33.CreateFromDocument(xml_data)
    elif 'MessageSchemaVersionId="ern/34"' in xml_data:
        return ern34.CreateFromDocument(xml_data)
    elif 'MessageSchemaVersionId="ern/341"' in xml_data:
        return ern341.CreateFromDocument(xml_data)
    elif 'MessageSchemaVersionId="ern/35"' in xml_data:
        return ern35.CreateFromDocument(xml_data)
    elif 'MessageSchemaVersionId="ern/351"' in xml_data:
        return ern351.CreateFromDocument(xml_data)
    elif 'MessageSchemaVersionId="ern/36"' in xml_data:
        return ern36.CreateFromDocument(xml_data)
    else:
        raise ValueError('No ERN version compatible with this DDEX file.')


def ddex_to_dict(ddex):
    """
    Parse a DDEX data structure into a dictionary whose leaves are unicode strings
    or data structures from pyxb.

    Args:
        ddex: the result of applying ddexreader.open_ddex

    Returns:
        A dictionarywhose leaves are unicode strings or data structures from pyxb.
    """
    # Ddex attributes start with an uppercase letter in pyxb. Factory is used by pyxb
    attributes = [attr for attr in dir(ddex) if attr[0].isupper() and attr != 'Factory']

    # Check if we have a leaf type (which means its repr will be a string containing a unicode string)
    if 'object' not in repr(ddex):
        return unicode(ddex)
    d = {}

    for attr in attributes:
        value = getattr(ddex, attr)
        # Some leaf elements have a value method, others do not
        if hasattr(value, 'value'):
            try:
                value = value.value()
            except pyxb.NotSimpleContentError:
                # In this case value was not a leaf element
                value = ddex_to_dict(value)
        elif isinstance(value, pyxb.binding.content._PluralBinding):
            value = [ddex_to_dict(el) for el in value]
        d[attr] = value
    return d
