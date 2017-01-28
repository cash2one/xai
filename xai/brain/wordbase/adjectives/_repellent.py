

#calss header
class _REPELLENT():
	def __init__(self,): 
		self.name = "REPELLENT"
		self.definitions = [u'making you feel strong disapproval and that you do not want to be involved with someone or something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
