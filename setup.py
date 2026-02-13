from setuptools import setup, find_packages

setup(
    name="wmdetection",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
        "scikit-learn",
        "matplotlib",
        "seaborn",
        "flask",
        "praw",
        "tweepy"
    ],
    entry_points={
        "console_scripts": [
            "wmdetection-train = wmdetection.train:main",
            "wmdetection-infer = wmdetection.infer:main",
        ],
    },
)