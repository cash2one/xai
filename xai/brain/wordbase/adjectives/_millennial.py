

#calss header
class _MILLENNIAL():
	def __init__(self,): 
		self.name = "MILLENNIAL"
		self.definitions = [u'relating to a millennium or to the year 2000: ', u'born around the year 2000: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
