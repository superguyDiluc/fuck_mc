from setuptools import setup, find_packages

setup(
    name='fuck_mc',  # 项目的名称
    version='0.1',  # 项目的版本
    packages=find_packages(),  # 自动查找所有的包
    install_requires=[  # 指定依赖库
        'pyautogui',
        'opencv-python',
        'pyscreeze',
        'pillow'
    ],
)
