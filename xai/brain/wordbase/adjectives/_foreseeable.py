

#calss header
class _FORESEEABLE():
	def __init__(self,): 
		self.name = "FORESEEABLE"
		self.definitions = [u'A foreseeable event or situation is one that can be known about or guessed before it happens.', u'as far into the future as you can imagine or plan for: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
