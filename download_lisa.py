from huggingface_hub import snapshot_download

# Hugging Face repo ID
model_id = "xinlai/LISA-13B-llama2-v1"

# 本機要存放的路徑
local_dir = "models/LISA-13B-llama2-v1"

# 下載整個 repo
snapshot_download(repo_id=model_id, local_dir=local_dir)

print(f"Model downloaded to {local_dir}")
