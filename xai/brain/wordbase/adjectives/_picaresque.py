

#calss header
class _PICARESQUE():
	def __init__(self,): 
		self.name = "PICARESQUE"
		self.definitions = [u'relating to a type of story in which the main character travels from place to place and has a series of adventures (= exciting experiences): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
