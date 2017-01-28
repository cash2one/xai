

#calss header
class _EXCEPTIONAL():
	def __init__(self,): 
		self.name = "EXCEPTIONAL"
		self.definitions = [u'much greater than usual, especially in skill, intelligence, quality, etc.: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
