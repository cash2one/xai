

#calss header
class _ILLUSORY():
	def __init__(self,): 
		self.name = "ILLUSORY"
		self.definitions = [u'not real and based on illusion: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
