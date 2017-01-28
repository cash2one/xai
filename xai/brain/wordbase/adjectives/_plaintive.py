

#calss header
class _PLAINTIVE():
	def __init__(self,): 
		self.name = "PLAINTIVE"
		self.definitions = [u'used to describe something that sounds slightly sad: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
