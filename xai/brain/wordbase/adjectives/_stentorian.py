

#calss header
class _STENTORIAN():
	def __init__(self,): 
		self.name = "STENTORIAN"
		self.definitions = [u'using a very loud voice, or (of a voice) very loud: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
