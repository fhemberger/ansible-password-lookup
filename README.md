# Ansible Module: Password Lookup

This is a **patched version** of the original Ansible [password lookup](https://docs.ansible.com/ansible/latest/plugins/lookup/password.html), to make sure password files encrypred with `ansible-vault` are decrypred properly.

It uses Ansible's internal method `_get_file_contents`, just like the `file` lookup plugin:

```py
content = None
if os.path.exists(b_path):
    b_content, show_data = self._loader._get_file_contents(b_path)
    content = to_text(b_content.rstrip(),
                      errors='surrogate_or_strict')
```


## License

[GPLv3](LICENSE)
