# this is a namespace package
try:
    import pkg_resources

    pkg_resources.declare_namespace(__name__)
except ImportError:
    import pkgutil

    __path__ = pkgutil.extend_path(__path__, __name__)

'''
__import__('pkg_resources').declare_namespace(__name__)
print(__import__('pkg_resources').declare_namespace(__name__))
'''
