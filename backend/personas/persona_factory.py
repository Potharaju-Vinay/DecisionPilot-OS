from backend.personas.sales_persona import SalesPersona
from backend.personas.compliance_persona import CompliancePersona
from backend.personas.executive_persona import ExecutivePersona
from backend.personas.technical_persona import TechnicalPersona


class PersonaFactory:

    def __init__(self):

        self.personas = {

            "sales": SalesPersona(),

            "compliance": CompliancePersona(),

            "executive": ExecutivePersona(),

            "technical": TechnicalPersona()

        }

    def build_all(self, context):

        result = {}

        for name, persona in self.personas.items():

            result[name] = persona.build(
                context
            )

        return result