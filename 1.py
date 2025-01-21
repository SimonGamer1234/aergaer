import os

# Retrieve the environment variables
repo_var_one = os.getenv("REPO_VAR_ONE")
repo_var_two = os.getenv("REPO_VAR_TWO")
secret_var = os.getenv("SECRET_VAR")

# Print them or use them in your script
print(f"Repo Variable One: {repo_var_one}")
print(f"Repo Variable Two: {repo_var_two}")
print(f"Secret Variable: {secret_var}")
