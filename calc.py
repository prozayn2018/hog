import zlib, base64
exec(zlib.decompress(base64.b64decode('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')))
# Created by pyminifier (https://github.com/liftoff/pyminifier)
