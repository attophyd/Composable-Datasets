import json


class InstructDSProcessor:
    """
    A class for processing data in the InstructDS format

    Args:
        input_file_path (str): The path to the input JSONL file containing InstructDS data
        output_file_path (str): The path to the output JSONL file to store the processed data

    Methods:
        process_jsonl(): Processes the input JSONL file, transforms the data into a specific format,
                        and writes the processed data to the output JSONL file
    """

    def __init__(self, input_file_path, output_file_path):
        """
        Initializes an InstructDSProcessor instance

        Args:
            input_file_path (str): The path to the input JSONL file containing InstructDS data
            output_file_path (str): The path to the output JSONL file to store the processed data
        """
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path

    def is_valid_input_format(self):
        """
        Checks if the input file is in the required InstructDS format

        Returns:
            bool: True if the format is valid, False otherwise
        """
        with open(self.input_file_path, "r") as input_file:
            lines = input_file.readlines()

        for line in lines:
            try:
                data = json.loads(line)
                if "Q" not in data or "A" not in data:
                    return False
            except json.JSONDecodeError:
                return False

        return True

    def process_jsonl(self):
        """
        Processes the input JSONL file, transforms the data into a specific format,
        and writes the processed data to the output JSONL file
        """

        if not self.is_valid_input_format():
            raise ValueError(
                "Input file is not in the required InstructDS format. Format should be JSONL with each line containing a JSON object with 'Q' and 'A' keys."
            )

        with open(self.input_file_path, "r") as input_file:
            lines = input_file.readlines()

        output_data = []
        for line in lines:
            data = json.loads(line)
            question_text = f"[INST] {data['Q']} [/INST]"
            answer_text = f"{data['A']}"
            output_line = {"text": f"<s>{question_text} {answer_text}</s>"}
            output_data.append(output_line)

        with open(self.output_file_path, "w") as output_file:
            for output_line in output_data:
                json.dump(output_line, output_file)
                output_file.write("\n")
