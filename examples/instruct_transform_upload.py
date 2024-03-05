# Import necessary modules
from composable_datasets.blocks.block_processors.instruct_transformer import InstructDSProcessor
from composable_datasets.blocks.block_processors.pq_upload import DataProcessor

# Define input and output paths
input_file_path = "data/all.jsonl"
output_file_path = "data/instruct_all.jsonl"
parquet_path = "data/instruct_all.parquet"

# Set Hub credentials
hub_username = "<HUB_USERNAME>"
hub_repo = "<HUB_REPOSITORY>"

# Process InstructDS data
processor = InstructDSProcessor(input_file_path, output_file_path)
processor.process_jsonl()

# Upload data to Parquet and Hub
data_processor = DataProcessor(output_file_path, parquet_path, hub_username, hub_repo)
data_processor.load_and_convert_data()
