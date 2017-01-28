

#calss header
class _HEAVYSET():
	def __init__(self,): 
		self.name = "HEAVYSET"
		self.definitions = [u'Someone who is heavyset has a large, wide, strong body.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
