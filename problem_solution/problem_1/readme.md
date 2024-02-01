# **Problem Statement: Author's Story Translation**

An author has written a captivating story in their native language and now wishes to translate it into a different language to reach a broader audience. Your task is to create a Python script that reads the author's story from an input file (`input.txt`), translates each sentence into the desired language, and saves the translated story into an output file (`output.txt`).

1. **Input File Format (`input.txt`):**

   - The input file contains the original story written in the author's native language.
   - Each line in the file represents a sentence in the story.
   - The sentences may contain punctuation and special characters.

   Example (`input.txt`):

   ```
   হোমওয়ার্ক সম্পূর্ণ করার পরে, অবশেষে তারা বন্ধুবান্ধবীর সাথে দরবারে সময় কাটাতে এসেছিল।
   রাতে, চাঁদ আকাশে উজ্জ্বল হয়ে উঠতে লাগত।
   ```

2. **Translation Process:**

   - Your Python script should use a translation service or library to translate each sentence from the author's language to the desired language.
   - Ensure that the translation process maintains the structure and essence of the original sentences.

3. **Output File Format (`output.txt`):**

   - The output file will contain the translated version of the story.
   - Each line in the file corresponds to a translated sentence.
   - Retain the same order as the original sentences.

   Example (`output.txt`):

   ```
   After completing homework, they finally came to spend time in the courtyard with friends.
   At night, the bright moon rises in the sky.
   ```

4. **Requirements:**

   - Use a language translation library or service in your Python script.
   - Handle any potential errors or exceptions during the translation process.
   - Provide informative messages for successful translation and any encountered issues.
   - Allow the script to be easily configurable for different source and target languages.

5. **Notes:**
   - Ensure that the translation service or library you choose supports the languages involved.
   - Maintain readability and coherence in the translated story.

# Solution also here

### need to install the translation library googletrans.

```
pip install googletrans
```

### comands to run this code

```
python3 main.py input.txt output.txt
```
