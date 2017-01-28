

#calss header
class _VERBAL():
	def __init__(self,): 
		self.name = "VERBAL"
		self.definitions = [u'spoken rather than written: ', u'relating to words: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
