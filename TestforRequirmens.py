import pkg_resources
import platform
import psutil
import wmi
import os

 
# Hard-coded library versions
library_versions = {
    'langchain': '0.0.171',
    'pygpt4all': '1.1.0',
    'chromadb': '0.3.23',
    'llama-cpp-python': '0.1.50',
    'urllib3': '2.0.2',
    'pdfminer.six': '20221105',
    'python-dotenv': '1.0.0',
    'unstructured': '0.6.6',
    'extract-msg': '0.41.1',
    'tabulate': '0.9.0',
    'pandoc': '2.3',
    'pypandoc': '1.11',
    'tqdm': '4.65.0'
}
print(r"""\

                               ._ o o
                               \_`-)|_
                            ,""       \ 
                          ,"  ## |   ಠ ಠ. 
                        ," ##   ,-\__    `.
                      ,"       /     `--._;)
                    ,"     ## /
                  ,"   ##    /


            """)
print("------------------------------------------")
print("------------------------------------------")


# Compare installed versions with the hard-coded versions
differences = []
for package, version in library_versions.items():
    installed_version = pkg_resources.get_distribution(package).version
    if installed_version != version:
        differences.append((package, installed_version, version))

# Print the differences
if differences:
    print("Differences between installed versions and hard-coded versions:")
    for package, installed_version, required_version in differences:
        print(f"{package}: Installed={installed_version}, Required={required_version}")
else:
    print("All required packages are installed with the correct versions.")
print("------------------------------------------")
print("------------------------------------------")
windows_version = platform.platform()
python_version = platform.python_version()
cpu_info = []
cpu = platform.processor()
cpu_info.append(cpu)

# Retrieve GPU information
wmi_obj = wmi.WMI()
gpu_info = []
for gpu in wmi_obj.Win32_VideoController():
    gpu_info.append(gpu.Name)

# Retrieve motherboard information
wmi_obj = wmi.WMI()
motherboard_info = []
for board in wmi_obj.Win32_BaseBoard():
    motherboard_info.append(board.Product)

print("------------------------------------------")
# Print the information
print("Windows Version:", windows_version)
print("------------------------------------------")
print("Python Version:", python_version)
print("------------------------------------------")
print("CPU:", cpu_info[0])
print("GPU:", gpu_info)
print("------------------------------------------")
print("Motherboard:", motherboard_info)
print("------------------------------------------")
print("------------------------------------------")