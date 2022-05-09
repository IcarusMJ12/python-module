import nox


@nox.session
def mypy(session):
  def type(session):
    session.install('mypy')
    session.run('mypy', 'modulemeta', 'tests', 'setup.py', 'noxfile.py')


@nox.session
def style(session):
  session.install('flake8')
  session.run('flake8', '--ignore=E111', 'modulemeta', 'tests', 'setup.py',
              'noxfile.py')


@nox.session
def unit(session):
  session.install('pytest', 'pytest-cov')
  session.run('python', 'setup.py', 'develop')
  session.run('pytest', '-v', '--cov-report', 'term-missing',
              '--cov-fail-under=100', '--cov-config=.coveragerc', '--cov',
              'modulemeta/', 'tests/', 'modulemeta/')
