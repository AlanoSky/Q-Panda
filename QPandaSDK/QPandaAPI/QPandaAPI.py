# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_QPandaAPI', [dirname(__file__)])
        except ImportError:
            import _QPandaAPI
            return _QPandaAPI
        if fp is not None:
            try:
                _mod = imp.load_module('_QPandaAPI', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _QPandaAPI = swig_import_helper()
    del swig_import_helper
else:
    import _QPandaAPI
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0


class intp(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, intp, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, intp, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _QPandaAPI.new_intp()
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _QPandaAPI.delete_intp
    __del__ = lambda self: None

    def assign(self, value):
        return _QPandaAPI.intp_assign(self, value)

    def value(self):
        return _QPandaAPI.intp_value(self)

    def cast(self):
        return _QPandaAPI.intp_cast(self)
    __swig_getmethods__["frompointer"] = lambda x: _QPandaAPI.intp_frompointer
    if _newclass:
        frompointer = staticmethod(_QPandaAPI.intp_frompointer)
intp_swigregister = _QPandaAPI.intp_swigregister
intp_swigregister(intp)

def intp_frompointer(t):
    return _QPandaAPI.intp_frompointer(t)
intp_frompointer = _QPandaAPI.intp_frompointer


_QPandaAPI.CPU_swigconstant(_QPandaAPI)
CPU = _QPandaAPI.CPU

_QPandaAPI.GPU_swigconstant(_QPandaAPI)
GPU = _QPandaAPI.GPU

_QPandaAPI.MEASURE_swigconstant(_QPandaAPI)
MEASURE = _QPandaAPI.MEASURE

_QPandaAPI.PMEASURE_swigconstant(_QPandaAPI)
PMEASURE = _QPandaAPI.PMEASURE
class QPandaAPI(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, QPandaAPI, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, QPandaAPI, name)
    __repr__ = _swig_repr
    __swig_setmethods__["msFileName"] = _QPandaAPI.QPandaAPI_msFileName_set
    __swig_getmethods__["msFileName"] = _QPandaAPI.QPandaAPI_msFileName_get
    if _newclass:
        msFileName = _swig_property(_QPandaAPI.QPandaAPI_msFileName_get, _QPandaAPI.QPandaAPI_msFileName_set)
    __swig_setmethods__["msResult"] = _QPandaAPI.QPandaAPI_msResult_set
    __swig_getmethods__["msResult"] = _QPandaAPI.QPandaAPI_msResult_get
    if _newclass:
        msResult = _swig_property(_QPandaAPI.QPandaAPI_msResult_get, _QPandaAPI.QPandaAPI_msResult_set)
    __swig_setmethods__["msState"] = _QPandaAPI.QPandaAPI_msState_set
    __swig_getmethods__["msState"] = _QPandaAPI.QPandaAPI_msState_get
    if _newclass:
        msState = _swig_property(_QPandaAPI.QPandaAPI_msState_get, _QPandaAPI.QPandaAPI_msState_set)

    def __init__(self):
        this = _QPandaAPI.new_QPandaAPI()
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _QPandaAPI.delete_QPandaAPI
    __del__ = lambda self: None

    def loadFile(self, sFilePath, Qnum):
        return _QPandaAPI.QPandaAPI_loadFile(self, sFilePath, Qnum)

    def setComputeUnit(self, iComputeUnit):
        return _QPandaAPI.QPandaAPI_setComputeUnit(self, iComputeUnit)

    def run(self, iRepeat):
        return _QPandaAPI.QPandaAPI_run(self, iRepeat)

    def getResult(self):
        return _QPandaAPI.QPandaAPI_getResult(self)

    def getQuantumState(self):
        return _QPandaAPI.QPandaAPI_getQuantumState(self)
QPandaAPI_swigregister = _QPandaAPI.QPandaAPI_swigregister
QPandaAPI_swigregister(QPandaAPI)


_QPandaAPI.qErrorNone_swigconstant(_QPandaAPI)
qErrorNone = _QPandaAPI.qErrorNone

_QPandaAPI.undefineError_swigconstant(_QPandaAPI)
undefineError = _QPandaAPI.undefineError

_QPandaAPI.qParameterError_swigconstant(_QPandaAPI)
qParameterError = _QPandaAPI.qParameterError

_QPandaAPI.qbitError_swigconstant(_QPandaAPI)
qbitError = _QPandaAPI.qbitError

_QPandaAPI.loadFileError_swigconstant(_QPandaAPI)
loadFileError = _QPandaAPI.loadFileError

_QPandaAPI.initStateError_swigconstant(_QPandaAPI)
initStateError = _QPandaAPI.initStateError

_QPandaAPI.destroyStateError_swigconstant(_QPandaAPI)
destroyStateError = _QPandaAPI.destroyStateError

_QPandaAPI.setComputeUnitError_swigconstant(_QPandaAPI)
setComputeUnitError = _QPandaAPI.setComputeUnitError

_QPandaAPI.runProgramError_swigconstant(_QPandaAPI)
runProgramError = _QPandaAPI.runProgramError

_QPandaAPI.getResultError_swigconstant(_QPandaAPI)
getResultError = _QPandaAPI.getResultError

_QPandaAPI.getQStateError_swigconstant(_QPandaAPI)
getQStateError = _QPandaAPI.getQStateError
# This file is compatible with both classic and new-style classes.


