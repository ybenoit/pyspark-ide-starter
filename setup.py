from setuptools import setup, find_packages

setup(
    name='pyspark-ide-starter',
    version='0.1',
    description='Starter project to run PySpark in local',
    url="",
    author='Yoann Benoit',
    author_email='',
    license='new BSD',
    packages=find_packages(),
    install_requires=[],
    tests_require=[],
    scripts=[],
    py_modules=["wordcount"],
    include_package_data=True,
    zip_safe=False
)
