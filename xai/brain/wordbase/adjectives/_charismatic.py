

#calss header
class _CHARISMATIC():
	def __init__(self,): 
		self.name = "CHARISMATIC"
		self.definitions = [u'used to describe a person who has charisma: ', u'belonging or relating to various groups within the Christian Church who believe that God gives people special powers, such as the ability to make others well again and to speak to him in a special language: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
