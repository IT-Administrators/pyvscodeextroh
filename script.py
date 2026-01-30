from pyvscodeextroh import PolicyEditor

editor = PolicyEditor()  # /etc/vscode/policy.json

editor.allow_publisher("microsoft")
editor.allow_publisher("github")
editor.allow_extension("IT-Administrators.mdmanroh")
editor.remove_publisher("IT-Administrators")
editor.remove_extension("IT-Administrators.mdmanroh")
