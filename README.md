# GitHub Repository Visibility Manager

A simple Python script to change the visibility of all your GitHub repositories to private.

## Prerequisites

- Python 3.6 or higher
- Git (optional, for cloning the repository)

## Features

- Fetches all your GitHub repositories
- Changes visibility of public repositories to private
- Provides detailed feedback and confirmation steps

## Installation & Usage

### Option 1: Using Setup Scripts (Recommended)

#### For macOS/Linux:

1. Clone or download this repository:
```bash
git clone https://github.com/yourusername/github-repo-manager.git
cd github-repo-manager
```

2. Make the setup script executable:
```bash
chmod +x setup.sh
```

3. Run the setup script:
```bash
./setup.sh
```

4. Activate the virtual environment:
```bash
source venv/bin/activate
```

5. Run the script:
```bash
python main.py
```

6. When finished, deactivate the virtual environment:
```bash
deactivate
```

#### For Windows:

1. Clone or download this repository:
```
git clone https://github.com/yourusername/github-repo-manager.git
cd github-repo-manager
```

2. Run the setup script:
```
setup.bat
```

3. Activate the virtual environment:
```
venv\Scripts\activate.bat
```

4. Run the script:
```
python main.py
```

5. When finished, deactivate the virtual environment:
```
deactivate
```

### Option 2: Manual Setup

1. Clone or download this repository:
```bash
git clone https://github.com/yourusername/github-repo-manager.git
cd github-repo-manager
```

2. Create and activate a virtual environment:
```bash
# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
venv\Scripts\activate
```

3. Install required dependencies:
```bash
pip install -r requirements.txt
```

4. Run the script:
```bash
python main.py
```

5. When finished, deactivate the virtual environment:
```bash
deactivate
```

### Option 3: Automatic Setup (Alternative)

The script can also set up the virtual environment automatically:

```bash
python main.py
```

The script will:
1. Create a virtual environment (if it doesn't exist)
2. Install required dependencies
3. Ask for your GitHub Personal Access Token (or use the `GITHUB_TOKEN` environment variable if set)
4. Ask for your GitHub username
5. Fetch all repositories you own
6. Ask for confirmation before making any changes
7. Change the visibility of all your public repositories to private
8. Show a summary of the changes made

## Setting up a GitHub Personal Access Token

1. Go to [GitHub Settings > Developer Settings > Personal Access Tokens](https://github.com/settings/tokens)
2. Click "Generate new token"
3. Give it a descriptive name
4. Select the `repo` scope (this gives full control of private repositories)
5. Click "Generate token"
6. Copy the token (you won't be able to see it again)

You can either:
- Set it as an environment variable: `export GITHUB_TOKEN=your_token_here`
- Enter it when prompted by the script

## Warning

This action will make all your public repositories private. This may affect:
- Users who have forked your repositories
- Visibility of your work to potential employers or collaborators
- Any services that depend on your repositories being public

There is no bulk operation to revert this change. You'll need to manually change repositories back to public if needed. 