from setuptools import find_packages, setup

# setup(
#     name='blip',
#     python_requires='>=3.6, <4',
#     packages=find_packages(exclude=('docs', 'test', 'examples')),
#     install_requires=[
#         "fairscale>=0.4.4"
#     ],
#     zip_safe=False)

setup(
    name="blip",
    py_modules=["blip"],
    version="1.0",
    description="",
    author="Salesforce",
    packages=find_packages(),
    install_requires=[
        "fairscale>=0.4.4"
    ],
    include_package_data=True,
)