

#calss header
class _HELLENISTIC():
	def __init__(self,): 
		self.name = "HELLENISTIC"
		self.definitions = [u'of or relating to the history, art, etc. of ancient Greece and other countries of the Eastern Mediterranean, especially during the 4th to the 1st century BC']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
