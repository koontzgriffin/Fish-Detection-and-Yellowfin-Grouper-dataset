# Fish Detection on the Yellowfin Expt Optical Footage
## The goal of this project is to detect fish in the given optical footage from the Yellowfin Expt. If detection is successful, the detected fish could then be matched with their image in the Sonar Footage of the same scene. 
***

### This Project utilizes the reserch paper ["YOLO-Fish: A robust fish detection model to detect fish in realistic underwater environment"](https://www.sciencedirect.com/science/article/abs/pii/S1574954122002977)

### The file `fish_detection.ipynb` is a python note book that goes through the process of utilizing the models developed in the paper to perform fish detection on a data set derived from the video `input.mp4`. A section of 500 frames of the video was extracted, annotated, and used to create a YOLO data set (`data_sets/raw_data_set`).

### Other data sets were created from the raw data set using `scripts/split_dataset.py`
### Usage : `$ python split_dataset.py [path to original .txt] [train_fraction] [shuffle (Y / N)]`


### Other Weight Files can be downloaded from the [YOLO-Fish github repo](https://github.com/tamim662/YOLO-Fish)

***

# Sources and useful links for further research:
### - [YOLO-Fish github repo](https://github.com/tamim662/YOLO-Fish)
### - [DeepFish Dataset](https://github.com/alzayats/DeepFish)
### - [OzFish Dataset](https://apps.aims.gov.au/metadata/view/38c829d4-6b6d-44a1-9476-f9b0955ce0b8)
### -[OpenCV YOLO Docs](https://docs.opencv.org/3.4/d6/d0f/group__dnn.html#ga9d118d70a1659af729d01b10233213ee)
### - [Object Detection Metrics github](https://github.com/rafaelpadilla/Object-Detection-Metrics/blob/master/samples/sample_2/README.md)
### - [Sonar Object Detection Dataset](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6176783/)
### - [Fish Classification Datasets](https://globalwetlandsproject.org/computer-vision-resources-fish-classification-datasets/)
### - [Unsupervised Fish Trajectory Tracking and Segmentation](https://paperswithcode.com/paper/unsupervised-fish-trajectory-tracking-and)
### - [Underwater Fish Species Recognition Using Deep Learning Techniques](https://ieeexplore.ieee.org/abstract/document/8711657)
### - [Accelerating Species Recognition and Labelling of Fish From Underwater Video With Machine-Assisted Deep Learning](https://www.frontiersin.org/articles/10.3389/fmars.2022.944582/full#note10)
### - [Automated Detection, Classification and Counting of Fish in Fish Passages With Deep Learning](https://www.frontiersin.org/articles/10.3389/fmars.2021.823173/full)
### - [Motion Prediction in Visual Object Tracking](https://ras.papercept.net/images/temp/IROS/files/2029.pdf)
### - [An underwater observation dataset for fish classification and fishery assessment](https://www.nature.com/articles/sdata2018190)
