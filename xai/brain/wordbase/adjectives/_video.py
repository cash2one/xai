

#calss header
class _VIDEO():
	def __init__(self,): 
		self.name = "VIDEO"
		self.definitions = [u'using video: ', u'connected with or used in the showing of moving pictures by television: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
