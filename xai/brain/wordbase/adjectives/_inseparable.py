

#calss header
class _INSEPARABLE():
	def __init__(self,): 
		self.name = "INSEPARABLE"
		self.definitions = [u'If two or more people are inseparable, they are such good friends that they spend most of their time together: ', u'If two or more things are inseparable, they are so closely connected that they cannot be considered separately: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
