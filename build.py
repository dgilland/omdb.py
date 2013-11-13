
import os

import omdb

if __name__ == '__main__':

    version = omdb.__version__

    # update VERSION based on package version
    with open('VERSION', 'w') as f:
        f.write(version)

    # update README with package version
    with open('README.md', 'r') as f:
        readme = f.readlines()

    for i, line in enumerate(readme):
        if line.startswith('Version:'):
            readme[i] = 'Version: `{0}`\n'.format(version)

    with open('README.md', 'w') as f:
        f.write(''.join(readme))

