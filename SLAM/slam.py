import cv2
import pygame

cv2.namedWindow("image", cv2.WINDOW_NORMAL)
def process_fram(img):
    img = cv2.resize(img, (1920//2, 1080//2))
    print(img.shape)

def load_data():

    cap = cv2.VideoCapture("video/test.mp4")
    while(cap.isOpened()):

        ret, fram = cap.read()

        if ret == True:
            process_fram(fram)
            cv2.imshow("Fram", fram)

            if cv2.waitKey(25) & 0xff == ord('q'):
                break
        else:
            break
    cap.release()


def pygame_fun():
    w, h = (1920//2, 1080//2)
    pygame.init()
    screen = pygame.display.set_mode((w,h))
    pygame.display.flip()
    while True:
        pass

def main():
    #load_data()
    pygame_fun()
    print("Hello")








if __name__ == '__main__':
    main()
