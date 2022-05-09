import nox


nox.options.sessions = ('mypy', 'style', 'unit')


@nox.session(python=('3.9', '3.10'))
def mypy(session):
  def type(session):
    session.install('mypy')
    session.run('mypy', 'modulemeta', 'tests', 'setup.py', 'noxfile.py')


@nox.session
def style(session):
  session.install('flake8')
  session.run('flake8', '--ignore=E111', 'modulemeta', 'tests', 'setup.py',
              'noxfile.py')


@nox.session(python=('3.9', '3.10'))
def unit(session):
  session.install('pytest', 'pytest-cov')
  session.run('python', 'setup.py', 'develop')
  session.run('pytest', '-v', '--cov-report', 'term-missing',
              '--cov-fail-under=100', '--cov-config=.coveragerc', '--cov',
              'modulemeta/', 'tests/', 'modulemeta/')


@nox.session
def pypi(session):
  session.install('build', 'twine')
  session.run('rm', '-rf', 'sdist', external=True)
  session.run('python', '-m', 'build')
  session.run('twine', 'check', 'dist/*')
  session.run('twine', 'upload', 'dist/*')
