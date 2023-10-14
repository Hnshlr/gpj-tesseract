# Applications in Practical High End Computing 2022-2023

Discover, analyze and predict the temporal and spatial patterns of complex networks using Machine Learning and Deep Learning.

© Copyright 2023, All rights reserved to Machine Mavericks

https://github.com/MachineMavericks/group-project

**Authors:** Hans Haller - Guillaume Barrier - Julien Thomas - Virendra Keshari - Amit Tamhane

Students (CSTE: CIDA & SETC) at Cranfield Uni. SATM, Bedfordshire, United Kingdom.

![cover](https://user-images.githubusercontent.com/74055973/284641427-a0d58b6d-7a24-4771-9fb1-ff8df7d8b77a.png)

## Context

Railways transportation systems play a critical role in modern societies, enabling the trans- portation of goods and people across vast distances. The study of railway networks using Machine Learning algorithms has been increasingly important in recent years, with the aim of improving their efficiency and resilience. By leveraging the power of Machine Learning algo- rithms, railway managers can better understand the complex patterns and relationships within their networks, identify bottlenecks and areas of congestion, and develop strategies for optimis- ing routing and scheduling decisions.

In the past, Machine Learning algorithms have been used to identify key routes and nodes in railway networks, optimise train schedules, and predict maintenance needs. This has resulted in significant improvements in operational efficiency, reduced travel times, and improved safety. As demonstrated in this project, the use of Machine Learning algorithms such as clustering methods, shortest path algorithms, and resilience analysis can provide valuable insights into railway network performance and help to identify areas for improvement.

This following paper is the technical report for the 2022/2023 Application in Practical High- end Computing Group Project of the Master of Science in Computational and Software Tech- niques in Engineering of Cranfield University. It aims to provide a toolbox for temporal and spatial pattern analysis of complex networks. The following work is specifically dedicated to rail- way networks to provide quick and reliable information to whoever may be involved in temporal and spatial railway architecture decision making. Some results of the solution are presented and discussed alongside relevance and potential improvements.

## Implementation

### Solution architecture

![arch](https://user-images.githubusercontent.com/74055973/284641439-7165af3b-088f-4ab8-bd43-9e982f2daf25.png)

### Setting up the web-application

Once the repository of the project is cloned, or downloaded from Cranfield's Canvas, create a virtual environment for the project to store all packages the application requires. 

To create a virtual environment, first open your command prompt or terminal and navigate to the backend sub-directory:

```cd ./backend```

Once in the backend directory, create a new virtual environment using the venv module in Python. The command to create a virtual environment is:

```python3 -m venv venv```

This will create a new directory called "venv" in the backend directory, which will contain all the necessary files for their virtual environment. 

To activate the virtual environment, run the following command:

```source env/bin/activate```

This will activate the virtual environment. You should see the name of the environment in your terminal prompt. Once the virtual environment is activated, you can install the dependencies required for the project using pip. The list of the required packages is listed in the requirements.txt file in the root of the directory backend.

To install the dependencies, run the following command:

```pip install -r requirements.txt```

Once the virtual environment is now set up and ready to use, the user can start the application by running the app.py file through their IDE, or using the following command:

```python3 app.py```

### You're set to go!

If you have any questions, please contact me at ```hans.haller.885@cranfield.ac.uk```.


## Acknowledgements

This code was developed as part of the Applications in Practical High End Computing course at Cranfield University, UK. 

The Chinese Railways Dataset is private data, courtesy of an insider close to Dr. Jun Li. 

The Indian Railways Dataset was found on Kaggle and is the courtesy of @sanjaybhangar and @geohacker.

‎

© Copyright 2023, All rights reserved to Machine Mavericks