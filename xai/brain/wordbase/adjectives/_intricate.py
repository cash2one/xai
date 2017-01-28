

#calss header
class _INTRICATE():
	def __init__(self,): 
		self.name = "INTRICATE"
		self.definitions = [u'having a lot of small parts or details that are arranged in a complicated way and are therefore sometimes difficult to understand, solve, or produce: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
