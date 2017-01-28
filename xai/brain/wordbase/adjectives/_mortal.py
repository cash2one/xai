

#calss header
class _MORTAL():
	def __init__(self,): 
		self.name = "MORTAL"
		self.definitions = [u'(of living things, especially people) unable to continue living for ever; having to die: ', u'causing death: ', u'extreme anxiety about or fear of someone or something: ', u'a very serious and dangerous enemy, danger, threat, etc.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
