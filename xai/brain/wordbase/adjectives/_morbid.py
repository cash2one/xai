

#calss header
class _MORBID():
	def __init__(self,): 
		self.name = "MORBID"
		self.definitions = [u'too interested in unpleasant subjects, especially death: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
