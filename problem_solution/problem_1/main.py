from googletrans import Translator
import sys

# Check the number of command-line arguments
if len(sys.argv) < 2:
    print("Usage: python script.py <input.txt> <output.txt>")
    sys.exit(1)

# Access the command-line argument
input_file = sys.argv[1]
output_file = sys.argv[2]

def translate_bengali_to_english(text):
    translator = Translator()
    translation = translator.translate(text, src='bn', dest='en')
    return translation.text

if __name__ == "__main__":
    try:
        with open(input_file, 'r', encoding='utf-8') as in_file, open(output_file, 'w', encoding='utf-8') as out_file:
            line_no = 0
            for line in in_file:
                # Process each line (remove newline character and split by '|')
                line = line.strip()
                line_no += 1
                try:
                    english_text = translate_bengali_to_english(line)
                except:
                    english_text = '\n'
                out_file.write(english_text + '\n')
                print(f'line no : {line_no}')
                
        print("translate bengali to english done")
    except FileNotFoundError:
        print(f"The file '{input_file}' or '{output_file}' was not found.")

    except Exception as e:
        print(f"Translation failed. Error: {e}")
        
