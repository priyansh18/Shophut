from django.core.management.base import BaseCommand
from store.models import Product


PRODUCTS = [
    # Men
    {"name": "Slim Fit Casual Shirt", "brand": "Roadster", "price": 899, "category": "men",
     "image_url": "https://images.unsplash.com/photo-1596755094514-f87e34085b2c?w=300&h=400&fit=crop"},
    {"name": "Running Shoes", "brand": "Nike", "price": 3999, "category": "men",
     "image_url": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=300&h=400&fit=crop"},
    {"name": "Leather Belt", "brand": "Levi's", "price": 699, "category": "men",
     "image_url": "https://images.unsplash.com/photo-1624222247344-550fb60583dc?w=300&h=400&fit=crop"},
    {"name": "Polo T-Shirt", "brand": "U.S. Polo", "price": 1299, "category": "men",
     "image_url": "https://images.unsplash.com/photo-1586363104862-3a5e2ab60d99?w=300&h=400&fit=crop"},
    {"name": "Denim Jeans", "brand": "Wrangler", "price": 1899, "category": "men",
     "image_url": "https://images.unsplash.com/photo-1542272604-787c3835535d?w=300&h=400&fit=crop"},
    {"name": "Formal Blazer", "brand": "Raymond", "price": 4999, "category": "men",
     "image_url": "https://images.unsplash.com/photo-1507679799987-c73779587ccf?w=300&h=400&fit=crop"},
    {"name": "Sports Joggers", "brand": "Puma", "price": 1599, "category": "men",
     "image_url": "https://images.unsplash.com/photo-1562157873-818bc0726f68?w=300&h=400&fit=crop"},
    {"name": "Canvas Sneakers", "brand": "Converse", "price": 2499, "category": "men",
     "image_url": "https://images.unsplash.com/photo-1463100099107-aa0980c362e6?w=300&h=400&fit=crop"},
    {"name": "Aviator Sunglasses", "brand": "Ray-Ban", "price": 5999, "category": "men",
     "image_url": "https://images.unsplash.com/photo-1511499767150-a48a237f0083?w=300&h=400&fit=crop"},
    {"name": "Leather Wallet", "brand": "Fossil", "price": 1499, "category": "men",
     "image_url": "https://images.unsplash.com/photo-1627123424574-724758594e93?w=300&h=400&fit=crop"},

    # Women
    {"name": "Floral Maxi Dress", "brand": "ONLY", "price": 1799, "category": "women",
     "image_url": "https://images.unsplash.com/photo-1572804013309-59a88b7e92f1?w=300&h=400&fit=crop"},
    {"name": "High Waist Jeans", "brand": "Levi's", "price": 2199, "category": "women",
     "image_url": "https://images.unsplash.com/photo-1541099649105-f69ad21f3246?w=300&h=400&fit=crop"},
    {"name": "Embroidered Kurti", "brand": "Biba", "price": 999, "category": "women",
     "image_url": "https://images.unsplash.com/photo-1583391733956-3750e0ff4e8b?w=300&h=400&fit=crop"},
    {"name": "Block Heels", "brand": "Mango", "price": 2999, "category": "women",
     "image_url": "https://images.unsplash.com/photo-1543163521-1bf539c55dd2?w=300&h=400&fit=crop"},
    {"name": "Crossbody Bag", "brand": "Baggit", "price": 1299, "category": "women",
     "image_url": "https://images.unsplash.com/photo-1548036328-c9fa89d128fa?w=300&h=400&fit=crop"},
    {"name": "Cotton Palazzo Set", "brand": "W", "price": 1499, "category": "women",
     "image_url": "https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?w=300&h=400&fit=crop"},
    {"name": "Printed Saree", "brand": "FabIndia", "price": 3999, "category": "women",
     "image_url": "https://images.unsplash.com/photo-1610030469983-98e550d6193c?w=300&h=400&fit=crop"},
    {"name": "Running Shoes", "brand": "Adidas", "price": 4499, "category": "women",
     "image_url": "https://images.unsplash.com/photo-1595950653106-6c9ebd614d3a?w=300&h=400&fit=crop"},
    {"name": "Hoop Earrings", "brand": "Accessorize", "price": 599, "category": "women",
     "image_url": "https://images.unsplash.com/photo-1535632066927-ab7c9ab60908?w=300&h=400&fit=crop"},
    {"name": "Oversized Sunglasses", "brand": "Vogue", "price": 2499, "category": "women",
     "image_url": "https://images.unsplash.com/photo-1577803645773-f96470509666?w=300&h=400&fit=crop"},

    # Kids
    {"name": "Cartoon Print T-Shirt", "brand": "Disney", "price": 499, "category": "kids",
     "image_url": "https://images.unsplash.com/photo-1519238263530-99bdd11df2ea?w=300&h=400&fit=crop"},
    {"name": "Denim Dungaree", "brand": "H&M", "price": 999, "category": "kids",
     "image_url": "https://images.unsplash.com/photo-1471286174890-9c112ffca5b4?w=300&h=400&fit=crop"},
    {"name": "Light-Up Sneakers", "brand": "Skechers", "price": 1799, "category": "kids",
     "image_url": "https://images.unsplash.com/photo-1551107696-a4b0c5a0d9a2?w=300&h=400&fit=crop"},
    {"name": "School Backpack", "brand": "Wildcraft", "price": 899, "category": "kids",
     "image_url": "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=300&h=400&fit=crop"},
    {"name": "Printed Shorts Set", "brand": "Max", "price": 599, "category": "kids",
     "image_url": "https://images.unsplash.com/photo-1518831959646-742c3a14ebf7?w=300&h=400&fit=crop"},

    # Home & Living
    {"name": "Cotton Bedsheet Set", "brand": "Spaces", "price": 1499, "category": "home",
     "image_url": "https://images.unsplash.com/photo-1522771739844-6a9f6d5f14af?w=300&h=400&fit=crop"},
    {"name": "Scented Candle Set", "brand": "Bath & Body", "price": 799, "category": "home",
     "image_url": "https://images.unsplash.com/photo-1602028915047-37269d1a73f7?w=300&h=400&fit=crop"},
    {"name": "Cushion Covers (Set of 5)", "brand": "Homecentre", "price": 999, "category": "home",
     "image_url": "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?w=300&h=400&fit=crop"},
    {"name": "Desk Lamp", "brand": "Philips", "price": 1199, "category": "home",
     "image_url": "https://images.unsplash.com/photo-1513506003901-1e6a229e2d15?w=300&h=400&fit=crop"},
    {"name": "Wall Clock", "brand": "Casio", "price": 699, "category": "home",
     "image_url": "https://images.unsplash.com/photo-1563861826100-9cb868fdbe1c?w=300&h=400&fit=crop"},

    # Beauty
    {"name": "Matte Lipstick", "brand": "MAC", "price": 1299, "category": "beauty",
     "image_url": "https://images.unsplash.com/photo-1586495777744-4413f21062fa?w=300&h=400&fit=crop"},
    {"name": "Foundation SPF 30", "brand": "Maybelline", "price": 599, "category": "beauty",
     "image_url": "https://images.unsplash.com/photo-1596462502278-27bfdc403348?w=300&h=400&fit=crop"},
    {"name": "Perfume Eau de Parfum", "brand": "Zara", "price": 1999, "category": "beauty",
     "image_url": "https://images.unsplash.com/photo-1541643600914-78b084683601?w=300&h=400&fit=crop"},
    {"name": "Hair Serum", "brand": "L'Oreal", "price": 499, "category": "beauty",
     "image_url": "https://images.unsplash.com/photo-1526947425960-945c6e72858f?w=300&h=400&fit=crop"},
    {"name": "Face Wash Combo", "brand": "Cetaphil", "price": 799, "category": "beauty",
     "image_url": "https://images.unsplash.com/photo-1556228578-0d85b1a4d571?w=300&h=400&fit=crop"},
]


class Command(BaseCommand):
    help = "Seed the database with sample products"

    def handle(self, *args, **options):
        Product.objects.all().delete()
        self.stdout.write("Cleared old products")

        for p in PRODUCTS:
            Product.objects.create(
                name=p["name"],
                brand=p.get("brand", ""),
                price=p["price"],
                digital=p.get("digital", False),
                category=p.get("category", "men"),
                image_url=p.get("image_url", ""),
            )
            self.stdout.write(f"Created: {p['brand']} - {p['name']} [{p['category']}]")

        self.stdout.write(self.style.SUCCESS(
            f"Done! Total products: {Product.objects.count()}"
        ))
