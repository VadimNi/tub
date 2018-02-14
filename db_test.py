from autofixture import Autofixture
from qa.models import Answer Question

fixture = AutoFixture(Answer, generate_fk=True)
entries = fixture.create(10)