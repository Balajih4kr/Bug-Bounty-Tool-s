import subprocess


subprocess.call(['snap', 'install', 'amass'])

subprocess.call(['git','clone','https://github.com/aboul3la/Sublist3r.git'])

subprocess.call(['apt','install','golang'])

subprocess.call(['go','install','github.com/tomnomnom/assetfinder@latest'])

subprocess.call(['git','clone','https://github.com/findomain/findomain.git'])

subprocess.call(['apt','install','dnsenum'])
subprocess.call(['git','clone','https://github.com/rbsec/dnscan.git'])
subprocess.call(['apt','install','nmap'])

subprocess.call(['go', 'install' ,'github.com/tomnomnom/waybackurls@latest'])

subprocess.call(['git',' clone',' https://github.com/FortyNorthSecurity/EyeWitness.git'])
