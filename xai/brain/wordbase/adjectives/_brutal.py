

#calss header
class _BRUTAL():
	def __init__(self,): 
		self.name = "BRUTAL"
		self.definitions = [u'cruel, violent, and completely without feelings: ', u"not considering someone's feelings: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
