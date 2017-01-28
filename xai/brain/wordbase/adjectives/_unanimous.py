

#calss header
class _UNANIMOUS():
	def __init__(self,): 
		self.name = "UNANIMOUS"
		self.definitions = [u'If a group of people are unanimous, they all agree about one particular matter or vote the same way, and if a decision or judgment is unanimous, it is formed or supported by everyone in a group: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
