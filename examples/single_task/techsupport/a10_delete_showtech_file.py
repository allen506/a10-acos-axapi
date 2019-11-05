- name: Delete a10_Generates Show Tech file example playbook
  connection: local
  hosts: localhost
  tasks:
  - name: Delete a10_Generates Show Tech file instance
    a10_generates_show_tech_file:
      a10_host: "{{ a10_host }}"
      a10_username: "{{ a10_username }}"
      a10_password: "{{ a10_password }}"
      a10_port: "{{ a10_port }}"
      a10_protocol: "{{ a10_protocol }}"
      state: absent
