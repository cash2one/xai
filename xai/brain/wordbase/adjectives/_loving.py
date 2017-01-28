

#calss header
class _LOVING():
	def __init__(self,): 
		self.name = "LOVING"
		self.definitions = [u'showing a lot of love towards someone: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
