from hw05 import *
import filecmp


## Tester file for HW5

rc4Cipher = RC4('keystring')
image = "winterTown.ppm"
noHead = "winterTownnoHead.ppm"
originalImage = open(noHead, 'r')
originalImage.seek(0)
encryptedImage = rc4Cipher.encrypt(originalImage)
encryptedImage.seek(0)
decryptedImage = rc4Cipher.decrypt(encryptedImage)
originalImage.close()
encryptedImage.close()
decryptedImage.close()

if filecmp.cmp(noHead, "decryptedImage.ppm"):
    print('RC4 is awesome')
else:
    print('Hmm, something seems fishy!')

