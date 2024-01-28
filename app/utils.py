from models import Category

def validate_part_data(data):
    # Check if all mandatory fields are present
    required_fields = ['serial_number', 'name', 'description', 'category', 'quantity', 'price', 'location']
    for field in required_fields:
        if field not in data:
            raise ValueError(f'Missing required field: {field}')

    # Check if the category exists
    category_name = data['category']
    if not Category.objects(name=category_name):
        raise ValueError(f"Category '{category_name}' does not exist.")
    
def validate_location(value):
    # List of mandatory fields for the "location" dictionary
    mandatory_fields = ['bookcase', 'column', 'cuvette', 'room', 'row', 'shelf']

    # Check if all mandatory fields are present
    for field in mandatory_fields:
        if field not in value:
            raise ValueError(f'Missing required field in location: {field}')

def validate_category_data(data):
    # Check if all mandatory fields are present
    required_fields = ['name', 'parent_name']
    for field in required_fields:
        if field not in data:
            raise ValueError(f'Missing required field: {field}')

    # Check if the parent category exists
    parent_name = data['parent_name']
    if parent_name and not Category.objects(name=parent_name):
        raise ValueError(f"Parent category '{parent_name}' does not exist.")