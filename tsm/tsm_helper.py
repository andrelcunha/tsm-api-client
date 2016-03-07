from __future__ import (absolute_import, unicode_literals)

from tsm.tsm_definitions import *

__author__ = 'bbrauns'


def convert_size_to_hi_lo(size):
    bin_str = '{0:064b}'.format(size)
    hi = int(bin_str[:32], 2)
    lo = int(bin_str[32:], 2)
    return hi, lo


def convert_hi_lo_to_size(hi, lo):
    bin_high = '{0:032b}'.format(hi)
    bin_low = '{0:032b}'.format(lo)
    bin_str = bin_high + bin_low
    return int(bin_str, 2)


def media_class_to_str(media_class):
    media_classes = {str(MEDIA_FIXED): 'fixed',
                     str(MEDIA_LIBRARY): 'library',
                     str(MEDIA_NETWORK): 'network',
                     str(MEDIA_SHELF): 'shelf',
                     str(MEDIA_OFFSITE): 'offsite',
                     str(MEDIA_UNAVAILABLE): 'unavailable'}
    return media_classes.get(str(media_class), 'unknown')


# noinspection PyProtectedMember,PyTypeChecker
def convert_tsm_structure_to_str(struct):
    repr_str = ''
    for field_definition in struct._fields_:
        value = getattr(struct, field_definition[0])
        if value is dsStruct64_t:
            value = str(convert_hi_lo_to_size(hi=value.hi,
                                              lo=value.lo))
        elif isinstance(value, Structure):
            value = '\'' + convert_tsm_structure_to_str(value) + '\''  # recursive
        else:
            value = getattr(struct, field_definition[0])
        repr_str += '{field}={value}, \n'.format(field=field_definition[0], value=value)
    return repr_str
