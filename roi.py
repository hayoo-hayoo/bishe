import numpy as np
import cv2
def mask(src):
    image = cv2.imread(src)  # 读图
    cv2.imshow("Oringinal", image) #显示原图
    print(image.shape[:2])

    # 输入图像是RGB图像，故构造一个三维数组，四个二维数组是mask四个点的坐标，
    site = np.array([[[350, 400], [200, 400], [200, 190], [350, 190]]], dtype=np.int32)

    im = np.zeros(image.shape[:2], dtype="uint8")  # 生成image大小的全黑图

    cv2.polylines(im, site, 1, 255)  # 在im上画site大小的线，1表示线段闭合，255表示线段颜色
    cv2.fillPoly(im, site, 255)  # 在im的site区域，填充颜色为255

    mask = im
    cv2.namedWindow('Mask', cv2.WINDOW_NORMAL)  # 可调整窗口大小，不加这句不可调整
    cv2.imshow("Mask", mask)
    masked = cv2.bitwise_and(image, image, mask=mask)  # 在模板mask上，将image和image做“与”操作
    cv2.namedWindow('Mask to Image', cv2.WINDOW_NORMAL)  # 同上
    cv2.imshow("Mask to Image", masked)
    cv2.waitKey(0)  # 图像一直显示，键盘按任意键即可关闭窗口
    return masked
if __name__ == '__main__':
    mask(r'C:\Users\44708\Documents\guoyijun\bishe\py2\HOG_SVM\dataset\20200511213018_IMG_0811.JPG')
