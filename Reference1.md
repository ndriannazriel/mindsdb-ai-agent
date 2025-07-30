CREATE DATABASE web_crawler
WITH ENGINE = 'web';

CREATE VIEW environments (
    SELECT * FROM web_crawler.crawler
    WHERE url = 'https://www.examplewebtobecrawled.com'
    AND crawl_depth = 0
);

--Create a vector enabled database where the data inserted into here will be automatically --vectorized so that it can be very quickly searched through [RetrievalAugmentedGeneration]
CREATE KNOWLEDGE_BASE  environment_kb
USING 
metadata_columns = ['url'],
content_columns = ['text_content'];

--Optional
DESCRIBE KNOWLEDGE_BASE environment_kb;

--Insert into knowledge base
INSERT INTO environment_kb
SELECT url, text_content FROM environments;

--Optional
SELECT * FROM environment_kb;

--Query the Knowledge Base by passing a string and then calculating the relevance and distance --to that string
SELECT * FROM environment_kb
WHERE content = 'What is staging'
AND relevance >= 0.6;

--It will rank all the results in the database based on the relevance score based on the --'content'