

#calss header
class _MAGNANIMOUS():
	def __init__(self,): 
		self.name = "MAGNANIMOUS"
		self.definitions = [u'very kind and generous towards an enemy or someone you have defeated: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
