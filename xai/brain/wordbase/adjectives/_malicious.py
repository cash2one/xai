

#calss header
class _MALICIOUS():
	def __init__(self,): 
		self.name = "MALICIOUS"
		self.definitions = [u'intended to harm or upset other people: ', u'intended to cause damage to a computer system, or to steal private information from a computer system: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
