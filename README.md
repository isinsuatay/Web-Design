# Liceria E-Commerce Website

Liceria is an e-commerce platform built with Python Django.

## Features

- Wide range of products categorized for easy browsing by users.
- User-friendly interface allows users to quickly access desired products.
- Account creation and membership.
- Users can add products to their cart, view their carts, and remove products from their carts.
- Authenticated users can save their carts and access them on subsequent visits.
- Users can modify quantities of products in their carts.

## Installation and Running

1. Clone this repository:
    ```
    git clone https://github.com/isinsuatay/Web-Design.git
    ```
2. Navigate to the project directory:
    ```
    cd Web-Design
    ```
3. Create a virtual environment (optional but recommended):
    ```
    python -m venv venv
    ```
4. Activate the virtual environment:
   - Windows:
     ```
     venv\Scripts\activate
     ```
   - macOS and Linux:
     ```
     source venv/bin/activate
     ```
5. Install necessary Python dependencies:
    ```
    pip install -r requirements.txt
    ```
6. Apply database migrations:
    ```
    python manage.py migrate
    ```
7. Run the project:
    ```
    python manage.py runserver
    ```
8. Visit `http://localhost:8000` in your browser.

## Technologies Used

- Python 3
- Django
- HTML/CSS
- JavaScript

## Screenshots
![Home Page](https://github.com/isinsuatay/Web-Design/blob/main/liceria-views/HomePage.png)
_**Figure 1:** Liceria's home page._

![Product](https://github.com/isinsuatay/Web-Design/blob/main/liceria-views/ProductPage.png)
_**Figure 2:** Product detail page._

![Product](https://github.com/isinsuatay/Web-Design/blob/main/liceria-views/Responsive.png)
_**Figure 3:** Responsive page._

## Contributing

If you'd like to contribute to Liceria, please open a pull request. We recommend opening an issue to discuss major changes before proceeding.
