# LDA Writeup

## Reason for approach

Latent Dirichlet Allocation (LDA) is a generative probabilistic model that is used to discover topics in a collection of documents. It assumes that each document is a mixture of topics, and each topic is a mixture of words. LDA is particularly useful for unsupervised learning tasks where the goal is to identify hidden structures in the data without any labeled examples. When reading through a large number of legal documents, a large portion of the text is repeated in a small number of ways. LDA is a good choice for this task because it can help identify the underlying topics and themes in the documents, allowing for better organization and understanding of the content. Addtionally, through prior research and articles, unsupervised learning can provide strong features for supervised learning tasks.

## Methodology

LDA was used in two ways on the documents within the combined datasets. The first to identify the topics within the documents, which can help in understanding the content and themes of the documents. The second approach was used to identify the topics across all documents, which can help in understanding the overall themes and trends in the data.

To analyze the intra-document topics, LDA was applied to each document individually. The number of topics was set to 5, and the model was trained on the text of each document, splitting the document by each new line. The labeled topics and lines were then aggregated into two lists, where the first list contained the each line of text and the second list contained the topic association for their respective line.

For the second approach on analyzing the inter-document topics. LDA was applied to the entire dataset, with the number of topics set to 5 once again. The model was trained on the text of all documents, with each *whole* document being treated as a single line. The labeled topics and documents were then aggregated into two lists, where the first list contained the each document and the second list contained the topic association for their respective document.

The two lists from both approaches were collected and aggregated so that each document had it's own dictionary of the lines it contains and the topics for both itself and each line. This singular list of dictionaries was then written to disk as a JSON file for future use and analysis.

## Citations

- Coates, Adam & Ng, Andrew & Lee, Honglak. (2011). An Analysis of Single-Layer Networks in Unsupervised Feature Learning. Journal of Machine Learning Research - Proceedings Track. 15. 215-223.
  - See [the paper on Research Gate](https://www.researchgate.net/publication/220321031_An_Analysis_of_Single-Layer_Networks_in_Unsupervised_Feature_Learning) for more details and citations.
