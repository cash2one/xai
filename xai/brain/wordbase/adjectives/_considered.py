

#calss header
class _CONSIDERED():
	def __init__(self,): 
		self.name = "CONSIDERED"
		self.definitions = [u'an opinion or decision that someone has reached after a lot of thought: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
