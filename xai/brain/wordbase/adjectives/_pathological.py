

#calss header
class _PATHOLOGICAL():
	def __init__(self,): 
		self.name = "PATHOLOGICAL"
		self.definitions = [u'(of a person) unable to control part of their behaviour; unreasonable: ', u'relating to or caused by a disease: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
