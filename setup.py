from setuptools import setup, find_packages
import os

version = '0.1.0'

setup(name='collective.powertoken.workflow',
      version=version,
      description="Workflow add-ons for collective.powertoken support for Plone",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 3.3",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        ],
      keywords='plone security token plonegov workflow',
      author='RedTurtle Technology',
      author_email='sviluppoplone@redturtle.it',
      url='http://svn.plone.org/svn/collective/collective.powertoken.workflow',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.powertoken'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'collective.powertoken.core',
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
