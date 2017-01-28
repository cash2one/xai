

#calss header
class _INHERENT():
	def __init__(self,): 
		self.name = "INHERENT"
		self.definitions = [u'existing as a natural or basic part of something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
