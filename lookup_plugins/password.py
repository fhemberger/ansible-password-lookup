# Patched version of Ansible's `password` lookup module
# Because Ansible contributors refuse to merge this PR,
# calling a bug a feature:
# https://github.com/ansible/ansible/pull/71142
#
# (c) 2012, Daniel Hokka Zakrisson <daniel@hozac.com>
# (c) 2013, Javier Candeira <javier@candeira.com>
# (c) 2013, Maykel Moya <mmoya@speedyrails.com>
# (c) 2017 Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
import os
import inspect

from ansible.module_utils._text import to_text  # type: ignore
from ansible.plugins.lookup import password     # type: ignore

# https://mail.python.org/pipermail/python-dev/2008-January/076194.html
def monkeypatch_method(cls):
    def decorator(func):
        setattr(cls, func.__name__, func)
        return func
    return decorator

@monkeypatch_method(password)
def _read_password_file(b_path):
    """Read the contents of a password file and return it
    Decrypt password automatically if file is encrypted with ansible-vault
    :arg b_path: A byte string containing the path to the password file
    :returns: a text string containing the contents of the password file or
        None if no password file was present.
    """
    content = None

    if os.path.exists(b_path):
        # Yes, I know this is very ugly ...
        # https://stackoverflow.com/a/7272464/409030
        self = inspect.currentframe().f_back.f_locals['self']
        content = to_text(self._loader._get_file_contents(b_path)[0], errors='surrogate_or_strict')

    return content

LookupModule = password.LookupModule
