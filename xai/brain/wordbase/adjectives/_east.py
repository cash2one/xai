

#calss header
class _EAST():
	def __init__(self,): 
		self.name = "EAST"
		self.definitions = [u'in or forming the east part of something: ', u'a wind coming from the east']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
