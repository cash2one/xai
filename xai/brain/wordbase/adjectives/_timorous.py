

#calss header
class _TIMOROUS():
	def __init__(self,): 
		self.name = "TIMOROUS"
		self.definitions = [u'nervous and without much confidence']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
