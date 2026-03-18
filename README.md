# ShopHut

A full-featured e-commerce web application built with Django, featuring a Myntra-inspired UI with category filtering, user authentication, cart management, and PayPal checkout.

**Live:** [https://shophut-priyanshsinghal.vercel.app/](https://shophut-priyanshsinghal.vercel.app/)

---

## Features

- **Product Catalog** — 35 curated products across 5 categories with real brand names and Unsplash images
- **Category Filtering** — Men, Women, Kids, Home & Living, Beauty with dynamic hero banners
- **User Authentication** — Login, Register, Logout with session management
- **Shopping Cart** — Add/remove items, quantity controls, persistent cart (cookie-based for guests, DB-backed for users)
- **Checkout** — Contact info, shipping address form, order summary sidebar
- **PayPal Integration** — Secure payment processing via PayPal SDK
- **Responsive Design** — Fully responsive across desktop, tablet, and mobile

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Django 4.2, Python 3.12 |
| Frontend | HTML5, CSS3, JavaScript, Bootstrap 4 |
| Icons | Font Awesome 6 |
| Fonts | Google Fonts (Assistant) |
| Static Files | WhiteNoise (compressed + hashed) |
| Database | SQLite |
| Deployment | Vercel (Serverless) |
| Images | Unsplash |

## Project Structure

```
ShopHut/
├── ecommerce/          # Django project settings, URLs, WSGI
├── store/              # Main app
│   ├── management/     # Custom management commands (seed_products)
│   ├── migrations/     # Database migrations
│   ├── templates/      # HTML templates (Myntra-style UI)
│   ├── models.py       # Product, Customer, Order, OrderItem, ShippingAddress
│   ├── views.py        # Store, cart, checkout, auth views
│   ├── urls.py         # URL routing
│   └── utils.py        # Cart utilities (cookie & DB cart)
├── static/
│   ├── css/main.css    # Premium CSS with design tokens & animations
│   └── js/cart.js      # Cart interactions (add/remove, cookie management)
├── staticfiles/        # Collected static files (WhiteNoise)
├── vercel.json         # Vercel deployment config
├── requirements.txt    # Python dependencies
└── manage.py
```

## Getting Started

### Prerequisites

- Python 3.9+
- pip

### Local Setup

```bash
# Clone the repo
git clone https://github.com/priyansh18/Shophut.git
cd Shophut

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Seed sample products
python manage.py seed_products

# Start development server
python manage.py runserver
```

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `SECRET_KEY` | Django secret key | dev key (insecure) |
| `DEBUG` | Enable debug mode | `False` |

## Pages

| Route | Description |
|-------|-------------|
| `/` | Home — all products |
| `/?category=men` | Men's products |
| `/?category=women` | Women's products |
| `/?category=kids` | Kids' products |
| `/?category=home` | Home & Living |
| `/?category=beauty` | Beauty products |
| `/cart/` | Shopping cart |
| `/checkout/` | Checkout page |
| `/login/` | Login |
| `/register/` | Register |
| `/logout/` | Logout |
| `/admin/` | Django admin |

## Deployment

Deployed on **Vercel** as a serverless Python function.

- Static files served via WhiteNoise with compressed manifest
- SQLite runs in `/tmp/` on Vercel's serverless filesystem
- Auto-migrates and seeds products on cold start

## License

MIT
