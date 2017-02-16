BEER_STYLES = {
    'Pale Ales': [
        'American Amber Ale',
        'English-Style Bitter',
        'Blonde Ale',
        'English-Style Pale Ale (ESB)',
    ],
    'Dark Lagers': [
        'American Amber Lager',
        'German-Style Dunkel',
        'German-Style Marzen / Oktoberfest',
        'German-Style Schwarzbier',
        'Vienna-Style Lager',
    ],
    'Brown Ales': [
        'American Brown Ale',
        'English-Style Brown Ale',
        'English-Style Mild',
    ],
    'India Pale Ales': [
        'American IPA',
        'Session IPA',
        'Brett IPA',
        'English-Style IPA',
        'Imperial India Pale Ale',
    ],
    'Wheat Beers': [
        'American-Style Wheat Wine Ale',
        'American Wheat',
        'Belgian-Style Witbier',
        'Berliner-Style Weisse',
        'German-Style Dunkelweizen',
        'German-Style Hefeweizen',
    ],
    'Strong Ales': [
        'American Barley Wine',
        'American Strong Ale',
        'American Imperial Red Ale',
        'British-Style Barley Wine Ale',
        'English-Style Old Ale',
    ],
    'Belgian Styles': [
        'Belgian-Style Blonde Ale',
        'Belgian-Style Dubbel',
        'Belgian-Style Golden Strong Ale',
        'Belgian-Style Pale Ale',
        'Belgian-Style Quadrupel',
        'Belgian-Style Saison',
        'Belgian-Style Tripel',
    ],
    'Hybrid Beers': [
        'American Cream Ale',
        'French-Style Biere de Garde',
        'California Common',
        'German-Style Brown/Altbier',
        'German-Style Kolsch',
        'Irish-Style Red',
    ],
    'Porters': [
        'American Porter',
        'American Imperial Porter',
        'Baltic-Style Porter',
        'English-Style Brown Porter',
        'Robust Porter',
        'Smoke Porter',
    ],
    'Stouts': [
        'American Imperial Stout',
        'American Imperial Stout (Barrel Aged)',
        'Russian Imperial Stout',
        'American Stout',
        'American Stout (Barrel Aged)',
        'English-Style Oatmeal Stout',
        'English-Style Sweet Stout (Milk Stout)',
        'Oyster Stout',
        'Irish-Style Dry Stout',
    ],
    'Bocks': [
        'German-Style Bock',
        'German-Style Doppelbock',
        'German-Style Maibock',
        'German-Style Weizenbock',
    ],
    'Scottish-Style Ales': [
        'Scotch Ale/Wee Heavy',
        'Scottish-Style Ale',
    ],
    'Wild/Sour Beers': [
        'American Brett',
        'American Sour',
        'Belgian-Style Flanders',
        'Belgian-Style Fruit Lambic',
        'Belgian-Style Lambic/Gueuze',
        'Sour Stout',
        'Contemporary Gose',
    ],
    'Pilseners and Pale Lagers': [
        'American Lager',
        'Inida Pale Lager',
        'Bohemian-Style Pilsener',
        'European-Style Export',
        'German-Style Helles',
        'German-Style Pilsener',
    ],
    'Specialty Beers': [
        'American Black Ale',
        'Barrel-Aged Beer',
        'Chocolate Beer',
        'Coffee Beer',
        'Fruit and Field Beer',
        'Gluten Free',
        'Herb and Spice Beer',
        'Winter Warmer',
        'Honey Beer',
        'Pumpkin Beer',
        'Rye Beer',
        'Session Beer',
        'Smoke Beer',
        'Specialty Beer',
    ]
}
BEER_STYLE_CHOICES = []
for styles in BEER_STYLES.values():
	BEER_STYLE_CHOICES.extend([(style, style) for style in styles])

GLASSWARE_STYLES = [
    ('BOOT', 'Boot'),
    ('MUG', 'Mug'),
    ('GOBLET', 'Goblet'),
    ('FLUTE', 'Flute'),
    ('NOVELTY', 'Novelty'),
    ('PILSNER', 'Pilsner'),
    ('PINT', 'Pint'),
    ('STEIN', 'Stein'),
    ('TASTER', 'Taster'),
    ('TULIP', 'Tulip'),
]
