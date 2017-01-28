

#calss header
class _TRANQUIL():
	def __init__(self,): 
		self.name = "TRANQUIL"
		self.definitions = [u'calm and peaceful and without noise, violence, worry, etc.: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
