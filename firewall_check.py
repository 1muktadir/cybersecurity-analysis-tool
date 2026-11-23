
import subprocess

print("Checking Windows Firewall Status...")

result = subprocess.run(
    ["netsh", "advfirewall", "show", "allprofiles"],
    capture_output=True,
    text=True
)

if result.returncode == 0:
    print(result.stdout)
else:
    print("Unable to check firewall status.")
