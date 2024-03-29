import sys
import hashlib
import json
from virus_total_apis import PublicApi as public_api

# Calculate the total number of arguments 
n = len(sys.argv)

# Read files
def file_input(file_name):
	file = open(file_name,"rb")
	output = file.read()
	return output

if(n == 1 or n > 2):
	print("[-]Invalid Syntax")
	print("Syntax : ./virus_total.py <file_name>")
else:
	api_key = "a4277cc2dd39da34841bcfcf86a67de2e39cafc20aff270d365325e89f3a3c81"
	content = file_input(sys.argv[1])
	md5_sum = hashlib.md5()
	md5_sum.update(content)
	digest = md5_sum.hexdigest()

	vt = public_api(api_key)
	response = vt.get_file_report(digest)
	print(json.dumps(response,sort_keys=False,indent=4))
