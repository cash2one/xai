

#calss header
class _KITTENISH():
	def __init__(self,): 
		self.name = "KITTENISH"
		self.definitions = [u'used to describe a woman who behaves in a humorous, silly way, especially as a way of attracting sexual attention']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
