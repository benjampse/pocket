# EXPERIMENTAL

# mod generated from https://github.com/piotr022/UV_K5_playground/releases/download/release-47/uv_k5_26_rssi_sbar_encoded_v47.bin



##--------------------- do not modify below this line ---------------------------------------------------
import os,sys,struct
print('Running',os.path.basename(sys.argv[0]),'mod...')
fw =  bytearray(open(sys.argv[1],'rb').read())

fw[0x0004:0x0004+4] = b'\xe7\xe5\x00\x00' #New Reset Handler
fw[0x003C:0x003C+4] = b'\x1d\xe7\x00\x00' #New SysTick Handler


payload = b'\x10\xb5\x06\x4c\x23\x78\x00\x2b\x07\xd1\x05\x4b\x00\x2b\x02\xd0\x04\x48\x00\xe0\x00\xbf\x01\x23\x23\x70\x10\xbd\xa8\x13\x00\x20\x00\x00\x00\x00\xc0\x00\x00\x00\x04\x4b\x10\xb5\x00\x2b\x03\xd0\x03\x49\x04\x48\x00\xe0\x00\xbf\x10\xbd\xc0\x46\x00\x00\x00\x00\xac\x13\x00\x20\xc0\x00\x00\x00\x00\x23\xc2\x5c\x01\x33\x00\x2a\xfb\xd1\x58\x1e\x70\x47\x00\x20\x70\x47\xd3\x08\xdb\x01\x59\x18\xe0\x23\x9b\x00\x99\x42\x07\xd8\x07\x23\x1a\x40\x06\x3b\x93\x40\x40\x68\x42\x5c\x13\x43\x43\x54\x70\x47\x40\x68\x40\x18\x70\x47\x00\x20\x70\x47\x0a\x00\x30\x3a\x03\x00\xd0\xb2\x09\x28\x05\xd9\x00\x20\x2d\x29\x01\xd1\x58\x68\x46\x30\x70\x47\x07\x20\x42\x43\x58\x68\x80\x18\xf9\xe7\x08\x20\x70\x47\x07\x20\x70\x47\x00\x20\x70\x47\x70\x47\x70\x47\xe0\x22\x10\xb5\x00\x21\x40\x68\x92\x00\x00\xf0\x95\xfb\x10\xbd\x10\xb5\xd5\x23\x98\x47\x10\xbd\x00\x00\xf8\xb5\xc3\x68\x04\x00\x5a\x1c\xc2\x60\xc7\x2a\x4c\xd9\x29\x4b\x00\x25\x19\x78\x01\x23\xff\x39\x48\x42\x48\x41\x21\x7c\x99\x43\x01\x43\x04\x20\x21\x74\x24\x49\x09\x68\x8b\x43\x23\x49\xdb\x00\x09\x78\x89\x00\x01\x40\x0b\x43\x21\x7c\x08\x30\x81\x43\x0b\x43\x23\x74\x53\x07\x09\xd1\x23\x68\x18\x68\xa8\x42\x05\xd0\x21\x00\x03\x68\x08\x31\x5b\x68\x98\x47\x05\x00\x66\x68\x00\x2e\x1b\xd0\xe3\x68\xdb\x07\x18\xd4\x16\x4b\x98\x47\x21\x7e\xc7\xb2\x8f\x42\x0a\xd0\x63\x69\x58\x68\xff\x29\x17\xd1\x00\x28\x03\xd0\x39\x00\x03\x68\x9b\x68\x98\x47\x27\x76\x21\x00\x33\x68\x30\x00\x1b\x68\x08\x31\x98\x47\x05\x43\xed\xb2\xab\x07\x01\xd5\x09\x4b\x98\x47\xeb\x07\x01\xd5\x08\x4b\x98\x47\xf8\xbd\x00\x28\xeb\xd0\x03\x68\xdb\x68\xe7\xe7\x35\x08\x00\x20\x00\x10\x06\x40\x1e\x0a\x00\x20\xb9\xb0\x00\x00\x39\xb6\x00\x00\xb1\xb6\x00\x00\xf7\xb5\x04\x00\x04\x26\x5f\x20\x14\x4f\xb8\x47\x01\x90\xa0\x68\x00\x28\x09\xd0\x23\x7b\x62\x8a\x02\x3b\x9a\x42\x04\xda\x80\x18\x01\xa9\x02\x22\x00\xf0\x0c\xfb\x63\x8a\x01\x3e\x02\x33\x9b\xb2\xf6\xb2\x63\x82\x00\x2e\xe6\xd1\x25\x7b\xab\x42\x0d\xd3\x0b\x20\x26\x74\xb8\x47\x02\x00\x20\x68\x00\x28\x06\xd0\x63\x68\x00\x2b\x03\xd0\xd2\x06\x29\x00\xd2\x0f\x98\x47\xf7\xbd\x61\xa9\x00\x00\x70\xb5\x1a\x4c\x23\x78\x00\x2b\x05\xd1\x00\xf0\xb5\xfa\x00\xf0\xc3\xfa\x01\x23\x23\x70\x16\x4b\x1b\x68\xdb\x07\x1f\xd5\x15\x4d\x2b\x7c\x01\x2b\x1b\xd1\x3f\x20\x13\x4c\xa0\x47\xc0\x21\x03\x00\x89\x01\x0b\x40\x8b\x42\x03\xd0\x01\x43\x10\x4b\x3f\x20\x98\x47\x0c\x20\xa0\x47\xc3\x07\x0a\xd5\x02\x20\x0c\x4b\x00\x21\x98\x47\x02\x20\xa0\x47\xc3\x04\x02\xd5\x28\x00\xff\xf7\xa1\xff\x08\x48\xff\xf7\x38\xff\x07\x4b\x98\x47\x70\xbd\xc0\x46\x24\x14\x00\x20\x00\x10\x06\x40\xe8\x13\x00\x20\x61\xa9\x00\x00\x01\xaf\x00\x00\xcc\x13\x00\x20\x99\xc3\x00\x00\xf8\xb5\x04\x00\x40\x68\x0d\x00\x00\x28\x1f\xd0\x03\x68\x5b\x68\x98\x47\x07\x00\x20\x68\x21\x89\x03\x68\x9b\x68\x98\x47\x06\x00\x60\x68\x29\x00\x03\x68\xdb\x68\x98\x47\x02\x00\x00\x2e\x05\xd0\x39\x00\x30\x00\x00\x2f\x0b\xd0\x00\xf0\x8e\xfa\x60\x68\x29\x00\x03\x68\xdb\x68\x98\x47\x23\x89\x1b\x18\x23\x81\x00\x20\xf8\xbd\x00\xf0\x8b\xfa\xf2\xe7\x70\xb5\x06\x00\x0d\x00\x00\x24\x28\x00\xff\xf7\xb0\xfe\x84\x42\x06\xd2\x29\x5d\x30\x00\x01\x34\xff\xf7\xc7\xff\xe4\xb2\xf3\xe7\x70\xbd\xf0\xb5\x0c\x00\x00\x21\x87\xb0\x17\x00\x01\x90\x07\x22\x04\xa8\x1e\x00\x03\x91\x00\xf0\x6d\xfa\x00\x2c\x04\xda\x2d\x21\x01\x98\xff\xf7\xb2\xff\x64\x42\x19\x4b\x00\x93\x00\x23\x19\x00\x08\x22\xd2\x1a\x97\x42\x19\xdc\x00\x9a\x12\x6a\x94\x46\x00\x22\xa4\x45\x03\xdc\x60\x46\x01\x32\x24\x1a\xf9\xe7\x30\x20\x84\x46\x94\x44\x65\x46\x03\xa8\xc5\x54\x00\x2a\x02\xd0\x00\x29\x00\xd1\x19\x00\x00\x9a\x01\x33\x04\x3a\x00\x92\xe1\xe7\x03\xab\x00\x29\x01\xd1\x30\x22\x1a\x70\x00\x2e\x02\xd0\x09\x21\xc9\x1b\x89\x1b\x01\x98\x59\x18\xff\xf7\xac\xff\x07\xb0\xf0\xbd\xc0\x46\x64\xed\x00\x00\xf0\xb5\x0c\x00\x87\xb0\x0d\xa9\x09\x78\x16\x00\xe3\x18\x0c\xaa\x05\x00\x12\x78\x05\x91\x01\x93\x80\x2b\x01\xdd\x80\x23\x01\x93\x6b\x46\x1b\x79\x03\x93\xb3\x18\x02\x93\x38\x2b\x01\xdd\x38\x23\x02\x93\x6b\x46\x37\x00\x1b\x7a\x04\x93\x04\x9b\x9f\x42\x10\xd2\x28\x68\x3a\x00\x03\x68\x21\x00\x5b\x68\x98\x47\x03\x9b\x28\x68\x59\x1e\x03\x68\x3a\x00\x5b\x68\xc9\xb2\x01\x37\x98\x47\xff\xb2\xeb\xe7\x27\x00\x03\x9b\x9f\x42\x10\xd2\x28\x68\x39\x00\x03\x68\x32\x00\x5b\x68\x98\x47\x04\x9b\x28\x68\x5a\x1e\x03\x68\x39\x00\x5b\x68\xd2\xb2\x01\x37\x98\x47\xff\xb2\xeb\xe7\x05\x9b\x00\x2b\x13\xd0\x01\x9b\x01\x34\xe4\xb2\x01\x3b\x9c\x42\x0d\xda\x77\x1c\x02\x9b\xff\xb2\x01\x3b\x9f\x42\xf3\xda\x28\x68\x3a\x00\x03\x68\x21\x00\x5b\x68\x98\x47\x01\x37\xf2\xe7\x07\xb0\xf0\xbd\x00\x00\xf0\xb5\x0b\x7a\x04\x00\x0d\x00\x87\xb0\x1b\x07\x00\xd5\x11\xe1\x0b\x68\x1b\x68\x00\x2b\x06\xd0\x87\x4b\x01\x20\x1b\x78\x00\x2b\x34\xd0\x07\xb0\xf0\xbd\x83\x68\x5a\x1c\x82\x60\x5b\x07\xf3\xd0\x82\x4b\x83\x4e\x1a\x68\x01\x23\x52\x09\x93\x43\x43\x74\x0c\x20\xb0\x47\xb4\x46\x7f\x49\x83\x07\x02\xd4\x62\x7c\x00\x2a\x01\xd0\x00\x22\x0a\x70\x0a\x78\x7c\x48\x0a\x2a\x06\xd8\x2f\x7a\x01\x26\x3b\x00\x33\x40\x02\x93\x37\x42\x3e\xd0\x01\x78\x00\x29\x00\xd0\xe0\xe0\x01\x24\x75\x4b\x04\x70\x80\x22\x18\x68\x00\xf0\x91\xf9\x2b\x7a\x23\x42\x00\xd0\xd5\xe0\x02\x20\xca\xe7\x70\x4b\x01\x20\x1b\x78\x00\x2b\xc5\xd1\x6f\x4b\x1d\x88\xfa\x23\x9b\x00\x9d\x42\x00\xd9\x6d\x4d\x14\x22\x00\x21\x6c\x48\x00\xf0\x7a\xf9\x4d\x23\x6b\x4c\x02\x22\x29\x00\x20\x00\x23\x81\x4c\x3b\xff\xf7\xf8\xfe\x02\x22\x60\x21\x67\x48\x00\xf0\x6c\xf9\x58\x23\x00\x22\x29\x00\x20\x00\x23\x81\x56\x3b\xff\xf7\xeb\xfe\x05\x22\x62\x49\x63\x48\x00\xf0\x56\xf9\x01\x20\x9c\xe7\x02\x9b\x01\x32\x0a\x70\x03\x70\x62\x7c\x00\x2a\x5e\xd0\x6f\x20\xe0\x47\x3f\x22\x0d\x23\x82\x43\x53\x43\xa2\x81\x9b\x11\x51\x4f\xa3\x73\x80\x22\x00\x21\x38\x68\x00\xf0\x47\xf9\x0c\x23\xe6\x5e\xc0\x23\x55\x4d\x5b\x00\x2b\x81\x00\x2e\x03\xdd\x20\x21\x28\x00\xff\xf7\x86\xfe\x03\x23\x00\x22\x31\x00\x28\x00\xff\xf7\xbc\xfe\x63\x7c\x00\x2b\x53\xd0\x3e\x68\x0f\x22\x30\x00\x4b\x49\x23\x30\x00\xf0\x22\xf9\x33\x00\x34\x36\x21\x33\x1a\x78\xd2\x43\x1a\x70\x01\x33\xb3\x42\xf9\xd1\xa3\x7b\x1c\x1c\x0d\x2b\x00\xd9\x0d\x24\xe4\xb2\x02\x9b\x9c\x42\x8b\xd0\x6b\x46\x02\x9a\x1b\x7a\x06\x2a\x00\xd9\x06\x23\x05\x21\x02\x98\x01\x33\xdb\xb2\x00\x93\x00\x27\x1f\x23\x41\x43\x08\x20\x00\x9a\x02\x9e\x9a\x1a\x3b\x00\xb0\x42\x7f\x41\x40\x31\x04\x33\x28\x00\xd2\xb2\xc9\xb2\x01\x97\xff\xf7\xcb\xfe\x02\x9b\x01\x33\xdb\xb2\x02\x93\xda\xe7\x67\x20\xe0\x47\x40\x08\xc0\xb2\x02\x00\xa0\x23\xa0\x3a\x18\x1a\x2c\x49\x02\x9b\x12\xb2\x0d\x78\x01\x33\xdb\xb2\xa8\x42\x03\xda\x01\x31\x0d\x2b\xf7\xd1\x01\x33\x91\xb2\x09\x0a\x22\x73\x61\x73\x8f\xe7\xa3\x7b\x05\xae\x03\x22\x30\x00\x23\x49\x03\x93\x00\xf0\xcd\xf8\x38\x68\x03\x9b\x08\x22\x23\x30\x09\x2b\x0f\xd9\x1f\x49\x00\xf0\xc4\xf8\x30\x23\x73\x70\x03\x9b\x27\x33\x33\x70\xac\x23\xff\x33\x31\x00\x28\x00\x2b\x81\xff\xf7\x37\xfe\x9d\xe7\x18\x49\x00\xf0\xb4\xf8\x03\x9b\x30\x33\x33\x70\x20\x23\x73\x70\xee\xe7\x00\x20\xf4\xe6\xea\x06\x00\x20\x00\x10\x06\x40\x61\xa9\x00\x00\xa5\x13\x00\x20\xa4\x13\x00\x20\x20\x14\x00\x20\xe3\x06\x00\x20\x06\x04\x00\x20\xe7\x03\x00\x00\xd1\x06\x00\x20\x98\x13\x00\x20\xd9\x06\x00\x20\xae\xd4\x00\x00\xeb\x06\x00\x20\x8c\x13\x00\x20\x62\xd4\x00\x00\x54\xed\x00\x00\x1e\xed\x00\x00\x9d\xd3\x00\x00\xb5\xd3\x00\x00\x16\x4b\x17\x49\x17\x4a\x19\x60\x5a\x60\x17\x4b\x17\x4a\x18\x48\x1a\x60\x18\x4a\x5a\x60\x18\x4a\x50\x60\x11\x60\x00\x22\x17\x49\x17\x48\x4a\x60\x0a\x60\x0a\x74\x4a\x82\x16\x49\x08\x30\x08\x60\x8a\x60\x0a\x82\x14\x49\x4b\x60\x14\x49\x4b\x60\x14\x4b\x15\x49\x5a\x60\x19\x60\xda\x60\x19\x1d\x1a\x74\xff\x32\x99\x60\x5b\x61\x1a\x76\x11\x4b\x11\x4a\x1a\x60\x70\x47\xc0\x46\xc4\x13\x00\x20\x2c\xed\x00\x00\x04\x07\x00\x20\x18\x14\x00\x20\x44\xed\x00\x00\x84\x06\x00\x20\x20\xd6\x00\x00\x10\x14\x00\x20\xe8\x13\x00\x20\x8c\xed\x00\x00\xfc\x13\x00\x20\x8c\x13\x00\x20\x98\x13\x00\x20\xcc\x13\x00\x20\x88\xed\x00\x00\x20\x14\x00\x20\x84\x08\x00\x20\x04\x4b\x05\x4a\x05\x48\x83\x42\x02\xd2\x02\xca\x02\xc3\xfa\xe7\x70\x47\xc0\x46\x8c\x13\x00\x20\xc8\xed\x00\x00\xa6\x13\x00\x20\x70\xb5\x00\x26\x0c\x4d\x0d\x4c\x64\x1b\xa4\x10\xa6\x42\x09\xd1\x00\x26\x00\xf0\x6d\xf8\x0a\x4d\x0a\x4c\x64\x1b\xa4\x10\xa6\x42\x05\xd1\x70\xbd\xb3\x00\xeb\x58\x98\x47\x01\x36\xee\xe7\xb3\x00\xeb\x58\x98\x47\x01\x36\xf2\xe7\xbc\xed\x00\x00\xbc\xed\x00\x00\xbc\xed\x00\x00\xc4\xed\x00\x00\x00\x23\x10\xb5\x9a\x42\x00\xd1\x10\xbd\xcc\x5c\xc4\x54\x01\x33\xf8\xe7\x03\x00\x82\x18\x93\x42\x00\xd1\x70\x47\x19\x70\x01\x33\xf9\xe7\x20\x20\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x77\xe5\x00\x00\x7b\xe5\x00\x00\x9b\xe5\x00\x00\xd7\xe5\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa1\xe5\x00\x00\xa5\xe5\x00\x00\xc7\xe5\x00\x00\xcb\xe5\x00\x00\x8d\x87\x81\x7b\x75\x6f\x69\x63\x5d\x53\x49\x3f\x35\x00\x00\x00\x01\x00\x00\x00\x0a\x00\x00\x00\x64\x00\x00\x00\xe8\x03\x00\x00\x10\x27\x00\x00\xa0\x86\x01\x00\x40\x42\x0f\x00\x80\x96\x98\x00\x00\xe1\xf5\x05\xfc\x13\x00\x20\x00\x00\x00\x00\x00\x00\x00\x00\xcf\xe5\x00\x00\x6d\xe9\x00\x00\xd3\xe5\x00\x00\xd5\xe5\x00\x00\xf8\xb5\xc0\x46\xf8\xbc\x08\xbc\x9e\x46\x70\x47\xf8\xb5\xc0\x46\xf8\xbc\x08\xbc\x9e\x46\x70\x47\x49\xe5\x00\x00\xf5\xeb\x00\x00\x21\xe5\x00\x00\xc4\x13\x00\x20\x00\x00\x00\x00\x00\x00\x00\x00\x10\x14\x00\x20\x00\x00\x00\x00\x00\x00\x00\x00\x01\xff'

fw += payload


open(sys.argv[1],'wb').write(fw)

