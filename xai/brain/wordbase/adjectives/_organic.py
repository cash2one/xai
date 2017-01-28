

#calss header
class _ORGANIC():
	def __init__(self,): 
		self.name = "ORGANIC"
		self.definitions = [u'not using artificial chemicals in the growing of plants and animals for food and other products: ', u'being or coming from living plants and animals: ', u'(of a disease or illness) producing a physical change in the structure of an organ or part of the body', u'(of a chemical substance) containing carbon: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
