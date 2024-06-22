# Copyright 2016, 2022 John J. Rofrano. All Rights Reserved.
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

# pylint: disable=too-few-public-methods

"""
Test Factory to make fake objects for testing
"""
import factory
from factory.fuzzy import FuzzyChoice, FuzzyDecimal, FuzzyText
from service.models import Product, Category

class ProductFactory(factory.Factory):
    """Creates fake products for testing, utilizing Faker and Fuzzy."""

    class Meta:
        model = Product  # Links this factory to the Product model.

    id = factory.Sequence(lambda n: n)  # Automatically incremented IDs.

    # Faker and Fuzzy attributes:
    name = FuzzyChoice(["Basic Hat", "Work Pants", "Casual Shirt", "Fresh Apple", "Organic Banana", "Steel Pots", "Cotton Towels", "Ford Sedan", "Chevy Pickup", "Steel Hammer", "Adjustable Wrench"])
    description = factory.Faker('sentence', nb_words=6)  # Generates a random sentence with 6 words.
    price = FuzzyDecimal(0.99, 999.99, 2)  # Generates a decimal price between 0.99 and 999.99, rounding to 2 decimal places.
    available = FuzzyChoice([True, False])  # Randomly sets availability as True or False.
    category = FuzzyChoice([e.name for e in Category])  # Chooses randomly from the Category enum names.
