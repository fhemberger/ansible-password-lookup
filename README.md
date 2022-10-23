# Ansible Module: Password Lookup

This is a **patch** for the original Ansible [password lookup](https://docs.ansible.com/ansible/latest/plugins/lookup/password.html), to make sure password files encrypted with `ansible-vault` are decrypted properly.

It uses Ansible's internal method `_get_file_contents`, just like the `file` lookup plugin:

```py
content = None
if os.path.exists(b_path):
  content = to_text(self._loader._get_file_contents(b_path)[0], errors='surrogate_or_strict')
```


## Why the patch?

The current implementation of the password lookup has an annoying bug.

Encrypt a file with `ansible-vault`:

- Ansible's `copy` module decrypts the file, writes the decrypted content to the target host.
- The `file` lookup module decrypts the file, returns the decrypted content.
- The `password` lookup module … well, it returns the **encrypted** content of the file.

This causes all kinds of trouble when you use the password plugin to create randomized, low-impact passwords (e.g. for technical `.htaccess` users, cookie secrets, etc.) which are stored encrypted inside the repository.


## Usage

Copy the `lookup_plugins` directory to the root of your Ansible project and execute `patch.sh` inside of it. This will download the latest version of the original `password.py` lookup plugin and apply the patch.


## License

[GPLv3](LICENSE)
