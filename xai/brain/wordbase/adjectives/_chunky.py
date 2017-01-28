

#calss header
class _CHUNKY():
	def __init__(self,): 
		self.name = "CHUNKY"
		self.definitions = [u'used to describe clothes that are thick and heavy, or jewellery made of large pieces: ', u'used to describe a person who is short and heavy']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
