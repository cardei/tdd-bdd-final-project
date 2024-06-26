######################################################################
# Copyright 2016, 2023 John J. Rofrano. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
######################################################################

"""
Product Steps

Steps file for products.feature

For information on Waiting until elements are present in the HTML see:
    https://selenium-python.readthedocs.io/waits.html
"""
import requests
from behave import given

# HTTP Return Codes
HTTP_200_OK = 200
HTTP_201_CREATED = 201
HTTP_204_NO_CONTENT = 204

@given('the following products')
def step_impl(context):
    """Delete all Products and load new ones."""
    # First, delete existing products to start with a clean slate
    rest_endpoint = f"{context.base_url}/products"
    response = requests.get(rest_endpoint)
    assert response.status_code == HTTP_200_OK
    
    # Delete each product found
    for product in response.json():
        delete_response = requests.delete(f"{rest_endpoint}/{product['id']}")
        assert delete_response.status_code == HTTP_204_NO_CONTENT

    # Now, load the new products from the background data in the feature files
    for row in context.table:
        payload = {
            "name": row['name'],
            "description": row['description'],
            "price": row['price'],
            "available": row['available'] in ['True', 'true', '1'],  # Convert to boolean
            "category": row['category']
        }
        post_response = requests.post(rest_endpoint, json=payload)
        assert post_response.status_code == HTTP_201_CREATED

