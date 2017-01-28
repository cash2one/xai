

#calss header
class _LEFT():
	def __init__(self,): 
		self.name = "LEFT"
		self.definitions = [u'on or towards the side of your body that is to the west when you are facing north: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
