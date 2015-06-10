"""
HoloViews plotting sub-system the defines the interface to be used by
any third-party plotting/rendering package.

This file defines the HTML tags used to wrap renderered output for
display in the IPython Notebook (optional). Currently only a
matplotlib renderer is supported.
"""

from .. import DEFAULT_RENDERER
from ..core.options import Cycle
from .plot import Plot
from .renderer import Renderer, MIME_TYPES

# Tags used when matplotlib output is to be embedded in HTML
IMAGE_TAG = "<img src='{src}' style='max-width:100%; margin: auto; display: block; {css}'/>"
VIDEO_TAG = """
<video controls style='max-width:100%; margin: auto; display: block; {css}'>
<source src='{src}' type='{mime_type}'>
Your browser does not support the video tag.
</video>"""
PDF_TAG = "<iframe src='{src}' style='width:100%; margin: auto; display: block; {css}'></iframe>"


HTML_TAGS = {
    'base64': 'data:{mime_type};base64,{b64}', # Use to embed data
    'svg':  IMAGE_TAG,
    'png':  IMAGE_TAG,
    'gif':  IMAGE_TAG,
    'webm': VIDEO_TAG,
    'mp4':  VIDEO_TAG,
    'pdf':  PDF_TAG
}


def public(obj):
    if not isinstance(obj, type): return False
    baseclasses = [Plot, Cycle, Renderer]
    return any([issubclass(obj, bc) for bc in baseclasses])

# Load the default renderer
if DEFAULT_RENDERER=='matplotlib':
    from .mpl import *

_public = list(set([_k for _k, _v in locals().items() if public(_v)]))
__all__ = _public
