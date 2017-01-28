

#calss header
class _SPOILED():
	def __init__(self,): 
		self.name = "SPOILED"
		self.definitions = [u'A spoiled child is allowed to do or have anything that it wants to, usually so that it expects to get everything it wants, and does not show respect to other people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
