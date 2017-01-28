

#calss header
class _SYSTEMIC():
	def __init__(self,): 
		self.name = "SYSTEMIC"
		self.definitions = [u'A systemic drug, disease, or poison reaches and has an effect on the whole of a body or a plant and not just one part of it.', u'A systemic problem or change is a basic one, experienced by the whole of an organization or a country and not just particular parts of it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
