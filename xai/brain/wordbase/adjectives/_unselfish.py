

#calss header
class _UNSELFISH():
	def __init__(self,): 
		self.name = "UNSELFISH"
		self.definitions = [u'An unselfish person thinks about what is good for other people, not just about their own advantage.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
