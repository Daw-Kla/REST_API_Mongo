from flask import request, jsonify
from models import Part, Category
from utils import validate_category_data, validate_part_data, validate_location


def register_routes(api_bp):
    """
    Registered routes for CRUD and search operations
    """
    @api_bp.route('/')
    def welcome():
        return ("Welcome to simple REST API")
    
    #Products
    @api_bp.route('/api/products', methods=['GET'])
    def get_all_parts():
        parts = Part.objects().all()
        return jsonify([part.to_json() for part in parts])

    @api_bp.route('/api/products/<string:serial_number>', methods=['GET'])
    def get_part(serial_number):
        part = Part.objects(serial_number=serial_number).first()
        if part:
            return jsonify(part.to_json())
        else:
            return jsonify({"error": "Part not found"}), 404

    @api_bp.route('/api/products', methods=['POST'])
    def create_part():
        try:
            data = request.json
            validate_part_data(data)
            validate_location(data.get('location'))

            # Ensure that the part belongs to a category and is not in a base category
            category_name = data.get('category')
            if not category_name:
                raise ValueError("Category is required for a part.")
            
            category = Category.objects(name=category_name).first()
            if not category:
                raise ValueError(f"Category '{category_name}' does not exist.")
            
            if not category.parent_name:
                raise ValueError("A part cannot be in a base category.")

            part = Part(**data)
            part.save()
            return jsonify(part.to_json()), 201
        except ValueError as e:
            return jsonify({"error": str(e)}), 400


    @api_bp.route('/api/products/<string:serial_number>', methods=['PUT'])
    def update_part(serial_number):
        try:
            part = Part.objects(serial_number=serial_number).first()
            if not part:
                return jsonify({"error": "Part not found"}), 404

            data = request.json
            validate_part_data(data)

            # Ensure that the updated part still belongs to a category and is not in a base category
            new_category_name = data.get('category')
            if not new_category_name:
                raise ValueError("Category is required for a part.")
            
            new_category = Category.objects(name=new_category_name).first()
            if not new_category:
                raise ValueError(f"Category '{new_category_name}' does not exist.")
            
            if not new_category.parent_name:
                raise ValueError("A part cannot be in a base category.")

            part.modify(**data)
            return jsonify(part.to_json())
        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    @api_bp.route('/api/products/<string:serial_number>', methods=['DELETE'])
    def delete_part(serial_number):
        part = Part.objects(serial_number=serial_number).first()
        if part:
            part.delete()
            return jsonify({"message": "Part deleted successfully"})
        else:
            return jsonify({"error": "Part not found"}), 404
        
    @api_bp.route('/api/products/search', methods=['POST'])
    def search_parts():
        try:
            data = request.json
            search_phrase = data.get('search_phrase')

            if not search_phrase:
                return jsonify({"error": "Missing search phrase"}), 400

            # Mandatory fields in the Part model for search
            mandatory_fields = ['serial_number', 'name', 'description', 'category', 'quantity', 'price']

            # Build a query to search a search_phrase in any of the mandatory fields
            query = {
                "$or": [
                    {field: {"$regex": f"^{search_phrase}$", "$options": "i"}} for field in mandatory_fields
                ]
            }

            parts = Part.objects(__raw__=query)
            if parts:
                return jsonify([part.to_json() for part in parts])
            else:
                return jsonify({"message": "No matching parts found"}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
    #Categories
    @api_bp.route('/api/categories', methods=['GET'])
    def get_all_categories():
        categories = Category.objects().all()
        return jsonify([category.to_json() for category in categories])

    @api_bp.route('/api/categories/<string:name>', methods=['GET'])
    def get_category(name):
        category = Category.objects(name=name).first()
        if category:
            return jsonify(category.to_json())
        else:
            return jsonify({"error": "Category not found"}), 404

    @api_bp.route('/api/categories', methods=['POST'])
    def create_category():
        try:
            data = request.json
            validate_category_data(data) 
            category = Category(**data)
            category.save()
            return jsonify(category.to_json()), 201
        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    @api_bp.route('/api/categories/<string:name>', methods=['PUT'])
    def update_category(name):
        try:
            category = Category.objects(name=name).first()
            if not category:
                return jsonify({"error": "Category not found"}), 404

            data = request.json
            validate_category_data(data) 

            category.modify(**data)
            return jsonify(category.to_json())
        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    @api_bp.route('/api/categories/<string:name>', methods=['DELETE'])
    def delete_category(name):
        category = Category.objects(name=name).first()
        if not category:
            return jsonify({"error": "Category not found"}), 404

        # Ensure that the category cannot be removed if there are parts assigned to it
        parts_with_category = Part.objects(category=name).count()
        if parts_with_category > 0:
            return jsonify({"error": "Cannot remove a category with assigned parts"}), 400

        # Ensure that a parent category cannot be removed if it has child categories with parts assigned
        child_categories = Category.objects(parent_name=name)
        for child_category in child_categories:
            if Part.objects(category=child_category.name).count() > 0:
                return jsonify({"error": "Cannot remove a parent category with child categories having assigned parts"}), 400

        category.delete()
        return jsonify({"message": "Category deleted successfully"})