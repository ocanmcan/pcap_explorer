from setuptools import find_packages, setup

setup(
    name="lpw",
    version=version,
    description="Using Local Packet Whisperer (LPW, Chat with PCAP/PCAPNG files locally, privately!",
    packages=find_packages(),
    package_dir={'lpw' : '.'},
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kspviswa/local-packet-whisperer",
    author="Viswa Kumar",
    author_email="kspviswaphd@gmail.com",
    license="MIT",
    scripts=['bin/lpw', 'bin/lpw_main.py', 'bin/lpw_ollamaClient.py', 'bin/lpw_packet.py', 'bin/lpw_prompt.py'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    install_requires = deps,
    include_package_data=True,
    python_requires=">=3.12",
)   
