
import numpy as np
import cv2
import matplotlib.pyplot as plt
import math

class HoughTransform():

            
    def hough_lines_acc(self,img, rho_resolution=1, theta_resolution=1):
    
        height, width = img.shape 
        img_diagonal = np.ceil(np.hypot(height, width)) 
        rhos = np.arange(-img_diagonal, img_diagonal + 1, rho_resolution)
        thetas = np.deg2rad(np.arange(-90, 90, theta_resolution))

    
        H = np.zeros((len(rhos), len(thetas)), dtype=np.uint64)
        y_idxs, x_idxs = np.nonzero(img) 

        for i in range(len(x_idxs)): 
            x = x_idxs[i]
            y = y_idxs[i]

            for j in range(len(thetas)): 
                rho = int((x * np.cos(thetas[j]) +
                        y * np.sin(thetas[j])) + img_diagonal)
                H[rho, j] += 1

        return H, rhos, thetas




    def hough_peaks(self,H, num_peaks, threshold=0, nhood_size=3):
    
    
        indicies = []
        H1 = np.copy(H)
        for i in range(num_peaks):
            idx = np.argmax(H1)
            H1_idx = np.unravel_index(idx, H1.shape) 
            indicies.append(H1_idx)

       
            idx_y, idx_x = H1_idx 
   
            if (idx_x - (nhood_size//2)) < 0: min_x = 0
            else: min_x = idx_x - (nhood_size//2)
            if ((idx_x + (nhood_size//2) + 1) > H.shape[1]): max_x = H.shape[1]
            else: max_x = idx_x + (nhood_size//2) + 1

   
            if (idx_y - (nhood_size//2)) < 0: min_y = 0
            else: min_y = idx_y - (nhood_size//2)
            if ((idx_y + (nhood_size//2) + 1) > H.shape[0]): max_y = H.shape[0]
            else: max_y = idx_y + (nhood_size//2) + 1

   
            for x in range(min_x, max_x):
                for y in range(min_y, max_y):
         
                    H1[y, x] = 0

            
                    if (x == min_x or x == (max_x - 1)):
                        H[y, x] = 255
                    if (y == min_y or y == (max_y - 1)):
                        H[y, x] = 255

   
        return indicies, H


    def plot_hough_acc(self,H):

        fig = plt.figure(figsize=(10, 10))
           
        plt.imshow(H, cmap='jet')
        
        plt.xlabel('Theta Direction'), plt.ylabel('Rho Direction')
        plt.tight_layout()
        plt.show()
        cv2.imwrite("output/Theta_Rho_Image.png",H)




    def hough_lines_draw(self,img, lines, rho, theta):
        for i in range(len(lines)):
    
            rho = rhos[lines[i][0]]
            theta = thetas[lines[i][1]]
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a*rho
            y0 = b*rho
            pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
            pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
            cv2.line(img, pt1, pt2, (0,0,255), 3, cv2.LINE_AA)
        



    
if __name__ == "__main__":

    img = cv2.imread('input/way.jpg')
    cv2.imshow('Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    blur = cv2.GaussianBlur(gray, (3, 3), 1.5)

    canny_edges = cv2.Canny(blur, 100, 200)
    cv2.imshow('Edges', canny_edges)
    cv2.imwrite("output/Edges.png",canny_edges)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    transform=HoughTransform()
   
    H, rhos, thetas = transform.hough_lines_acc(canny_edges)
    lines,H= transform.hough_peaks(H, 3) # find peaks
    transform.plot_hough_acc(H) 
    transform.hough_lines_draw(img, lines, rhos, thetas)
    cv2.imshow('Detected Lines', img)
    cv2.imwrite("output/Detected Lines.png",img)

    


   #OPENCV PART 
    cv2houghlines = cv2.HoughLines(canny_edges, 1, np.pi / 180, 150, None, 0, 0)

    if cv2houghlines is not None:
        for i in range(0, len(cv2houghlines)):
            rho = cv2houghlines[i][0][0]
            theta = cv2houghlines[i][0][1]
            a = math.cos(theta)
            b = math.sin(theta)
            x0 = a * rho
            y0 = b * rho
            pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
            pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
            cv2.line(img, pt1, pt2, (0,0,255), 3, cv2.LINE_AA)

    cv2.imshow('OpenCV Detected Lines', img)
    cv2.imwrite("output/OpenCV Detected Lines.png",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()