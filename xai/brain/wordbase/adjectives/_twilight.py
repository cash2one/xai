

#calss header
class _TWILIGHT():
	def __init__(self,): 
		self.name = "TWILIGHT"
		self.definitions = [u'used to describe a way of life that involves illegal or immoral activities, and is on the edge of normal society: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
