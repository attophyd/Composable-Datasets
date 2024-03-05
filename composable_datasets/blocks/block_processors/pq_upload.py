from datasets import Dataset, DatasetDict, Features, Value


class ParquetUploader:
    def __init__(self, jsonl_path, parquet_path, hub_username, hub_repo):
        """
        Initializes a ParquetUploader object

        Parameters:
            - jsonl_path (str): The path to the input JSON Lines file
            - parquet_path (str): The path to save the output Parquet file
            - hub_username (str): The username for the Hugging Face Model Hub
            - hub_repo (str): The repository name for the Hugging Face Model Hub
        """
        self.jsonl_path = jsonl_path
        self.parquet_path = parquet_path
        self.hub_username = hub_username
        self.hub_repo = hub_repo

    def load_and_convert_data(self):
        """
        Loads data from the specified JSON Lines file, extracts the "text" field,
        and converts it to a Parquet file. The resulting dataset is then pushed to
        the Hugging Face Model Hub under the specified username and repository
        """
        data = Dataset.from_json(self.jsonl_path)
        data = data.map(lambda x: {"text": x["text"]}, batched=True)
        data.to_parquet(self.parquet_path)
        features = Features({"text": Value("string")})
        dataset = DatasetDict({"train": data})
        dataset.push_to_hub(f"{self.hub_username}/{self.hub_repo}")
