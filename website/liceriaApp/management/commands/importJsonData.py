import json
from django.core.management.base import BaseCommand
from django.core.files import File
from liceriaApp.models import Category, Product

class Command(BaseCommand):
    help = 'Imports data from JSON file to database'

    def handle(self, *args, **kwargs):
        with open('liceriaApp/static/json/data.json', 'r') as f:
            data = json.load(f)

            for item in data:
                category_name = item['category']
                category, _ = Category.objects.get_or_create(name=category_name)

                product = Product.objects.create(
                    name=item['name'],
                    price=item['price'],
                    category=category
                )

                if 'src' in item:
                    image_path = 'liceriaApp' + item['src']
                    product.image.save(image_path.split('/')[-1], File(open(image_path, 'rb')))
                    self.stdout.write(self.style.SUCCESS(f"Image for product '{product.name}' added successfully"))
                else:
                    self.stdout.write(self.style.WARNING(f"No image found for product '{product.name}'"))
                
                self.stdout.write(self.style.SUCCESS(f"Product '{product.name}' added to category '{category.name}'"))
