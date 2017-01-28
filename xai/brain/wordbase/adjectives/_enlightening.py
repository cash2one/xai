

#calss header
class _ENLIGHTENING():
	def __init__(self,): 
		self.name = "ENLIGHTENING"
		self.definitions = [u'giving you more information and understanding of something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
