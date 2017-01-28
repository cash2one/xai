

#calss header
class _INDISPOSED():
	def __init__(self,): 
		self.name = "INDISPOSED"
		self.definitions = [u'ill, especially in a way that makes you unable to do something: ', u'not willing: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
