

#calss header
class _UNSYMPATHETIC():
	def __init__(self,): 
		self.name = "UNSYMPATHETIC"
		self.definitions = [u"not sympathetic (= showing that you understand or care about someone's suffering)"]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
