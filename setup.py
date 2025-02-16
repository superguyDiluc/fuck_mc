from setuptools import setup, find_packages

setup(
    name='fuck_mc',
    version='0.1',
    description='A Tool For Shenghai',
    author='Diluc',
    author_email='1727327536@qq.com',
    packages=find_packages(),
    install_requires=[  # 指定依赖库
        'pyautogui',
        'opencv-python',
        'pyscreeze',
        'pillow',
        'keyboard'
    ]
)
