

#calss header
class _WEST():
	def __init__(self,): 
		self.name = "WEST"
		self.definitions = [u'in or forming the west part of something: ', u'a wind coming from the west']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
