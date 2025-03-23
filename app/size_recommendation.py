def get_height_range(height):
    """Return the height range category based on the height."""
    if 150 <= height <= 165:
        return '150-165'
    elif 165 < height <= 170:
        return '165-170'
    elif 170 < height <= 175:
        return '170-175'
    else:
        return None  # Or handle for out-of-range values if needed

def recommend_size(usual_size, height, fit_preference):
    """Recommend size based on usual size, height, and fit preference."""
    
    # Ensure the fit preference is case-insensitive and handle "tight" or "looser"
    fit_preference = fit_preference.lower()  # Convert to lowercase
    
    if fit_preference not in ["tight", "looser"]:
        return "Invalid fit preference. Please choose 'tight' or 'looser'."
    
    height_range = get_height_range(height)
    
    if not height_range:
        return "Height out of range, please provide a valid height (150-175 cm)"
    
    # Define size mapping based on height ranges and fit preferences (as provided in the dataset)
    size_mapping = {
        '150-165': {
            4: {'tight': 'XXS', 'looser': 'XXS'},
            6: {'tight': 'XXS', 'looser': 'XS'},
            8: {'tight': 'XS', 'looser': 'S'},
        },
        '165-170': {
            10: {'tight': 'S', 'looser': 'M'},
        },
        '170-175': {
            12: {'tight': 'M', 'looser': 'L'},
            14: {'tight': 'L', 'looser': 'XL'},
            16: {'tight': 'XL', 'looser': 'XL'},
        },
    }
    
    # Find the recommended size based on height, usual size, and fit preference
    if usual_size in size_mapping[height_range]:
        if fit_preference in size_mapping[height_range][usual_size]:
            return size_mapping[height_range][usual_size][fit_preference]
        else:
            return "Fit preference not valid"
    else:
        return "Usual size not valid for this height range"
