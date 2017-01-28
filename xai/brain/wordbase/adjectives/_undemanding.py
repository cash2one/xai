

#calss header
class _UNDEMANDING():
	def __init__(self,): 
		self.name = "UNDEMANDING"
		self.definitions = [u'not needing a lot of time, energy, or attention: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
