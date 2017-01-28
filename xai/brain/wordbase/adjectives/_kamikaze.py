

#calss header
class _KAMIKAZE():
	def __init__(self,): 
		self.name = "KAMIKAZE"
		self.definitions = [u'A kamikaze attack is a sudden violent attack on an enemy, especially one in which the person or people attacking know that they will be killed: ', u'being willing to take risks and not worrying about safety: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
