

#calss header
class _POPULOUS():
	def __init__(self,): 
		self.name = "POPULOUS"
		self.definitions = [u'A populous country, area, or place has a lot of people living in it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
