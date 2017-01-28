

#calss header
class _NURSERY():
	def __init__(self,): 
		self.name = "NURSERY"
		self.definitions = [u'relating to the teaching of children who are between the ages of two or three to five years old: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
