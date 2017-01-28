

#calss header
class _UNLEAVENED():
	def __init__(self,): 
		self.name = "UNLEAVENED"
		self.definitions = [u'Unleavened bread or similar food that is made without yeast and is therefore flat.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
