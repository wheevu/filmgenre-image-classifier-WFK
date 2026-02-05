# Multi-Label Film Genre Classifier | KENTECH WFK AI Program

**1st Place Winner | July 2025**

A computer vision project built for the KENTECH WFK AI Program (Korea-Vietnam tech exchange) to classify film genres from poster images. This repository documents the approach, data pipeline, and methodology.

## Team

Cross-cultural collaboration between Vietnamese and Korean students

![Course Project](docs/06-course-project.png)

&gt; **Note:** This is a documentation repository. Original training was conducted on shared team infrastructure during the competition. This repo preserves the technical approach and slide materials.

## The Problem

Standard movie genre classification often relies on metadata or trailers. We wanted to see if we could predict genres purely from visual poster elements (color schemes, composition, imagery) using computer vision.

**The Data Challenge:** Initial scraping yielded highly imbalanced classes:
- Action: 41 images
- Romance: 308 images  
- Sci-Fi: 11 images

Training on this would create a severely biased model that just predicts "Romance" for everything.

## The Solution

### 1. Data Engineering & Balancing

Instead of accepting bad data, I engineered a balanced dataset from scratch.

**Discovery phase:** Found initial dataset on Kaggle (~4,000 movie posters), but exploratory analysis revealed severe class imbalance.

![Initial dataset source](docs/01-initial-dataset.png)
*Initial dataset from Kaggle (Movie Genre from its Poster)*

**The Problem:** Highly imbalanced classes would create a biased model:
- Action: 41 images
- Romance: 308 images  
- Sci-Fi: 11 images

![Imbalanced dataset](docs/02-imbalanced-dataset.png)
*Class distribution showing severe imbalance*

**The Fix:** Sourced a larger dataset from Hugging Face (90,000+ image URLs) to curate balanced training data.

![New dataset source](docs/03-new-dataset.png)
*Hugging Face dataset with 90,000 image URLs*

**Automation:** Wrote Python scripts using pandas and requests to handle the scale—manual sorting was impossible.

![Handling dataset](docs/04-handling-new-dataset.png)
*Automation script for downloading 90k images*

![Categorizing dataset](docs/07-categorizing.png)
*Python script organizing images by genre folders*

- **Sourced 90,000+ image URLs** from Hugging Face datasets (`Pablinho/movies-dataset`)
- **Built automated extraction pipeline** using Python (pandas + requests) to download and categorize images by genre
- **Curated balanced dataset** of ~500 images per class (Action, Animation, Horror, Sci-Fi, Romance)

![Initial imbalanced dataset](docs/02-imbalanced-dataset.png)
*Initial data showed severe class imbalance that would bias the model*

![Handling new dataset](docs/04-handling-new-dataset.png)
*Python automation script to process 90k images—manual sorting was impossible*

### 2. Model Architecture

Given the 3-week competition timeline and limited compute resources, I focused on **rapid prototyping with Transfer Learning**:

- **Base Model:** MobileNet (via Teachable Machine interface for rapid iteration)
- **Training Data:** 500 balanced samples per genre
- **Approach:** Transfer learning to leverage pre-trained visual features rather than training from scratch

![Training setup](docs/05-training-the-model.png)
*Training setup with balanced classes (~500 samples each)*

### 3. Results

- **1st Place** in KENTECH WFK AI Program competition
- Demonstrated that **data quality &gt; model complexity**—winning with smart dataset engineering rather than a fancy architecture
- Successfully classified multiple genres (Action, Animation, Horror, Romance, Sci-Fi) from poster imagery alone

## Key Technical Skills Demonstrated

- **Data Pipeline Engineering:** Python, pandas, requests for large-scale image processing
- **Data Quality & EDA:** Identifying and fixing class imbalance issues
- **Computer Vision:** Transfer learning, MobileNet architecture, multi-label classification
- **Rapid Prototyping:** Delivering working solution under tight deadline (3 weeks) with cross-cultural team

## What I Learned

The biggest lesson was that **real-world data is messy**, and 80% of the work is cleaning and balancing it. The model architecture matters less than feeding it representative data. 

Also learned to build automation early—when you're dealing with 90,000 images, you can't manual-sort your way out of problems.

---

*Built during the KENTECH World Friends Korea AI Program at Can Tho University, July 2025.*