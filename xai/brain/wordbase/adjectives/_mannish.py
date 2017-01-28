

#calss header
class _MANNISH():
	def __init__(self,): 
		self.name = "MANNISH"
		self.definitions = [u"If you describe a woman as mannish, you mean that her appearance or behaviour are too much like a man's: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
