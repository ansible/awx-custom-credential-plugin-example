AWX Custom Credential Plugin Example
---

To write your own plugin (or to test this example plugin):

1.  Fork this repository and edit its source code to interface with your credential management system of choice.
2.  Define any necessary Python dependencies (e.g., client SDKs) necessary to integrate with your credential system by setting the `requirements` variable in `setup.py`.
3.  From *all* AWX/Red Hat Ansible Tower nodes, install the plugin into the AWX virtualenv:

```shell
~ awx-python -m pip install git+https://github.com/ansible/awx-custom-credential-plugin-example.git
```

4.  From *any* AWX/Red Hat Ansible Tower node, run this command to register the plugin:

```shell
~ awx-manage setup_managed_credential_types
```

5.  Restart all AWX Tower services on all nodes.

![Example Credential Plugin](https://user-images.githubusercontent.com/214912/79345288-ebbc4a80-7efe-11ea-884e-58635b2d4600.gif)
