# GPT Store Mining and Analysis

This repository contains materials from the paper *GPT Store Mining and Analysis*.

## Abstract

As an important extension of the ChatGPT ecosystem, GPT Store has developed into an active market hosting more than 3 million customized ChatGPTs (GPTs). Despite its large scale, the current academic community still has obvious limitations in its understanding of the ecosystem of this platform. Based on a complete dataset of more than 700,000 GPTs, this paper has achieved a multi-dimensional analysis of GPT Store. We first systematically examined the platform operation mechanism, covering core elements such as the classification system, interaction mode, and evaluation system. We also comprehensively analyzed the security risks, such as data leakage and jailbreak in GPT Store. Finally, through a user study, this work revealed the behavioral characteristics and experience pain points in real usage scenarios. Based on these findings, we provide operational platform optimization suggestions, including functional improvement, security enhancement, and interaction improvement. This study not only constructs an analytical framework for the GPT Store ecosystem but also provides empirical evidence and optimization directions for its future development.

## Repository Structure

This repository is organized into the following sections:

- Data Collection: The methodology used to collect data from the GPT Store.
- Dataset: The dataset used for analysis, including key statistics such as the number of GPTs, creators, and data attributes (e.g., categories, ratings, descriptions).
- Security Risk Analysis: Detailed analysis of the security vulnerabilities within the GPT Store.
- User Study: Summary of the user research conducted through surveys and interviews, highlighting key findings related to user preferences, behaviors, and security concerns.

## Data Collection

In this study, we employed an efficient and reliable method for collecting data from the GPT Store platform.

The OpenAI GPT Store platform provides an API at the endpoint https://chatgpt.com/backend-api/gizmos/search?q=*, where the * can be replaced with a search query string. This API returns detailed information about GPT models, including categories, descriptions, ratings, files, and more. We used a dynamic URL template for data requests, replacing the * in the URL with different search query strings to scrape various resources.

Given the need to collect large volumes of data, we employed a concurrent processing strategy to improve efficiency. In our implementation, we used Python's ThreadPoolExecutor library with a maximum concurrency of 50. This allowed multiple requests to be sent simultaneously, significantly speeding up the data collection process. Requests were processed through the as_completed method, ensuring that each completed request was handled promptly, without waiting for all requests to finish.

You can find the `crawler.py` file in the [Dataset](Dataset) folder. It is our web scraping program, and before using it, please make sure to fill in the header section.

## Dataset

You can find our dataset in the [Dataset/Data](Dataset/Data) folder. Due to repository size limitations, we have only included five example dataset files. If you wish to download the complete dataset, please visit our Google Drive link: [GPTs Dataset](https://drive.google.com/file/d/1l0KdCA6ug6kWesiTKYOw07AkLlCHn6Sr/view?usp=drive_link).

## Security Risk Analysis

Our analysis has revealed several key security vulnerabilities within the GPT Store ecosystem, including:

- Prompt Leakage
- File Leakage
- Jailbreak: 
- Malicious Redirects
- Policy Violations

To assess these risks, we conducted security tests on a subset of GPT models. The prompts used in our tests, as well as the results, can be found in the [Security Risk](Security%20Risk) folder. These tests helped highlight vulnerabilities and provide insights into potential improvements for platform security.

Our analysis identified and classified several types of policy violations within the GPT Store ecosystem. These violations were categorized into six distinct types, each representing a particular area of concern. The categories are as follows:

1. Gambling
2. Adult Content
3. Copyright
4. Politics
5. Drug
6. Offensive Talk

Each violation type is denoted by a unique number, as mentioned above. The detailed results, including the models and their corresponding violations, can be found in the [Security Risk](Security%20Risk) folder.

## User Study

In order to gain deeper insights into user interactions with the GPT Store and to understand their preferences, concerns, and experiences, we conducted a comprehensive user study. This included both a quantitative survey and qualitative one-on-one interviews.

You can find our survey and interview results in the [User Study](User%20Study) folder.
