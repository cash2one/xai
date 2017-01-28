

#calss header
class _INTEGRAL():
	def __init__(self,): 
		self.name = "INTEGRAL"
		self.definitions = [u'necessary and important as a part of a whole: ', u'contained within something; not separate: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
