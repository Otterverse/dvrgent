from setuptools import setup

setup(
    name='dvrgent',
    packages=['ui', 'hdhomerun', 'schedulesdirect'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-sqlalchemy',
	'flask-wtf',
	'WTForms-SQLAlchemy',
    ],
)
