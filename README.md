# Hough-Transform-Applications
Hough Transform Applications

## Design and implement Hough Transform method for finding lines.
In both parts, we wrote a class applying hough transform manually and using opencv library. In first part, we need a four function which are named hough_lines_acc, hough_peaks, plot_hough_acc, hough_lines_draw. For hough_lines_acc, will build the Hough Accumulator for the given image. Hough peaks function will force the algorithm to look elsewhere after it's already selected a point from a 'pocket' of local maxima. Plot_hough_acc is a simple funciton used to plot a Hough Accumulator. Hough_lines_draw is drawing the lines from the Hough Accumulatorlines using OpevCV cv2.line.
To apply the function in an image, we need a image. This is the image;

![image](https://github.com/onlinEngineer/Hough-Transform-Applications/assets/70773825/d23348a0-d85d-48d8-90f9-e4d7c6eb19c2)

Before applying functions, first we convert to image into gray scale, and after we find out the edges on the image by using Canny Edges algoritm. This is the edges.

![image](https://github.com/onlinEngineer/Hough-Transform-Applications/assets/70773825/ee6869b8-468a-421b-b9b9-48be908ff2d6)

The image hough transform is ready to be applied. We run hough_lines_accumulator on the shapes canny_edges image, find out peaks and plot the hough space, brighter spots have higher votes.

![image](https://github.com/onlinEngineer/Hough-Transform-Applications/assets/70773825/da420d92-60fa-4780-b58d-8d0d8dbba690)

Finally, showing image with manual Hough Transform Lines.

![image](https://github.com/onlinEngineer/Hough-Transform-Applications/assets/70773825/5518884d-3732-406c-a24f-21a0df33b479)

Comparing the result, we are doing the same process by using opencv houghline function. This is the result of opencv result.

![image](https://github.com/onlinEngineer/Hough-Transform-Applications/assets/70773825/89a5c6bb-761d-4952-afcd-eca46f8c915c)

As seen on the pictures, the results are almost the same.

## Demonstrate lane detectionon the following video

![image](https://github.com/onlinEngineer/Hough-Transform-Applications/assets/70773825/c50c3c0e-fc43-4a2b-ad6b-5188a2b3d6b7)

By using opencv hough transform library, we can easily detect the lines. Before running the hough transform fuction, we apply some operations on an image such as convert the gray scale and detect the edges by using canny edge detector. This is an example image detected lines.

![image](https://github.com/onlinEngineer/Hough-Transform-Applications/assets/70773825/c11c11f0-7a70-433e-9ba4-23a4b7d42fb2)
