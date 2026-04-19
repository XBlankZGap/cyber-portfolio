def create_wazuh_install_script():
    # Collect user input
    company = input("Enter company name: ").strip().replace(" ", "")
    department = input("Enter department: ").strip().replace(" ", "")
    staff_name = input("Enter staff name: ").strip().replace(" ", "")
    staff_id = input("Enter ID number: ").strip()

    # Create the WAZUH_AGENT_NAME from input
    wazuh_agent_name = f"{company}_{department}_{staff_name}_{staff_id}"

    # Wazuh install command
    manager_ip = "192.168.0.193"  # change this if needed
    deb_package = "wazuh-agent_4.12.0-1_amd64.deb"
    script = (
        f"wget https://packages.wazuh.com/4.x/apt/pool/main/w/wazuh-agent/{deb_package} "
        f"&& sudo WAZUH_MANAGER='{manager_ip}' WAZUH_AGENT_NAME='{wazuh_agent_name}' "
        f"dpkg -i ./{deb_package}"
    )

    print("\nGenerated Wazuh install command:\n")
    print(script)


if __name__ == "__main__":
    create_wazuh_install_script()

