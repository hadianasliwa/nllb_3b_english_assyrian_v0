from huggingface_hub import HfApi
api = HfApi()

api.upload_folder(
    folder_path="nllb_eng_aii_lora",
    repo_id="hadiana/nllb_3b_english_assyrian_v0",
    repo_type="model",
)