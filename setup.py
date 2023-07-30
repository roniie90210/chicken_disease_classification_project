import setuptools

with open('README.md',"r",encoding="utf-8") as f:
    long_description = f.read()
    

__version__ ="0.0.0"

REPO_NAME="chicken_disease_classification_project"
AUTHOR_USERNAME="roniie90210"
SRC_REPO="cnnClassifiers"
AUTHOR_EMAIL="rohan.kshatriya92@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USERNAME,
    author_email=AUTHOR_EMAIL,
    description="A smalll python package for CNN app",
    long_description=long_description,
    url=f"https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": "https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)