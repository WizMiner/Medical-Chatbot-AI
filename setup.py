from setuptools import find_packages, setup

setup(
    name='Generative AI Project',
    version='0.0.0',
    author='MINTE',
    author_email='mintesinottamene0917@gmail.com',
    description='A Generative AI project for chatbot development',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        # Add dependencies here
        # Example: 'numpy>=1.21.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
