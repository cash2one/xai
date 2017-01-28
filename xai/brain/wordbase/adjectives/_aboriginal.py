

#calss header
class _ABORIGINAL():
	def __init__(self,): 
		self.name = "ABORIGINAL"
		self.definitions = [u'used to refer to a person or living thing that has existed in a country or continent since the earliest time known to people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
