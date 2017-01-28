

#calss header
class _WORSE():
	def __init__(self,): 
		self.name = "WORSE"
		self.definitions = [u'comparative of  bad : more unpleasant, difficult, or severe than before or than something else that is also bad: ', u'to become more ill, or to become a more severe condition: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
