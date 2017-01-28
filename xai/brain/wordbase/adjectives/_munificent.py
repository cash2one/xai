

#calss header
class _MUNIFICENT():
	def __init__(self,): 
		self.name = "MUNIFICENT"
		self.definitions = [u'very generous with money: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
