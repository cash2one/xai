

#calss header
class _HORRIBLE():
	def __init__(self,): 
		self.name = "HORRIBLE"
		self.definitions = [u'very unpleasant or bad: ', u'very shocking and frightening: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
