#!/usr/bin/env python3
import requests
import os
import sys
from getpass import getpass

def get_all_repos(token, username):
    """Fetch all repositories for the authenticated user."""
    repos = []
    page = 1
    
    while True:
        url = f"https://api.github.com/user/repos?per_page=100&page={page}"
        headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json"
        }
        
        response = requests.get(url, headers=headers)
        
        if response.status_code != 200:
            print(f"Error fetching repositories: {response.status_code}")
            print(response.json())
            sys.exit(1)
        
        page_repos = response.json()
        if not page_repos:
            break
            
        repos.extend(page_repos)
        page += 1
    
    # Filter to only include repos owned by the user
    return [repo for repo in repos if repo["owner"]["login"] == username]

def make_repo_private(token, repo_name, owner):
    """Change a repository's visibility to private."""
    url = f"https://api.github.com/repos/{owner}/{repo_name}"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {
        "private": True
    }
    
    response = requests.patch(url, headers=headers, json=data)
    
    if response.status_code == 200:
        print(f"✅ Successfully made {repo_name} private")
        return True
    else:
        print(f"❌ Failed to make {repo_name} private: {response.status_code}")
        print(response.json())
        return False

def main():
    print("GitHub Repository Visibility Manager")
    print("====================================")
    print("This script will change all your GitHub repositories to private.")
    print("WARNING: This action cannot be undone in bulk. You'll need to manually")
    print("change repositories back to public if needed.")
    print()
    
    # Get GitHub personal access token
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print("Please enter your GitHub Personal Access Token.")
        print("(The token needs 'repo' scope permissions)")
        print("You can create one at: https://github.com/settings/tokens")
        token = getpass("GitHub Token: ")
    
    # Get GitHub username
    username = input("Enter your GitHub username: ")
    
    # Confirm action
    confirm = input(f"Are you sure you want to make ALL repositories for {username} private? (yes/no): ")
    if confirm.lower() != "yes":
        print("Operation cancelled.")
        sys.exit(0)
    
    # Get all repositories
    print(f"Fetching repositories for {username}...")
    repos = get_all_repos(token, username)
    
    if not repos:
        print("No repositories found or you don't have access to any repositories.")
        sys.exit(0)
    
    # Show summary
    print(f"Found {len(repos)} repositories owned by {username}.")
    
    # Final confirmation
    confirm = input(f"Ready to change {len(repos)} repositories to private. Proceed? (yes/no): ")
    if confirm.lower() != "yes":
        print("Operation cancelled.")
        sys.exit(0)
    
    # Change visibility
    success_count = 0
    for repo in repos:
        if repo["private"]:
            print(f"⏭️  Skipping {repo['name']} (already private)")
            continue
            
        if make_repo_private(token, repo["name"], username):
            success_count += 1
    
    # Summary
    print("\nOperation completed!")
    print(f"Successfully changed {success_count} repositories to private.")
    if success_count < len(repos):
        print(f"Skipped {len(repos) - success_count} repositories (already private or failed).")

if __name__ == "__main__":
    main()
