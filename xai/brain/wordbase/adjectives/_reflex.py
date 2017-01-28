

#calss header
class _REFLEX():
	def __init__(self,): 
		self.name = "REFLEX"
		self.definitions = [u'A reflex angle is more than 180\xb0 and less than 360\xb0.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
