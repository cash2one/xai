

#calss header
class _STUFFY():
	def __init__(self,): 
		self.name = "STUFFY"
		self.definitions = [u'A stuffy room or building is unpleasant because it has no fresh air: ', u'old-fashioned, formal, and boring: ', u'If your nose is stuffy or you have a stuffy nose, your nose is blocked with mucus, usually because you have a cold.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
