

#calss header
class _NORTH():
	def __init__(self,): 
		self.name = "NORTH"
		self.definitions = [u'in or forming the north part of something: ', u'a wind coming from the north']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
