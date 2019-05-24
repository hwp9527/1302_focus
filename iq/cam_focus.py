import numpy as np
import cv2


def definition_score(img):
    # try:
    #     bridge = CvBridge()
    #     cv_image = bridge.imgmsg_to_cv2(data, "mono8")
    #     np_image = np.array(img)
    # except CvBridgeError as e:
    #     print(e)

    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY);
    np_image = np.array(img_gray)
    ##calculate the fft magnitude
    img_float32 = np.float32(np_image)
    # dft = cv2.dft(img_float32)
    dft = cv2.dft(img_float32, flags=cv2.DFT_COMPLEX_OUTPUT)

    dft_shift = np.fft.fftshift(dft)
    magnitude_spectrum = cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1])

    # normalize
    magnitude_spectrum_normalized = magnitude_spectrum / np.sum(magnitude_spectrum)

    # frequency domain entropy (-> Entropy Based Measure of Camera Focus. Matej Kristan, Franjo Pernu. University of Ljubljana. Slovenia)
    fde = np.sum(magnitude_spectrum_normalized * np.log(magnitude_spectrum_normalized))

    return -fde



# if __name__=="__main__":
#     img1 = cv2.imread("./efg.jpg")
#     img2 = cv2.imread("./gjk.jpg")
#     print(definition_score(img1))
#     print(definition_score(img2))

