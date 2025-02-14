from django.template.defaultfilters import slugify
from everycheese.users.tests.factories import UserFactory
from ..models import Cheese
import factory
import factory.fuzzy
import  pytest


@pytest.fixture
def cheese():
    return CheeseFactory()


class CheeseFactory(factory.django.DjangoModelFactory):
    name = factory.fuzzy.FuzzyText()
    slug = factory.LazyAttribute(lambda obj: slugify(obj.name))
    description = factory.Faker('paragraph', nb_sentences=3, variable_nb_sentences=2)
    firmness = factory.fuzzy.FuzzyChoice(x[0] for x in Cheese.Firmness.choices)
    country_of_origin = factory.Faker('country_code')
    creator = factory.SubFactory(UserFactory)

    class Meta:
        model = Cheese
