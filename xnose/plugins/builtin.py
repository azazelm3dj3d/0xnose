"""
Lists builtin plugins.
"""
plugins = []
builtins = (
    ('xnose.plugins.attrib', 'AttributeSelector'),
    ('xnose.plugins.capture', 'Capture'),
    ('xnose.plugins.logcapture', 'LogCapture'),
    ('xnose.plugins.cover', 'Coverage'),
    ('xnose.plugins.debug', 'Pdb'),
    ('xnose.plugins.deprecated', 'Deprecated'),
    ('xnose.plugins.doctests', 'Doctest'),
    ('xnose.plugins.isolate', 'IsolationPlugin'),
    ('xnose.plugins.failuredetail', 'FailureDetail'),
    ('xnose.plugins.prof', 'Profile'),
    ('xnose.plugins.skip', 'Skip'),
    ('xnose.plugins.testid', 'TestId'),
    ('xnose.plugins.multiprocess', 'MultiProcess'),
    ('xnose.plugins.xunit', 'Xunit'),
    ('xnose.plugins.allmodules', 'AllModules'),
    ('xnose.plugins.collect', 'CollectOnly'),
    )

for module, cls in builtins:
    try:
        plugmod = __import__(module, globals(), locals(), [cls])
    except KeyboardInterrupt:
        raise
    except:
        continue
    plug = getattr(plugmod, cls)
    plugins.append(plug)
    globals()[cls] = plug

