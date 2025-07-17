import convertapi
from dotenv import load_dotenv
import os

convertapi.api_credentials = os.getenv('convertapi')


def save_result_and_convert_to_pdf(result, out_path):
  """Saves the result to a markdown file and converts it to a PDF."""
  file_path = "temp_result.md"

  with open(file_path, "w") as f:
      f.write(str(result))

  print(f"Result saved to {file_path}")

  # Use convertapi to convert markdown to PDF

  convertapi.convert(
      'pdf', 
       {
      'File': f'/content/{file_path}',
      'MarginTop': '20',
      'MarginRight': '20',
      'MarginBottom': '20',
      'MarginLeft': '20'
  }, 
      from_format = 'md'
      ).save_files(out_path)

# Call the function to save and convert the final script
# save_result_and_convert_to_pdf(final_script, '/content/')