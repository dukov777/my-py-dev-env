import subprocess

print('hello from container')
current_dir = subprocess.run(['cat', '/proc/version'], capture_output=True)
print(current_dir.stdout)
