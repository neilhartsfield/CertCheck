import shutil
import tempfile
import os, sys
from pathlib import Path
from art import *

#Print Cert Check title
tprint("Cert Check")

# Define argument position (for MER's file path) & define certificate blobs 
path = sys.argv[1]
blobs = {
    '02FAF3E291435468607857694DF5E45B68851868': 'AddTrust External CA Root (2020)',
    '0563B8630D62D75ABBC8AB1E4BDFB5A899B24D43': 'DigiCert Assured ID Root CA (2031)',
    '2B8F1B57330DBBA2D07A6C51F70EE90DDAB9AD8E': 'USERTrust RSA Certification Authority (2038)', 
    '3679CA35668772304D30A5FB873B0FA77BB70D54': 'VeriSign Universal Root Certification Authority (2037)', 
    '4EB6D578499B1CCF5F581EAD56BE3D9B6744A5E5': 'VeriSign Class 3 Public Primary Certification Authority - G5 (2036)', 
    '8FBE4D070EF8AB1BCCAF2A9D5CCAE7282A2C66B3': 'Microsoft Code Verification Root (2025)', 
    'B1BC968BD4F49D622AA89A81F2150152A41D829C': 'GlobalSign Root CA (2028)', 
    'D1EB23A46D17D68FD92564C2F1F1601764D8E349': 'AAA Certificate Services (2028)', 
    'D69B561148F01C77C54578C10926DF5B856976AD': 'GlobalSign (2029)', 
    'E12DFB4B41D7D9C32B30514BAC1D81D8385E2D46': 'UTN-USERFirst-Object (2019)', 
    '090D03435EB2A8364F79B78CB173D35E8EB63558': 'GlobalSign CodeSigning CA - SHA256 - G3 (2024)', 
    '0BBFAB97059595E8D1EC48E89EB8657C0E5AAE71': 'GlobalSign (2028)', 
    '17661DFBA03E6AAA09142E012D216864F01D1F5E': 'McAfee Code Signing CA 2 (2024)', 
    '3BA63A6E4841355772DEBEF9CDCF4D5AF353A297': 'DigiCert SHA2 Assured ID Timestamping CA (2031)', 
    '495847A93187CFB8C71F840CB7B41497AD95C64F': 'VeriSign Class 3 Code Signing 2010 CA (2020)', 
    '9151B539751B891401C745A9DE301CBDBADF3FB6': 'McAfee OV SSL CA 2 (2024)', 
    'A75AC657AA7A4CDFE5F9DE393E69EFCAB659D250': 'AddTrust External CA Root (2023)', 
    'B69E752BBE88B4458200A7C0F4F5B3CCE6F35B47': 'COMODO RSA Code Signing CA (2028)', 
    'CC1DEEBF6D55C2C9061BA16F10A0BFA6979A4A32': 'GlobalSign Root CA (2021)', 
    'D89E3BD43D5D909B47A18977AA9D5CE36CEE184C': 'USERTrust RSA Certification Authority by AAA Certificate Services (2028)', 
    'EAB040689A0D805B5D6FD654FC168CFF00B78BE3': 'USERTrust RSA Certification Authority (2020)', 
    'F1E7B6C0C10DA9436ECC04FF5FC3B6916B46CF4C': 'GlobalSign CodeSigning CA - G3 (2024)', 
    }

# Check if path exits
if os.path.exists(path):
    print("Target MER file", path, "exists.")

# Create temp file and extract MER contents to it
tmp = tempfile.TemporaryDirectory()
print("Temporary directory created at:", tmp.name)
shutil.unpack_archive(path, tmp.name)

# Join PS_DIR_CERT with temp file directory structure
cert_text = os.path.join(tmp.name, "0", "CMD_PS_DIR_CERT.txt")

# Open CMD_PS_DIR_CERT, compare with blobs, report those found/missing
file1 = open(cert_text, "r")
readfile = file1.read()

for item in blobs:
    if item in readfile:
        print("Certificate found: {}".format(blobs[item]))
    else:
        print("*****MISSING*****: {}".format(blobs[item]))

file1.close()

print("Cleaning up temp files:", tmp.name)