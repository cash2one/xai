

#calss header
class _NUTTY():
	def __init__(self,): 
		self.name = "NUTTY"
		self.definitions = [u'containing, tasting of, or similar to nuts: ', u'crazy, silly, or strange: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
