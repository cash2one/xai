

#calss header
class _PURITANICAL():
	def __init__(self,): 
		self.name = "PURITANICAL"
		self.definitions = [u'believing or involving the belief that it is important to work hard and control yourself, and that pleasure is wrong or unnecessary: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
