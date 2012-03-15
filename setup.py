from setuptools import setup, find_packages

setup(name='helloworld',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      install_requires=['setuptools', 'yafowil.webob',]
      entry_points = """\
      [console_scripts]      
      helloworld = helloworld.run:run    
      """ 
)