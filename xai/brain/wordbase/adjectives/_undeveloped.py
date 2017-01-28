

#calss header
class _UNDEVELOPED():
	def __init__(self,): 
		self.name = "UNDEVELOPED"
		self.definitions = [u'An undeveloped place or piece of land has not been built on or used for farming.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
