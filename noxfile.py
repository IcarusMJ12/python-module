import nox


@nox.session
def unit(session):
    session.install('pytest', 'pytest-cov')
    session.run('python', 'setup.py', 'develop')
    session.run('pytest', '-v', '--cov-report', 'term-missing', '--cov-fail-under=100',  '--cov-config=.coveragerc', '--cov', 'modulemeta/', 'tests/', 'modulemeta/')
