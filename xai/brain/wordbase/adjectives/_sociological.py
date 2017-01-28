

#calss header
class _SOCIOLOGICAL():
	def __init__(self,): 
		self.name = "SOCIOLOGICAL"
		self.definitions = [u'related to or involving sociology: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
