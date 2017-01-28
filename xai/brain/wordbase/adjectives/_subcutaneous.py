

#calss header
class _SUBCUTANEOUS():
	def __init__(self,): 
		self.name = "SUBCUTANEOUS"
		self.definitions = [u'existing under the skin: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
