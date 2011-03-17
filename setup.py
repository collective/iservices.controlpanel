from setuptools import setup, find_packages
import os

version = '0.3.1'

setup(name='iservices.controlpanel',
      version=version,
      description="A generic control panel for themers and site integrators",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Intended Audience :: System Administrators",
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='plone theme control panel',
      author='Noe Nieto',
      author_email='noe@iservices.com.mx',
      url='https://github.com/collective/iservices.controlpanel',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['iservices'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Products.CMFPlone',
          'plone.app.registry',
          
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
