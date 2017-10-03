# PyImCra - Reddit scraper 
This script scrapes images from the subreddit of a person.  
Afterwards it clusters all the faces found in the images based on the euclidean distance. 
The images in the biggest cluster are saved in the chosen directory as being the person in the subreddit.

## Getting started
You can follow the instructions below to deploy this software to your local machine. 

### Prerequisites
You will need the following hardware/software for the project to work:
* CUDA and a decent Nvidia GPU
* [Tensorflow 1.0](https://www.tensorflow.org/)
* [Facenet](https://github.com/davidsandberg/facenet)
* [OpenCV 3.0](http://opencv.org/opencv-3-0.html)
* Pretrained Facenet model (Protobuf file)

### Install
1. Clone this repository on your local machine
2. Open a terminal and cd into the repository
3. Run the following script:
`python src/image_scraper.py /path/to/model.pb /path/to/names/file.txt /path/to/output/dir/`
  * model (String): Path to the model (.pb file)
  * names (String): Path to a textfile containing the names of the subreddits (.txt file)
  * out_dir (String): The output directory where the images will be saved 
  * --image_size (int - Optional): The size the images will be saved as (Default: 160px)
  * --gpu_memory_fraction (float - Optional): Upper bound on the amount of GPU memory that will be used by the process (Default: 1.0)
  
## License
This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/PXL-IT/PyImCra/blob/image/LICENSE.md) file for details.
## Authors
* [Thijs Lanssens](https://github.com/Lanssens) 
* [Maarten Bloemen](https://github.com/MaartenBloemen) 