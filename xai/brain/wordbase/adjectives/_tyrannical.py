

#calss header
class _TYRANNICAL():
	def __init__(self,): 
		self.name = "TYRANNICAL"
		self.definitions = [u'using, showing, or relating to the unfair and cruel use of power over other people in a country, group, etc.: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
