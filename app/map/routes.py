from flask import render_template, jsonify
from app.map import map_bp
import random

# Dummy data for marker locations
markers = [
    {'id': 'W001', 'lat': 28.7041, 'lon': 77.1025, 'status': 'Abnormal (Spike)', 'battery': 89},
    {'id': 'W002', 'lat': 19.0760, 'lon': 72.8777, 'status': 'Normal', 'battery': 85},
    {'id': 'W003', 'lat': 13.0827, 'lon': 80.2707, 'status': 'Normal', 'battery': 91},
    {'id': 'W004', 'lat': 22.5726, 'lon': 88.3639, 'status': 'Low Battery', 'battery': 58},
    {'id': 'W005', 'lat': 26.9124, 'lon': 75.7873, 'status': 'Normal', 'battery': 80},
    {'id': 'W006', 'lat': 21.1702, 'lon': 72.8311, 'status': 'Normal', 'battery': 75},
    {'id': 'W007', 'lat': 12.9716, 'lon': 77.5946, 'status': 'Normal', 'battery': 92},
    {'id': 'W008', 'lat': 23.2599, 'lon': 77.4126, 'status': 'Abnormal (Drop)', 'battery': 82},
    {'id': 'W009', 'lat': 25.3176, 'lon': 82.9739, 'status': 'Normal', 'battery': 88},
    {'id': 'W010', 'lat': 15.3173, 'lon': 75.7139, 'status': 'Low Battery', 'battery': 55},
    {'id': 'W011', 'lat': 24.5854, 'lon': 73.7125, 'status': 'Normal', 'battery': 93},
    {'id': 'W012', 'lat': 30.7333, 'lon': 76.7794, 'status': 'Normal', 'battery': 87},
    {'id': 'W013', 'lat': 27.0238, 'lon': 74.2179, 'status': 'Normal', 'battery': 78},
    {'id': 'W014', 'lat': 17.3850, 'lon': 78.4867, 'status': 'Normal', 'battery': 90},
    {'id': 'W015', 'lat': 29.9457, 'lon': 78.1642, 'status': 'Abnormal (Spike)', 'battery': 86},
    {'id': 'W016', 'lat': 22.3072, 'lon': 73.1812, 'status': 'Normal', 'battery': 88},
    {'id': 'W017', 'lat': 11.0168, 'lon': 76.9558, 'status': 'Low Battery', 'battery': 54},
    {'id': 'W018', 'lat': 19.7515, 'lon': 75.7139, 'status': 'Normal', 'battery': 91},
    {'id': 'W019', 'lat': 23.3441, 'lon': 85.3096, 'status': 'Normal', 'battery': 84},
    {'id': 'W020', 'lat': 21.2514, 'lon': 81.6296, 'status': 'Abnormal (Drop)', 'battery': 79}

]

@map_bp.route('/')
def map_view():
    return render_template('map.html')

@map_bp.route('/update_markers')
def update_markers():
    # Randomly update marker data for demonstration
    updated_markers = []
    for marker in markers:
        # Generate a random battery level
        new_battery = random.randint(50, 100)
        
        # Determine the status based on the battery level
        if new_battery < 60:
            status = "Low Battery"
        else:
            status = random.choice(["Normal", "Abnormal (Spike)"])
        
        # Create the updated marker with new values
        updated_marker = {
            **marker,
            "status": status,
            "battery": f"{new_battery}%"
        }
        updated_markers.append(updated_marker)
    
    return jsonify(updated_markers)
