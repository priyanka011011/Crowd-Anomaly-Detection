## Use Case: ZAF043 Crowd Anomaly Detection


## Overview
This project is part of our efforts in solving problems in densely crowded environments analysis. Following our previous topics in classifying crowd states, segmenting videos into components, estimating crowd size and tracking objects in crowds, the goal here is to detect the deviations from normal crowd behaviors, which is motivated by the ubiquity of camera surveillance systems, the challenges in modeling crowd behaviors, and the importance of automatic crowd monitoring for various applications.

Anomaly detection is an active area of research on its own. Various approaches have been proposed, for both crowded and non-crowded scenes. Existing approaches focus uniquely on motion information, ignoring abnormality information due to variations of object appearance. This makes them impervious to abnormalities that do not involve motion outliers, e.g., a truck that crosses a bridge with weight restrictions. Furthermore, descriptors such as optical flow, pixel change histograms, or other traditional background subtraction operations, are difficult for crowded scenes, where the background is by definition dynamic, of widespread clutter, and complicated occlusions.

anomaly detection and localization can be broken down into two sub-problems: 1) how to characterize crowd behaviors, and 2) how to measure the "anomaly score" of a specific behavior. For the first issue, we propose to model motion patterns in crowds via the use of mixture of dynamic textures (MDT), which is a unified description capturing both the appearance and dynamics of visual processes. In the second part, instead of directly modeling the anomalous behavior itself, the normalcy is first learnt, and then the "anomaly score" of an observation is computed by measuring the difference from the normalcy model. Specifically, two components are proposed to reflect the normalcy in different perspectives.  


![peds0_biker](https://github.com/priyanka011011/Crowd-Anomaly-Detection/assets/63203112/1ba3d710-e01f-47b2-b23f-442a815a80bc)

![MDT_vidf4_33_007_88](https://github.com/priyanka011011/Crowd-Anomaly-Detection/assets/63203112/1b8fafa8-0689-47b5-9e9f-d17d37fc899b)

Methodology
(describe the steps) There are 10000 different news stories and additional news stories.

Run the classifier on 1 mln random stories out of 1000 news sources. Get 10k stories where the classifier output is the closest to the decision boundary and get these examples labeled.
Get 10k random labeled stories from the 10k random labeled stories from 1000 news we care about.
Pick a random sample of 1 mln stories from 1000 news sources and have them labeled. Pick the subset of 10k stories where the model’s output is both wrong and farthest away from the decision boundary.
Using different methods of classifying a bag of news articles from 1000 news sources, measure the accuracy of the model with an original train dataset.

Business Segments
(advise for which business segments you can apply the model) Business Segments are the following, please following the names of business segments given:

Airlines
Autonomous Driving
Banking & Finance
Business & Private Sector
Government & Public Services
Healthcare
Human Resources
Lifestyle & Social Media
Media & Publishing
Retail & E-commerce
AI Application
(describe how your model can be useful in real life or business)

Objective
Models
Predictions format
Data
Put a link to the dataset.

Papers
- Anomaly Detection in Crowded Scenes
  Vijay Mahadevan, Weixin Li, Viral Bhalodia and Nuno Vasconcelos.
  In Proc. IEEE Conference on Computer Vision and Pattern Recognition (CVPR),
  San Francisco, CA, 2010. [pdf](http://www.svcl.ucsd.edu/publications/conference/2010/cvpr2010/cvpr_anomaly_2010.pdf)
  
- Anomaly Detection and Localization in Crowded Scenes
  Weixin Li, Vijay Mahadevan and Nuno Vasconcelos
  IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI)
  Vol. 36, No. 1, pp18-32, January, 2014. [pdf](http://www.svcl.ucsd.edu/publications/journal/2013/pami.anomaly/pami_anomaly.pdf)  


Demo link
Record a 1 min demo and kindly provide a link for this.

## Team
* Sanjeeb Tiwary (sanjeebtiwary)
* Vaibhavi (Vaibhavi15-04)
* Paramesh (Paramaatma)
