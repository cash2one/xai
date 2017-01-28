

#calss header
class _ADULT():
	def __init__(self,): 
		self.name = "ADULT"
		self.definitions = [u'grown to full size and strength: ', u'typical of or suitable for adults: ', u'Adult films, magazines, and books show naked people and sexual acts and are not for children.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
