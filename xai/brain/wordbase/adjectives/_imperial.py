

#calss header
class _IMPERIAL():
	def __init__(self,): 
		self.name = "IMPERIAL"
		self.definitions = [u'belonging or relating to an empire or the person or country that rules it: ', u'The imperial system of measurement uses units such as inches, miles, and pints: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
