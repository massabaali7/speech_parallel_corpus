# speech_parallel_corpus
Creating Speech-to-Speech Corpus From Dubbed Series

Dubbed series are gaining a lot of popularity in recent years with strong support from major media service providers. Such popularity is fueled by studies that showed that dubbed versions of TV shows are more popular than their subtitled equivalents. We propose an unsupervised approach to construct speech-to-speech corpus, aligned on short segment levels, to produce a parallel speech corpus in the source- and target- languages. Our methodology exploits video frames, speech recognition, machine translation, and
noisy frames removal algorithms to match segments in both languages. 

- Paper: ##
- Demo: https://colab.research.google.com/drive/1dAcxBRiJ_fC5VrZ4LySUkiwLTXNcAjSu?usp=sharing
- Dataset: 
  - Series 1: https://mailaub-my.sharepoint.com/:u:/g/personal/mab87_mail_aub_edu/EdD4PEjBYb5Khc3hHDhns6kBN32ZvS1OnXztLohWlyT94w?e=LUvdUC
  - Series 2: https://mailaub-my.sharepoint.com/:u:/g/personal/mab87_mail_aub_edu/Ea-ZfEDy6hdJgoQ3MVCuZIoBmM2or1SSeVyuCVJSZ-BGoA?e=PCmZHM
  - Series 3: https://mailaub-my.sharepoint.com/:u:/g/personal/mab87_mail_aub_edu/EdDx-SZN2AxLn8EmOaQgNukBq1zoNi1yrg1HF_L4bd7FyA?e=kdyTrc

# Install required libraries
- pip install pydub
- pip install inaSpeechSegmenter
- pip install image-similarity-measures
- pip install SpeechRecognition
- pip install googletrans==4.0.0-rc1 
- pip install textblob-ar-mk

# Download wiki word vectors

- Choose wiki word vectors from the following website: https://fasttext.cc/docs/en/pretrained-vectors.html based on the target language in our case here Arabic
https://dl.fbaipublicfiles.com/fasttext/vectors-wiki/wiki.ar.zip
- Upload two videos for the same episode (in two different languages)
    - Run the video matching algorithm 
- Run the VAD (Voice Activity Detection) to create csv files for both episodes 
    - python run_speech_segment.py "ep1TR.wav" "ep1AR.wav"
- Run the automatic matching algorithm
  - Add the following attributes in order Path, Dubbed file, Org file, langSrc, langTrgt 
  - python run_segment_automatic_match.py "/content/gdrive/MyDrive/parallel_corpus/samples/" "ep1AR" "ep1TR" "tr" "ar"

To see the matched segments check the result.csv file 
