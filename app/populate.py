from main import app
from models import Part, Category

with app.app_context():
    # Populate dataset with startup data
    main_category_data = {
        "name": "Electronics",
        "parent_name": ""  # Empty parent_name indicates a base category
    }
    main_category = Category(**main_category_data)
    main_category.save()

    side_category_1_data = {
        "name": "Resistors",
        "parent_name": "Electronics"
    }
    side_category_1 = Category(**side_category_1_data)
    side_category_1.save()

    side_category_2_data = {
        "name": "Capacitors",
        "parent_name": "Electronics"
    }
    side_category_2 = Category(**side_category_2_data)
    side_category_2.save()

    part_1_data = {
        "serial_number": "123456",
        "name": "Resistor 1",
        "description": "A resistor for testing",
        "category": "Resistors",
        "quantity": 10,
        "price": 1.99,
        "location": {"room": "A", "bookcase": "B", "shelf": "1", "cuvette": "C", "column": "2", "row": "3"}
    }
    part_1 = Part(**part_1_data)
    part_1.save()

    part_2_data = {
        "serial_number": "789012",
        "name": "Capacitor 1",
        "description": "A capacitor for testing",
        "category": "Capacitors",
        "quantity": 5,
        "price": 2.99,
        "location": {"room": "A", "bookcase": "B", "shelf": "2", "cuvette": "C", "column": "2", "row": "4"}
    }
    part_2 = Part(**part_2_data)
    part_2.save()

    part_3_data = {
        "serial_number": "345678",
        "name": "Resistor 2",
        "description": "Another resistor for testing",
        "category": "Resistors",
        "quantity": 8,
        "price": 1.49,
        "location": {"room": "A", "bookcase": "C", "shelf": "1", "cuvette": "D", "column": "1", "row": "2"}
    }
    part_3 = Part(**part_3_data)
    part_3.save()

    part_4_data = {
        "serial_number": "901234",
        "name": "Capacitor 2",
        "description": "Another capacitor for testing",
        "category": "Capacitors",
        "quantity": 3,
        "price": 3.49,
        "location": {"room": "B", "bookcase": "A", "shelf": "2", "cuvette": "E", "column": "3", "row": "5"}
    }
    part_4 = Part(**part_4_data)
    part_4.save()

    part_5_data = {
        "serial_number": "567890",
        "name": "Resistor 3",
        "description": "Yet another resistor for testing",
        "category": "Resistors",
        "quantity": 12,
        "price": 2.99,
        "location": {"room": "B", "bookcase": "B", "shelf": "1", "cuvette": "F", "column": "2", "row": "1"}
    }
    part_5 = Part(**part_5_data)
    part_5.save()

    part_6_data = {
        "serial_number": "123123",
        "name": "Capacitor 3",
        "description": "Yet another capacitor for testing",
        "category": "Capacitors",
        "quantity": 7,
        "price": 1.99,
        "location": {"room": "B", "bookcase": "C", "shelf": "2", "cuvette": "G", "column": "1", "row": "3"}
    }
    part_6 = Part(**part_6_data)
    part_6.save()

    print("Collections and sample data created.")
