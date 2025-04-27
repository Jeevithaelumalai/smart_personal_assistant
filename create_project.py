import os

# Project structure definition
structure = {
    'mood-analyzer': [
        'app.py',
        'config.py',
        'requirements.txt',
        '.env',
        ('templates', ['index.html']),
        ('static', ['style.css', 'script.js'])
    ]
}

def create_project(base, structure):
    """Creates the project folder structure with empty files"""
    try:
        os.makedirs(base, exist_ok=True)
        print(f"Created base directory: {base}")
        
        for item in structure:
            if isinstance(item, tuple):
                dir_name, files = item
                path = os.path.join(base, dir_name)
                os.makedirs(path, exist_ok=True)
                print(f"Created directory: {path}")
                
                for file in files:
                    file_path = os.path.join(path, file)
                    with open(file_path, 'w') as f:
                        pass  # Create empty file
                    print(f"Created file: {file_path}")
            else:
                file_path = os.path.join(base, item)
                with open(file_path, 'w') as f:
                    pass  # Create empty file
                print(f"Created file: {file_path}")
                
        return True
    except Exception as e:
        print(f"Error creating structure: {e}")
        return False

if __name__ == '__main__':
    # Create the project structure
    success = create_project('.', structure['mood-analyzer'])
    
    if success:
        print("\nProject structure created successfully!")
        print("\nNext steps:")
        print("1. Add content to the files")
        print("2. Install dependencies with: pip install -r requirements.txt")
        print("3. Run the app with: python app.py")
    else:
        print("\nFailed to create project structure")