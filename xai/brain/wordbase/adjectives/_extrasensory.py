

#calss header
class _EXTRASENSORY():
	def __init__(self,): 
		self.name = "EXTRASENSORY"
		self.definitions = [u'without the use of hearing, seeing, touch, taste, and smell']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
