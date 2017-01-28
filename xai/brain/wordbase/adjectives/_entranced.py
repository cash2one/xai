

#calss header
class _ENTRANCED():
	def __init__(self,): 
		self.name = "ENTRANCED"
		self.definitions = [u'If you are entranced by someone or something that is very interesting or beautiful, you cannot stop watching him, her, or it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
