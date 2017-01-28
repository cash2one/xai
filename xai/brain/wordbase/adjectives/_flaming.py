

#calss header
class _FLAMING():
	def __init__(self,): 
		self.name = "FLAMING"
		self.definitions = [u'used to add force, especially anger, to something that is said: ', u'a very angry argument in which people shout at each other: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
