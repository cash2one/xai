

#calss header
class _ETHNIC():
	def __init__(self,): 
		self.name = "ETHNIC"
		self.definitions = [u'relating to a particular race of people: ', u'from a different race, or interesting because characteristic of an ethnic group that is very different from those that are common in western culture: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
