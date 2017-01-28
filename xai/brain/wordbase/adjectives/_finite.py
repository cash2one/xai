

#calss header
class _FINITE():
	def __init__(self,): 
		self.name = "FINITE"
		self.definitions = [u'having a limit or end: ', u'in a form that shows the tense and subject of a verb, rather than the infinitive form or a participle: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
