

#calss header
class _BLACK():
	def __init__(self,): 
		self.name = "BLACK"
		self.definitions = [u'having the darkest colour there is, like the colour of coal or of a very dark night: ', u'relating or belonging to people with black or dark brown skin, especially people who live in Africa or whose family originally came from Africa: ', u'without any milk or cream added: ', u'without hope: ', u'bad or evil: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
