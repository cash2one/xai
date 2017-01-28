

#calss header
class _UNFORTUNATE():
	def __init__(self,): 
		self.name = "UNFORTUNATE"
		self.definitions = [u'unlucky or having bad effects: ', u'(of remarks or behaviour) not suitable in a way that could cause embarrassment or offence: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
