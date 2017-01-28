

#calss header
class _FOSTER():
	def __init__(self,): 
		self.name = "FOSTER"
		self.definitions = [u"used to refer to someone or something connected with the care of children, usually for a limited time, by someone who is not the child's legal parent: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
