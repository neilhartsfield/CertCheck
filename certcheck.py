import shutil
import tempfile
import os, sys
from pathlib import Path
from art import *

# Print Cert Check title
tprint('Cert Check')
print('Author: Neil Hartsfield (Neil.Hartsfield@Trellix.com)')
print('Updated on 07/28/2022 with Juan Sanchez (Juan.SanchezCalvo@Trellix.com)\n')

# Define argument position (for MER's file path) & define certificate blob dictionary 
path = sys.argv[1]
blobs = {
    '02FAF3E291435468607857694DF5E45B68851868': 'AddTrust External CA Root (2020)',
    '0563B8630D62D75ABBC8AB1E4BDFB5A899B24D43': 'DigiCert Assured ID Root CA (2031)',
    '2B8F1B57330DBBA2D07A6C51F70EE90DDAB9AD8E': 'USERTrust RSA Certification Authority (2038)', 
    '3679CA35668772304D30A5FB873B0FA77BB70D54': 'VeriSign Universal Root Certification Authority (2037)', 
    '4EB6D578499B1CCF5F581EAD56BE3D9B6744A5E5': 'VeriSign Class 3 Public Primary Certification Authority - G5 (2036)', 
    '8FBE4D070EF8AB1BCCAF2A9D5CCAE7282A2C66B3': 'Microsoft Code Verification Root (2025)', 
    'B1BC968BD4F49D622AA89A81F2150152A41D829C': 'GlobalSign Root CA (2028)',
    '4EFC31460C619ECAE59C1BCE2C008036D94C84B8': 'GlobalSign Code Signing Root R45 (2045)', 
    'D1EB23A46D17D68FD92564C2F1F1601764D8E349': 'AAA Certificate Services (2028)', 
    'D69B561148F01C77C54578C10926DF5B856976AD': 'GlobalSign (2029)', 
    'E12DFB4B41D7D9C32B30514BAC1D81D8385E2D46': 'UTN-USERFirst-Object (2019)', 
    '090D03435EB2A8364F79B78CB173D35E8EB63558': 'GlobalSign CodeSigning CA - SHA256 - G3 (2024)', 
    '0BBFAB97059595E8D1EC48E89EB8657C0E5AAE71': 'GlobalSign (2028)', 
    '17661DFBA03E6AAA09142E012D216864F01D1F5E': 'McAfee Code Signing CA 2 (2024)', 
    '3BA63A6E4841355772DEBEF9CDCF4D5AF353A297': 'DigiCert SHA2 Assured ID Timestamping CA (2031)',
    '4C5D80D2CD06B1A493C49B2E9BED4A57C2F873E5': 'GlobalSign Code Signing Root R45 (2029)', 
    '495847A93187CFB8C71F840CB7B41497AD95C64F': 'VeriSign Class 3 Code Signing 2010 CA (2020)',
    '7A2146EDB29E2EAD64AFBE7CEAD0B6085D437A32': 'GlobalSign GCC R45 CodeSigning CA 2020 (2030)', 
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
    print('Target MER file', path, 'exists.')

# Get file name
if os.path.exists(path):
    file_name = os.path.basename(path)

# Create temp file and extract MER contents to it
# Open CMD_PS_DIR_CERT, compare with blobs, report those found/missing
# Join PS_DIR_CERT with temp file directory structure
with tempfile.TemporaryDirectory() as tmp:
     print('Creating temporary directory:', tmp)
     shutil.unpack_archive(path, tmp)
     d = tmp
     for path in os.listdir(d):
        full_path = os.path.join(d, path)
        if os.path.isdir(full_path):
            print('Directory structure of MER: ', full_path, '\n')
            cert_text = os.path.join(full_path, 'CMD_PS_DIR_CERT.txt')
            with open(cert_text,encoding="ANSI") as fd:
               contents = fd.read()

for item in blobs:
    if item in contents:
        print('Certificate found: {}'.format(blobs[item]))
    else:
        print('*****MISSING*****: {}'.format(blobs[item]))
        
print('\nCleaning up temp files:', tmp)
print('Thank you for using Cert Check!')
