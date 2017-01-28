

#calss header
class _SCORNFUL():
	def __init__(self,): 
		self.name = "SCORNFUL"
		self.definitions = [u'showing or feeling scorn for someone or something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
