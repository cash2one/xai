

#calss header
class _PHENOMENAL():
	def __init__(self,): 
		self.name = "PHENOMENAL"
		self.definitions = [u'extremely successful or special, especially in a surprising way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
