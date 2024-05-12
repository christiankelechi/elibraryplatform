# from transformers import BartTokenizer, BartForConditionalGeneration

# # Load tokenizer and model
# tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
# model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')

# # Function to generate summary
# import random

# # Function to generate summary with varied parameters
# def generate_summary(text):
#     # Define parameter ranges
#     min_length_range = [500, 800]  # Vary min_length between 1000 and 5000
#     max_length_range = [10000, 50000]  # Vary max_length between 10000 and 50000
#     length_penalty_range = [1.5, 2.5]  # Vary length_penalty between 1.5 and 2.5
#     num_beams_range = [2, 4, 6]  # Vary num_beams between 2, 4, and 6
    
#     # Randomly select parameters
#     min_length = random.choice(min_length_range)
#     max_length = random.choice(max_length_range)
#     length_penalty = random.uniform(*length_penalty_range)
#     num_beams = random.choice(num_beams_range)
    
#     # Tokenize and generate summary
#     inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=1024, truncation=True)
#     summary_ids = model.generate(inputs, max_length=max_length, min_length=min_length, 
#                                  length_penalty=length_penalty, num_beams=num_beams, early_stopping=True)
#     summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
#     return summary

# # # Example usage
# # text = "Your input text here"
# # summary = generate_summary(text)
# # print(summary)

# from transformers import BartTokenizer, BartForConditionalGeneration
# import random

# # Load tokenizer and model
# tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn', force_download=True)
# model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn', force_download=True)

# # Function to generate summary
# def generate_summary(text):
#     # Define parameter ranges
#     min_length_range = [500, 800]  # Vary min_length between 1000 and 5000
#     max_length_range = [10000, 50000]  # Vary max_length between 10000 and 50000
#     length_penalty_range = [1.5, 2.5]  # Vary length_penalty between 1.5 and 2.5
#     num_beams_range = [2, 4, 6]  # Vary num_beams between 2, 4, and 6
    
#     # Randomly select parameters
#     min_length = random.choice(min_length_range)
#     max_length = random.choice(max_length_range)
#     length_penalty = random.uniform(*length_penalty_range)
#     num_beams = random.choice(num_beams_range)
    
#     # Tokenize and generate summary
#     inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=1024, truncation=True)
#     summary_ids = model.generate(inputs, max_length=max_length, min_length=min_length, 
#                                  length_penalty=length_penalty, num_beams=num_beams, early_stopping=True)
#     summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
#     return summary

# # Example usage
# text = "Your input text here"
# summary = generate_summary(text)
# print(summary)
