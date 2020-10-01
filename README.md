# streamchat.ai - Training a transformer model (GPT-2) on livestream chat messages

![Prospective webpage design](webpage_design.png "Prospective webpage design")

**Project Status**: Failed to generate meaningful output.

The goal of the project was to fine-tune a ML model in an attempt to generate messages in the style of those found on [Twitch](https://www.twitch.tv/) livestreams.

The ideal output would be novel phrases complete with emotes. At a stretch these output messages would even have some sense of emergent sentiment.

## Process

_The accompanying Jupiter Notebook shows a step-by-step of project methodology._

-   Firstly the data was downloaded and processed into training, test and validation datasets, along with a compilation set, described in the _Data Processing_ section below.

-   A tokenizer was then trained on the compilation dataset, generating tokens based on the data's vocabulary including the unique emotes. This tokenizer used was a byte-level BPE (Byte-pair encoding).

-   LineByLine dataset objects were then created for both training and testing data. A padding token `<PAD>` was used to fill any of the remaining block-size for each line.

-   The GPT-2 model was then initialized and configured with the datasets and various training parameters.

-   This model was then trained on a [colab](https://colab.research.google.com/) instance (Thanks Google 🙂)

-   The `run_generation.py` script was then run with various prompts. (From the example by [🤗 Huggingface's Transformers](https://github.com/huggingface/transformers))

## Results

I first tried a prompt of `<BOS>` to try and get some form of novel output, however this just resulted in pairs of `<BOS><EOS>`.

I then tried various other single word phrases which almost always resulted in an emote token being appended like _Pog_ or _Sadge_. (Somewhat interesting)

With slightly longer prompts like `It's a` or `What is`, longer form phrases were generated but made little sense. One fun thing was when prompted with `It was me`, the model passed back `It was me :)` (smiley), the completion of a Twitch meme.

It seems as though the dataset was unable to offer a comprehensive picture of what word sequences are expected as most data points were extremely short, if not single words.

## Potential reasons for failure

This was my first applied ML project, so inexperience certainly played its part. The model was most likely overfit on the highly varied, non-repetitive data points, unable to form a cohesive model of the input text style. From my understanding, this type of transformer model is most effective at predicting sequences of words. This was at odds with the dataset, which as described contains many single word datapoints.

It was a long-shot from the start to expect this model to provide meaningful output, however plenty was learned from the failure. I'd have to do further research to better understand methods of generating this type of short-form text.

## Data processing

Most work is handled within the notebook, however some preprocessing work was done to get the data in a suitable format.

[Twitch Chat Downloader](https://pypi.org/project/tcd/) was used to gather a collection of 10 streams worth of chat data (approx 30Mb)

`compile_chatlogs.py`:
Iterates through raw .txt files and cleans up raw Twitch chat data.

-   Removes chatter's username + timestamp
-   Adds `<BOS>` and `<EOS>` symbols to each message

`create_datasets.py`:
Uses sklearn's builtins to split apart compiled data into train/test/validate datasets.
