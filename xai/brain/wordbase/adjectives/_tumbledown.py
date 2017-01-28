

#calss header
class _TUMBLEDOWN():
	def __init__(self,): 
		self.name = "TUMBLEDOWN"
		self.definitions = [u'(of a building) in a very bad condition, especially in a state of decay: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
