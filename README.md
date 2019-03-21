# Maze-Solving-using-A-star-algorithm
In this repository, I have made a maze solving system. The system takes in input of an maze using a camera. This Image is converted into a grid, then you can give the starting and the ending point and the system solves the maze using A* 
algorithm

# Requirements
1) Python3
2) Opencv
3) heapq
4) matplotlib

# Steps
## 1) Input image using the camera
![IMAG2747](https://user-images.githubusercontent.com/24778913/54785699-e84b8680-4c4c-11e9-99d3-8a50f430c43f.jpg)
<br>
<br>
## 2) Detect the maze using image thresholding
![Screenshot from 2019-03-22 02-23-11](https://user-images.githubusercontent.com/24778913/54785762-07e2af00-4c4d-11e9-8472-08152d4930b1.png)
## 3) Convert the image into a smaller grid (because the image size is very big)
![Screenshot from 2019-03-22 02-28-13](https://user-images.githubusercontent.com/24778913/54787244-22b72280-4c51-11e9-83b4-04e8021a5ee3.png)
## 4) Take the start and the end point from the user
![Screenshot from 2019-03-22 02-28-53](https://user-images.githubusercontent.com/24778913/54785826-33659980-4c4d-11e9-9c9f-c7e87fa48fb7.png)
## 5) Solve the grid using A-star algorithm
I have provided some sources from where I studied the algorithm in the references section.<br>
![Screenshot from 2019-03-22 02-29-04](https://user-images.githubusercontent.com/24778913/54785841-3f515b80-4c4d-11e9-87f1-57d7b7badad7.png)

# Things to improve
1) The process of converting a high resolution image into a grid is not accurate and is also not very efficient.<br>
2) Plotting the result on the live camera feed.<br>


# References 
1)<a href="https://www.youtube.com/watch?v=ySN5Wnu88nE&t=199s">Computerphile</a><br>
2)<a href="https://www.youtube.com/watch?v=aKYlikFAV4k">CodingTrain</a><br>
3)<a href="https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2">Medium</a><br>
4)<a href="https://www.raywenderlich.com/3016-introduction-to-a-pathfinding">raywenderlich</a><br>
5)<a href="https://www.analytics-link.com/single-post/2018/09/14/Applying-the-A-Path-Finding-Algorithm-in-Python-Part-1-2D-square-grid">Analytics link</a>
