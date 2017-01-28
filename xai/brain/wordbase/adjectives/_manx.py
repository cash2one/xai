

#calss header
class _MANX():
	def __init__(self,): 
		self.name = "MANX"
		self.definitions = [u'of the Isle of Man, the people who live there, or their language']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
