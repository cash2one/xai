

#calss header
class _DISCOURTEOUS():
	def __init__(self,): 
		self.name = "DISCOURTEOUS"
		self.definitions = [u"rude and not considering other people's feelings: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
