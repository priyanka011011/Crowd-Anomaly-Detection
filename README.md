## Use Case: ZAF043 Crowd Anomaly Detection


## Overview
This project is part of our efforts in solving problems in densely crowded environments analysis. Following our previous topics in classifying crowd states, segmenting videos into components, estimating crowd size and tracking objects in crowds, the goal here is to detect the deviations from normal crowd behaviors, which is motivated by the ubiquity of camera surveillance systems, the challenges in modeling crowd behaviors, and the importance of automatic crowd monitoring for various applications.

Anomaly detection is an active area of research on its own. Various approaches have been proposed, for both crowded and non-crowded scenes. Existing approaches focus uniquely on motion information, ignoring abnormality information due to variations of object appearance. This makes them impervious to abnormalities that do not involve motion outliers, e.g., a truck that crosses a bridge with weight restrictions. Furthermore, descriptors such as optical flow, pixel change histograms, or other traditional background subtraction operations, are difficult for crowded scenes, where the background is by definition dynamic, of widespread clutter, and complicated occlusions.

anomaly detection and localization can be broken down into two sub-problems: 1) how to characterize crowd behaviors, and 2) how to measure the "anomaly score" of a specific behavior. For the first issue, we propose to model motion patterns in crowds via the use of mixture of dynamic textures (MDT), which is a unified description capturing both the appearance and dynamics of visual processes. In the second part, instead of directly modeling the anomalous behavior itself, the normalcy is first learnt, and then the "anomaly score" of an observation is computed by measuring the difference from the normalcy model. Specifically, two components are proposed to reflect the normalcy in different perspectives.  

<p float="center">
 <img src="https://github.com/priyanka011011/Crowd-Anomaly-Detection/assets/63203112/1ba3d710-e01f-47b2-b23f-442a815a80bc" width="45%" />
 <img src="https://github.com/priyanka011011/Crowd-Anomaly-Detection/assets/63203112/1b8fafa8-0689-47b5-9e9f-d17d37fc899b" width="45%" />
</p>

## Methodology
The methodology for anomaly detection in crowded environments, involves two main components: characterizing crowd behaviors and measuring the "anomaly score" of specific behaviors. Here is an overview of the proposed methodology:

- Mixture of Dynamic Textures (MDT): The project suggests using MDT to model motion patterns in crowds. MDT is a unified description that captures both the appearance and dynamics of visual processes in crowded scenes.

- MDT captures the complexity and dynamics of crowded scenes by considering the spatial and temporal variations in the video data. It helps in modeling the visual processes and behaviors exhibited by the crowd.
Measuring Anomaly Score:

- Learning Normalcy: The methodology involves learning the normal behavior of the crowd first. This is done by modeling the expected patterns, motion, and appearance characteristics of a typical crowd behavior.

- Anomaly Score Computation: Once the normalcy model is established, the anomaly score of an observation or behavior is computed by measuring the difference or deviation from the normalcy model.

- Two Components of Normalcy: The methodology proposes two components to reflect the normalcy from different perspectives, although the specific details of these components are not mentioned in the given information.

The combination of characterizing crowd behaviors using MDT and measuring the anomaly score based on the deviation from the normalcy model enables the detection of deviations from normal crowd behaviors in densely crowded environments.

## Business Segments
Anomaly detection in crowded environments, the potential business segments that could benefit from this technology include:

- Security and Surveillance: Anomaly detection in crowded scenes can significantly enhance security and surveillance systems. It can help identify suspicious or abnormal behavior in real-time, enabling early detection of potential threats or criminal activities.

- Transportation and Infrastructure: Monitoring crowded transportation hubs, such as airports, train stations, or bus terminals, can be crucial for ensuring smooth operations and passenger safety. Anomaly detection can help identify unusual or abnormal crowd behaviors that may indicate congestion, security breaches, or other issues requiring intervention.

- Event Management: Anomaly detection can be valuable in managing large-scale events, such as concerts, festivals, or sports games. It can help organizers identify and respond to crowd-related incidents, such as overcrowding, unauthorized access, or potentially dangerous situations, improving crowd safety and overall event experience.

- Retail and Commercial Spaces: Detecting anomalies in crowded retail environments can assist in loss prevention, identifying suspicious activities, or unusual behaviors that may indicate theft, shoplifting, or other security concerns. It can also provide insights into customer behavior patterns and optimize store layouts.

- Crowd Control and Safety: Anomaly detection technology can be applied to ensure crowd control and safety in public spaces, including city centers, parks, or tourist attractions. It can help monitor crowd density, detect overcrowding situations, and identify potential safety risks or emergencies in real-time.

- Public Safety and Law Enforcement: Anomaly detection can support law enforcement agencies in public safety efforts, such as crowd management during protests, demonstrations, or public gatherings. It can assist in identifying unusual crowd behaviors, potential threats, or criminal activities, aiding in proactive and timely responses.

- Smart City Applications: Anomaly detection in crowded environments aligns with the concept of smart cities, where data-driven technologies are leveraged to enhance urban management. It can contribute to intelligent urban planning, traffic optimization, and overall safety and security in densely populated areas.

- These business segments highlight potential applications of anomaly detection technology in various industries where monitoring crowded scenes and identifying deviations from normal behaviors is critical for operational efficiency, safety, and security.


## Objective
The objective of the project is to detect deviations from normal crowd behaviors in densely crowded environments. The motivation behind this objective is the prevalence of camera surveillance systems, the challenges in modeling crowd behaviors, and the importance of automatic crowd monitoring for various applications.

# Model
The proposed approach for anomaly detection in crowded scenes involves two main components: characterizing crowd behaviors and measuring the "anomaly score" of a specific behavior.

- Characterizing Crowd Behaviors: The project suggests using a mixture of dynamic textures (MDT) to model motion patterns in crowds. MDT provides a unified description that captures both the appearance and dynamics of visual processes in crowded scenes.

- Measuring Anomaly Score: Instead of directly modeling anomalous behavior, the project proposes learning the normalcy first. The normal behavior is modeled, and then the    "anomaly score" of an observation is computed by measuring the difference from the normalcy model. Two components are introduced to reflect the normalcy from different perspectives.

# Predictions Format:
The specific format for predictions or outputs generated by the anomaly detection system is not mentioned in the given information. However, it can be inferred that the output would include anomaly scores for observations or behaviors in crowded scenes. The anomaly score indicates the degree of deviation from normal crowd behaviors, helping to identify abnormal events or occurrences in real-time monitoring scenarios.

# Dataset

UCSD Anomaly Detection Dataset

The UCSD Anomaly Detection Dataset was acquired with a stationary camera mounted at an elevation, overlooking pedestrian walkways. The crowd density in the walkways was variable, ranging from sparse to very crowded. In the normal setting, the video contains only pedestrians. Abnormal events are due to either:
               - the circulation of non pedestrian entities in the walkways
               - anomalous pedestrian motion patterns
Commonly occurring anomalies include bikers, skaters, small carts, and people walking across a walkway or in the grass that surrounds it. A few instances of people in wheelchair were also recorded. All abnormalities are naturally occurring, i.e. they were not staged for the purposes of assembling the dataset. The data was split into 2 subsets, each corresponding to a different scene. The video footage recorded from each scene was split into various clips of around 200 frames.

- Peds1: clips of groups of people walking towards and away from the camera, and some amount of perspective distortion. Contains 34 training video samples and 36 testing video samples.

- Peds2: scenes with pedestrian movement parallel to the camera plane. Contains 16 training video samples and 12 testing video samples.

For each clip, the ground truth annotation includes a binary flag per frame, indicating whether an anomaly is present at that frame. In addition, a subset of 10 clips for Peds1 and 12 clips for Peds2 are provided with manually generated pixel-level binary masks, which identify the regions containing anomalies. This is intended to enable the evaluation of performance with respect to ability of algorithms to localize anomalies.

Dataset Download
- UCSD Anomaly Detection Dataset

Examples of Anomalies

| Peds1 : Cart                        | Peds1 : Wheelchair                  |
| ----------------------------------- | ----------------------------------- |
| ![vidf4_33_007_frame080_mark](https://github.com/priyanka011011/Crowd-Anomaly-Detection/assets/63203112/92aff7f9-a790-472d-b7f9-4211e4cf9147) |  ![vidf3_33_002_frame110_mark](https://github.com/priyanka011011/Crowd-Anomaly-Detection/assets/63203112/fe32f054-303d-44cb-bf29-2e7d6791beb9) |


| Peds1 : Skater                      | Peds1 : Biker                       |
| ----------------------------------- | ----------------------------------- |
| ![vidf1_33_008_frame130_mark](https://github.com/priyanka011011/Crowd-Anomaly-Detection/assets/63203112/5c060288-5138-43a0-9d24-787c8531a061)| ![vidf1_33_002_frame138_mark](https://github.com/priyanka011011/Crowd-Anomaly-Detection/assets/63203112/785b87bc-5a75-42ff-baad-4e949e10269f)|

## Papers
- Anomaly Detection in Crowded Scenes
   Vijay Mahadevan, Weixin Li, Viral Bhalodia and Nuno Vasconcelos.
   In Proc. IEEE Conference on Computer Vision and Pattern Recognition (CVPR),
   San Francisco, CA, 2010. 
  - [pdf](http://www.svcl.ucsd.edu/publications/conference/2010/cvpr2010/cvpr_anomaly_2010.pdf)
  - [BidTeX](http://www.svcl.ucsd.edu/publications/conference/2010/cvpr2010/cvpr_anomaly.bib)
- Anomaly Detection and Localization in Crowded Scenes
  Weixin Li, Vijay Mahadevan and Nuno Vasconcelos
  IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI)
  Vol. 36, No. 1, pp18-32, January, 2014. 
  - [pdf](http://www.svcl.ucsd.edu/publications/journal/2013/pami.anomaly/pami_anomaly.pdf)  
  - [BitTeX](https://scholar.googleusercontent.com/scholar.bib?q=info:NyHX-w2VTwwJ:scholar.google.com/&output=citation&scisdr=Cm13Jnw7EMW_o_H15ao:AGlGAw8AAAAAZG7z_aoDnxf4jjNFfori1TUDp3Q&scisig=AGlGAw8AAAAAZG7z_RYIxRaV062HgyYdtuuMGoQ&scisf=4&ct=citation&cd=-1&hl=en)

## Team
- Sanjeeb Tiwary 
   - [sanjeebtiwary](https://github.com/sanjeebtiwary)
- Vaibhavi 
   - [Vaibhavi15-04](https://github.com/Vaibhavi15-04)
- Paramesh 
   - [Paramaatma](https://github.com/Paramaatma)
