# Data Sources
1. [PS_Nepali_SA](https://github.com/pudasainishushant/NepaliSentimentAnalysis/tree/main/sentiment_data) Contains 6K sentiment annotated Nepali texts. (2 class data)

2. [Movie_Reviews](https://www.kaggle.com/datasets/shikharghimire/nepali-language-sentiment-analysis-movie-reviews) Contains sentiment annotated movie reviews in Nepali text. (2 class data)

3. [RR_Nepali_SA](https://github.com/rockerritesh/NepaliSentiment/tree/master) (3 class data)

4. [S1_Nepali_SA](https://github.com/sagarl123/NepaliNLP-SentimentAnalysis/blob/main/collected_labeled_data.csv) (3 class data)

5. [NepCov19Tweets](https://www.kaggle.com/datasets/mathew11111/nepcov19tweets/code?datasetId=1660323) Contains 33K sentiment annotated Nepali Tweets regarding Covid19 (3 class data)

6. [NepCov19TweetsPlus](https://huggingface.co/datasets/raygx/NepCov19TweetsPlus) extension of NepCov19Tweets with augmented data on Neutral class for balanced dataset. (3 class data)

7. [NepQuake15](https://github.com/RayGone/Nepali-Sentiment-Analysis-Data/blob/main/NepQuake15/annotated.csv) Collection of sentiment annotated tweets made during the major earthquake of 2015 in Nepal. (3 class data)

# Data-Repo

Here the intention of this data-repo is to build a single Sentiment Analysis Dataset in Nepali. What's being done here is merging the different datasets into one for easy availabitly and use.

## Findings in Data Exploration

It was found that the source texts for the datasets [1], [3] and [4] are the same. [3] and [4] are almost identical. However, [1] contains 2 class sentiment labels. Thus, the sentiment differs from that of [3] and [4].

### 2 Class Sentiment Data
> If you are interested in 2 class sentiment analysis, then you should use Movie Reviews [3], NepCov19Tweets, NepQuake15 [7], and PS_Nepali_SA data [1].

### 3 Class Sentiment Data
> If you are interested in 3 class sentiment analysis, then you should use Movie Reviews [3], NepCov19Tweets(Plus) [5] or [6], NepQuake15 [7], and S1_Nepali_SA [4] data.

*We can observe in the dataset that S1_Nepali_SA, RR_Nepali_SA, and PS_Nepali_SA contains same source texts with different labels assigned. S1_Nepali_SA and RR_Nepali_SA are pretty much identical with very few differences. But, PS_Nepali_SA is 2 class sentiment dataset and many of the neutral class data has be re-labeled to either positive or negative.*

*Note: NepCov19TweetsPlus can be downloaded from huggingface_hub and same processing steps as used for NepCov19Tweets can be used.*


# Other Data Sources

- [Aspect-Baseed_SA](https://github.com/oya163/nepali-sentiment-analysis/blob/master/data/nepcls/csv/ss_ac_at_txt_bal.csv)
- [EC_Nepali_SA](https://github.com/ecabott/nepali-sentiment-analysis/tree/main/datasets) -> This is same as NepCov19Tweets dataset with few rows extra.
- [SU_Nepali_SA](https://github.com/suwubham/sarn) -> contains three datasets where dataset1.csv is from [1,3,4], dataset2.csv seems different but haven't checked yet, and dataset3.csv is something that I've found in other repos and ignored.
- [OM_Nepali_SA](https://github.com/om0121/sentiment-analysis-of-nepali-text)
- [News-Headline_SA](https://github.com/bjayadikary/sentiment_analysis_of_nepali_news_headlines/blob/main/data_files/training_data/first_training_data_updated_balanced.tsv)
- [MS_Nepali_SA](https://github.com/merishnaSuwal/nep-off-langdetect/tree/main/NepSA/dataset/balanced)