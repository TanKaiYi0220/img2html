import random

class AccordionRandom:
    num_items = [1, 2, 3, 4]
    weights = [0.4, 0.3, 0.2, 0.1]

    @classmethod
    def get_num_items(cls):
        num = random.choices(cls.num_items, weights=cls.weights)[0]
        return num
    
class ButtonRandom:
    class_idx = [i for i in range(9)]
    weights = [
        0.50, # Primary
        0.20, # Secondary
        0.10, # Success
        0.10, # Danger
        0.10, # Warning
        0.04, # Info
        0.02, # Light
        0.02, # Dark
        0.02  # Link
    ]

    @classmethod
    def get_button_idx(cls):
        num = random.choices(cls.class_idx, weights=cls.weights)[0]
        return num
    
class CardRandom:
    card_class_idx = [i for i in range(4)]
    card_weights = [0.25, 0.25, 0.25, 0.25]

    button_class_idx = [i for i in range(9)]
    button_weights = [
        0.50, # Primary
        0.20, # Secondary
        0.10, # Success
        0.10, # Danger
        0.10, # Warning
        0.04, # Info
        0.02, # Light
        0.02, # Dark
        0.02  # Link
    ]

    @classmethod
    def get_button_idx(cls):
        num = random.choices(cls.button_class_idx, weights=cls.button_weights)[0]
        return num
    
    @classmethod
    def get_card_idx(cls):
        num = random.choices(cls.card_class_idx, weights=cls.card_weights)[0]
        cls.card_weights = [0.0 for _ in range(4)]
        cls.card_weights[num] = 1
        return num
    
    @classmethod
    def reset(cls):
        cls.card_weights = [0.25, 0.25, 0.25, 0.25]
    
class CarouselRandom:
    carousel_idx = [i for i in range(2)]
    carousel_weights = [0.5, 0.5]

    @classmethod
    def get_carousel_idx(cls):
        num = random.choices(cls.carousel_idx, weights=cls.carousel_weights)[0]
        return num
    
class DropdownRandom:
    button_class_idx = [i for i in range(2)]
    button_weights = [
        0.65, # Primary
        0.35  # Secondary
    ]

    @classmethod
    def get_button_idx(cls):
        num = random.choices(cls.button_class_idx, weights=cls.button_weights)[0]
        return num
    
class NavBarRandom:
    navbar_class_idx = [i for i in range(7)]
    navbar_weights = [
        0.30, # navbar brand_text-dropdown-search
        0.20, # navbar brand_text-dropdown
        0.20, # navbar brand_text-search
        0.10, # navbar dropdown-search
        0.10, # navbar brand_text
        0.05, # navbar dropdown
        0.05  # navbar search
    ]
    item_num_idx = [i for i in range(4)]
    item_num_weights = [0.1, 0.4, 0.3, 0.2]

    @classmethod
    def get_navbar_idx(cls):
        num = random.choices(cls.navbar_class_idx, weights=cls.navbar_weights)[0]
        return num
    
    @classmethod
    def get_item_idx(cls):
        num = random.choices(cls.item_num_idx, weights=cls.item_num_weights)[0]
        return num
    

