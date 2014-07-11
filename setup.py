from setuptools import setup 
 
import luther
 
if __name__ == "__main__": 
 
    setup( 
        name = luther.__title__, 
        version = luther.__version__, 
        author = luther.__author__, 
        packages = ['luther'], 
    ) 
