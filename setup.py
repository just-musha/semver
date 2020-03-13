from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='semver',
    version='0.1.0',
    author='mbulatova',
    author_email='maria.r.bulatova@gmail.com',
    description='Git semantic versioning tool',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/mbulatova/semver',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=['pygithub', 'click'],
    python_requires='>=3.6',
    entry_points={
        'console_scripts':[
            'semver=semver.cli:cli'
        ],
    }
)
