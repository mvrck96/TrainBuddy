"""_summary_
"""
import os

from dotenv import find_dotenv, load_dotenv
from prefect.filesystems import GitHub

print(find_dotenv())
load_dotenv(find_dotenv())

PREFECT_BLOCKNAME_GITHUB = os.environ.get("PREFECT_BLOCKNAME_GITHUB")
GITHUB_REPO_PATH = os.environ.get("GITHUB_REPO_PATH")
GITHUB_REPO_BRANCH = os.environ.get("GITHUB_REPO_BRANCH")


#############################################
################# GitHub
##############################################
gh_block = GitHub(
    name=PREFECT_BLOCKNAME_GITHUB,
    repository=GITHUB_REPO_PATH,
    include_git_objects=False,
    reference=GITHUB_REPO_BRANCH,
    # path="NewsBuddy/api_manager/flows/fetch_news.py"
)
# gh_block.get_directory(local_path='NewsBuddy/api_manager/flows/')
gh_block.save(PREFECT_BLOCKNAME_GITHUB, overwrite=True)
print(f"Created Github block named {PREFECT_BLOCKNAME_GITHUB}")
