

#calss header
class _SAVOURY():
	def __init__(self,): 
		self.name = "SAVOURY"
		self.definitions = [u'Savoury food is salty or spicy and not sweet in taste: ', u'If you say that something is not savoury, you mean that it is not pleasant or socially acceptable: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
