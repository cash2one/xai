

#calss header
class _CHARY():
	def __init__(self,): 
		self.name = "CHARY"
		self.definitions = [u'uncertain and frightened to take risks, or unwilling to take action: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
